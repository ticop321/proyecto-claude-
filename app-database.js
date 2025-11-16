// Database Manager - IndexedDB para almacenamiento local
class CircadianDB {
    constructor() {
        this.dbName = 'CircadianProtocolDB';
        this.version = 1;
        this.db = null;
    }

    // Inicializar base de datos
    async init() {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open(this.dbName, this.version);

            request.onerror = () => reject(request.error);
            request.onsuccess = () => {
                this.db = request.result;
                resolve(this.db);
            };

            request.onupgradeneeded = (event) => {
                const db = event.target.result;

                // Store para registros de sueño
                if (!db.objectStoreNames.contains('sleep')) {
                    const sleepStore = db.createObjectStore('sleep', {
                        keyPath: 'id',
                        autoIncrement: true
                    });
                    sleepStore.createIndex('date', 'date', { unique: false });
                }

                // Store para suplementos
                if (!db.objectStoreNames.contains('supplements')) {
                    const suppStore = db.createObjectStore('supplements', {
                        keyPath: 'id',
                        autoIncrement: true
                    });
                    suppStore.createIndex('date', 'date', { unique: false });
                }

                // Store para ejercicio
                if (!db.objectStoreNames.contains('exercise')) {
                    const exStore = db.createObjectStore('exercise', {
                        keyPath: 'id',
                        autoIncrement: true
                    });
                    exStore.createIndex('date', 'date', { unique: false });
                }

                // Store para métricas de salud
                if (!db.objectStoreNames.contains('health')) {
                    const healthStore = db.createObjectStore('health', {
                        keyPath: 'id',
                        autoIncrement: true
                    });
                    healthStore.createIndex('date', 'date', { unique: false });
                }

                // Store para notas/diario
                if (!db.objectStoreNames.contains('notes')) {
                    const notesStore = db.createObjectStore('notes', {
                        keyPath: 'id',
                        autoIncrement: true
                    });
                    notesStore.createIndex('date', 'date', { unique: false });
                }

                // Store para configuración
                if (!db.objectStoreNames.contains('settings')) {
                    db.createObjectStore('settings', { keyPath: 'key' });
                }
            };
        });
    }

    // Métodos genéricos
    async add(storeName, data) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction([storeName], 'readwrite');
            const store = transaction.objectStore(storeName);
            const request = store.add(data);

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async getAll(storeName) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction([storeName], 'readonly');
            const store = transaction.objectStore(storeName);
            const request = store.getAll();

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async getByDate(storeName, date) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction([storeName], 'readonly');
            const store = transaction.objectStore(storeName);
            const index = store.index('date');
            const request = index.getAll(date);

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async getByDateRange(storeName, startDate, endDate) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction([storeName], 'readonly');
            const store = transaction.objectStore(storeName);
            const index = store.index('date');
            const range = IDBKeyRange.bound(startDate, endDate);
            const request = index.getAll(range);

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async update(storeName, data) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction([storeName], 'readwrite');
            const store = transaction.objectStore(storeName);
            const request = store.put(data);

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async delete(storeName, id) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction([storeName], 'readwrite');
            const store = transaction.objectStore(storeName);
            const request = store.delete(id);

            request.onsuccess = () => resolve();
            request.onerror = () => reject(request.error);
        });
    }

    // Métodos específicos para Sueño
    async addSleepLog(data) {
        const sleepData = {
            date: data.date || new Date().toISOString().split('T')[0],
            bedTime: data.bedTime,
            wakeTime: data.wakeTime,
            duration: data.duration, // en minutos
            quality: data.quality, // 1-10
            interruptions: data.interruptions || 0,
            notes: data.notes || '',
            timestamp: new Date().toISOString()
        };
        return await this.add('sleep', sleepData);
    }

    async getSleepStats(days = 7) {
        const endDate = new Date().toISOString().split('T')[0];
        const startDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000)
            .toISOString().split('T')[0];

        const logs = await this.getByDateRange('sleep', startDate, endDate);

        if (logs.length === 0) return null;

        const avgDuration = logs.reduce((sum, log) => sum + log.duration, 0) / logs.length;
        const avgQuality = logs.reduce((sum, log) => sum + log.quality, 0) / logs.length;

        return {
            avgDuration: Math.round(avgDuration),
            avgQuality: avgQuality.toFixed(1),
            totalLogs: logs.length,
            logs: logs
        };
    }

    // Métodos específicos para Suplementos
    async addSupplementLog(data) {
        const suppData = {
            date: data.date || new Date().toISOString().split('T')[0],
            supplements: data.supplements, // array de nombres
            time: data.time,
            taken: data.taken !== false, // boolean
            notes: data.notes || '',
            timestamp: new Date().toISOString()
        };
        return await this.add('supplements', suppData);
    }

    async getSupplementAdherence(days = 7) {
        const endDate = new Date().toISOString().split('T')[0];
        const startDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000)
            .toISOString().split('T')[0];

        const logs = await this.getByDateRange('supplements', startDate, endDate);

        if (logs.length === 0) return 0;

        const taken = logs.filter(log => log.taken).length;
        return Math.round((taken / logs.length) * 100);
    }

    // Métodos específicos para Ejercicio
    async addExerciseLog(data) {
        const exData = {
            date: data.date || new Date().toISOString().split('T')[0],
            type: data.type, // 'cardio', 'strength', 'flexibility'
            duration: data.duration, // en minutos
            intensity: data.intensity, // 'low', 'medium', 'high'
            notes: data.notes || '',
            timestamp: new Date().toISOString()
        };
        return await this.add('exercise', exData);
    }

    async getExerciseStats(days = 7) {
        const endDate = new Date().toISOString().split('T')[0];
        const startDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000)
            .toISOString().split('T')[0];

        const logs = await this.getByDateRange('exercise', startDate, endDate);

        const uniqueDays = new Set(logs.map(log => log.date)).size;
        const totalDuration = logs.reduce((sum, log) => sum + log.duration, 0);

        return {
            daysExercised: uniqueDays,
            totalMinutes: totalDuration,
            totalSessions: logs.length,
            logs: logs
        };
    }

    // Métodos específicos para Salud
    async addHealthLog(data) {
        const healthData = {
            date: data.date || new Date().toISOString().split('T')[0],
            weight: data.weight || null,
            bloodPressure: data.bloodPressure || null, // { systolic, diastolic }
            heartRate: data.heartRate || null,
            mood: data.mood || null, // 1-10
            energy: data.energy || null, // 1-10
            stress: data.stress || null, // 1-10
            symptoms: data.symptoms || [], // array de strings
            notes: data.notes || '',
            timestamp: new Date().toISOString()
        };
        return await this.add('health', healthData);
    }

    async getHealthTrends(days = 7) {
        const endDate = new Date().toISOString().split('T')[0];
        const startDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000)
            .toISOString().split('T')[0];

        const logs = await this.getByDateRange('health', startDate, endDate);

        if (logs.length === 0) return null;

        const avgMood = logs.filter(l => l.mood).reduce((sum, l) => sum + l.mood, 0) /
            logs.filter(l => l.mood).length || 0;
        const avgEnergy = logs.filter(l => l.energy).reduce((sum, l) => sum + l.energy, 0) /
            logs.filter(l => l.energy).length || 0;
        const avgStress = logs.filter(l => l.stress).reduce((sum, l) => sum + l.stress, 0) /
            logs.filter(l => l.stress).length || 0;

        return {
            avgMood: avgMood.toFixed(1),
            avgEnergy: avgEnergy.toFixed(1),
            avgStress: avgStress.toFixed(1),
            logs: logs
        };
    }

    // Método para obtener todas las métricas del día
    async getDailyMetrics(date) {
        date = date || new Date().toISOString().split('T')[0];

        const [sleep, supplements, exercise, health] = await Promise.all([
            this.getByDate('sleep', date),
            this.getByDate('supplements', date),
            this.getByDate('exercise', date),
            this.getByDate('health', date)
        ]);

        return {
            date,
            sleep: sleep[0] || null,
            supplements: supplements,
            exercise: exercise,
            health: health[0] || null
        };
    }

    // Exportar todos los datos
    async exportAllData() {
        const [sleep, supplements, exercise, health, notes] = await Promise.all([
            this.getAll('sleep'),
            this.getAll('supplements'),
            this.getAll('exercise'),
            this.getAll('health'),
            this.getAll('notes')
        ]);

        return {
            exportDate: new Date().toISOString(),
            version: this.version,
            data: {
                sleep,
                supplements,
                exercise,
                health,
                notes
            }
        };
    }

    // Importar datos
    async importData(jsonData) {
        try {
            const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;

            for (const [storeName, records] of Object.entries(data.data)) {
                for (const record of records) {
                    delete record.id; // Remove ID to allow auto-increment
                    await this.add(storeName, record);
                }
            }

            return true;
        } catch (error) {
            console.error('Error importing data:', error);
            return false;
        }
    }

    // Limpiar toda la base de datos
    async clearAll() {
        const stores = ['sleep', 'supplements', 'exercise', 'health', 'notes'];

        for (const storeName of stores) {
            const transaction = this.db.transaction([storeName], 'readwrite');
            const store = transaction.objectStore(storeName);
            await new Promise((resolve, reject) => {
                const request = store.clear();
                request.onsuccess = resolve;
                request.onerror = () => reject(request.error);
            });
        }
    }

    // Obtener configuración
    async getSetting(key) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['settings'], 'readonly');
            const store = transaction.objectStore('settings');
            const request = store.get(key);

            request.onsuccess = () => resolve(request.result?.value || null);
            request.onerror = () => reject(request.error);
        });
    }

    // Guardar configuración
    async saveSetting(key, value) {
        return await this.update('settings', { key, value });
    }
}

// Inicializar base de datos global
const db = new CircadianDB();

// Inicializar cuando se cargue el DOM
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', async () => {
        try {
            await db.init();
            console.log('✅ Base de datos inicializada');
        } catch (error) {
            console.error('❌ Error al inicializar base de datos:', error);
        }
    });
}
