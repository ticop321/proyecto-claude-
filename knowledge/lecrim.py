"""
Ley de Enjuiciamiento Criminal (LECrim)
Procedimientos penales, plazos, recursos y tramitación
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class FaseProcesal:
    """Fase del procedimiento penal"""
    nombre: str
    descripcion: str
    plazo: str
    articulos: List[str]
    actuaciones_principales: List[str]
    derechos_imputado: List[str]


@dataclass
class Recurso:
    """Recurso procesal"""
    nombre: str
    procedencia: str
    plazo: str
    organo_competente: str
    motivos: List[str]
    efectos: str
    tramite: str


class LECrim:
    """
    Ley de Enjuiciamiento Criminal
    Procedimientos, plazos y recursos procesales
    """

    def __init__(self):
        self.fases = self._cargar_fases()
        self.recursos = self._cargar_recursos()
        self.plazos = self._cargar_plazos()

    def _cargar_fases(self) -> Dict[str, FaseProcesal]:
        """Carga las fases del procedimiento penal"""
        fases = {}

        fases["diligencias_previas"] = FaseProcesal(
            nombre="Diligencias Previas (Procedimiento Abreviado)",
            descripcion="Fase de investigación inicial para delitos menos graves (pena hasta 9 años)",
            plazo="6 meses prorrogables (total máximo 18 meses)",
            articulos=["757", "779", "780", "782"],
            actuaciones_principales=[
                "Incoación por denuncia, querella o de oficio",
                "Práctica de diligencias de investigación",
                "Declaración del investigado (art. 775)",
                "Conclusión: sobreseimiento o apertura juicio oral"
            ],
            derechos_imputado=[
                "Derecho a guardar silencio",
                "Derecho a no declarar contra sí mismo",
                "Derecho a asistencia letrada (obligatoria)",
                "Derecho a intérprete si no habla castellano",
                "Derecho a ser informado de los cargos"
            ]
        )

        fases["instruccion_sumario"] = FaseProcesal(
            nombre="Instrucción - Sumario Ordinario",
            descripcion="Procedimiento para delitos graves (pena superior a 9 años)",
            plazo="Sin plazo legal determinado (debe ser dentro de un tiempo prudencial)",
            articulos=["299", "300", "301", "622", "627"],
            actuaciones_principales=[
                "Incoación del Sumario",
                "Instrucción por Juez de Instrucción",
                "Auto de procesamiento o no procesamiento",
                "Conclusión del sumario",
                "Calificaciones provisionales"
            ],
            derechos_imputado=[
                "Asistencia letrada obligatoria",
                "No declarar contra sí mismo",
                "Conocer los cargos",
                "Proponer diligencias",
                "Recurrir resoluciones"
            ]
        )

        fases["juicio_oral"] = FaseProcesal(
            nombre="Juicio Oral",
            descripcion="Fase de enjuiciamiento con práctica de prueba oral, pública y contradictoria",
            plazo="Variable según procedimiento",
            articulos=["680 y ss (abreviado)", "741 y ss (ordinario)"],
            actuaciones_principales=[
                "Sesión del juicio oral",
                "Cuestiones previas",
                "Práctica de prueba (testigos, peritos, documental)",
                "Informes de acusación y defensa",
                "Última palabra del acusado",
                "Deliberación y sentencia"
            ],
            derechos_imputado=[
                "Presunción de inocencia",
                "Defensa letrada",
                "Última palabra",
                "Juicio público (salvo excepciones)",
                "No declarar contra sí mismo",
                "Contradicción de la prueba"
            ]
        )

        fases["ejecucion"] = FaseProcesal(
            nombre="Ejecución de Sentencia",
            descripcion="Cumplimiento efectivo de la pena impuesta",
            plazo="Variable según tipo de pena",
            articulos=["983 y ss LECrim", "Arts. 1 y ss CP en ejecución"],
            actuaciones_principales=[
                "Firmeza de sentencia",
                "Liquidación de condena",
                "Ingreso en prisión (si procede)",
                "Control de ejecución por Juzgado de lo Penal o Vigilancia Penitenciaria",
                "Tramitación beneficios penitenciarios"
            ],
            derechos_imputado=[
                "Abono de prisión preventiva",
                "Beneficios penitenciarios según LOGP",
                "Suspensión de pena (art. 80-87 CP)",
                "Sustitución de pena (art. 88-89 CP)",
                "Libertad condicional (art. 90-93 CP)"
            ]
        )

        fases["juicio_faltas"] = FaseProcesal(
            nombre="Juicio por Delitos Leves (antigua Faltas)",
            descripcion="Procedimiento simplificado para delitos leves",
            plazo="Juicio inmediato o señalado en días siguientes",
            articulos=["962 y ss"],
            actuaciones_principales=[
                "Citación directa a juicio",
                "Celebración en acto único",
                "Práctica de prueba",
                "Sentencia (puede ser verbal, luego documentada)"
            ],
            derechos_imputado=[
                "Asistencia letrada (recomendable)",
                "Conocer acusación",
                "Proponer prueba",
                "Última palabra",
                "Recurrir sentencia"
            ]
        )

        return fases

    def _cargar_recursos(self) -> Dict[str, Recurso]:
        """Carga los recursos procesales penales"""
        recursos = {}

        recursos["reforma"] = Recurso(
            nombre="Recurso de Reforma",
            procedencia="Contra providencias y autos no definitivos dictados por Juzgados",
            plazo="3 días desde notificación",
            organo_competente="Mismo órgano que dictó la resolución",
            motivos=["Error de hecho o derecho en la resolución"],
            efectos="No suspensivo (salvo casos excepcionales)",
            tramite="Escrito de reforma → Resolución en 3 días → Si se desestima, cabe recurso de apelación subsidiario"
        )

        recursos["apelacion"] = Recurso(
            nombre="Recurso de Apelación",
            procedencia="Contra sentencias de Juzgado de lo Penal y autos definitivos",
            plazo="10 días desde notificación de sentencia",
            organo_competente="Audiencia Provincial",
            motivos=[
                "Error en valoración de la prueba",
                "Quebrantamiento de forma",
                "Infracción de ley (aplicación indebida de norma)",
                "Vulneración derechos fundamentales"
            ],
            efectos="Suspensivo (la sentencia no es firme hasta resolver apelación)",
            tramite="Escrito de preparación (5 días) → Escrito de interposición (10 días) → Traslado a otras partes → Resolución por AP (puede convocar vista)"
        )

        recursos["casacion"] = Recurso(
            nombre="Recurso de Casación",
            procedencia="Contra sentencias de Audiencia Provincial en procedimiento abreviado (pena >5 años) y Tribunal Superior de Justicia",
            plazo="5 días preparación + 20 días interposición",
            organo_competente="Tribunal Supremo - Sala Segunda (Penal)",
            motivos=[
                "Infracción de ley: aplicación indebida, inaplicación o interpretación errónea de norma penal o procesal",
                "Quebrantamiento de forma: vulneración normas procesales esenciales",
                "Vulneración derechos fundamentales",
                "Error en valoración de prueba (si hay contradicción con otras sentencias firmes)"
            ],
            efectos="No suspensivo (salvo que se acuerde suspensión ejecución)",
            tramite="Preparación (5 días) → Admisión a trámite → Interposición (20 días) → Oposición → Resolución TS (puede convocar vista o resolver sin ella)"
        )

        recursos["queja"] = Recurso(
            nombre="Recurso de Queja",
            procedencia="Contra inadmisión de recursos de apelación o casación",
            plazo="3 días desde notificación de inadmisión",
            organo_competente="Órgano superior que debía conocer del recurso inadmitido",
            motivos=["Inadmisión indebida del recurso"],
            efectos="No suspensivo",
            tramite="Escrito de queja → Informe del órgano que inadmitió → Resolución (admitiendo o desestimando queja)"
        )

        recursos["revision"] = Recurso(
            nombre="Recurso de Revisión",
            procedencia="Contra sentencias firmes condenatorias por error judicial",
            plazo="Sin plazo (puede interponerse en cualquier momento)",
            organo_competente="Tribunal Supremo - Sala Segunda",
            motivos=[
                "Aparición de nuevos hechos o pruebas que evidencian error",
                "Documentos falsos que fundaron la condena",
                "Condena basada en testimonio falso, cohecho o prevaricación probados",
                "Condenas contradictorias por mismos hechos"
            ],
            efectos="No suspensivo (no suspende ejecución salvo acuerdo)",
            tramite="Escrito de revisión → Admisión a trámite → Informe Fiscal → Vista (si procede) → Sentencia (estimando o desestimando)"
        )

        recursos["amparo"] = Recurso(
            nombre="Recurso de Amparo Constitucional",
            procedencia="Contra resoluciones judiciales que vulneren derechos fundamentales (tras agotar vía judicial ordinaria)",
            plazo="30 días desde notificación de resolución que agotó vía judicial",
            organo_competente="Tribunal Constitucional",
            motivos=[
                "Vulneración derechos fundamentales Título I CE (arts. 14-29)",
                "Especialmente: presunción inocencia, tutela judicial efectiva, debido proceso"
            ],
            efectos="No suspensivo (puede solicitarse suspensión cautelar)",
            tramite="Escrito de amparo → Admisión a trámite (si cumple requisitos) → Alegaciones → Sentencia TC"
        )

        return recursos

    def _cargar_plazos(self) -> Dict[str, str]:
        """Carga los plazos procesales más relevantes"""
        return {
            # RECURSOS
            "recurso_reforma": "3 días",
            "recurso_apelacion_preparacion": "5 días",
            "recurso_apelacion_interposicion": "10 días",
            "recurso_casacion_preparacion": "5 días",
            "recurso_casacion_interposicion": "20 días",
            "recurso_queja": "3 días",
            "recurso_amparo": "30 días",

            # INSTRUCCIÓN
            "diligencias_previas": "6 meses (prorrogables hasta 18 meses)",
            "sumario_ordinario": "Sin plazo legal determinado",
            "prision_provisional_maxima": "Hasta 2 años (prorrogable en casos excepcionales hasta 4 años)",

            # PRISIÓN PREVENTIVA
            "prision_preventiva_delitos_hasta_3_años": "Máximo 1 año",
            "prision_preventiva_delitos_3_a_6_años": "Máximo 2 años",
            "prision_preventiva_delitos_mas_6_años": "Máximo 4 años",

            # NOTIFICACIONES
            "personacion_acusacion_particular": "15 días desde que se tiene conocimiento",
            "traslado_escritos": "Generalmente 10 días",
            "proposicion_prueba": "5 días desde traslado de calificaciones",

            # PRESCRIPCIÓN (remisión al CP)
            "prescripcion_delito_leve": "1 año",
            "prescripcion_delito_menos_grave": "5 años",
            "prescripcion_delito_grave": "10 años (o según pena máxima del delito)",

            # COMPARECENCIAS
            "citacion_juicio_delito_leve": "Mínimo 24 horas de antelación (si se cita en el acto)",
            "citacion_juicio_abreviado": "Mínimo 10 días de antelación",
        }

    def obtener_fase(self, nombre_fase: str) -> Optional[FaseProcesal]:
        """Obtiene información sobre una fase procesal"""
        return self.fases.get(nombre_fase)

    def obtener_recurso(self, nombre_recurso: str) -> Optional[Recurso]:
        """Obtiene información sobre un recurso"""
        return self.recursos.get(nombre_recurso)

    def obtener_plazo(self, tipo_plazo: str) -> Optional[str]:
        """Obtiene un plazo procesal específico"""
        return self.plazos.get(tipo_plazo)

    def listar_recursos_procedentes(self, tipo_resolucion: str, organo: str) -> List[Recurso]:
        """Lista los recursos procedentes contra un tipo de resolución"""
        recursos_procedentes = []

        for recurso in self.recursos.values():
            # Lógica simplificada - en realidad sería más compleja
            if tipo_resolucion.lower() in recurso.procedencia.lower():
                recursos_procedentes.append(recurso)

        return recursos_procedentes

    def generar_esquema_procedimiento(self, tipo_procedimiento: str) -> str:
        """Genera un esquema del procedimiento penal"""
        esquemas = {
            "abreviado": """
