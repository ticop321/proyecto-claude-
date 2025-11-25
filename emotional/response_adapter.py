"""
Adaptador de Respuestas
Ajusta el tono y contenido de las respuestas según el estado emocional
"""

from typing import Dict
from .emotion_detector import EstadoEmocional


class ResponseAdapter:
    """
    Adapta las respuestas según el estado emocional del usuario
    """

    def __init__(self):
        self.tonos = self._definir_tonos()

    def _definir_tonos(self) -> Dict[str, Dict]:
        """Define las características de cada tono de respuesta"""
        return {
            "empatico": {
                "apertura": [
                    "Entiendo que esta situación debe ser muy difícil para usted.",
                    "Comprendo su preocupación, es totalmente normal sentirse así.",
                    "Lamento mucho que esté pasando por esto.",
                    "Entiendo lo duro que debe ser atravesar esta situación."
                ],
                "cierre": [
                    "Estoy aquí para ayudarle en lo que necesite.",
                    "No está solo/a en esto, hay soluciones posibles.",
                    "Recuerde que cuenta con protección legal y apoyo profesional.",
                    "Le acompañaré en este proceso paso a paso."
                ],
                "estilo": "cálido, comprensivo, cercano"
            },
            "tecnico": {
                "apertura": [
                    "Paso a analizar su consulta desde el punto de vista jurídico.",
                    "Procedemos al análisis legal de la situación planteada.",
                    "A continuación, el análisis técnico-jurídico del caso."
                ],
                "cierre": [
                    "Para más detalles, consulte con un abogado colegiado.",
                    "Esta información es orientativa. Se recomienda asesoramiento personalizado.",
                    "Le recomiendo contactar con un letrado especializado."
                ],
                "estilo": "profesional, preciso, objetivo"
            },
            "pedagogico": {
                "apertura": [
                    "Le voy a explicar esto de forma clara y sencilla.",
                    "Permítame explicarle cómo funciona este aspecto legal paso a paso.",
                    "Voy a desglosar esta cuestión para que quede totalmente clara."
                ],
                "cierre": [
                    "Espero haber aclarado sus dudas. Si tiene más preguntas, adelante.",
                    "¿Ha quedado claro? No dude en preguntar lo que necesite.",
                    "Si algo no ha quedado claro, por favor pregúnteme sin problema."
                ],
                "estilo": "didáctico, claro, accesible"
            },
            "tecnico_comprensivo": {
                "apertura": [
                    "Entiendo que ser acusado es una situación muy estresante. Vamos a analizar su caso con rigor.",
                    "Comprendo su situación. Procedamos al análisis jurídico de forma objetiva.",
                    "Entiendo su preocupación. Analicemos los aspectos legales de su caso."
                ],
                "cierre": [
                    "Hay opciones de defensa viables. Un abogado podrá desarrollarlas.",
                    "La ley ofrece garantías y medios de defensa. No está indefenso.",
                    "Existen vías legales para defender sus derechos adecuadamente."
                ],
                "estilo": "profesional pero comprensivo, equilibrado"
            },
            "contencion": {
                "apertura": [
                    "⚠️ IMPORTANTE: Veo que está pasando por una situación de crisis.",
                    "⚠️ Detecto que puede estar en una situación de emergencia.",
                    "⚠️ Su seguridad es lo primero. Necesita ayuda profesional inmediata."
                ],
                "mensaje_principal": [
                    "Por favor, contacte INMEDIATAMENTE con estos servicios de emergencia:",
                    "Es fundamental que hable YA con profesionales especializados:",
                    "Necesita atención profesional urgente. Estos recursos pueden ayudarle:"
                ],
                "enfasis": "⚠️ Esta es una situación que requiere atención profesional especializada, no solo asesoramiento legal.",
                "estilo": "directo, claro, enfocado en seguridad"
            }
        }

    def adaptar_respuesta(self, respuesta_base: str, estado: EstadoEmocional) -> str:
        """
        Adapta una respuesta según el estado emocional

        Args:
            respuesta_base: Respuesta técnica base
            estado: Estado emocional del usuario

        Returns:
            Respuesta adaptada al tono apropiado
        """
        tono = estado.recomendacion_tono
        config_tono = self.tonos.get(tono, self.tonos["tecnico"])

        # Caso especial: contención de crisis
        if tono == "contencion":
            return self._respuesta_contencion(estado)

        # Construcción de respuesta adaptada
        respuesta_adaptada = ""

        # Apertura empática
        import random
        apertura = random.choice(config_tono["apertura"])
        respuesta_adaptada += f"{apertura}\n\n"

        # Contenido principal (respuesta base)
        respuesta_adaptada += respuesta_base

        # Cierre apropiado
        cierre = random.choice(config_tono["cierre"])
        respuesta_adaptada += f"\n\n{cierre}"

        # Añadir disclaimer si urgencia alta
        if estado.nivel_urgencia in ["Alta", "Crítica"]:
            respuesta_adaptada += self._disclaimer_urgencia()

        return respuesta_adaptada

    def _respuesta_contencion(self, estado: EstadoEmocional) -> str:
        """Genera respuesta de contención en caso de crisis"""
        from .emotion_detector import EmotionDetector

        detector = EmotionDetector()
        recursos = detector.obtener_recursos_emergencia("suicidio")

        respuesta = "⚠️ **ATENCIÓN URGENTE** ⚠️\n\n"

        respuesta += "Veo que está atravesando una situación de crisis muy difícil. "
        respuesta += "**Su seguridad y bienestar son lo más importante.**\n\n"

        respuesta += "## RECURSOS DE EMERGENCIA INMEDIATA:\n\n"

        # Recursos según el tipo de crisis
        if any(ind in estado.indicadores for ind in ["suicidio", "matarme", "morir"]):
            respuesta += "### 📞 Teléfono de Atención a la Conducta Suicida\n"
            respuesta += "**024**\n"
            respuesta += "- Atención 24 horas\n"
            respuesta += "- Gratuito y confidencial\n"
            respuesta += "- Profesionales especializados\n\n"

        if any(ind in estado.indicadores for ind in ["violencia", "maltrato", "pegar", "golpear"]):
            respuesta += "### 📞 Teléfono contra la Violencia de Género\n"
            respuesta += "**016**\n"
            respuesta += "- Atención 24 horas\n"
            respuesta += "- No deja rastro en la factura\n"
            respuesta += "- Asesoramiento y derivación urgente\n\n"

        respuesta += "### 📞 Emergencias Generales\n"
        respuesta += "**112** - Policía, ambulancia, emergencias\n"
        respuesta += "**091** - Policía Nacional\n"
        respuesta += "**062** - Guardia Civil\n\n"

        respuesta += "---\n\n"
        respuesta += "⚠️ **Por favor, contacte con estos servicios AHORA MISMO.** ⚠️\n\n"
        respuesta += "Son profesionales especializados que pueden ayudarle de forma inmediata. "
        respuesta += "No está solo/a, y hay personas preparadas para ayudarle en esta situación.\n\n"

        respuesta += "El asesoramiento legal es importante, pero en este momento **su seguridad y bienestar son la prioridad absoluta**.\n\n"

        respuesta += "---\n\n"
        respuesta += "*Nota: Este sistema no puede sustituir la atención de profesionales especializados en crisis. "
        respuesta += "Los recursos indicados ofrecen ayuda inmediata y confidencial.*"

        return respuesta

    def _disclaimer_urgencia(self) -> str:
        """Disclaimer para casos de urgencia"""
        return (
            "\n\n---\n\n"
            "⚠️ **IMPORTANTE - URGENCIA DETECTADA**\n\n"
            "Si tiene una citación judicial próxima o un plazo a punto de vencer, "
            "contacte INMEDIATAMENTE con un abogado colegiado. Los plazos procesales "
            "son perentorios (no se pueden extender) y su pérdida puede tener consecuencias graves.\n\n"
            "**Servicios de orientación jurídica gratuita:**\n"
            "- Turno de oficio del Colegio de Abogados de su ciudad\n"
            "- Justicia Gratuita (si cumple requisitos económicos)\n"
            "- Servicios de orientación jurídica de ayuntamientos\n"
        )

    def generar_mensaje_derivacion(self, tipo: str) -> str:
        """Genera mensaje de derivación a profesionales"""
        mensajes = {
            "abogado": (
                "**Le recomiendo encarecidamente contactar con un abogado penalista.**\n\n"
                "Este es un caso que requiere asesoramiento profesional personalizado. "
                "Un letrado especializado podrá:\n"
                "- Analizar toda la documentación\n"
                "- Diseñar una estrategia de defensa específica\n"
                "- Representarle ante los tribunales\n"
                "- Proteger sus derechos procesales\n\n"
                "**Cómo encontrar un abogado:**\n"
                "- Colegio de Abogados de su ciudad (turno de oficio)\n"
                "- Justicia Gratuita (si cumple requisitos)\n"
                "- Abogados especializados en Derecho Penal\n"
            ),
            "psicologo": (
                "**Le recomiendo también apoyo psicológico profesional.**\n\n"
                "Atravesar un proceso penal (como víctima o acusado) es muy estresante. "
                "Un psicólogo especializado puede ayudarle a:\n"
                "- Gestionar la ansiedad y el estrés\n"
                "- Procesar emocionalmente la situación\n"
                "- Mantener la salud mental durante el proceso\n\n"
                "Muchos Colegios de Abogados ofrecen servicio de apoyo psicológico gratuito para víctimas."
            ),
            "policia": (
                "**Si está en peligro inminente, contacte con la Policía:**\n\n"
                "- **091** - Policía Nacional\n"
                "- **062** - Guardia Civil\n"
                "- **112** - Emergencias generales\n\n"
                "Si ha sido víctima de un delito reciente, presente denuncia cuanto antes "
                "para que se puedan asegurar las pruebas y adoptar medidas de protección si son necesarias."
            ),
            "servicios_sociales": (
                "**Servicios Sociales pueden ofrecerle apoyo:**\n\n"
                "Los Servicios Sociales de su ayuntamiento o comunidad autónoma pueden proporcionar:\n"
                "- Ayudas económicas\n"
                "- Alojamiento temporal\n"
                "- Asesoramiento y orientación\n"
                "- Derivación a recursos especializados\n\n"
                "Contacte con los Servicios Sociales de su localidad para más información."
            )
        }

        return mensajes.get(tipo, "Se recomienda contactar con profesionales especializados.")

    def ajustar_lenguaje_tecnico(self, texto: str, nivel: str) -> str:
        """
        Ajusta el nivel de tecnicismo del lenguaje

        Args:
            texto: Texto original
            nivel: 'alto', 'medio', 'bajo'

        Returns:
            Texto adaptado al nivel
        """
        # Diccionario de traducciones de términos técnicos
        traducciones = {
            "alto": {
                # Términos técnicos completos
            },
            "medio": {
                "tipo penal": "delito",
                "subsunción": "aplicación de la ley al caso",
                "bien jurídico protegido": "derecho o valor que protege la ley",
                "dolo": "intención de cometer el delito",
                "culpa": "negligencia o descuido",
                "eximente": "causa que elimina la responsabilidad",
                "atenuante": "circunstancia que reduce la pena",
                "agravante": "circunstancia que aumenta la pena"
            },
            "bajo": {
                "tipo penal": "delito",
                "subsunción": "ver si los hechos encajan en la ley",
                "bien jurídico protegido": "lo que la ley protege",
                "dolo": "hacerlo a propósito",
                "culpa": "hacerlo sin querer por descuido",
                "eximente": "razón para no ser castigado",
                "atenuante": "razón para rebajar el castigo",
                "agravante": "razón para aumentar el castigo",
                "querella": "acusación formal",
                "diligencias previas": "investigación del caso",
                "juicio oral": "juicio",
                "sentencia": "decisión del juez"
            }
        }

        if nivel not in traducciones:
            return texto

        texto_adaptado = texto
        for tecnico, simple in traducciones[nivel].items():
            texto_adaptado = texto_adaptado.replace(tecnico, simple)

        return texto_adaptado
