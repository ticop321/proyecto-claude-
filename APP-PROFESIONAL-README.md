# 🌙 Protocolo Circadiano Pro - Aplicación Profesional

## 📱 Descripción

Aplicación web profesional completa para el seguimiento y gestión del protocolo de descanso circadiano para trabajadores nocturnos. **Totalmente funcional, interactiva y con almacenamiento local.**

## ✨ Características Principales

### 🎯 Dashboard Interactivo
- **Métricas en tiempo real** de sueño, suplementos, ejercicio y salud
- **Estadísticas automáticas** de últimos 7 días
- **Gráficos de tendencias** visuales
- **Timeline de actividad** reciente
- **Indicadores de progreso** animados

### 😴 Módulo de Sueño
- Registro de horarios de dormir y despertar
- **Cálculo automático** de duración de sueño
- Escala de calidad (1-10)
- Registro de interrupciones
- Notas personalizadas
- Estadísticas de promedio semanal

### 💊 Control de Suplementos
- Lista de suplementos recomendados
- Registro de adherencia diaria
- **Cálculo automático** de % de adherencia
- Historial completo
- Recordatorios configurables

### 🏃 Registro de Ejercicio
- Tipos: Cardio, Fuerza, Flexibilidad, Mixto
- Duración en minutos
- Nivel de intensidad
- Contador de días activos
- Total de minutos semanales

### 🫀 Métricas de Salud
- Peso corporal
- Presión arterial (sistólica/diastólica)
- Frecuencia cardíaca
- Estado de ánimo (1-10)
- Nivel de energía (1-10)
- Nivel de estrés (1-10)
- Registro de síntomas
- **Score de bienestar** calculado automáticamente

### 📊 Análisis y Reportes
- Gráficos de tendencias
- Estadísticas comparativas
- Promedios semanales
- Identificación de patrones

### 🔔 Notificaciones
- Recordatorios del navegador
- Alertas para suplementos (08:00)
- Recordatorio de ejercicio (18:00)
- Personalizables

### 💾 Gestión de Datos
- **Almacenamiento local** con IndexedDB
- **No requiere conexión** a internet
- **Exportación** de datos en JSON
- **Importación** de respaldos
- Persistencia automática
- Datos completamente privados

## 🚀 Cómo Usar la Aplicación

### Instalación
1. **Descarga el archivo** `app-profesional.html`
2. **Abre el archivo** en tu navegador (Chrome, Firefox, Edge recomendados)
3. ¡Listo! La aplicación funciona completamente sin servidor

### Primeros Pasos

1. **Activar Notificaciones** (opcional)
   - Ve a Configuración
   - Click en "Activar Notificaciones"
   - Acepta el permiso del navegador

2. **Registrar tu primer sueño**
   - Dashboard → "Registrar Sueño"
   - Ingresa hora de dormir y despertar
   - Califica calidad del sueño
   - Guardar

3. **Registrar suplementos**
   - Dashboard → "Tomar Suplementos"
   - Selecciona los que tomaste
   - Guardar

4. **Registrar ejercicio**
   - Dashboard → "Registrar Ejercicio"
   - Tipo, duración, intensidad
   - Guardar

5. **Métricas de salud**
   - Dashboard → "Métricas Salud"
   - Ingresa peso, presión, estado de ánimo, etc.
   - Guardar

### Navegación

**Menú Lateral:**
- 📊 **Dashboard**: Vista general y acciones rápidas
- 😴 **Sueño**: Historial detallado de sueño
- 💊 **Suplementos**: Control de adherencia
- 🏃 **Ejercicio**: Registro de actividad física
- 🫀 **Salud**: Métricas y tendencias de salud
- 📋 **Protocolo**: Tu protocolo circadiano completo
- 📈 **Reportes**: Análisis y gráficos detallados
- ⚙️ **Configuración**: Ajustes y gestión de datos

### Exportar Datos

