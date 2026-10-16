# Guion del Reel: «A las 4 tu cerebro pide azúcar»

Fecha: 16-10-2026 · Skill: ig-reel (con ig-human e ig-caption) · Duración estimada: ~42 s

## Por qué este contenido

- **Referencia viral:** *"When you don't sleep well, you're automatically going to have higher blood sugars…"* (Beyond Binge Eating), 5,5 veces la mediana de su canal.
- **Fórmula:** condición + consecuencia automática, adaptada al turno de noche.
- **Por qué esta y no la de 19x («la verdadera razón...»):** esa fórmula fracasó en español (0,6x) y esta encaja con tu público (trabajadores nocturnos) y con tu propia experiencia.
- **Puntuación del gancho:** 81 STRONG (`hookscore.py --lang es`, sobre las dos primeras frases).

## Guion

| Tiempo | Lo que dices | Texto en pantalla | Plano |
|---|---|---|---|
| 0:00 | A las 4 tu cerebro pide azúcar. | **4 AM: TU CEREBRO PIDE AZÚCAR** | Primer plano, ya en movimiento: abres un cajón o miras la máquina de vending |
| 0:02 | Y no es falta de voluntad, es química, | NO ES VOLUNTAD | Corte a cámara, de frente |
| 0:05 | y está medida en laboratorio. | | |
| 0:07 | Dos noches durmiendo 4 horas: | 2 NOCHES · 4 HORAS | Cambio de plano |
| 0:09 | la hormona del hambre sube un 28 % | HAMBRE +28 % | Gráfico o gesto con la mano hacia arriba |
| 0:12 | y la que te dice «ya basta» baja un 18 %. | SACIEDAD −18 % | Gesto hacia abajo |
| 0:16 | ¿Y qué te pide? Dulce y harinas. | | Plano de bollería o snacks |
| 0:18 | Hasta un 45 % más. | DULCE Y HARINAS +45 % | |
| 0:20 | En Berkeley lo vieron con escáneres: cuando duermes poco, | ESCÁNER CEREBRAL | Imagen de resonancia o dibujo del cerebro |
| 0:23 | la parte del cerebro que decide con cabeza se apaga | CONTROL ↓ | |
| 0:27 | y la amígdala, la que quiere el premio ya, se enciende. | PREMIO ↑ | |
| 0:31 | Ahí pierdes. | | Pausa corta, mirada a cámara |
| 0:32 | Así que decide antes: sal de casa con 2 tuppers hechos. | DECIDE ANTES | Tú metiendo 2 táperes en la mochila |
| 0:36 | Comenta TURNO y te mando mi plan. | **COMENTA «TURNO»** | A cámara |
| 0:38 | Porque a las 4 no decides tú. Decide tu cerebro. | 4 AM | Vuelta al plano inicial: el bucle |

**Notas de grabación:**
- Graba en vertical, 1080x1920. El texto en pantalla debe quedar entre y=230 e y=1440 y dejar libres los 230 píxeles de la derecha.
- Pon subtítulos en todo el vídeo: la mayoría lo ve primero sin sonido.
- La última frase repite «4» y «cerebro» del gancho para que la repetición del vídeo enlace.
- Velocidad calculada a 165 palabras por minuto. Si hablas más rápido, durará menos de 42 segundos.

## Texto de la publicación

```
Comenta TURNO y te mando mi plan de comidas para trabajar de noche.

Los antojos de dulce a las 4 de la mañana no son falta de voluntad. Dormir poco sube la hormona del hambre y apaga la parte del cerebro que decide con cabeza.

Si trabajas de noche, la solución no es aguantar: es decidir antes de salir de casa.

Fuentes: Spiegel et al., Ann Intern Med 2004 · Greer, Goldstein y Walker, Nat Commun 2013.

#trabajonocturno #nutricion #habitossaludables
```

Revisión con `caption.py`: READY (una sola petición, 3 hashtags, los términos de búsqueda «trabajar de noche» y «antojos de dulce» en la parte visible).

## Datos del guion: comprobados en PubMed

| Afirmación | Fuente |
|---|---|
| Tras 2 noches de 4 horas: grelina +28 %, leptina −18 %, apetito por alimentos densos en calorías y ricos en carbohidratos +33 % a +45 % | Spiegel K, Tasali E, Penev P, Van Cauter E. *Ann Intern Med* 2004. [DOI 10.7326/0003-4819-141-11-200412070-00008](https://doi.org/10.7326/0003-4819-141-11-200412070-00008) |
| Sin dormir, baja la actividad de la corteza frontal e insular al evaluar la comida, sube la de la amígdala y aumenta el deseo de alimentos muy calóricos (UC Berkeley, con resonancia magnética funcional) | Greer SM, Goldstein AN, Walker MP. *Nat Commun* 2013. [DOI 10.1038/ncomms3259](https://doi.org/10.1038/ncomms3259) |

**Límites que conviene conocer (por si te preguntan en comentarios):**
- El estudio de 2004 se hizo con **12 hombres jóvenes y sanos**, durante solo 2 noches.
- El de Berkeley usó **una noche entera sin dormir**, no turnos de noche.
- Ninguno de los dos estudió específicamente a trabajadores nocturnos. El guion habla de «dormir poco», que es lo que se midió.

## Pendiente antes de publicar

- **Petición «Comenta TURNO»:** promete un plan de comidas. Ten el plan listo antes de publicar o cambia la petición.
- **Tu voz:** no existe `~/.claude/instagram/voice.md`. Si me pasas 2 o 3 reels tuyos, ajusto el guion a tu forma de hablar.
