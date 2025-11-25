"""
Analizador de Casos Penales
Identifica tipos penales, analiza elementos y circunstancias
"""

import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from knowledge.codigo_penal import CodigoPenal, TipoPenal, CircunstanciaModificativa


@dataclass
class AnalisisElementos:
    """Análisis de elementos del tipo penal"""
    elementos_concurrentes: List[str]
    elementos_ausentes: List[str]
    elementos_dudosos: List[str]
    conclusion: str  # "Tipo completo", "Tipo incompleto", "Tipo no concurre"


@dataclass
class ResultadoAnalisis:
    """Resultado completo del análisis de un caso"""
    tipos_penales_identificados: List[TipoPenal]
    tipo_principal: Optional[TipoPenal]
    analisis_elementos: Dict[str, AnalisisElementos]
    circunstancias_atenuantes: List[CircunstanciaModificativa]
    circunstancias_agravantes: List[CircunstanciaModificativa]
    circunstancias_eximentes: List[CircunstanciaModificativa]
    pena_estimada: str
    prescripcion: Dict[str, str]
    calificacion_juridica: str
    fundamentacion: str
    advertencias: List[str]
    alternativas_juridicas: List[str]


class CaseAnalyzer:
    """
    Analizador de casos penales
    Identifica delitos, analiza elementos y circunstancias
    """

    def __init__(self):
        self.codigo_penal = CodigoPenal()

    def analizar_caso(self, hechos: str, contexto: Dict = None) -> ResultadoAnalisis:
        """
        Analiza un caso completo a partir de los hechos

        Args:
            hechos: Descripción de los hechos del caso
            contexto: Información adicional (fecha, lugar, antecedentes, etc.)

        Returns:
            ResultadoAnalisis con todos los elementos del análisis
        """
        if contexto is None:
            contexto = {}

        # Paso 1: Identificar tipos penales posibles
        tipos_identificados = self._identificar_tipos_penales(hechos)

        # Paso 2: Analizar elementos de cada tipo
        analisis_elementos = {}
        for tipo in tipos_identificados:
            analisis = self._analizar_elementos_tipo(hechos, tipo, contexto)
            analisis_elementos[tipo.nombre] = analisis

        # Paso 3: Determinar tipo principal (el que mejor se ajusta)
        tipo_principal = self._determinar_tipo_principal(tipos_identificados, analisis_elementos)

        # Paso 4: Identificar circunstancias modificativas
        atenuantes = self._identificar_atenuantes(hechos, contexto)
        agravantes = self._identificar_agravantes(hechos, contexto)
        eximentes = self._identificar_eximentes(hechos, contexto)

        # Paso 5: Calcular pena estimada
        pena_estimada = self._calcular_pena(tipo_principal, atenuantes, agravantes)

        # Paso 6: Verificar prescripción
        prescripcion = self._verificar_prescripcion(tipo_principal, contexto.get('fecha_hechos'))

        # Paso 7: Generar calificación jurídica
        calificacion = self._generar_calificacion_juridica(
            tipo_principal, atenuantes, agravantes, eximentes
        )

        # Paso 8: Generar fundamentación
        fundamentacion = self._generar_fundamentacion(
            hechos, tipo_principal, analisis_elementos, atenuantes, agravantes, eximentes
        )

        # Paso 9: Generar advertencias
        advertencias = self._generar_advertencias(
            tipo_principal, analisis_elementos, contexto
        )

        # Paso 10: Identificar alternativas jurídicas
        alternativas = self._identificar_alternativas_juridicas(
            tipos_identificados, tipo_principal
        )

        return ResultadoAnalisis(
            tipos_penales_identificados=tipos_identificados,
            tipo_principal=tipo_principal,
            analisis_elementos=analisis_elementos,
            circunstancias_atenuantes=atenuantes,
            circunstancias_agravantes=agravantes,
            circunstancias_eximentes=eximentes,
            pena_estimada=pena_estimada,
            prescripcion=prescripcion,
            calificacion_juridica=calificacion,
            fundamentacion=fundamentacion,
            advertencias=advertencias,
            alternativas_juridicas=alternativas
        )

    def _identificar_tipos_penales(self, hechos: str) -> List[TipoPenal]:
        """Identifica los tipos penales aplicables según los hechos"""
        return self.codigo_penal.identificar_tipos_por_palabras_clave(hechos)

    def _analizar_elementos_tipo(self, hechos: str, tipo: TipoPenal,
                                 contexto: Dict) -> AnalisisElementos:
        """Analiza si concurren los elementos del tipo penal"""
        hechos_lower = hechos.lower()

        elementos_concurrentes = []
        elementos_ausentes = []
        elementos_dudosos = []

        # Analizar elementos objetivos
        for elemento in tipo.elementos_objetivos:
            if self._elemento_presente(elemento, hechos_lower):
                elementos_concurrentes.append(f"✓ {elemento}")
            elif self._elemento_posible(elemento, hechos_lower):
                elementos_dudosos.append(f"? {elemento}")
            else:
                elementos_ausentes.append(f"✗ {elemento}")

        # Analizar elementos subjetivos
        for elemento in tipo.elementos_subjetivos:
            if self._elemento_presente(elemento, hechos_lower):
                elementos_concurrentes.append(f"✓ {elemento}")
            elif self._elemento_posible(elemento, hechos_lower):
                elementos_dudosos.append(f"? {elemento}")
            else:
                elementos_ausentes.append(f"✗ {elemento}")

        # Determinar conclusión
        if not elementos_ausentes and not elementos_dudosos:
            conclusion = "Tipo completo - Todos los elementos concurren"
        elif elementos_ausentes:
            conclusion = f"Tipo incompleto - Faltan elementos: {len(elementos_ausentes)}"
        else:
            conclusion = f"Tipo probable - Elementos dudosos: {len(elementos_dudosos)}"

        return AnalisisElementos(
            elementos_concurrentes=elementos_concurrentes,
            elementos_ausentes=elementos_ausentes,
            elementos_dudosos=elementos_dudosos,
            conclusion=conclusion
        )

    def _elemento_presente(self, elemento: str, hechos: str) -> bool:
        """Verifica si un elemento está claramente presente en los hechos"""
        # Lógica simplificada - en producción sería NLP avanzado
        elemento_lower = elemento.lower()

        # Mapeo de elementos a palabras clave
        keywords = {
            "conducta: matar": ["matar", "muerte", "fallecer", "morir", "acabar con la vida"],
            "dolo": ["intencion", "voluntad", "querer", "proposito", "deliberad"],
            "ánimo de lucro": ["lucro", "dinero", "beneficio", "vender", "ganar", "enriquec"],
            "engaño": ["engaño", "mentira", "falso", "fraudulent", "ardid", "trampa"],
            "violencia": ["violencia", "golpe", "agresi", "fuerza física"],
            "intimidacion": ["amenaza", "intimidar", "miedo", "coaccion"],
            "sin consentimiento": ["sin consentimiento", "en contra de su voluntad", "negativa", "rechazar"],
        }

        # Buscar palabras clave del elemento en los hechos
        for key, words in keywords.items():
            if key in elemento_lower:
                return any(word in hechos for word in words)

        # Búsqueda genérica
        palabras_elemento = elemento_lower.split()
        return any(palabra in hechos for palabra in palabras_elemento if len(palabra) > 3)

    def _elemento_posible(self, elemento: str, hechos: str) -> bool:
        """Verifica si un elemento es posible pero no está claramente expresado"""
        # Lógica para elementos que pueden inferirse
        return "posible" in hechos or "probablemente" in hechos

    def _determinar_tipo_principal(self, tipos: List[TipoPenal],
                                   analisis: Dict[str, AnalisisElementos]) -> Optional[TipoPenal]:
        """Determina cuál es el tipo penal principal del caso"""
        if not tipos:
            return None

        # Ordenar por número de elementos concurrentes
        tipos_ordenados = sorted(
            tipos,
            key=lambda t: len(analisis[t.nombre].elementos_concurrentes) -
                         len(analisis[t.nombre].elementos_ausentes),
            reverse=True
        )

        return tipos_ordenados[0] if tipos_ordenados else None

    def _identificar_atenuantes(self, hechos: str, contexto: Dict) -> List[CircunstanciaModificativa]:
        """Identifica circunstancias atenuantes"""
        atenuantes = []
        hechos_lower = hechos.lower()

        # Arrebato/obcecación
        if any(word in hechos_lower for word in ["arrebato", "obcecacion", "ira", "calentura", "impulso"]):
            atenuante = self.codigo_penal.buscar_circunstancia("atenuante_arrebato")
            if atenuante:
                atenuantes.append(atenuante)

        # Confesión
        if any(word in hechos_lower for word in ["confesar", "confesion", "reconocer", "admitir"]):
            atenuante = self.codigo_penal.buscar_circunstancia("atenuante_confesion")
            if atenuante:
                atenuantes.append(atenuante)

        # Reparación
        if any(word in hechos_lower for word in ["reparar", "reparacion", "devolver", "indemnizar", "pagar"]):
            atenuante = self.codigo_penal.buscar_circunstancia("atenuante_reparacion")
            if atenuante:
                atenuantes.append(atenuante)

        # Adicción
        if any(word in hechos_lower for word in ["adiccion", "drogadicto", "alcoholico", "dependencia"]):
            atenuante = self.codigo_penal.buscar_circunstancia("atenuante_adiccion")
            if atenuante:
                atenuantes.append(atenuante)

        return atenuantes

    def _identificar_agravantes(self, hechos: str, contexto: Dict) -> List[CircunstanciaModificativa]:
        """Identifica circunstancias agravantes"""
        agravantes = []
        hechos_lower = hechos.lower()

        # Alevosía
        if any(word in hechos_lower for word in ["alevosia", "sorpresa", "indefens", "dormid", "espalda"]):
            agravante = self.codigo_penal.buscar_circunstancia("agravante_alevosa")
            if agravante:
                agravantes.append(agravante)

        # Ensañamiento
        if any(word in hechos_lower for word in ["ensañamiento", "sadismo", "crueldad", "tortura", "sufrimiento"]):
            agravante = self.codigo_penal.buscar_circunstancia("agravante_ensanamiento")
            if agravante:
                agravantes.append(agravante)

        # Precio/recompensa
        if any(word in hechos_lower for word in ["precio", "recompensa", "pago", "contrato", "sicario"]):
            agravante = self.codigo_penal.buscar_circunstancia("agravante_precio")
            if agravante:
                agravantes.append(agravante)

        # Abuso de superioridad
        if any(word in hechos_lower for word in ["varios", "grupo", "superioridad", "indefens"]):
            agravante = self.codigo_penal.buscar_circunstancia("agravante_abuso_superioridad")
            if agravante:
                agravantes.append(agravante)

        # Discriminación
        if any(word in hechos_lower for word in ["racista", "xenofob", "homofob", "machista", "discrimin"]):
            agravante = self.codigo_penal.buscar_circunstancia("agravante_discriminacion")
            if agravante:
                agravantes.append(agravante)

        # Abuso de confianza
        if any(word in hechos_lower for word in ["confianza", "amigo", "familiar", "empleado"]):
            agravante = self.codigo_penal.buscar_circunstancia("agravante_abuso_confianza")
            if agravante:
                agravantes.append(agravante)

        # Reincidencia
        if contexto.get("antecedentes") or "antecedentes" in hechos_lower:
            agravante = self.codigo_penal.buscar_circunstancia("agravante_reincidencia")
            if agravante:
                agravantes.append(agravante)

        return agravantes

    def _identificar_eximentes(self, hechos: str, contexto: Dict) -> List[CircunstanciaModificativa]:
        """Identifica circunstancias eximentes"""
        eximentes = []
        hechos_lower = hechos.lower()

        # Legítima defensa
        if any(word in hechos_lower for word in ["defensa", "defender", "agresi", "atacar", "repeler"]):
            if "legitima defensa" in hechos_lower or ("agresi" in hechos_lower and "defens" in hechos_lower):
                eximente = self.codigo_penal.buscar_circunstancia("eximente_legitima_defensa")
                if eximente:
                    eximentes.append(eximente)

        # Anomalía psíquica
        if any(word in hechos_lower for word in ["esquizofrenia", "psicosis", "trastorno mental", "demencia", "incapaz"]):
            eximente = self.codigo_penal.buscar_circunstancia("eximente_anomalia_psiquica")
            if eximente:
                eximentes.append(eximente)

        # Estado de necesidad
        if any(word in hechos_lower for word in ["necesidad", "evitar mal", "hambre extrema"]):
            eximente = self.codigo_penal.buscar_circunstancia("eximente_estado_necesidad")
            if eximente:
                eximentes.append(eximente)

        # Miedo insuperable
        if any(word in hechos_lower for word in ["miedo insuperable", "terror", "amenaza grave"]):
            eximente = self.codigo_penal.buscar_circunstancia("eximente_miedo_insuperable")
            if eximente:
                eximentes.append(eximente)

        return eximentes

    def _calcular_pena(self, tipo: Optional[TipoPenal], atenuantes: List, agravantes: List) -> str:
        """Calcula la pena estimada"""
        if not tipo:
            return "No se puede calcular pena sin tipo penal principal"

        pena = f"**Pena básica:** {tipo.pena_minima} a {tipo.pena_maxima}\n"

        if atenuantes:
            pena += f"\n**Con {len(atenuantes)} atenuante(s):**\n"
            for at in atenuantes:
                pena += f"  - {at.nombre}: {at.efectos}\n"
            pena += "  → Probable rebaja de pena en grado inferior\n"

        if agravantes:
            pena += f"\n**Con {len(agravantes)} agravante(s):**\n"
            for ag in agravantes:
                pena += f"  - {ag.nombre}: {ag.efectos}\n"
            pena += "  → Posible agravación según art. 66 CP\n"

        pena += f"\n**Gravedad del delito:** {tipo.gravedad}"

        return pena

    def _verificar_prescripcion(self, tipo: Optional[TipoPenal], fecha_hechos: Optional[str]) -> Dict[str, str]:
        """Verifica si el delito o la pena han prescrito"""
        if not tipo:
            return {"estado": "No aplicable - sin tipo penal"}

        prescripcion_info = self.codigo_penal.get_prescripcion(tipo.nombre.lower())

        if not fecha_hechos:
            return {
                "delito": prescripcion_info.get("prescripcion_delito", "No determinado"),
                "pena": prescripcion_info.get("prescripcion_pena", "No determinado"),
                "estado": "No se puede calcular sin fecha de los hechos"
            }

        # Aquí iría lógica de cálculo de fechas (simplificado)
        return {
            "delito": prescripcion_info.get("prescripcion_delito", "No determinado"),
            "pena": prescripcion_info.get("prescripcion_pena", "No determinado"),
            "estado": "Requiere cálculo preciso con fecha exacta",
            "fecha_hechos": fecha_hechos
        }

    def _generar_calificacion_juridica(self, tipo: Optional[TipoPenal],
                                       atenuantes: List, agravantes: List,
                                       eximentes: List) -> str:
        """Genera la calificación jurídica formal del caso"""
        if not tipo:
            return "Sin calificación jurídica - tipo penal no determinado"

        calificacion = f"**Delito de {tipo.nombre}**\n\n"
        calificacion += f"📋 **Artículos:** {', '.join(tipo.articulos)} del Código Penal\n\n"
        calificacion += f"🎯 **Bien jurídico protegido:** {tipo.bien_juridico}\n\n"

        if eximentes:
            calificacion += f"⚖️ **Circunstancias eximentes:**\n"
            for ex in eximentes:
                calificacion += f"  - {ex.nombre} (art. {ex.articulo})\n"
            calificacion += "\n"

        if atenuantes:
            calificacion += f"📉 **Circunstancias atenuantes:**\n"
            for at in atenuantes:
                calificacion += f"  - {at.nombre} (art. {at.articulo})\n"
            calificacion += "\n"

        if agravantes:
            calificacion += f"📈 **Circunstancias agravantes:**\n"
            for ag in agravantes:
                calificacion += f"  - {ag.nombre} (art. {ag.articulo})\n"
            calificacion += "\n"

        return calificacion

    def _generar_fundamentacion(self, hechos: str, tipo: Optional[TipoPenal],
                                analisis: Dict[str, AnalisisElementos],
                                atenuantes: List, agravantes: List, eximentes: List) -> str:
        """Genera la fundamentación jurídica completa"""
        if not tipo:
            return "No es posible generar fundamentación sin tipo penal principal"

        fundamentacion = "## FUNDAMENTACIÓN JURÍDICA\n\n"

        # 1. Hechos probados
        fundamentacion += "### 1. HECHOS PROBADOS\n\n"
        fundamentacion += f"{hechos}\n\n"

        # 2. Calificación jurídica
        fundamentacion += "### 2. CALIFICACIÓN JURÍDICA\n\n"
        fundamentacion += f"Los hechos descritos son constitutivos de un delito de **{tipo.nombre}** "
        fundamentacion += f"previsto y penado en los artículos {', '.join(tipo.articulos)} del Código Penal.\n\n"

        # 3. Análisis de elementos
        fundamentacion += "### 3. ELEMENTOS DEL TIPO PENAL\n\n"

        analisis_tipo = analisis.get(tipo.nombre)
        if analisis_tipo:
            fundamentacion += "**Elementos objetivos y subjetivos concurrentes:**\n"
            for elem in analisis_tipo.elementos_concurrentes:
                fundamentacion += f"{elem}\n"
            fundamentacion += "\n"

            if analisis_tipo.elementos_dudosos:
                fundamentacion += "**Elementos que requieren mayor análisis probatorio:**\n"
                for elem in analisis_tipo.elementos_dudosos:
                    fundamentacion += f"{elem}\n"
                fundamentacion += "\n"

        # 4. Circunstancias modificativas
        if eximentes or atenuantes or agravantes:
            fundamentacion += "### 4. CIRCUNSTANCIAS MODIFICATIVAS DE LA RESPONSABILIDAD CRIMINAL\n\n"

            if eximentes:
                fundamentacion += "**Eximentes:**\n"
                for ex in eximentes:
                    fundamentacion += f"- {ex.nombre} (art. {ex.articulo} CP): {ex.descripcion}\n"
                fundamentacion += "\n"

            if atenuantes:
                fundamentacion += "**Atenuantes:**\n"
                for at in atenuantes:
                    fundamentacion += f"- {at.nombre} (art. {at.articulo} CP): {at.descripcion}\n"
                fundamentacion += "\n"

            if agravantes:
                fundamentacion += "**Agravantes:**\n"
                for ag in agravantes:
                    fundamentacion += f"- {ag.nombre} (art. {ag.articulo} CP): {ag.descripcion}\n"
                fundamentacion += "\n"

        # 5. Conclusión
        fundamentacion += "### 5. CONCLUSIÓN\n\n"
        fundamentacion += f"En consecuencia, los hechos expuestos son subsumibles en el tipo penal de "
        fundamentacion += f"**{tipo.nombre}**, con las circunstancias modificativas señaladas, "
        fundamentacion += f"lo que determina una pena de {tipo.pena_minima} a {tipo.pena_maxima}, "
        fundamentacion += f"que deberá ser modulada por el tribunal en atención a las circunstancias concurrentes.\n\n"

        return fundamentacion

    def _generar_advertencias(self, tipo: Optional[TipoPenal],
                             analisis: Dict[str, AnalisisElementos],
                             contexto: Dict) -> List[str]:
        """Genera advertencias sobre el caso"""
        advertencias = []

        # Advertencia general
        advertencias.append("⚠️ Este análisis es orientativo y no sustituye el asesoramiento de un abogado colegiado")

        # Advertencias específicas del caso
        if tipo:
            analisis_tipo = analisis.get(tipo.nombre)
            if analisis_tipo and analisis_tipo.elementos_dudosos:
                advertencias.append(
                    f"⚠️ Existen elementos dudosos que requieren mayor análisis probatorio: "
                    f"{len(analisis_tipo.elementos_dudosos)} elementos"
                )

            if tipo.gravedad == "Grave":
                advertencias.append("⚠️ Delito GRAVE - Se recomienda asistencia letrada urgente")

            # Advertencia sobre prescripción
            if not contexto.get('fecha_hechos'):
                advertencias.append("⚠️ Para verificar prescripción, es necesario indicar la fecha de los hechos")

        # Advertencias procedimentales
        advertencias.append("⚠️ Consulte los plazos procesales aplicables en su caso concreto")

        return advertencias

    def _identificar_alternativas_juridicas(self, tipos: List[TipoPenal],
                                            tipo_principal: Optional[TipoPenal]) -> List[str]:
        """Identifica calificaciones jurídicas alternativas"""
        alternativas = []

        if not tipo_principal:
            return ["No es posible determinar alternativas sin tipo principal"]

        # Otros tipos identificados como alternativas
        for tipo in tipos:
            if tipo != tipo_principal:
                alternativas.append(
                    f"Calificación alternativa como **{tipo.nombre}** "
                    f"(arts. {', '.join(tipo.articulos)} CP) - {tipo.bien_juridico}"
                )

        # Alternativas por grados de ejecución
        alternativas.append("Valorar posible tentativa (art. 16 CP) si el delito no se consumó")
        alternativas.append("Valorar participación como cómplice o cooperador necesario (arts. 27-29 CP)")

        return alternativas
