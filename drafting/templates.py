"""
Plantillas de documentos legales
Formatos estándar para diferentes tipos de escritos
"""

class PlantillasLegales:
    """
    Repositorio de plantillas legales estándar
    """

    @staticmethod
    def plantilla_querella() -> dict:
        """Plantilla de querella criminal"""
        return {
            "encabezado": "AL JUZGADO DE INSTRUCCIÓN {numero} DE {ciudad}",
            "estructura": [
                "HECHOS",
                "FUNDAMENTOS DE DERECHO",
                "OTROSÍ DIGO",
                "SUPLICO"
            ],
            "campos_requeridos": [
                "querellante",
                "querellado",
                "hechos",
                "calificacion_juridica",
                "juzgado"
            ]
        }

    @staticmethod
    def plantilla_recurso_apelacion() -> dict:
        """Plantilla de recurso de apelación"""
        return {
            "encabezado": "A LA AUDIENCIA PROVINCIAL DE {ciudad}",
            "estructura": [
                "I. PREPARACIÓN DEL RECURSO",
                "II. INTERPOSICIÓN DEL RECURSO",
                "MOTIVOS DEL RECURSO",
                "SUPLICO"
            ],
            "plazos": {
                "preparacion": "5 días",
                "interposicion": "10 días"
            }
        }

    @staticmethod
    def plantilla_escrito_acusacion() -> dict:
        """Plantilla de escrito de acusación"""
        return {
            "estructura": [
                "HECHOS PROBADOS",
                "CALIFICACIÓN JURÍDICA",
                "PARTICIPACIÓN",
                "CIRCUNSTANCIAS MODIFICATIVAS",
                "RESPONSABILIDAD CIVIL",
                "CONCLUSIONES"
            ]
        }

    @staticmethod
    def clausulas_estándar() -> dict:
        """Cláusulas estándar frecuentes"""
        return {
            "presuncion_inocencia": """El acusado goza de la presunción de inocencia reconocida en el artículo 24.2 de la Constitución Española, correspondiendo a la acusación la carga de probar los hechos mediante prueba de cargo válida, lícita y suficiente, obtenida con todas las garantías procesales.""",

            "tutela_judicial": """Se invoca el derecho a la tutela judicial efectiva reconocido en el artículo 24 de la Constitución Española, que comprende el derecho a obtener una resolución fundada en Derecho, a la defensa y asistencia letrada, y a utilizar los medios de prueba pertinentes para la defensa.""",

            "in_dubio_pro_reo": """En aplicación del principio "in dubio pro reo", cualquier duda razonable sobre los hechos o la culpabilidad debe resolverse a favor del acusado, conforme a reiterada doctrina constitucional y jurisprudencia del Tribunal Supremo.""",

            "fundamentacion_sentencia": """Toda sentencia debe estar debidamente fundamentada, exponiendo de forma clara los hechos probados, la valoración de la prueba y la aplicación del Derecho, conforme exige el artículo 120.3 de la Constitución Española.""",

            "proporcionalidad": """El principio de proporcionalidad (art. 25.1 CE) exige que las penas sean proporcionadas a la gravedad del hecho y a la culpabilidad del autor, debiendo individualizarse en atención a las circunstancias del caso concreto."""
        }
