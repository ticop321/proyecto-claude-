"""
Sistema de Jurisprudencia del Tribunal Supremo y Tribunal Constitucional
Base de sentencias relevantes y doctrina jurisprudencial
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sentencia:
    """Sentencia judicial"""
    tribunal: str  # TS, TC, AP, etc.
    numero: str
    fecha: str
    ponente: str
    materia: str
    tipo_penal: str
    resumen: str
    doctrina: str  # Doctrina jurisprudencial establecida
    enlace_cendoj: str
    palabras_clave: List[str]


class Jurisprudencia:
    """
    Base de datos de jurisprudencia penal española
    Sentencias del TS, TC y Audiencias Provinciales relevantes
    """

    def __init__(self):
        self.sentencias = self._cargar_sentencias()

    def _cargar_sentencias(self) -> Dict[str, Sentencia]:
        """Carga sentencias relevantes por materia"""
        sentencias = {}

        # HOMICIDIO - DOLO EVENTUAL
        sentencias["STS_531/2022"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 531/2022",
            fecha="2022-06-08",
            ponente="Manuel Marchena Gómez",
            materia="Homicidio - Dolo eventual vs imprudencia",
            tipo_penal="Homicidio",
            resumen="Distinción entre dolo eventual e imprudencia consciente en casos de homicidio vial. El conductor que conduce de forma temeraria asumiendo el resultado de muerte tiene dolo eventual.",
            doctrina="Para apreciar dolo eventual es necesario: 1) Conocimiento del peligro concreto; 2) Representación del resultado como probable; 3) Aceptación o conformidad con el resultado (teoría de la probabilidad + voluntad). No basta la mera asunción del riesgo si no hay conformidad.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["dolo eventual", "imprudencia", "homicidio vial", "temeridad"]
        )

        # LEGÍTIMA DEFENSA
        sentencias["STS_234/2021"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 234/2021",
            fecha="2021-03-15",
            ponente="Andrés Martínez Arrieta",
            materia="Legítima defensa - Requisitos",
            tipo_penal="Eximente",
            resumen="Aplicación de legítima defensa completa al repeler agresión con arma blanca. Necesidad racional del medio empleado.",
            doctrina="La legítima defensa requiere: 1) Agresión ilegítima (actual o inminente); 2) Necesidad racional del medio empleado (proporcionalidad entre agresión y defensa); 3) Falta de provocación suficiente. La racionalidad del medio se valora ex ante, en el momento de la agresión, considerando circunstancias del caso concreto.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["legitima defensa", "agresion ilegitima", "proporcionalidad", "eximente"]
        )

        # HURTO - ÁNIMO DE LUCRO
        sentencias["STS_789/2020"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 789/2020",
            fecha="2020-11-20",
            ponente="Vicente Magro Servet",
            materia="Hurto - Ánimo de lucro",
            tipo_penal="Hurto",
            resumen="El ánimo de lucro en el hurto no requiere enriquecimiento económico directo, basta con obtener utilidad o beneficio, incluso de uso temporal.",
            doctrina="El ánimo de lucro consiste en el propósito de obtener un beneficio o utilidad, no necesariamente económico. Incluye: a) Lucro patrimonial directo; b) Ahorro de gastos; c) Utilidad de uso; d) Beneficio para tercero. No se requiere incorporación definitiva al patrimonio del autor.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["hurto", "animo de lucro", "apropiacion", "beneficio"]
        )

        # ESTAFA - ENGAÑO BASTANTE
        sentencias["STS_456/2021"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 456/2021",
            fecha="2021-05-12",
            ponente="Ana María Ferrer García",
            materia="Estafa - Engaño bastante",
            tipo_penal="Estafa",
            resumen="El engaño debe ser idóneo, suficiente y adecuado para producir error en el sujeto pasivo, valorado en el caso concreto.",
            doctrina="El 'engaño bastante' requiere: 1) Entidad objetiva suficiente para producir error (no meras exageraciones comerciales); 2) Idoneidad en relación al sujeto pasivo concreto (valoración ex ante); 3) Relación causal entre engaño-error-disposición patrimonial. El engaño debe recaer sobre elementos esenciales del negocio.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["estafa", "engaño bastante", "error", "idoneidad"]
        )

        # ROBO CON VIOLENCIA - INTIMIDACIÓN
        sentencias["STS_678/2019"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 678/2019",
            fecha="2019-10-08",
            ponente="Juan Ramón Berdugo Gómez de la Torre",
            materia="Robo - Intimidación",
            tipo_penal="Robo con violencia",
            resumen="La intimidación en el robo debe ser suficiente para coartar la libertad de la víctima y facilitar el apoderamiento.",
            doctrina="Intimidación: amenaza de un mal grave, inminente, posible y determinante de la entrega. Se valora objetiva y subjetivamente: 1) Gravedad objetiva del mal amenazado; 2) Circunstancias del sujeto pasivo (edad, condiciones); 3) Contexto espaciotemporal; 4) Que anule o restrinja la libertad de decisión.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["robo", "intimidacion", "violencia", "amenaza"]
        )

        # AGRESIÓN SEXUAL - CONSENTIMIENTO
        sentencias["STS_344/2023"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 344/2023",
            fecha="2023-04-20",
            ponente="Susana Polo García",
            materia="Agresión sexual - Ausencia de consentimiento (LO 10/2022)",
            tipo_penal="Agresión sexual",
            resumen="Aplicación de la reforma LO 10/2022: solo existe consentimiento cuando se manifieste libremente mediante actos que expresen inequívocamente la voluntad.",
            doctrina="Tras LO 10/2022 ('Ley del solo sí es sí'): 1) Solo hay consentimiento si se expresa de forma libre, voluntaria e inequívoca; 2) El silencio o pasividad NO equivalen a consentimiento; 3) No se requiere violencia o intimidación para el tipo básico; 4) La ausencia de consentimiento es el núcleo del tipo. Se invierte la lógica: debe probarse consentimiento positivo.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["agresion sexual", "consentimiento", "solo si es si", "LO 10/2022"]
        )

        # VIOLENCIA DE GÉNERO - HABITUALIDAD
        sentencias["STS_567/2020"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 567/2020",
            fecha="2020-09-15",
            ponente="Eduardo de Porres Ortiz de Urbina",
            materia="Violencia de género - Habitualidad",
            tipo_penal="Violencia de género",
            resumen="La habitualidad en violencia de género (art. 173.2) requiere pluralidad de actos en un contexto de dominación, no meras reiteraciones aisladas.",
            doctrina="Violencia habitual (art. 173.2): 1) Pluralidad de actos violentos (al menos 3); 2) En periodo temporal razonable; 3) Dirigidos contra víctimas del art. 173.2; 4) Creando clima de dominación y sometimiento; 5) Los actos pueden ser faltas o delitos; 6) No requiere condenas previas. Es delito autónomo distinto a suma de actos individuales.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["violencia de genero", "habitualidad", "maltrato", "art 173.2"]
        )

        # TRÁFICO DE DROGAS - POSESIÓN PARA CONSUMO
        sentencias["STS_892/2021"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 892/2021",
            fecha="2021-11-10",
            ponente="Andrés Palomo del Arco",
            materia="Tráfico de drogas - Distinción con autoconsumo",
            tipo_penal="Tráfico de drogas",
            resumen="Criterios para distinguir posesión para tráfico de posesión para consumo propio: cantidad, pureza, distribución, elementos de precisión, dinero.",
            doctrina="Indicios de tráfico vs autoconsumo: 1) Cantidad (superior a dosis de 5 días = indicio tráfico); 2) Pureza elevada; 3) Distribución en dosis; 4) Balanzas de precisión; 5) Material de corte; 6) Dinero en efectivo; 7) Listas de clientes; 8) Comunicaciones. No basta un solo indicio, se valoran conjuntamente. El acusado puede acreditar consumo propio.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["trafico drogas", "autoconsumo", "posesion", "indicios"]
        )

        # ATENUANTE DE CONFESIÓN
        sentencias["STS_234/2022"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 234/2022",
            fecha="2022-03-18",
            ponente="Carmen Lamela Díaz",
            materia="Atenuante de confesión - Requisitos",
            tipo_penal="Circunstancias modificativas",
            resumen="La confesión debe ser anterior a conocer que el procedimiento se dirige contra él, veraz y sin reservas mentales.",
            doctrina="Atenuante de confesión (art. 21.4): 1) Antes de saber que es investigado; 2) Espontánea (no por descubrimiento policial); 3) Veraz y completa; 4) Mantenida posteriormente; 5) Reconocimiento de participación. Si confiesa tras ser descubierto: atenuante analógica de colaboración (menor entidad). La retractación posterior elimina la atenuante.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["confesion", "atenuante", "art 21.4", "espontaneidad"]
        )

        # ATENUANTE DE REPARACIÓN
        sentencias["STS_445/2021"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 445/2021",
            fecha="2021-06-05",
            ponente="Javier Hernández García",
            materia="Atenuante de reparación - Alcance",
            tipo_penal="Circunstancias modificativas",
            resumen="La reparación puede ser total (muy cualificada), sustancial (cualificada) o parcial (simple), con distintos efectos atenuatorios.",
            doctrina="Reparación del daño (art. 21.5): 1) Antes del juicio oral; 2) Efectiva (no mera promesa); 3) Valoración: total = 2 grados, sustancial = 1 grado, parcial = mitad inferior. Incluye: restitución, indemnización, satisfacción moral. En delitos económicos: devolución íntegra + intereses. La reparación tardía (tras sentencia) no es atenuante pero influye en ejecución.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["reparacion", "atenuante", "art 21.5", "indemnizacion"]
        )

        # AGRAVANTE DE ALEVOSÍA
        sentencias["STS_123/2020"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 123/2020",
            fecha="2020-02-12",
            ponente="Miguel Colmenero Menéndez de Luarca",
            materia="Alevosía - Concepto y aplicación",
            tipo_penal="Circunstancias modificativas",
            resumen="La alevosía requiere eliminación consciente de defensas de la víctima, asegurando ejecución sin riesgo procedente de su defensa.",
            doctrina="Alevosía (art. 22.1): Elementos: 1) Objetivo: eliminación de defensa de la víctima; 2) Subjetivo: búsqueda consciente de esa situación (no basta aprovechamiento casual). Modalidades: a) Sorpresa súbita; b) Acecho; c) Víctima dormida/inconsciente; d) Desvalimiento por edad/enfermedad. Requiere decisión previa de ejecutar sin riesgos. En agresión impulsiva sin premeditación: difícil apreciarla.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["alevosia", "agravante", "art 22.1", "indefension"]
        )

        # PRESCRIPCIÓN
        sentencias["STS_567/2022"] = Sentencia(
            tribunal="Tribunal Supremo - Sala Segunda",
            numero="STS 567/2022",
            fecha="2022-07-20",
            ponente="Antonio del Moral García",
            materia="Prescripción del delito - Interrupción",
            tipo_penal="Prescripción",
            resumen="El plazo de prescripción se interrumpe con la incoación del procedimiento judicial contra el investigado. Diferencia entre interrupción y suspensión.",
            doctrina="Prescripción (arts. 131-132): 1) Plazos según gravedad de pena; 2) Se computa desde comisión del delito; 3) Interrupción: incoación procedimiento contra investigado (desde que se le atribuyen hechos); 4) Suspensión: si procedimiento se dirige contra imputado, máximo suspensión = mitad del plazo de prescripción. Tras reforma LO 1/2015: se endurece prescripción delitos graves.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["prescripcion", "interrupcion", "suspension", "plazos"]
        )

        # TRIBUNAL CONSTITUCIONAL - PRESUNCIÓN DE INOCENCIA
        sentencias["STC_63/2021"] = Sentencia(
            tribunal="Tribunal Constitucional",
            numero="STC 63/2021",
            fecha="2021-03-08",
            ponente="Cándido Conde-Pumpido Tourón",
            materia="Presunción de inocencia - Prueba de cargo",
            tipo_penal="Derechos fundamentales",
            resumen="La presunción de inocencia requiere actividad probatoria de cargo, obtenida lícitamente, practicada con garantías y valorada racionalmente.",
            doctrina="Presunción de inocencia (art. 24.2 CE): 1) Derecho a no ser condenado sin pruebas; 2) Requisitos de la prueba: a) De cargo (acreditativa de culpabilidad); b) Lícitamente obtenida; c) Practicada con contradicción; d) Valoración racional; 3) No basta prueba indiciaria débil; 4) Declaración víctima puede ser prueba única si es creíble y está corroborada; 5) Control constitucional: irracionalidad o arbitrariedad manifiesta.",
            enlace_cendoj="https://www.poderjudicial.es/search/AN/openDocument/...",
            palabras_clave=["presuncion inocencia", "prueba cargo", "derechos fundamentales", "TC"]
        )

        return sentencias

    def buscar_por_materia(self, materia: str) -> List[Sentencia]:
        """Busca sentencias por materia"""
        resultados = []
        materia_lower = materia.lower()

        for sentencia in self.sentencias.values():
            if (materia_lower in sentencia.materia.lower() or
                materia_lower in sentencia.tipo_penal.lower() or
                any(materia_lower in palabra for palabra in sentencia.palabras_clave)):
                resultados.append(sentencia)

        return resultados

    def buscar_por_tipo_penal(self, tipo_penal: str) -> List[Sentencia]:
        """Busca sentencias sobre un tipo penal específico"""
        return self.buscar_por_materia(tipo_penal)

    def buscar_por_palabra_clave(self, palabra: str) -> List[Sentencia]:
        """Busca sentencias por palabra clave"""
        resultados = []
        palabra_lower = palabra.lower()

        for sentencia in self.sentencias.values():
            if any(palabra_lower in palabra_clave for palabra_clave in sentencia.palabras_clave):
                resultados.append(sentencia)

        return resultados

    def obtener_doctrina(self, materia: str) -> str:
        """Obtiene la doctrina jurisprudencial consolidada sobre una materia"""
        sentencias = self.buscar_por_materia(materia)

        if not sentencias:
            return f"No se encontró jurisprudencia específica sobre '{materia}'"

        doctrina_consolidada = f"## Doctrina jurisprudencial sobre {materia}\n\n"

        for i, sentencia in enumerate(sentencias, 1):
            doctrina_consolidada += f"### {i}. {sentencia.numero} ({sentencia.fecha})\n"
            doctrina_consolidada += f"**{sentencia.materia}**\n\n"
            doctrina_consolidada += f"{sentencia.doctrina}\n\n"
            doctrina_consolidada += f"_Fuente: {sentencia.tribunal}_\n"
            doctrina_consolidada += f"_Enlace CENDOJ: {sentencia.enlace_cendoj}_\n\n"
            doctrina_consolidada += "---\n\n"

        return doctrina_consolidada

    def generar_cita_jurisprudencial(self, clave_sentencia: str) -> str:
        """Genera una cita formal de una sentencia"""
        sentencia = self.sentencias.get(clave_sentencia)
        if not sentencia:
            return ""

        return f"{sentencia.numero}, de {sentencia.fecha} ({sentencia.tribunal}, Ponente: {sentencia.ponente})"