## PROCEDIMIENTO ABREVIADO (Delitos con pena hasta 9 años)

### 1. FASE DE INSTRUCCIÓN: Diligencias Previas
- **Órgano:** Juzgado de Instrucción
- **Plazo:** 6 meses (prorrogables hasta 18 meses total)
- **Actuaciones:**
  * Incoación (denuncia/querella/oficio)
  * Investigación
  * Declaración del investigado (art. 775)
  * Proposición y práctica de diligencias

### 2. CONCLUSIÓN DE LA INSTRUCCIÓN
- Decreto de conclusión
- Opciones:
  * **Sobreseimiento** (provisional/libre)
  * **Apertura del juicio oral**

### 3. FASE INTERMEDIA
- Escrito de acusación (Ministerio Fiscal y acusaciones)
- Escrito de defensa
- Traslado para proposición de prueba
- Auto de apertura del juicio oral

### 4. JUICIO ORAL
- **Órgano:** Juzgado de lo Penal
- **Actuaciones:**
  * Cuestiones previas
  * Práctica de prueba
  * Conclusiones
  * Última palabra del acusado
  * Sentencia

### 5. RECURSOS
- Apelación ante Audiencia Provincial (10 días)
- Casación ante TS (si pena >5 años, 5+20 días)

### 6. EJECUCIÓN
- Firmeza de sentencia
- Ejecución de la pena
""",
            "ordinario": """
