"""
Motor de Razonamiento Jurídico
Implementa silogismo jurídico y argumentación estructurada
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Argumento:
    """Argumento jurídico estructurado"""
    premisa_mayor: str  # Norma jurídica
    premisa_menor: str  # Hechos del caso
    conclusion: str     # Consecuencia jurídica
    fundamentos: List[str]
    contrargumentos: List[str]
    solidez: str  # Alta, Media, Baja


class LegalReasoning:
    """
    Motor de razonamiento jurídico
    Genera argumentación estructurada y silogismos
    """

    def __init__(self):
        pass

    def construir_silogismo(self, norma: str, hechos: str,
                           conclusion: str) -> Argumento:
        """
        Construye un silogismo jurídico completo

        Estructura:
        - Premisa mayor (norma): "El que matare a otro será castigado..."
        - Premisa menor (hechos): "Juan mató a Pedro..."
        - Conclusión: "Luego Juan debe ser castigado..."
        """
        # Analizar solidez del argumento
        solidez = self._evaluar_solidez(norma, hechos, conclusion)

        # Generar fundamentos
        fundamentos = self._generar_fundamentos(norma, hechos)

        # Identificar posibles contrargumentos
        contrargumentos = self._identificar_contrargumentos(norma, hechos, conclusion)

        return Argumento(
            premisa_mayor=norma,
            premisa_menor=hechos,
            conclusion=conclusion,
            fundamentos=fundamentos,
            contrargumentos=contrargumentos,
            solidez=solidez
        )

    def _evaluar_solidez(self, norma: str, hechos: str, conclusion: str) -> str:
        """Evalúa la solidez del argumento"""
        # Lógica simplificada
        if norma and hechos and conclusion:
            if len(hechos) > 100 and "artículo" in norma.lower():
                return "Alta"
            elif len(hechos) > 50:
                return "Media"
        return "Baja"

    def _generar_fundamentos(self, norma: str, hechos: str) -> List[str]:
        """Genera los fundamentos del argumento"""
        fundamentos = []

        # Fundamento normativo
        fundamentos.append(f"Fundamento normativo: {norma}")

        # Fundamento fáctico
        fundamentos.append(f"Fundamento fáctico: Los hechos acreditados permiten la subsunción en el tipo penal")

        # Fundamento jurisprudencial (ejemplo)
        fundamentos.append("Fundamento jurisprudencial: Doctrina consolidada del Tribunal Supremo")

        return fundamentos

    def _identificar_contrargumentos(self, norma: str, hechos: str,
                                     conclusion: str) -> List[str]:
        """Identifica posibles contrargumentos"""
        contrargumentos = []

        # Contrargumentos típicos
        contrargumentos.append("Posible alegación de ausencia de dolo/culpa")
        contrargumentos.append("Posible concurrencia de causas de justificación o exculpación")
        contrargumentos.append("Valoración probatoria: insuficiencia de prueba de cargo")

        return contrargumentos

    def generar_argumentacion_defensa(self, caso: Dict) -> str:
        """Genera argumentación para la defensa"""
        argumentacion = "## ARGUMENTACIÓN DE LA DEFENSA\n\n"

        argumentacion += "### 1. PRESUNCIÓN DE INOCENCIA\n\n"
        argumentacion += "El acusado goza de presunción de inocencia (art. 24.2 CE), "
        argumentacion += "correspondiendo a la acusación la carga de probar los hechos "
        argumentacion += "y la participación del acusado más allá de toda duda razonable.\n\n"

        argumentacion += "### 2. INSUFICIENCIA PROBATORIA\n\n"
        argumentacion += "- La prueba aportada por la acusación es insuficiente\n"
        argumentacion += "- No se ha acreditado la concurrencia de todos los elementos del tipo\n"
        argumentacion += "- Existen dudas razonables sobre la participación del acusado\n\n"

        argumentacion += "### 3. TESIS ALTERNATIVA\n\n"
        argumentacion += "Los hechos admiten una explicación alternativa compatible con la inocencia, "
        argumentacion += "lo que determina la aplicación del principio \"in dubio pro reo\".\n\n"

        argumentacion += "### 4. ATENUANTES APLICABLES\n\n"
        argumentacion += "En caso de estimarse la concurrencia del tipo penal, concurren las siguientes atenuantes:\n"
        argumentacion += "- [Especificar atenuantes del caso concreto]\n\n"

        argumentacion += "### 5. PETICIÓN\n\n"
        argumentacion += "Por todo lo expuesto, SOLICITO: Sentencia absolutoria por aplicación del principio "
        argumentacion += "de presunción de inocencia, o subsidiariamente, la aplicación de las atenuantes señaladas.\n\n"

        return argumentacion

    def generar_argumentacion_acusacion(self, caso: Dict) -> str:
        """Genera argumentación para la acusación"""
        argumentacion = "## ARGUMENTACIÓN DE LA ACUSACIÓN\n\n"

        argumentacion += "### 1. HECHOS PROBADOS\n\n"
        argumentacion += "Han quedado acreditados los siguientes hechos mediante prueba de cargo "
        argumentacion += "válida, lícita y suficiente:\n"
        argumentacion += "[Enumeración de hechos probados]\n\n"

        argumentacion += "### 2. CALIFICACIÓN JURÍDICA\n\n"
        argumentacion += "Los hechos son constitutivos del delito de [tipo penal], "
        argumentacion += "previsto y penado en los artículos [artículos] del Código Penal.\n\n"

        argumentacion += "### 3. ELEMENTOS DEL TIPO\n\n"
        argumentacion += "Concurren todos los elementos del tipo penal:\n\n"

        argumentacion += "**Elementos objetivos:**\n"
        argumentacion += "- [Elemento 1]\n"
        argumentacion += "- [Elemento 2]\n\n"

        argumentacion += "**Elementos subjetivos:**\n"
        argumentacion += "- Dolo: el acusado conocía y quería el resultado\n"
        argumentacion += "- [Otros elementos subjetivos]\n\n"

        argumentacion += "### 4. PARTICIPACIÓN DEL ACUSADO\n\n"
        argumentacion += "La participación del acusado como autor [material/mediato/coautor/cómplice] "
        argumentacion += "ha quedado acreditada mediante:\n"
        argumentacion += "- [Prueba 1]\n"
        argumentacion += "- [Prueba 2]\n\n"

        argumentacion += "### 5. CIRCUNSTANCIAS MODIFICATIVAS\n\n"
        argumentacion += "Concurren las siguientes circunstancias [agravantes/atenuantes]:\n"
        argumentacion += "- [Circunstancia 1]\n\n"

        argumentacion += "### 6. PETICIÓN\n\n"
        argumentacion += "Por todo lo expuesto, SOLICITO: Sentencia condenatoria por el delito de [tipo penal] "
        argumentacion += "con imposición de la pena de [pena solicitada].\n\n"

        return argumentacion

    def analizar_jurisprudencia_aplicable(self, tipo_penal: str) -> str:
        """Analiza la jurisprudencia aplicable al caso"""
        analisis = f"## JURISPRUDENCIA APLICABLE - {tipo_penal.upper()}\n\n"

        analisis += "### Doctrina del Tribunal Supremo\n\n"
        analisis += "El Tribunal Supremo ha establecido de forma reiterada que para la apreciación "
        analisis += f"del delito de {tipo_penal} es necesario:\n\n"

        # Ejemplos genéricos (en producción usaría base de datos real)
        analisis += "1. La concurrencia de todos los elementos del tipo, tanto objetivos como subjetivos\n"
        analisis += "2. La acreditación mediante prueba de cargo suficiente y lícitamente obtenida\n"
        analisis += "3. La valoración conjunta y razonada de la prueba practicada\n\n"

        analisis += "### Sentencias relevantes\n\n"
        analisis += "- STS [número/fecha]: [Doctrina relevante]\n"
        analisis += "- STS [número/fecha]: [Doctrina relevante]\n\n"

        analisis += "### Aplicación al caso concreto\n\n"
        analisis += "La doctrina jurisprudencial citada resulta aplicable al presente caso en cuanto...\n\n"

        return analisis

    def aplicar_principios_interpretativos(self, norma: str, caso: str) -> Dict[str, str]:
        """
        Aplica los principios de interpretación de la ley penal

        Principios:
        - Legalidad (nullum crimen, nulla poena sine lege)
        - Interpretación restrictiva
        - Prohibición de analogía in malam partem
        - In dubio pro reo
        - Proporcionalidad
        """
        interpretaciones = {}

        interpretaciones["legalidad"] = (
            "Principio de legalidad (art. 25.1 CE): Solo pueden castigarse conductas "
            "expresamente previstas en la ley penal vigente al tiempo de su comisión."
        )

        interpretaciones["restrictiva"] = (
            "Las normas penales sancionadoras deben interpretarse restrictivamente, "
            "sin extender su aplicación más allá de los casos claramente previstos."
        )

        interpretaciones["prohibicion_analogia"] = (
            "Está prohibida la analogía in malam partem (perjudicial para el reo). "
            "No pueden crearse delitos ni agravarse penas por analogía."
        )

        interpretaciones["in_dubio_pro_reo"] = (
            "En caso de duda sobre los hechos o la aplicación de la norma, "
            "debe resolverse de forma favorable al acusado (in dubio pro reo)."
        )

        interpretaciones["proporcionalidad"] = (
            "Las penas deben ser proporcionales a la gravedad del hecho y "
            "la culpabilidad del autor (art. 25.1 CE)."
        )

        return interpretaciones

    def construir_cadena_argumentativa(self, premisas: List[str],
                                       conclusion: str) -> str:
        """Construye una cadena argumentativa lógica"""
        cadena = "## CADENA ARGUMENTATIVA\n\n"

        for i, premisa in enumerate(premisas, 1):
            cadena += f"**{i}.** {premisa}\n\n"

        cadena += f"**CONCLUSIÓN:** {conclusion}\n\n"

        return cadena

    def detectar_falacias(self, argumento: str) -> List[str]:
        """Detecta posibles falacias en un argumento"""
        falacias = []

        # Falacia ad hominem
        if any(word in argumento.lower() for word in ["delincuente habitual", "mala persona"]):
            falacias.append("Posible falacia ad hominem: argumento contra la persona en vez de contra los hechos")

        # Petición de principio
        if "obviamente" in argumento.lower() or "evidentemente" in argumento.lower():
            falacias.append("Posible petición de principio: se da por probado lo que debe demostrarse")

        # Generalización apresurada
        if "siempre" in argumento.lower() or "nunca" in argumento.lower():
            falacias.append("Posible generalización apresurada: uso de términos absolutos sin justificación")

        return falacias

    def generar_esquema_subsuncion(self, norma: str, hechos: str) -> str:
        """Genera un esquema de subsunción (hechos → norma → consecuencia)"""
        esquema = "## ESQUEMA DE SUBSUNCIÓN\n\n"

        esquema += "### 1. SUPUESTO DE HECHO NORMATIVO (Tatbestand)\n"
        esquema += f"{norma}\n\n"

        esquema += "### 2. SUPUESTO DE HECHO REAL\n"
        esquema += f"{hechos}\n\n"

        esquema += "### 3. JUICIO DE SUBSUNCIÓN\n"
        esquema += "¿Los hechos reales se ajustan al supuesto normativo?\n\n"

        esquema += "**Análisis:**\n"
        esquema += "- Elemento 1 del tipo: [Concurre/No concurre] ✓/✗\n"
        esquema += "- Elemento 2 del tipo: [Concurre/No concurre] ✓/✗\n"
        esquema += "- Elemento N del tipo: [Concurre/No concurre] ✓/✗\n\n"

        esquema += "### 4. CONSECUENCIA JURÍDICA\n"
        esquema += "Si todos los elementos concurren → Aplicación de la consecuencia jurídica prevista en la norma\n\n"

        return esquema
