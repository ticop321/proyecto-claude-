// Protocolo de Descanso Circadiano - App Logic
// Basado en evidencia científica para trabajadores nocturnos

document.addEventListener('DOMContentLoaded', function() {
    console.log('🌙 Protocolo de Descanso Circadiano iniciado');

    // Inicializar funcionalidades
    initCurrentTimeHighlight();
    initInteractiveElements();
    initLocalStorage();
    addPrintButton();
    addProgressTracker();

    // Actualizar cada minuto
    setInterval(initCurrentTimeHighlight, 60000);
});

/**
 * Resalta el bloque de tiempo actual basado en la hora del sistema
 */
function initCurrentTimeHighlight() {
    const now = new Date();
    const currentHour = now.getHours();
    const currentMinute = now.getMinutes();
    const currentTime = currentHour * 60 + currentMinute; // Minutos desde medianoche

    // Remover highlight previo
    document.querySelectorAll('.time-block').forEach(block => {
        block.classList.remove('current-time');
    });

    // Definir rangos de tiempo (en minutos desde medianoche)
    const timeRanges = [
        { start: 7*60, end: 7*60+30, selector: 0 },      // 07:00-07:30
        { start: 7*60+30, end: 8*60, selector: 1 },      // 07:30-08:00
        { start: 8*60, end: 8*60+30, selector: 2 },      // 08:00-08:30
        { start: 8*60+30, end: 16*60+30, selector: 3 },  // 08:30-16:30 (Sueño)
        { start: 16*60+30, end: 17*60, selector: 4 },    // 16:30-17:00
        { start: 17*60, end: 18*60, selector: 5 },       // 17:00-18:00
        { start: 18*60, end: 19*60, selector: 6 },       // 18:00-19:00
        { start: 19*60, end: 21*60, selector: 7 },       // 19:00-21:00
        { start: 21*60, end: 22*60+30, selector: 8 },    // 21:00-22:30
        { start: 22*60+30, end: 23*60, selector: 9 },    // 22:30-23:00
        { start: 23*60, end: 24*60, selector: 10 },      // 23:00-00:00
        { start: 0, end: 7*60, selector: 10 }            // 00:00-07:00 (trabajo)
    ];

    // Encontrar el bloque actual
    const currentRange = timeRanges.find(range =>
        currentTime >= range.start && currentTime < range.end
    );

    if (currentRange !== undefined) {
        const blocks = document.querySelectorAll('.time-block');
        if (blocks[currentRange.selector]) {
            blocks[currentRange.selector].classList.add('current-time');
            blocks[currentRange.selector].style.border = '3px solid #ff6b6b';
            blocks[currentRange.selector].style.boxShadow = '0 0 20px rgba(255, 107, 107, 0.5)';

            // Scroll suave al elemento actual
            blocks[currentRange.selector].scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        }
    }

    // Mostrar hora actual en consola
    console.log(`⏰ Hora actual: ${currentHour.toString().padStart(2, '0')}:${currentMinute.toString().padStart(2, '0')}`);
}

/**
 * Añade interactividad a los elementos
 */
function initInteractiveElements() {
    // Hacer los bloques de tiempo clicables para marcar como completados
    document.querySelectorAll('.time-block').forEach((block, index) => {
        // Añadir botón de completado
        const checkButton = document.createElement('button');
        checkButton.className = 'check-button';
        checkButton.innerHTML = '✓ Completado';
        checkButton.style.cssText = `
            background: #28a745;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            font-size: 0.9em;
            transition: all 0.3s ease;
        `;

        checkButton.addEventListener('click', function() {
            toggleComplete(block, index);
        });

        block.appendChild(checkButton);

        // Cargar estado guardado
        const savedState = localStorage.getItem(`block_${index}`);
        if (savedState === 'completed') {
            block.classList.add('completed');
            updateCheckButton(block, true);
        }
    });

    // Añadir tooltips informativos
    addTooltips();
}

/**
 * Toggle estado de completado
 */
function toggleComplete(block, index) {
    const isCompleted = block.classList.toggle('completed');

    if (isCompleted) {
        block.style.opacity = '0.7';
        block.style.background = '#d4edda';
        localStorage.setItem(`block_${index}`, 'completed');
    } else {
        block.style.opacity = '1';
        block.style.background = '';
        localStorage.removeItem(`block_${index}`);
    }

    updateCheckButton(block, isCompleted);
    updateProgress();
}

/**
 * Actualiza el botón de check
 */
function updateCheckButton(block, isCompleted) {
    const button = block.querySelector('.check-button');
    if (button) {
        if (isCompleted) {
            button.innerHTML = '↺ Reiniciar';
            button.style.background = '#6c757d';
        } else {
            button.innerHTML = '✓ Completado';
            button.style.background = '#28a745';
        }
    }
}

/**
 * Inicializar localStorage
 */