1. Click en **"Exportar"** (botón superior derecho)
2. Se descargará un archivo JSON con todos tus datos
3. Guarda este archivo como respaldo

### Importar Datos

1. Ve a **Configuración**
2. Selecciona archivo JSON de respaldo
3. Click en **"Importar"**
4. Tus datos se restaurarán

## 🎨 Interfaz

### Dashboard
- **4 Tarjetas** de estadísticas principales
- **Acciones rápidas** para registro
- **Timeline** de actividad reciente
- **Gráfico** de tendencias de sueño

### Formularios Modales
- Diseño limpio y profesional
- Validación de datos
- Guardado instantáneo
- Feedback visual

### Gráficos
- Tendencias de última semana
- Visualización de progreso
- Comparativas automáticas

## 💻 Tecnología

- **HTML5**: Estructura semántica
- **CSS3**: Diseño profesional responsive
- **JavaScript Vanilla**: Sin dependencias externas
- **IndexedDB**: Base de datos local del navegador
- **Canvas API**: Gráficos nativos
- **Notification API**: Recordatorios del navegador
- **LocalStorage**: Configuraciones

## 📱 Compatibilidad

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+
- ✅ Responsive (móvil y escritorio)

## 🔒 Privacidad

- **100% local**: Todos los datos se almacenan solo en tu navegador
- **Sin servidor**: No se envía información a ningún lugar
- **Privado**: Solo tú tienes acceso a tus datos
- **Offline**: Funciona sin conexión a internet

## 📊 Datos que se Registran

### Sueño
- Fecha
- Hora de dormir
- Hora de despertar
- Duración (calculada)
- Calidad (1-10)
- Interrupciones
- Notas

### Suplementos
- Fecha y hora
- Lista de suplementos tomados
- Estado (tomado/no tomado)
- Notas

### Ejercicio
- Fecha
- Tipo (cardio, fuerza, flexibilidad)
- Duración (minutos)
- Intensidad (baja, media, alta)
- Notas

### Salud
- Fecha
- Peso
- Presión arterial
- Frecuencia cardíaca
- Estado de ánimo
- Nivel de energía
- Nivel de estrés
- Síntomas
- Notas

## 🎯 Casos de Uso

### Uso Diario
1. **Mañana** (después del turno): Registrar sueño
2. **Tarde** (antes de ejercicio): Registrar suplementos
3. **Noche** (después de ejercicio): Registrar actividad física
4. **Semanal**: Revisar estadísticas y tendencias
5. **Mensual**: Exportar datos para consulta médica

### Seguimiento Médico
- Exporta tus datos mensuales
- Comparte el archivo JSON con tu médico
- Análisis de tendencias a largo plazo
- Identificación de patrones

### Optimización Personal
- Identifica correlaciones (sueño vs. energía)
- Ajusta protocolo según resultados
- Mide efectividad de cambios
- Mantén adherencia al protocolo

## 🔧 Solución de Problemas

### Los datos no se guardan
- Verifica que tu navegador soporta IndexedDB
- No uses modo incógnito
- Limpia caché si hay problemas

### Notificaciones no funcionan
- Verifica permisos del navegador
- Activa notificaciones en Configuración
- Prueba en navegador compatible

### La app no carga
- Usa navegador moderno (Chrome, Firefox, Edge)
- Verifica que JavaScript esté habilitado
- Abre la consola (F12) para ver errores

## 📈 Próximas Mejoras

- [ ] Más tipos de gráficos
- [ ] Exportación a PDF
- [ ] Modo oscuro
- [ ] Recordatorios personalizados
- [ ] Integración con dispositivos wearables
- [ ] Análisis predictivo con IA

## 🤝 Soporte

Si encuentras algún problema o tienes sugerencias, abre un issue en el repositorio.

## 📄 Licencia

Uso personal y educativo. Consulta con profesional médico para implementación del protocolo.

---

**Versión 1.0** - Aplicación Profesional Completa
Desarrollado con evidencia científica sobre ritmos circadianos y trabajo nocturno.
