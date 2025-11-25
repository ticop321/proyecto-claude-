"""
Asesor Estratégico Procesal
Proporciona recomendaciones sobre estrategia de defensa y acusación
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class RecomendacionEstrategica:
    """Recomendación estratégica"""
    tipo: str  # defensa, acusacion, procedimental
    prioridad: str  # Alta, Media, Baja
    accion: str
    fundamento: str
    riesgos: List[str]
    beneficios: List[str]


class StrategicAdvisor:
    """
    Asesor estratégico procesal
    Analiza riesgos y oportunidades, recomienda estrategias
    """

    def __init__(self):
        pass

    def analizar_posicion_procesal(self, rol: str, caso: Dict) -> Dict[str, any]:
        """
        Analiza la posición procesal de una parte

        Args:
            rol: 'defensa', 'acusacion_publica', 'acusacion_particular'
            caso: Información del caso

        Returns:
            Análisis de fortalezas, debilidades, oportunidades y amenazas (FODA)
        """
        if rol == 'defensa':
            return self._analizar_posicion_defensa(caso)
        elif rol in ['acusacion_publica', 'acusacion_particular']:
            return self._analizar_posicion_acusacion(caso)
        else:
            return {}

    def _analizar_posicion_defensa(self, caso: Dict) -> Dict[str, List[str]]:
        """Análisis FODA para la defensa"""
        return {
            "fortalezas": [
                "Presunción de inocencia como punto de partida",
                "Carga de la prueba sobre la acusación",
                "Principio in dubio pro reo",
                "Derecho a no declarar contra sí mismo"
            ],
            "debilidades": [
                "Posible existencia de pruebas de cargo sólidas",
                "Antecedentes penales (si existen)",
                "Dificultad probatoria de versión exculpatoria"
            ],
            "oportunidades": [
                "Atenuantes aplicables",
                "Posibilidad de conformidad con rebaja de pena",
                "Suspen sión o sustitución de la pena",
                "Vicios procedimentales aprovechables"
            ],
            "amenazas": [
                "Prueba de cargo contundente",
                "Testigos de la acusación",
                "Pruebas periciales adversas",
                "Riesgo de prisión provisional"
            ]
        }

    def _analizar_posicion_acusacion(self, caso: Dict) -> Dict[str, List[str]]:
        """Análisis FODA para la acusación"""
        return {
            "fortalezas": [
                "Pruebas de cargo disponibles",
                "Presunción de veracidad de atestados policiales",
                "Apoyo de peritos oficiales",
                "Testimonio de la víctima"
            ],
            "debilidades": [
                "Carga de la prueba",
                "Necesidad de probar más allá de duda razonable",
                "Posibles vicios en obtención de pruebas"
            ],
            "oportunidades": [
                "Jurisprudencia favorable",
                "Prueba preconstituida sólida",
                "Confesión del acusado",
                "Agravantes aplicables"
            ],
            "amenazas": [
                "Defensa activa y técnica",
                "Insuficiencia probatoria sobrevenida",
                "Vulneración de derechos fundamentales",
                "Contradicciones en testigos"
            ]
        }

    def recomendar_estrategia_defensa(self, analisis_caso: Dict) -> List[RecomendacionEstrategica]:
        """Recomienda estrategia de defensa según el caso"""
        recomendaciones = []

        # Estrategia 1: Presunción de inocencia
        recomendaciones.append(RecomendacionEstrategica(
            tipo="defensa",
            prioridad="Alta",
            accion="Invocar presunción de inocencia e insuficiencia probatoria",
            fundamento="Art. 24.2 CE - Derecho a presunción de inocencia. La acusación debe probar todos los elementos del tipo.",
            riesgos=["Requiere demostrar insuficiencia de prueba de cargo"],
            beneficios=["Sentencia absolutoria si la prueba es insuficiente", "No requiere probar inocencia activamente"]
        ))

        # Estrategia 2: Atenuantes
        recomendaciones.append(RecomendacionEstrategica(
            tipo="defensa",
            prioridad="Alta",
            accion="Acreditar circunstancias atenuantes aplicables",
            fundamento="Arts. 21, 66 CP - Las atenuantes reducen la pena incluso con condena",
            riesgos=["Implica aceptar cierta responsabilidad"],
            beneficios=["Rebaja sustancial de pena", "Posibilidad de suspensión o sustitución"]
        ))

        # Estrategia 3: Conformidad
        recomendaciones.append(RecomendacionEstrategica(
            tipo="defensa",
            prioridad="Media",
            accion="Valorar conformidad con acusación con rebaja de pena",
            fundamento="Art. 787 LECrim - Conformidad con rebaja de 1/3 de pena",
            riesgos=["Renuncia a juicio y recursos limitados", "Antecedentes penales"],
            beneficios=["Rebaja automática de 1/3", "Evita incertidumbre del juicio", "Menor pena de prisión"]
        ))

        # Estrategia 4: Nulidades
        recomendaciones.append(RecomendacionEstrategica(
            tipo="defensa",
            prioridad="Alta si procede",
            accion="Denunciar vulneración de derechos fundamentales y nulidad de pruebas",
            fundamento="Art. 11.1 LOPJ - Prueba ilícita. Tutela judicial efectiva (art. 24 CE)",
            riesgos=["Difícil de probar", "Requiere fundamentación sólida"],
            beneficios=["Exclusión de prueba de cargo", "Posible absolución por falta de pruebas"]
        ))

        # Estrategia 5: Versión alternativa
        recomendaciones.append(RecomendacionEstrategica(
            tipo="defensa",
            prioridad="Media",
            accion="Construir versión alternativa de los hechos compatible con inocencia",
            fundamento="In dubio pro reo - Duda razonable beneficia al acusado",
            riesgos=["Requiere credibilidad y prueba de apoyo"],
            beneficios=["Genera duda razonable", "No requiere probar certeza, solo posibilidad"]
        ))

        return recomendaciones

    def recomendar_estrategia_acusacion(self, analisis_caso: Dict) -> List[RecomendacionEstrategica]:
        """Recomienda estrategia de acusación"""
        recomendaciones = []

        # Estrategia 1: Prueba de cargo
        recomendaciones.append(RecomendacionEstrategica(
            tipo="acusacion",
            prioridad="Alta",
            accion="Asegurar prueba de cargo sólida sobre todos los elementos del tipo",
            fundamento="Presunción de inocencia exige prueba de cargo válida, lícita y suficiente",
            riesgos=["Insuficiencia probatoria puede llevar a absolución"],
            beneficios=["Cumplimiento de carga probatoria", "Mayor probabilidad de condena"]
        ))

        # Estrategia 2: Testigos y peritos
        recomendaciones.append(RecomendacionEstrategica(
            tipo="acusacion",
            prioridad="Alta",
            accion="Preparar exhaustivamente a testigos y peritos",
            fundamento="La prueba testifical y pericial es fundamental en el juicio oral",
            riesgos=["Testigos pueden contradecirse o retractarse"],
            beneficios=["Prueba directa de los hechos", "Mayor credibilidad ante el tribunal"]
        ))

        # Estrategia 3: Calificación precisa
        recomendaciones.append(RecomendacionEstrategica(
            tipo="acusacion",
            prioridad="Alta",
            accion="Calificación jurídica precisa y calificación alternativa subsidiaria",
            fundamento="Evitar absolución por error en calificación",
            riesgos=["Calificación excesiva puede no prosperar"],
            beneficios=["Mayor probabilidad de condena", "Alternativas si no prospera calificación principal"]
        ))

        # Estrategia 4: Agravantes
        recomendaciones.append(RecomendacionEstrategica(
            tipo="acusacion",
            prioridad="Media",
            accion="Acreditar circunstancias agravantes si concurren",
            fundamento="Arts. 22, 66 CP - Agravantes aumentan la pena",
            riesgos=["Requiere prueba específica de cada agravante"],
            beneficios=["Mayor pena", "Refleja mayor gravedad del hecho"]
        ))

        return recomendaciones

    def evaluar_riesgos_procesales(self, rol: str, caso: Dict) -> Dict[str, List[str]]:
        """Evalúa los riesgos procesales según el rol"""
        riesgos = {
            "altos": [],
            "medios": [],
            "bajos": []
        }

        if rol == "defensa":
            # Riesgos para la defensa
            if caso.get("prueba_cargo_solida"):
                riesgos["altos"].append("Prueba de cargo sólida - Alto riesgo de condena")

            if caso.get("antecedentes"):
                riesgos["medios"].append("Antecedentes penales - Posible agravante de reincidencia")

            if caso.get("delito_grave"):
                riesgos["altos"].append("Delito grave - Riesgo de pena privativa de libertad elevada")

            if caso.get("prision_provisional"):
                riesgos["altos"].append("Prisión provisional decretada - Impacto en defensa")

        elif rol in ["acusacion_publica", "acusacion_particular"]:
            # Riesgos para la acusación
            if caso.get("prueba_debil"):
                riesgos["altos"].append("Prueba insuficiente - Riesgo de absolución")

            if caso.get("vicios_procedimentales"):
                riesgos["altos"].append("Vicios procedimentales - Riesgo de nulidad de pruebas")

            if caso.get("testigos_poco_creibles"):
                riesgos["medios"].append("Credibilidad de testigos cuestionable")

        return riesgos

    def recomendar_medidas_cautelares(self, caso: Dict) -> List[str]:
        """Recomienda sobre medidas cautelares"""
        recomendaciones = []

        recomendaciones.append("**Prisión provisional (art. 503 LECrim):**")
        recomendaciones.append("- Requiere: indicios racionales de criminalidad + riesgo de fuga o reiteración delictiva")
        recomendaciones.append("- Proporcional: solo para delitos con pena de prisión")
        recomendaciones.append("- Temporal: plazos máximos según gravedad del delito")

        recomendaciones.append("\n**Alternativas a la prisión provisional:**")
        recomendaciones.append("- Libertad provisional con fianza")
        recomendaciones.append("- Retirada de pasaporte")
        recomendaciones.append("- Comparecencias periódicas")
        recomendaciones.append("- Prohibición de salida del territorio nacional")
        recomendaciones.append("- Prohibición de aproximación o comunicación con víctima")

        recomendaciones.append("\n**Recomendación:** Solicitar medida menos gravosa que sea suficiente para asegurar los fines del proceso")

        return recomendaciones

    def recomendar_recursos(self, sentencia_tipo: str, fundamentos: List[str]) -> List[RecomendacionEstrategica]:
        """Recomienda qué recursos interponer"""
        recomendaciones = []

        if sentencia_tipo == "juzgado_penal":
            recomendaciones.append(RecomendacionEstrategica(
                tipo="procedimental",
                prioridad="Alta",
                accion="Recurso de apelación ante Audiencia Provincial",
                fundamento="Art. 790 LECrim - Contra sentencias de Juzgado de lo Penal",
                riesgos=["Confirmación de sentencia", "Posible condena en costas"],
                beneficios=["Segunda instancia completa", "Revisión de hechos y derecho", "Efecto suspensivo"]
            ))

        if sentencia_tipo == "audiencia_provincial" and "pena_grave" in fundamentos:
            recomendaciones.append(RecomendacionEstrategica(
                tipo="procedimental",
                prioridad="Alta",
                accion="Recurso de casación ante Tribunal Supremo",
                fundamento="Art. 847 LECrim - Si pena superior a 5 años",
                riesgos=["Muy formalista", "Tasa de estimación baja", "Sin efecto suspensivo"],
                beneficios=["Unificación de doctrina", "Corrección de infracciones graves"]
            ))

        if "vulneracion_derechos_fundamentales" in fundamentos:
            recomendaciones.append(RecomendacionEstrategica(
                tipo="procedimental",
                prioridad="Alta",
                accion="Recurso de amparo ante Tribunal Constitucional",
                fundamento="Art. 53.2 CE - Protección de derechos fundamentales",
                riesgos=["Admisión muy restrictiva", "Requiere agotamiento previo de recursos", "Muy largo"],
                beneficios=["Protección máxima de derechos fundamentales", "Jurisprudencia vinculante"]
            ))

        return recomendaciones

    def calcular_probabilidad_exito(self, estrategia: str, factores: Dict) -> Tuple[str, float]:
        """
        Calcula probabilidad estimada de éxito de una estrategia
        (Simplificado - en producción usaría ML y datos históricos)
        """
        # Factores: pruebas, jurisprudencia_favorable, calidad_defensa, etc.

        probabilidad = 50.0  # Base

        if factores.get("pruebas_solidas"):
            probabilidad += 20.0
        if factores.get("jurisprudencia_favorable"):
            probabilidad += 15.0
        if factores.get("atenuantes"):
            probabilidad += 10.0
        if factores.get("debilidad_acusacion"):
            probabilidad += 15.0

        if factores.get("antecedentes"):
            probabilidad -= 10.0
        if factores.get("agravantes"):
            probabilidad -= 15.0

        # Limitar entre 0-100
        probabilidad = max(0.0, min(100.0, probabilidad))

        # Clasificación
        if probabilidad >= 75:
            clasificacion = "Alta"
        elif probabilidad >= 50:
            clasificacion = "Media-Alta"
        elif probabilidad >= 25:
            clasificacion = "Media-Baja"
        else:
            clasificacion = "Baja"

        return (clasificacion, probabilidad)

    def generar_plan_accion(self, rol: str, fase_procesal: str) -> List[str]:
        """Genera un plan de acción según rol y fase procesal"""
        planes = {
            ("defensa", "instruccion"): [
                "1. Personarse como acusado con abogado",
                "2. Estudiar diligencias y pruebas de cargo",
                "3. Solicitar diligencias de descargo",
                "4. Valorar declaración (derecho a guardar silencio)",
                "5. Impugnar pruebas ilícitas si las hay",
                "6. Oponerse a medidas cautelares o solicitar alternativas",
                "7. Preparar defensa para fase intermedia"
            ],
            ("defensa", "juicio_oral"): [
                "1. Preparar cuestiones previas",
                "2. Revisar proposición de prueba",
                "3. Preparar contrainterrogatorios",
                "4. Ensayar declaración del acusado (si declara)",
                "5. Preparar informe oral de defensa",
                "6. Preparar escrito de conclusiones definitivas",
                "7. Preparar última palabra del acusado"
            ],
            ("acusacion", "instruccion"): [
                "1. Personarse como acusación (particular o popular)",
                "2. Proponer diligencias de investigación",
                "3. Asegurar prueba preconstituida",
                "4. Impulsar la instrucción",
                "5. Oponerse al archivo/sobreseimiento",
                "6. Solicitar medidas cautelares si procede"
            ],
            ("acusacion", "juicio_oral"): [
                "1. Presentar escrito de acusación",
                "2. Proponer prueba",
                "3. Preparar interrogatorios de testigos y peritos",
                "4. Preparar documentación de cargo",
                "5. Preparar informe oral de acusación",
                "6. Solicitar pena y responsabilidad civil"
            ]
        }

        return planes.get((rol, fase_procesal), ["Plan no disponible para esta combinación"])

    def advertir_plazos_criticos(self, fase: str) -> List[str]:
        """Advierte sobre plazos críticos a vigilar"""
        plazos = {
            "instruccion": [
                "⏰ Diligencias previas: 6 meses (máx. 18 meses)",
                "⏰ Prisión provisional: plazos máximos según pena",
                "⏰ Proposición de diligencias: durante la instrucción"
            ],
            "intermedia": [
                "⏰ Escrito de acusación: 10 días desde conclusión instrucción",
                "⏰ Escrito de defensa: 10 días desde traslado acusación",
                "⏰ Proposición de prueba: 5 días"
            ],
            "juicio": [
                "⏰ Preparación recurso apelación: 5 días desde sentencia",
                "⏰ Interposición recurso apelación: 10 días",
                "⏰ Preparación casación: 5 días",
                "⏰ Interposición casación: 20 días"
            ],
            "recursos": [
                "⏰ Apelación preparación: 5 días",
                "⏰ Apelación interposición: 10 días",
                "⏰ Casación preparación: 5 días",
                "⏰ Casación interposición: 20 días",
                "⏰ Amparo constitucional: 30 días"
            ]
        }

        return plazos.get(fase, ["Fase no reconocida"])