## PROCEDIMIENTO ORDINARIO (Delitos con pena superior a 9 años)

### 1. FASE DE INSTRUCCIÓN: Sumario
- **Órgano:** Juzgado de Instrucción
- **Plazo:** Plazo razonable (sin límite legal específico)
- **Actuaciones:**
  * Incoación del Sumario
  * Investigación completa
  * Auto de procesamiento (imputación formal)
  * Diligencias de investigación

### 2. CONCLUSIÓN DEL SUMARIO
- Declaración de conclusión
- Traslado a partes

### 3. CALIFICACIONES
- Escrito de calificación provisional (Fiscal y acusaciones)
- Defensa
- Calificaciones definitivas

### 4. APERTURA JUICIO ORAL
- Auto de apertura
- Proposición de prueba
- Remisión a Audiencia Provincial

### 5. JUICIO ORAL
- **Órgano:** Audiencia Provincial (con Jurado popular si procede)
- **Tramitación:** Similar a procedimiento abreviado pero ante tribunal colegiado
- Sentencia

### 6. RECURSOS
- Casación ante Tribunal Supremo
- Excepcionalmente: Revisión

### 7. EJECUCIÓN
""",
            "delito_leve": """
## JUICIO POR DELITO LEVE (antigua Falta)

### 1. INICIACIÓN
- Denuncia o atestado policial
- Citación directa a juicio

### 2. JUICIO (Acto único)
- **Órgano:** Juzgado de Instrucción
- **Tramitación:**
  * Comparecencia de partes
  * Práctica de prueba (acto único)
  * Conclusiones orales
  * Sentencia (puede ser verbal, luego se documenta)

### 3. RECURSOS
- Apelación ante Audiencia Provincial (10 días)

### 4. EJECUCIÓN
"""
        }

        return esquemas.get(tipo_procedimiento, "Tipo de procedimiento no reconocido")

    def calcular_fecha_limite_recurso(self, tipo_recurso: str, fecha_notificacion: str) -> str:
        """
        Calcula la fecha límite para interponer un recurso
        (Simplificado - en producción usar datetime)
        """
        plazos_recursos = {
            "reforma": "3 días hábiles",
            "apelacion": "10 días hábiles (preparación en 5 días)",
            "casacion": "5 días preparación + 20 días interposición",
            "queja": "3 días hábiles",
            "amparo": "30 días hábiles"
        }

        plazo = plazos_recursos.get(tipo_recurso, "Plazo no determinado")
        return f"Fecha notificación: {fecha_notificacion} → Plazo: {plazo}"