function initLocalStorage() {
    // Resetear diariamente
    const lastReset = localStorage.getItem('lastReset');
    const today = new Date().toDateString();

    if (lastReset !== today) {
        // Nuevo día, limpiar completados
        for (let i = 0; i < 20; i++) {
            localStorage.removeItem(`block_${i}`);
        }
        localStorage.setItem('lastReset', today);
        console.log('🔄 Progreso diario reseteado');
    }
}

/**
 * Añade botón de imprimir
 */
function addPrintButton() {
    const header = document.querySelector('header');
    const printBtn = document.createElement('button');
    printBtn.innerHTML = '🖨️ Imprimir Protocolo';
    printBtn.style.cssText = `
        background: white;
        color: #1e3c72;
        border: 2px solid white;
        padding: 12px 24px;
        border-radius: 25px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        margin-top: 20px;
        transition: all 0.3s ease;
    `;

    printBtn.addEventListener('mouseenter', function() {
        this.style.background = '#1e3c72';
        this.style.color = 'white';
    });

    printBtn.addEventListener('mouseleave', function() {
        this.style.background = 'white';
        this.style.color = '#1e3c72';
    });

    printBtn.addEventListener('click', function() {
        window.print();
    });

    header.appendChild(printBtn);
}

/**
 * Añade tracker de progreso diario
 */
function addProgressTracker() {
    const protocolSection = document.querySelector('.protocol-section');

    const progressDiv = document.createElement('div');
    progressDiv.className = 'progress-tracker';
    progressDiv.style.cssText = `
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        text-align: center;
    `;

    progressDiv.innerHTML = `
        <h3 style="color: white; margin: 0 0 10px 0;">📊 Progreso de Hoy</h3>
        <div class="progress-bar" style="
            background: rgba(255,255,255,0.3);
            height: 30px;
            border-radius: 15px;
            overflow: hidden;
            margin: 15px 0;
        ">
            <div class="progress-fill" style="
                background: #28a745;
                height: 100%;
                width: 0%;
                transition: width 0.5s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
            "></div>
        </div>
        <p class="progress-text" style="margin: 10px 0 0 0; font-size: 1.1em;">0 de 11 actividades completadas</p>
    `;

    protocolSection.insertBefore(progressDiv, protocolSection.querySelector('.protocol-day'));
    updateProgress();
}

/**
 * Actualiza el progreso
 */
function updateProgress() {
    const totalBlocks = 11; // Bloques principales del día
    let completed = 0;

    for (let i = 0; i < totalBlocks; i++) {
        if (localStorage.getItem(`block_${i}`) === 'completed') {
            completed++;
        }
    }

    const percentage = (completed / totalBlocks) * 100;
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.querySelector('.progress-text');

    if (progressFill && progressText) {
        progressFill.style.width = `${percentage}%`;
        progressFill.textContent = `${Math.round(percentage)}%`;
        progressText.textContent = `${completed} de ${totalBlocks} actividades completadas`;

        // Celebración al completar todo
        if (completed === totalBlocks) {
            progressText.innerHTML = `
                🎉 ¡Excelente! Has completado todas las actividades del día<br>
                <small>Mantener este ritmo es clave para tu salud circadiana</small>
            `;
        }
    }
}

/**
 * Añade tooltips informativos
 */
function addTooltips() {
    // Añadir información contextual sobre términos clave
    const terms = {
        'Melatonina': 'Hormona que regula el ciclo sueño-vigilia. Producida naturalmente por la glándula pineal.',
        'Ritmo circadiano': 'Ciclo biológico de aproximadamente 24 horas que regula funciones fisiológicas.',
        'Luz azul': 'Longitud de onda que suprime la melatonina y afecta el ritmo circadiano.',
        'SCN': 'Núcleo Supraquiasmático: reloj maestro del cerebro ubicado en el hipotálamo.'
    };

    Object.keys(terms).forEach(term => {
        const regex = new RegExp(`\\b${term}\\b`, 'gi');
        document.querySelectorAll('p, li').forEach(element => {
            if (element.innerHTML.match(regex) && !element.querySelector('.tooltip')) {
                element.innerHTML = element.innerHTML.replace(
                    regex,
                    `<span class="tooltip" title="${terms[term]}" style="
                        border-bottom: 2px dotted #667eea;
                        cursor: help;
                    ">${term}</span>`
                );
            }
        });
    });
}

/**
 * Función para exportar datos (futuro)
 */
function exportData() {
    const data = {
        date: new Date().toISOString(),
        completed: [],
        notes: localStorage.getItem('userNotes') || ''
    };

    for (let i = 0; i < 20; i++) {
        if (localStorage.getItem(`block_${i}`) === 'completed') {
            data.completed.push(i);
        }
    }

    console.log('📦 Datos exportados:', data);
    return data;
}

// Exponer funciones globales
window.circadianProtocol = {
    exportData,
    resetProgress: () => {
        for (let i = 0; i < 20; i++) {
            localStorage.removeItem(`block_${i}`);
        }
        location.reload();
    }
};

console.log('✅ App cargada. Funciones disponibles en window.circadianProtocol');
