// Aplicación Principal - Protocolo Circadiano Pro
class CircadianApp {
    constructor() {
        this.currentView = 'dashboard';
        this.charts = {};
        this.notificationTimeout = null;
    }

    async init() {
        // Esperar a que la base de datos esté lista
        await new Promise(resolve => {
            if (db.db) {
                resolve();
            } else {
                setTimeout(resolve, 100);
            }
        });

        this.setupEventListeners();
        this.updateCurrentDate();
        await this.loadDashboard();
        await this.checkNotifications();

        // Actualizar fecha cada minuto
        setInterval(() => this.updateCurrentDate(), 60000);

        // Verificar notificaciones cada 5 minutos
        setInterval(() => this.checkNotifications(), 300000);

        console.log('✅ Aplicación inicializada');
    }

    setupEventListeners() {
        // Navegación
        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', (e) => {
                const view = e.currentTarget.dataset.view;
                this.switchView(view);
            });
        });

        // Cerrar modal al hacer clic fuera
        document.getElementById('modal').addEventListener('click', (e) => {
            if (e.target.id === 'modal') {
                this.closeModal();
            }
        });
    }

    updateCurrentDate() {
        const now = new Date();
        const options = {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        };
        document.getElementById('current-date').textContent =
            now.toLocaleDateString('es-ES', options);
    }

    switchView(viewName) {
        // Actualizar navegación
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
            if (item.dataset.view === viewName) {
                item.classList.add('active');
            }
        });

        // Ocultar todas las vistas
        document.querySelectorAll('.view').forEach(view => {
            view.classList.add('hidden');
        });

        // Mostrar vista seleccionada
        const view = document.getElementById(`${viewName}-view`);
        if (view) {
            view.classList.remove('hidden');
        }

        // Actualizar título
        const titles = {
            dashboard: 'Dashboard',
            sleep: 'Registro de Sueño',
            supplements: 'Control de Suplementos',
            exercise: 'Ejercicio y Actividad',
            health: 'Métricas de Salud',
            protocol: 'Protocolo Circadiano',
            reports: 'Reportes y Análisis',
            settings: 'Configuración'
        };
        document.getElementById('view-title').textContent = titles[viewName] || viewName;

        this.currentView = viewName;

        // Cargar contenido específico de la vista
        this.loadView(viewName);
    }

    async loadView(viewName) {
        switch (viewName) {
            case 'dashboard':
                await this.loadDashboard();
                break;
            case 'sleep':
                await this.loadSleepView();
                break;
            case 'supplements':
                await this.loadSupplementsView();
                break;
            case 'exercise':
                await this.loadExerciseView();
                break;
            case 'health':
                await this.loadHealthView();
                break;
            case 'protocol':
                await this.loadProtocolView();
                break;
            case 'reports':
                await this.loadReportsView();
                break;
            case 'settings':
                await this.loadSettingsView();
                break;
        }
    }

    // ==================== DASHBOARD ====================
    async loadDashboard() {
        try {
            // Cargar estadísticas
            const [sleepStats, suppAdherence, exStats, healthTrends] = await Promise.all([
                db.getSleepStats(7),
                db.getSupplementAdherence(7),
                db.getExerciseStats(7),
                db.getHealthTrends(7)
            ]);

            // Actualizar tarjetas de estadísticas
            if (sleepStats) {
                const hours = Math.floor(sleepStats.avgDuration / 60);
                const minutes = sleepStats.avgDuration % 60;
                document.getElementById('avg-sleep').textContent = `${hours}.${Math.round(minutes / 6)}h`;
            }

            document.getElementById('supplement-adherence').textContent = `${suppAdherence}%`;

            if (exStats) {
                document.getElementById('exercise-count').textContent =
                    `${exStats.daysExercised}/5`;
            }

            if (healthTrends) {
                const score = ((parseFloat(healthTrends.avgMood) +
                    parseFloat(healthTrends.avgEnergy)) / 2).toFixed(1);
                document.getElementById('health-score').textContent = `${score}/10`;
            }

            // Cargar actividad reciente
            await this.loadRecentActivity();

            // Cargar gráfico de tendencias
            this.createTrendsChart();

        } catch (error) {
            console.error('Error cargando dashboard:', error);
        }
    }

    async loadRecentActivity() {
        const container = document.getElementById('recent-activity');
        const today = new Date().toISOString().split('T')[0];
        const yesterday = new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString().split('T')[0];

        try {
            const [todayData, yesterdayData] = await Promise.all([
                db.getDailyMetrics(today),
                db.getDailyMetrics(yesterday)
            ]);

            let html = '';

            // Actividades de hoy
            if (todayData.sleep) {
                html += `
                    <div class="timeline-item">
                        <div class="timeline-time">Hoy - ${todayData.sleep.wakeTime}</div>
                        <div class="timeline-content">
                            😴 Registrado sueño: ${Math.floor(todayData.sleep.duration / 60)}h ${todayData.sleep.duration % 60}m
                            <br>Calidad: ${todayData.sleep.quality}/10
                        </div>
                    </div>
                `;
            }

            if (todayData.exercise.length > 0) {
                todayData.exercise.forEach(ex => {
                    html += `
                        <div class="timeline-item">
                            <div class="timeline-time">Hoy - ${ex.timestamp.split('T')[1].slice(0, 5)}</div>
                            <div class="timeline-content">
                                🏃 Ejercicio ${ex.type}: ${ex.duration} min
                                <br>Intensidad: ${ex.intensity}
                            </div>
                        </div>
                    `;
                });
            }

            // Actividades de ayer
            if (yesterdayData.sleep) {
                html += `
                    <div class="timeline-item">
                        <div class="timeline-time">Ayer - ${yesterdayData.sleep.wakeTime}</div>
                        <div class="timeline-content">
                            😴 Sueño: ${Math.floor(yesterdayData.sleep.duration / 60)}h ${yesterdayData.sleep.duration % 60}m
                        </div>
                    </div>
                `;
            }

            if (html === '') {
                html = '<p style="color: #64748b;">No hay actividad reciente. ¡Comienza a registrar tus datos!</p>';
            }

            container.innerHTML = html;

        } catch (error) {
            console.error('Error cargando actividad reciente:', error);
            container.innerHTML = '<p style="color: #ef4444;">Error cargando actividad</p>';
        }
    }

    createTrendsChart() {
        const canvas = document.getElementById('trends-chart');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');

        // Datos de ejemplo (en producción vendrían de la DB)
        const data = {
            labels: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
            sleep: [7.5, 8, 7, 7.5, 8, 7.5, 8],
            quality: [8, 7, 6, 8, 9, 7, 8]
        };

        this.drawLineChart(ctx, data, canvas.width, canvas.height);
    }

    drawLineChart(ctx, data, width, height) {
        ctx.clearRect(0, 0, width, height);

        const padding = 40;
        const chartWidth = width - padding * 2;
        const chartHeight = height - padding * 2;

        // Dibujar ejes
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 1;

        // Eje Y
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.stroke();

        // Eje X
        ctx.beginPath();
        ctx.moveTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();

        // Dibujar líneas de sueño
        ctx.strokeStyle = '#2563eb';
        ctx.lineWidth = 3;
        ctx.beginPath();

        data.sleep.forEach((value, index) => {
            const x = padding + (chartWidth / (data.sleep.length - 1)) * index;
            const y = height - padding - (value / 10) * chartHeight;

            if (index === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });

        ctx.stroke();

        // Dibujar puntos
        ctx.fillStyle = '#2563eb';
        data.sleep.forEach((value, index) => {
            const x = padding + (chartWidth / (data.sleep.length - 1)) * index;
            const y = height - padding - (value / 10) * chartHeight;

            ctx.beginPath();
            ctx.arc(x, y, 4, 0, Math.PI * 2);
            ctx.fill();
        });

        // Dibujar etiquetas X
        ctx.fillStyle = '#64748b';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';

        data.labels.forEach((label, index) => {
            const x = padding + (chartWidth / (data.labels.length - 1)) * index;
            ctx.fillText(label, x, height - padding + 20);
        });

        // Título
        ctx.fillStyle = '#1e293b';
        ctx.font = 'bold 14px sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Horas de Sueño', padding, padding - 15);
    }

    // ==================== MODALES Y FORMULARIOS ====================
    async logSleep() {
        const modalBody = document.getElementById('modal-body');
        document.getElementById('modal-title').textContent = 'Registrar Sueño';

        modalBody.innerHTML = `
            <form id="sleep-form" class="form-grid">
                <div class="form-group">
                    <label class="form-label">Fecha</label>
                    <input type="date" name="date" class="form-input" value="${new Date().toISOString().split('T')[0]}" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Hora de dormir</label>
                    <input type="time" name="bedTime" class="form-input" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Hora de despertar</label>
                    <input type="time" name="wakeTime" class="form-input" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Calidad del sueño (1-10)</label>
                    <input type="range" name="quality" min="1" max="10" value="7" class="form-input" oninput="this.nextElementSibling.textContent = this.value">
                    <span style="font-weight: bold; color: var(--primary);">7</span>
                </div>
                <div class="form-group">
                    <label class="form-label">Interrupciones</label>
                    <input type="number" name="interruptions" min="0" class="form-input" value="0">
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label class="form-label">Notas</label>
                    <textarea name="notes" class="form-textarea" placeholder="¿Cómo te sentiste al despertar?"></textarea>
                </div>
                <div style="grid-column: 1 / -1; display: flex; gap: 10px; justify-content: flex-end;">
                    <button type="button" class="btn btn-secondary" onclick="app.closeModal()">Cancelar</button>
                    <button type="submit" class="btn btn-primary">Guardar</button>
                </div>
            </form>
        `;

        document.getElementById('sleep-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);

            const bedTime = formData.get('bedTime');
            const wakeTime = formData.get('wakeTime');

            // Calcular duración
            const [bedHour, bedMin] = bedTime.split(':').map(Number);
            const [wakeHour, wakeMin] = wakeTime.split(':').map(Number);

            let duration = (wakeHour * 60 + wakeMin) - (bedHour * 60 + bedMin);
            if (duration < 0) duration += 24 * 60; // Si cruzó medianoche

            await db.addSleepLog({
                date: formData.get('date'),
                bedTime,
                wakeTime,
                duration,
                quality: parseInt(formData.get('quality')),
                interruptions: parseInt(formData.get('interruptions')),
                notes: formData.get('notes')
            });

            this.closeModal();
            this.showNotification('Registro de sueño guardado', 'success');
            await this.loadDashboard();
        });

        this.openModal();
    }

    async logSupplements() {
        const modalBody = document.getElementById('modal-body');
        document.getElementById('modal-title').textContent = 'Registrar Suplementos';

        const supplements = [
            'Melatonina 1-3mg',
            'Vitamina D3 2000-4000 IU',
            'Magnesio 200-400mg',
            'Omega-3 1-2g',
            'NAC 600mg',
            'Taurina 1-2g',
            'L-Teanina 200mg',
            'Vitamina B Complex'
        ];

        modalBody.innerHTML = `
            <form id="supplement-form">
                <div class="form-group">
                    <label class="form-label">Fecha</label>
                    <input type="date" name="date" class="form-input" value="${new Date().toISOString().split('T')[0]}" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Hora</label>
                    <input type="time" name="time" class="form-input" value="${new Date().toTimeString().slice(0, 5)}" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Suplementos tomados</label>
                    ${supplements.map(supp => `
                        <div style="margin: 8px 0;">
                            <label style="display: flex; align-items: center; gap: 8px;">
                                <input type="checkbox" name="supplements" value="${supp}">
                                <span>${supp}</span>
                            </label>
                        </div>
                    `).join('')}
                </div>
                <div class="form-group">
                    <label class="form-label">Notas</label>
                    <textarea name="notes" class="form-textarea" placeholder="Efectos o comentarios"></textarea>
                </div>
                <div style="display: flex; gap: 10px; justify-content: flex-end; margin-top: 20px;">
                    <button type="button" class="btn btn-secondary" onclick="app.closeModal()">Cancelar</button>
                    <button type="submit" class="btn btn-primary">Guardar</button>
                </div>
            </form>
        `;

        document.getElementById('supplement-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);

            const selectedSupplements = formData.getAll('supplements');

            await db.addSupplementLog({
                date: formData.get('date'),
                time: formData.get('time'),
                supplements: selectedSupplements,
                taken: selectedSupplements.length > 0,
                notes: formData.get('notes')
            });

            this.closeModal();
            this.showNotification('Suplementos registrados', 'success');
            await this.loadDashboard();
        });

        this.openModal();
    }

    async logExercise() {
        const modalBody = document.getElementById('modal-body');
        document.getElementById('modal-title').textContent = 'Registrar Ejercicio';

        modalBody.innerHTML = `
            <form id="exercise-form" class="form-grid">
                <div class="form-group">
                    <label class="form-label">Fecha</label>
                    <input type="date" name="date" class="form-input" value="${new Date().toISOString().split('T')[0]}" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Tipo de ejercicio</label>
                    <select name="type" class="form-select" required>
                        <option value="cardio">Cardio</option>
                        <option value="strength">Fuerza</option>
                        <option value="flexibility">Flexibilidad</option>
                        <option value="mixed">Mixto</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Duración (minutos)</label>
                    <input type="number" name="duration" min="1" class="form-input" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Intensidad</label>
                    <select name="intensity" class="form-select" required>
                        <option value="low">Baja</option>
                        <option value="medium">Media</option>
                        <option value="high">Alta</option>
                    </select>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label class="form-label">Notas</label>
                    <textarea name="notes" class="form-textarea" placeholder="Detalles del ejercicio"></textarea>
                </div>
                <div style="grid-column: 1 / -1; display: flex; gap: 10px; justify-content: flex-end;">
                    <button type="button" class="btn btn-secondary" onclick="app.closeModal()">Cancelar</button>
                    <button type="submit" class="btn btn-primary">Guardar</button>
                </div>
            </form>
        `;

        document.getElementById('exercise-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);

            await db.addExerciseLog({
                date: formData.get('date'),
                type: formData.get('type'),
                duration: parseInt(formData.get('duration')),
                intensity: formData.get('intensity'),
                notes: formData.get('notes')
            });

            this.closeModal();
            this.showNotification('Ejercicio registrado', 'success');
            await this.loadDashboard();
        });

        this.openModal();
    }

    async logHealth() {
        const modalBody = document.getElementById('modal-body');
        document.getElementById('modal-title').textContent = 'Métricas de Salud';

        modalBody.innerHTML = `
            <form id="health-form" class="form-grid">
                <div class="form-group">
                    <label class="form-label">Fecha</label>
                    <input type="date" name="date" class="form-input" value="${new Date().toISOString().split('T')[0]}" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Peso (kg)</label>
                    <input type="number" step="0.1" name="weight" class="form-input">
                </div>
                <div class="form-group">
                    <label class="form-label">Presión Sistólica</label>
                    <input type="number" name="systolic" class="form-input">
                </div>
                <div class="form-group">
                    <label class="form-label">Presión Diastólica</label>
                    <input type="number" name="diastolic" class="form-input">
                </div>
                <div class="form-group">
                    <label class="form-label">Frecuencia Cardíaca</label>
                    <input type="number" name="heartRate" class="form-input">
                </div>
                <div class="form-group">
                    <label class="form-label">Estado de ánimo (1-10)</label>
                    <input type="range" name="mood" min="1" max="10" value="7" class="form-input" oninput="this.nextElementSibling.textContent = this.value">
                    <span style="font-weight: bold; color: var(--primary);">7</span>
                </div>
                <div class="form-group">
                    <label class="form-label">Energía (1-10)</label>
                    <input type="range" name="energy" min="1" max="10" value="7" class="form-input" oninput="this.nextElementSibling.textContent = this.value">
                    <span style="font-weight: bold; color: var(--primary);">7</span>
                </div>
                <div class="form-group">
                    <label class="form-label">Estrés (1-10)</label>
                    <input type="range" name="stress" min="1" max="10" value="5" class="form-input" oninput="this.nextElementSibling.textContent = this.value">
                    <span style="font-weight: bold; color: var(--primary);">5</span>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label class="form-label">Síntomas</label>
                    <textarea name="symptoms" class="form-textarea" placeholder="Describe cualquier síntoma (dolor de cabeza, fatiga, etc.)"></textarea>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label class="form-label">Notas</label>
                    <textarea name="notes" class="form-textarea" placeholder="Observaciones adicionales"></textarea>
                </div>
                <div style="grid-column: 1 / -1; display: flex; gap: 10px; justify-content: flex-end;">
                    <button type="button" class="btn btn-secondary" onclick="app.closeModal()">Cancelar</button>
                    <button type="submit" class="btn btn-primary">Guardar</button>
                </div>
            </form>
        `;

        document.getElementById('health-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);

            const systolic = formData.get('systolic');
            const diastolic = formData.get('diastolic');

            await db.addHealthLog({
                date: formData.get('date'),
                weight: formData.get('weight') ? parseFloat(formData.get('weight')) : null,
                bloodPressure: systolic && diastolic ? {
                    systolic: parseInt(systolic),
                    diastolic: parseInt(diastolic)
                } : null,
                heartRate: formData.get('heartRate') ? parseInt(formData.get('heartRate')) : null,
                mood: parseInt(formData.get('mood')),
                energy: parseInt(formData.get('energy')),
                stress: parseInt(formData.get('stress')),
                symptoms: formData.get('symptoms') ? formData.get('symptoms').split(',').map(s => s.trim()) : [],
                notes: formData.get('notes')
            });

            this.closeModal();
            this.showNotification('Métricas de salud guardadas', 'success');
            await this.loadDashboard();
        });

        this.openModal();
    }

    // ==================== EXPORTACIÓN ====================
    async exportData() {
        try {
            const data = await db.exportAllData();
            const json = JSON.stringify(data, null, 2);
            const blob = new Blob([json], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `protocolo-circadiano-${new Date().toISOString().split('T')[0]}.json`;
            a.click();
            URL.revokeObjectURL(url);

            this.showNotification('Datos exportados exitosamente', 'success');
        } catch (error) {
            console.error('Error exportando datos:', error);
            this.showNotification('Error al exportar datos', 'error');
        }
    }

    // ==================== VISTAS ADICIONALES ====================
    async loadSleepView() {
        // Implementación completa de vista de sueño
        const view = document.getElementById('sleep-view');
        view.innerHTML = '<div class="spinner"></div>';

        setTimeout(() => {
            view.innerHTML = `
                <div class="content-section">
                    <div class="section-header">
                        <h3 class="section-title">Historial de Sueño</h3>
                        <button class="btn btn-primary" onclick="app.logSleep()">+ Registrar Sueño</button>
                    </div>
                    <p>Vista de historial de sueño en desarrollo...</p>
                </div>
            `;
        }, 500);
    }

    async loadProtocolView() {
        const view = document.getElementById('protocol-view');
        view.innerHTML = `
            <div class="content-section">
                <div class="section-header">
                    <h3 class="section-title">Tu Protocolo Circadiano</h3>
                </div>
                <p style="margin-bottom: 20px;">Protocolo personalizado para horario 23:00 - 07:00 hrs</p>
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-time">07:00 - 07:30</div>
                        <div class="timeline-content">
                            <strong>🕶️ Regreso con protección</strong><br>
                            Usa gafas oscuras, evita luz solar directa
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">08:30 - 16:30</div>
                        <div class="timeline-content">
                            <strong>😴 SUEÑO PRINCIPAL (8h)</strong><br>
                            Oscuridad total, 16-19°C, silencio
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">18:00 - 19:00</div>
                        <div class="timeline-content">
                            <strong>🏃 Ejercicio moderado</strong><br>
                            30-40 min cardio, preferiblemente con luz natural
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">23:00 - 07:00</div>
                        <div class="timeline-content">
                            <strong>💼 TURNO DE TRABAJO</strong><br>
                            Luz brillante >1000 lux, cafeína estratégica
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    async loadSettingsView() {
        const view = document.getElementById('settings-view');
        view.innerHTML = `
            <div class="content-section">
                <div class="section-header">
                    <h3 class="section-title">Configuración</h3>
                </div>
                <div class="form-group">
                    <label class="form-label">Notificaciones del navegador</label>
                    <button class="btn btn-primary" onclick="app.requestNotificationPermission()">Activar Notificaciones</button>
                </div>
                <div class="form-group">
                    <label class="form-label">Importar datos</label>
                    <input type="file" accept=".json" id="import-file" class="form-input">
                    <button class="btn btn-secondary" onclick="app.importData()">Importar</button>
                </div>
                <div class="form-group">
                    <label class="form-label">Gestión de datos</label>
                    <button class="btn btn-secondary" onclick="app.exportData()">Exportar Datos</button>
                    <button class="btn" style="background: #ef4444; color: white;" onclick="app.clearAllData()">Limpiar Todos los Datos</button>
                </div>
            </div>
        `;
    }

    // ==================== UTILIDADES ====================
    openModal() {
        document.getElementById('modal').classList.add('active');
    }

    closeModal() {
        document.getElementById('modal').classList.remove('active');
    }

    showNotification(message, type = 'success') {
        const notification = document.getElementById('notification');
        const content = document.getElementById('notification-content');

        content.textContent = message;
        notification.className = `notification ${type} show`;

        if (this.notificationTimeout) {
            clearTimeout(this.notificationTimeout);
        }

        this.notificationTimeout = setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }

    async requestNotificationPermission() {
        if ('Notification' in window) {
            const permission = await Notification.requestPermission();
            if (permission === 'granted') {
                this.showNotification('Notificaciones activadas', 'success');
            }
        }
    }

    async checkNotifications() {
        // Verificar si es hora de recordatorios
        const now = new Date();
        const hour = now.getHours();

        // Recordatorio de suplementos matutinos (08:00)
        if (hour === 8 && now.getMinutes() < 5) {
            this.sendNotification('Hora de tomar suplementos matutinos', 'Melatonina, Magnesio antes de dormir');
        }

        // Recordatorio de ejercicio (18:00)
        if (hour === 18 && now.getMinutes() < 5) {
            this.sendNotification('Hora de ejercicio', '30-40 min de actividad física');
        }
    }

    sendNotification(title, body) {
        if ('Notification' in window && Notification.permission === 'granted') {
            new Notification(title, {
                body,
                icon: '🌙',
                badge: '🌙'
            });
        }
    }

    showQuickLog() {
        // Mostrar menú rápido de registro
        this.logSleep();
    }

    async clearAllData() {
        if (confirm('¿Estás seguro de que quieres eliminar TODOS los datos? Esta acción no se puede deshacer.')) {
            await db.clearAll();
            this.showNotification('Todos los datos han sido eliminados', 'success');
            await this.loadDashboard();
        }
    }

    viewAll(type) {
        // Implementar navegación a vista completa
        console.log('Ver todo:', type);
    }
}

// Inicializar aplicación
const app = new CircadianApp();

// Cargar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => app.init());
} else {
    app.init();
}
