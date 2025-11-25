"""
Detector de Estado Emocional
Analiza el mensaje del usuario para detectar su estado emocional
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class EstadoEmocional:
    """Estado emocional detectado"""
    emocion_principal: str
    intensidad: str  # Baja, Media, Alta
    emociones_secundarias: List[str]
    indicadores: List[str]
    nivel_urgencia: str  # Normal, Media, Alta, Crítica
    requiere_derivacion: bool
    recomendacion_tono: str  # empático, técnico, pedagógico, contencion


class EmotionDetector:
    """
    Detector de emociones en mensajes de usuarios
    Identifica ansiedad, miedo, confusión, ira, desesperación, etc.
    """

    def __init__(self):
        self.palabras_clave_emociones = self._cargar_palabras_clave()

    def _cargar_palabras_clave(self) -> Dict[str, List[str]]:
        """Carga palabras clave asociadas a cada emoción"""
        return {
            "ansiedad": [
                "preocupado", "nervioso", "ansioso", "inquieto", "estresado",
                "no puedo dormir", "no sé qué hacer", "angustiado", "agobiado",
                "tengo miedo", "me siento mal", "no puedo más"
            ],
            "miedo": [
                "miedo", "terror", "asustado", "pánico", "temor", "amenaza",
                "me van a", "van a hacerme", "peligro", "riesgo", "vulnerable"
            ],
            "confusion": [
                "no entiendo", "confundido", "perdido", "no sé", "dudas",
                "no comprendo", "qué significa", "cómo funciona", "explícame",
                "no me aclaro"
            ],
            "ira": [
                "rabia", "enfadado", "furioso", "indignado", "injusticia",
                "no es justo", "me han engañado", "abuso", "cabrón", "hijos de puta"
            ],
            "desesperacion": [
                "desesperado", "no hay salida", "todo está perdido", "no tengo esperanza",
                "no puedo seguir", "me quiero morir", "suicidio", "acabar con todo",
                "ya no puedo más", "sin solución"
            ],
            "vergüenza": [
                "vergüenza", "humillado", "avergonzado", "culpa", "arrepentido",
                "me siento sucio", "no puedo mirarlo a la cara", "me da vergüenza"
            ],
            "victima": [
                "me han", "me hicieron", "abusaron de mí", "me atacaron",
                "víctima", "agredido", "violado", "maltratado", "amenazado"
            ],
            "acusado": [
                "me acusan", "dicen que", "no es verdad", "inocente",
                "no lo hice", "falsa acusación", "me han denunciado", "citación judicial"
            ],
            "urgencia": [
                "urgente", "inmediato", "ahora mismo", "hoy", "rápido",
                "cuanto antes", "tengo citación", "mañana", "plazo", "vence"
            ],
            "crisis": [
                "suicidio", "matarme", "acabar con mi vida", "no quiero vivir",
                "matar", "vengarme", "hacerle daño", "violencia", "arma"
            ]
        }

    def detectar_emocion(self, mensaje: str) -> EstadoEmocional:
        """
        Detecta el estado emocional del usuario a partir de su mensaje

        Args:
            mensaje: Texto del mensaje del usuario

        Returns:
            EstadoEmocional con toda la información detectada
        """
        mensaje_lower = mensaje.lower()

        # Detectar todas las emociones presentes
        emociones_detectadas = {}
        indicadores_encontrados = []

        for emocion, palabras in self.palabras_clave_emociones.items():
            count = 0
            indicadores = []
            for palabra in palabras:
                if palabra in mensaje_lower:
                    count += 1
                    indicadores.append(palabra)

            if count > 0:
                emociones_detectadas[emocion] = count
                indicadores_encontrados.extend(indicadores)

        # Determinar emoción principal
        if emociones_detectadas:
            emocion_principal = max(emociones_detectadas, key=emociones_detectadas.get)
        else:
            emocion_principal = "neutral"

        # Determinar intensidad
        total_indicadores = sum(emociones_detectadas.values())
        if total_indicadores >= 5:
            intensidad = "Alta"
        elif total_indicadores >= 2:
            intensidad = "Media"
        else:
            intensidad = "Baja"

        # Emociones secundarias
        emociones_secundarias = [
            em for em, count in emociones_detectadas.items()
            if em != emocion_principal and count > 0
        ]

        # Nivel de urgencia
        nivel_urgencia = self._evaluar_urgencia(emociones_detectadas, mensaje_lower)

        # Requiere derivación?
        requiere_derivacion = self._evaluar_derivacion(emociones_detectadas, mensaje_lower)

        # Tono recomendado
        tono_recomendado = self._recomendar_tono(emocion_principal, intensidad, nivel_urgencia)

        return EstadoEmocional(
            emocion_principal=emocion_principal,
            intensidad=intensidad,
            emociones_secundarias=emociones_secundarias,
            indicadores=indicadores_encontrados,
            nivel_urgencia=nivel_urgencia,
            requiere_derivacion=requiere_derivacion,
            recomendacion_tono=tono_recomendado
        )

    def _evaluar_urgencia(self, emociones: Dict[str, int], mensaje: str) -> str:
        """Evalúa el nivel de urgencia del caso"""
        # Urgencia crítica
        if emociones.get("crisis", 0) > 0:
            return "Crítica"

        # Urgencia alta
        if (emociones.get("desesperacion", 0) >= 2 or
            emociones.get("urgencia", 0) >= 2 or
            "citación" in mensaje or
            "juicio mañana" in mensaje):
            return "Alta"

        # Urgencia media
        if (emociones.get("ansiedad", 0) >= 2 or
            emociones.get("miedo", 0) >= 2 or
            emociones.get("urgencia", 0) > 0):
            return "Media"

        # Urgencia normal
        return "Normal"

    def _evaluar_derivacion(self, emociones: Dict[str, int], mensaje: str) -> bool:
        """Evalúa si se debe derivar a profesionales de emergencia"""
        # Crisis suicida
        if any(palabra in mensaje for palabra in ["suicidio", "matarme", "acabar con mi vida", "no quiero vivir"]):
            return True

        # Violencia inminente
        if any(palabra in mensaje for palabra in ["voy a matarlo", "voy a hacerle daño", "tengo un arma"]):
            return True

        # Violencia de género activa
        if any(palabra in mensaje for palabra in ["me está pegando", "me tiene encerrada", "me va a matar"]):
            return True

        # Desesperación extrema
        if emociones.get("desesperacion", 0) >= 3 and emociones.get("crisis", 0) > 0:
            return True

        return False

    def _recomendar_tono(self, emocion: str, intensidad: str, urgencia: str) -> str:
        """Recomienda el tono de respuesta apropiado"""
        # Crisis o derivación
        if urgencia == "Crítica":
            return "contencion"

        # Confusión → Pedagógico
        if emocion == "confusion":
            return "pedagogico"

        # Ansiedad, miedo, desesperación → Empático
        if emocion in ["ansiedad", "miedo", "desesperacion", "vergüenza", "victima"]:
            return "empatico"

        # Acusado, ira → Técnico pero comprensivo
        if emocion in ["acusado", "ira"]:
            return "tecnico_comprensivo"

        # Neutral → Técnico
        return "tecnico"

    def generar_informe_emocional(self, estado: EstadoEmocional) -> str:
        """Genera un informe del estado emocional detectado"""
        informe = "## ANÁLISIS EMOCIONAL\n\n"

        informe += f"**Emoción principal:** {estado.emocion_principal.capitalize()} ({estado.intensidad})\n\n"

        if estado.emociones_secundarias:
            informe += f"**Emociones secundarias:** {', '.join(estado.emociones_secundarias)}\n\n"

        informe += f"**Nivel de urgencia:** {estado.nivel_urgencia}\n\n"

        if estado.requiere_derivacion:
            informe += "⚠️ **REQUIERE DERIVACIÓN INMEDIATA A PROFESIONALES**\n\n"

        informe += f"**Tono recomendado:** {estado.recomendacion_tono}\n\n"

        if estado.indicadores:
            informe += f"**Indicadores detectados:** {', '.join(estado.indicadores[:5])}\n\n"

        return informe

    def obtener_recursos_emergencia(self, tipo_crisis: str) -> Dict[str, str]:
        """Obtiene recursos de emergencia según el tipo de crisis"""
        recursos = {
            "suicidio": {
                "telefono": "024 - Teléfono de atención a la conducta suicida",
                "descripcion": "Servicio confidencial y gratuito de atención a personas en crisis suicida, 24 horas"
            },
            "violencia_genero": {
                "telefono": "016 - Teléfono contra la violencia de género",
                "descripcion": "Atención 24 horas, no deja rastro en factura telefónica"
            },
            "emergencias": {
                "telefono": "112 - Emergencias",
                "descripcion": "Policía, bomberos, ambulancia - Emergencias generales"
            },
            "policia": {
                "telefono": "091 - Policía Nacional",
                "descripcion": "Atención inmediata en casos de delitos o peligro"
            },
            "guardia_civil": {
                "telefono": "062 - Guardia Civil",
                "descripcion": "Atención en zonas rurales y carreteras"
            },
            "menores": {
                "telefono": "116111 - ANAR (Ayuda a Niños y Adolescentes en Riesgo)",
                "descripcion": "Atención especializada a menores de edad, 24 horas"
            }
        }

        return recursos
