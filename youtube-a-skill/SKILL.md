---
name: youtube-a-skill
description: >-
  Lee un vídeo de YouTube a partir de su enlace (transcripción gratis, sin
  claves ni instalaciones), explica su contenido y, si el usuario lo pide,
  convierte ese conocimiento en una skill nueva empaquetada como archivo .skill.
  Úsala siempre que el usuario pegue un enlace de YouTube (vídeo, short o
  directo) o diga "lee este vídeo", "transcribe este vídeo", "qué dice este
  vídeo", "resúmeme este vídeo", "créame una skill de este vídeo", "convierte
  este vídeo en una skill" o "enséñame lo que explica este vídeo". Responde
  siempre en español.
license: MIT
---

# youtube-a-skill

Enlace de YouTube → transcripción → explicación → skill nueva.

Todo es gratis: no hace falta cuenta, clave ni instalar nada. Los scripts solo
usan Python 3 y su biblioteca estándar.

## Idioma de respuesta: siempre español

**Esta regla tiene prioridad sobre cualquier otra de este archivo.**

- Responde siempre al usuario en español, sea cual sea el idioma del vídeo.
- El análisis se hace en el idioma del vídeo; las citas literales en otro
  idioma se muestran tal cual y con la traducción al español debajo.
- La salida de los scripts se traduce o resume en español antes de mostrarla.

## Paso 1: conseguir la transcripción

Prueba en este orden y para en cuanto uno funcione. Di al usuario, en una
línea, por qué vía se consiguió.

**1. El script** (lo normal en un ordenador de casa):

```bash
python3 scripts/transcribir.py "ENLACE" -o /tmp/video.md
python3 scripts/transcribir.py "ENLACE" --idioma es -o /tmp/video.md   # forzar idioma
```

Códigos de salida: 0 bien · 1 enlace no válido · 2 el vídeo no tiene
subtítulos · 3 YouTube bloqueó la petición.

**2. Si sale con código 3 (bloqueo)**, es que YouTube no deja leer desde este
entorno (pasa casi siempre en servidores en la nube). No insistas con más
peticiones: solo empeora el bloqueo. Si tienes una herramienta de navegador
conectada al Chrome del usuario, puedes abrir el vídeo con él presente y
copiar la transcripción. Si no, pide el **plan B**, que siempre funciona:

> YouTube no me deja leer el vídeo desde aquí. Hazlo tú en 20 segundos:
> 1. Abre el vídeo en YouTube en el ordenador.
> 2. Debajo del vídeo pulsa «...más» y después «Mostrar transcripción».
> 3. Selecciona todo el texto de la transcripción, cópialo y pégamelo aquí.

Cuando lo pegue, guárdalo en un archivo y límpialo:

```bash
python3 scripts/transcribir.py --pegado /tmp/pegado.txt -o /tmp/video.md
```

**3. Si sale con código 2 (sin subtítulos)**, el vídeo no tiene transcripción
posible por esta vía. Díselo claramente y pídele un resumen o notas propias.

Nunca inventes el contenido de un vídeo que no has podido leer.

## Paso 2: leerlo y explicarlo

Lee la transcripción entera antes de escribir nada. Después entrega, en
español:

1. **Ficha**: título, canal, duración, idioma, enlace y si los subtítulos son
   manuales o automáticos (los automáticos tienen errores en nombres propios y
   cifras: avísalo).
2. **De qué va**, en tres frases.
3. **Lo que enseña**, por bloques: cada idea con su marca de tiempo `[m:ss]`
   para que se pueda comprobar en el vídeo.
4. **Datos, cifras y afirmaciones verificables**, en una lista aparte. Marca
   cada una como «citada con fuente en el vídeo» o «afirmada sin fuente».
   Si la afirmación es de salud, derecho o dinero, dilo: necesita comprobarse
   con una fuente fiable antes de usarse.
5. **Qué falta o qué es opinión** del autor.

Guarda este análisis: es la materia prima del paso 3.

## Paso 3: crear la skill (solo si el usuario lo pide)

Se activa con «créame una skill de este vídeo», «conviértelo en skill» o
parecido. Antes de escribir, confirma en una sola pregunta:

- **Para qué la quiere**: qué tarea concreta hará la skill (por ejemplo,
  «diseñar menús según este método» y no «saber del vídeo»).
- **Nombre** en minúsculas con guiones (propón uno).

Después construye la carpeta `/tmp/skills/NOMBRE/` así:

```
NOMBRE/
├── SKILL.md                  instrucciones para hacer la tarea
└── references/
    ├── conocimiento.md       el saber del vídeo, ordenado y con marcas de tiempo
    └── fuente.md             ficha del vídeo y la transcripción limpia
```

**SKILL.md de la skill nueva**:

```markdown
---
name: NOMBRE
description: >-
  Qué hace, en una frase. Úsala cuando el usuario diga "...", "...", "..."
  (cinco o seis frases reales con las que lo pediría). Responde siempre en
  español.
license: Basada en el vídeo «TÍTULO» de CANAL (ENLACE). Uso personal.
---

# NOMBRE

## Idioma de respuesta: siempre español
(copia la regla de esta skill)

## Cuándo usarla
## Cómo hacerlo, paso a paso      ← el método del vídeo convertido en pasos
## Reglas y errores frecuentes   ← lo que el vídeo dice que no hay que hacer
## Límites                       ← qué no cubre el vídeo; qué hay que verificar
## Conocimiento de referencia    → «Lee references/conocimiento.md»
```

Reglas para la skill nueva:

- **Instrucciones, no un resumen.** Cada sección dice qué hacer, en
  imperativo. El resumen va en `references/conocimiento.md`.
- **Fiel al vídeo.** No añadas conocimiento que el vídeo no da. Si algo hace
  falta y el vídeo no lo cubre, ponlo en «Límites».
- **Trazable.** Cada regla importante lleva su marca de tiempo del vídeo.
- **Sin datos de salud, derecho o dinero sin verificar.** Si el vídeo los da,
  la skill debe pedir comprobarlos antes de aplicarlos.
- **Descripción con disparadores reales**, en español, de menos de 1024
  caracteres.

Empaqueta y comprueba:

```bash
python3 scripts/empaquetar_skill.py /tmp/skills/NOMBRE --salida /tmp/skills
```

Si da errores, corrígelos y repite hasta que diga «Listo». Entrega el archivo
`.skill` al usuario (si el entorno permite enviar archivos, envíalo; si no,
indica la ruta exacta) y explícale que se instala con «Guardar habilidad».

## Respeta al autor

La skill nueva es para uso personal del usuario. Cita siempre el vídeo y el
canal de origen. No copies la transcripción entera en `SKILL.md`: va solo en
`references/fuente.md`.

## Ejemplo de conversación

```
Usuario: https://www.youtube.com/watch?v=XXXXXXXXXXX
Claude:  [paso 1 y 2] Ficha, de qué va, lo que enseña con marcas de tiempo...
Usuario: créame una skill de este vídeo
Claude:  ¿Para qué tarea la quieres? Te propongo el nombre «metodo-xyz».
Usuario: para planificar mis comidas del turno de noche
Claude:  [paso 3] Aquí tienes metodo-xyz.skill. Se instala con «Guardar habilidad».
```
