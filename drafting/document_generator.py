"""
Generador de Documentos Legales
Crea documentos profesionales con formato forense español
"""

from datetime import datetime
from typing import Dict, List, Optional
import os


class DocumentGenerator:
    """
    Generador de documentos legales profesionales
    Querellas, denuncias, recursos, informes, contratos
    """

    def __init__(self):
        self.output_dir = "generated_documents"
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        """Crea el directorio de salida si no existe"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generar_querella(self, datos: Dict) -> str:
        """
        Genera una querella criminal

        Datos requeridos:
        - querellante: Dict con nombre, dni, domicilio, etc.
        - querellado: Dict con identificación del querellado
        - hechos: Relato de los hechos
        - calificacion_juridica: Delito(s) imputados
        - peticiones: List de peticiones al juzgado
        - juzgado: Órgano judicial competente
        """
        documento = self._header_documento("QUERELLA CRIMINAL")

        # Encabezamiento
        documento += f"AL JUZGADO DE INSTRUCCIÓN {datos.get('juzgado', '[NÚMERO]')} DE {datos.get('ciudad', '[CIUDAD]')}\n\n"

        # Representación
        documento += f"{datos['querellante']['nombre']}, mayor de edad, con DNI {datos['querellante']['dni']}, "
        documento += f"con domicilio en {datos['querellante']['domicilio']}, "
        documento += f"representado por el Procurador D./Dña. {datos.get('procurador', '[PROCURADOR]')} "
        documento += f"y asistido por el Letrado D./Dña. {datos.get('letrado', '[LETRADO]')}, "
        documento += f"con despacho profesional en {datos.get('despacho', '[DIRECCIÓN DESPACHO]')}, "
        documento += "ante el Juzgado comparezco y como mejor proceda en Derecho, DIGO:\n\n"

        # Hechos
        documento += "## HECHOS\n\n"
        if isinstance(datos['hechos'], list):
            for i, hecho in enumerate(datos['hechos'], 1):
                documento += f"**{self._numero_ordinal(i)}.-** {hecho}\n\n"
        else:
            documento += f"{datos['hechos']}\n\n"

        # Calificación Jurídica
        documento += "## FUNDAMENTOS DE DERECHO\n\n"
        documento += f"**PRIMERO.- Competencia y legitimación**\n\n"
        documento += f"Este Juzgado es competente para conocer de la presente querella de conformidad "
        documento += f"con el artículo 14 de la Ley de Enjuiciamiento Criminal, por haberse cometido los hechos "
        documento += f"en su partido judicial.\n\n"
        documento += f"El querellante está legitimado para ejercitar la acción penal de conformidad con los "
        documento += f"artículos 101, 270 y siguientes de la Ley de Enjuiciamiento Criminal.\n\n"

        documento += f"**SEGUNDO.- Calificación jurídica**\n\n"
        documento += f"{datos['calificacion_juridica']}\n\n"

        documento += f"**TERCERO.- Responsabilidad civil**\n\n"
        documento += f"Del delito objeto de esta querella se han derivado daños y perjuicios para el querellante, "
        documento += f"cuya cuantificación se realizará en el momento procesal oportuno, sin perjuicio de ejercitar "
        documento += f"desde este momento la acción civil ex delicto.\n\n"

        # Otrosí
        documento += "## OTROSÍ DIGO\n\n"
        documento += "**PRIMERO.-** Que de conformidad con el art. 280 LECrim, designo como domicilio a efectos de notificaciones "
        documento += f"el sito en {datos.get('domicilio_notificaciones', datos['querellante']['domicilio'])}.\n\n"

        documento += "**SEGUNDO.-** Que de conformidad con el art. 281 LECrim, solicito que todas las citaciones y comunicaciones "
        documento += f"se realicen a través de mi Procurador.\n\n"

        # Peticiones
        documento += "## SUPLICO AL JUZGADO\n\n"
        if isinstance(datos['peticiones'], list):
            for peticion in datos['peticiones']:
                documento += f"- {peticion}\n"
        else:
            documento += f"{datos['peticiones']}\n"

        documento += f"\n{datos.get('ciudad', '[CIUDAD]')}, a {self._fecha_actual()}\n\n"
        documento += f"Fdo.: {datos.get('letrado', '[LETRADO]')}\n"
        documento += f"Letrado del Ilustre Colegio de Abogados de {datos.get('colegio_abogados', '[CIUDAD]')}\n"

        return self._guardar_documento(documento, "querella")

    def generar_denuncia(self, datos: Dict) -> str:
        """Genera una denuncia"""
        documento = self._header_documento("DENUNCIA")

        documento += f"AL JUZGADO DE INSTRUCCIÓN / FISCALÍA / POLICÍA NACIONAL\n\n"

        documento += f"{datos['denunciante']['nombre']}, mayor de edad, con DNI {datos['denunciante']['dni']}, "
        documento += f"con domicilio en {datos['denunciante']['domicilio']}, "
        documento += "comparece y como mejor proceda en Derecho, EXPONE:\n\n"

        documento += "## HECHOS\n\n"
        documento += f"{datos['hechos']}\n\n"

        documento += "Por lo expuesto,\n\n"
        documento += "## SOLICITA\n\n"
        documento += "Que se tenga por presentada esta denuncia, se proceda a su investigación y se adopten "
        documento += "las medidas necesarias para el esclarecimiento de los hechos y la determinación de responsabilidades.\n\n"

        documento += f"{datos.get('ciudad', '[CIUDAD]')}, a {self._fecha_actual()}\n\n"
        documento += f"Fdo.: {datos['denunciante']['nombre']}\n"

        return self._guardar_documento(documento, "denuncia")

    def generar_recurso_apelacion(self, datos: Dict) -> str:
        """Genera recurso de apelación"""
        documento = self._header_documento("RECURSO DE APELACIÓN")

        documento += f"A LA AUDIENCIA PROVINCIAL DE {datos.get('ciudad', '[CIUDAD]').upper()}\n"
        documento += f"SECCIÓN {datos.get('seccion', '[NÚMERO]')}ª\n\n"

        # Encabezamiento
        documento += f"{datos['recurrente']['nombre']}, representado por el Procurador D./Dña. {datos.get('procurador', '[PROCURADOR]')} "
        documento += f"y asistido por el Letrado D./Dña. {datos.get('letrado', '[LETRADO]')}, "
        documento += f"en el procedimiento abreviado {datos.get('procedimiento', '[NÚMERO/AÑO]')} seguido ante el "
        documento += f"Juzgado de lo Penal {datos.get('juzgado', '[NÚMERO]')} de {datos.get('ciudad', '[CIUDAD]')}, "
        documento += "ante la Audiencia comparezco y como mejor proceda en Derecho, DIGO:\n\n"

        # Preparación
        documento += "## I. PREPARACIÓN DEL RECURSO\n\n"
        documento += f"Por medio del presente escrito, y dentro del plazo legalmente establecido, procedo a la "
        documento += f"**PREPARACIÓN DEL RECURSO DE APELACIÓN** contra la sentencia dictada por el Juzgado de lo Penal "
        documento += f"{datos.get('juzgado', '[NÚMERO]')} de {datos.get('ciudad', '[CIUDAD]')} en fecha "
        documento += f"{datos.get('fecha_sentencia', '[FECHA]')}, en virtud de la cual se condena a mi representado.\n\n"

        documento += "Manifiesto mi intención de interponer recurso de apelación contra dicha resolución por no estar conforme "
        documento += "con la misma, solicitando que se tengan por preparados los recursos y se remitan las actuaciones "
        documento += "a la Audiencia Provincial.\n\n"

        # Interposición
        documento += "## II. INTERPOSICIÓN DEL RECURSO\n\n"
        documento += "### MOTIVOS DEL RECURSO\n\n"

        if isinstance(datos.get('motivos', []), list):
            for i, motivo in enumerate(datos['motivos'], 1):
                documento += f"**MOTIVO {self._numero_romano(i)}.- {motivo['titulo']}**\n\n"
                documento += f"{motivo['contenido']}\n\n"
        else:
            documento += f"{datos.get('motivos', 'A desarrollar en el escrito de interposición')}\n\n"

        # Peticiones (suplico)
        documento += "## SUPLICO A LA AUDIENCIA PROVINCIAL\n\n"
        documento += "Que tenga por interpuesto en tiempo y forma RECURSO DE APELACIÓN contra la sentencia dictada, "
        documento += "y previos los trámites legales oportunos, dicte nueva sentencia por la que:\n\n"

        if isinstance(datos.get('peticiones', []), list):
            for peticion in datos['peticiones']:
                documento += f"- {peticion}\n"
        else:
            documento += "- Se revoque la sentencia recurrida y se dicte sentencia absolutoria.\n"
            documento += "- Subsidiariamente, se reduzca la pena impuesta en aplicación de las circunstancias atenuantes concurrentes.\n"

        documento += f"\n{datos.get('ciudad', '[CIUDAD]')}, a {self._fecha_actual()}\n\n"
        documento += f"Fdo.: {datos.get('letrado', '[LETRADO]')}\n"

        return self._guardar_documento(documento, "recurso_apelacion")

    def generar_recurso_casacion(self, datos: Dict) -> str:
        """Genera recurso de casación"""
        documento = self._header_documento("RECURSO DE CASACIÓN")

        documento += "AL TRIBUNAL SUPREMO\n"
        documento += "SALA SEGUNDA (PENAL)\n\n"

        documento += f"{datos['recurrente']['nombre']}, representado por el Procurador D./Dña. {datos.get('procurador', '[PROCURADOR]')} "
        documento += f"y asistido por el Letrado D./Dña. {datos.get('letrado', '[LETRADO]')}, "
        documento += "ante la Sala comparezco y como mejor proceda en Derecho, DIGO:\n\n"

        # Preparación
        documento += "## I. PREPARACIÓN DEL RECURSO\n\n"
        documento += f"Que por medio del presente escrito procedo a la **PREPARACIÓN DEL RECURSO DE CASACIÓN** "
        documento += f"contra la sentencia dictada por la Audiencia Provincial de {datos.get('ciudad', '[CIUDAD]')} "
        documento += f"en fecha {datos.get('fecha_sentencia', '[FECHA]')}, "
        documento += f"en el Rollo de Apelación {datos.get('rollo', '[NÚMERO/AÑO]')}.\n\n"

        # Interposición
        documento += "## II. INTERPOSICIÓN DEL RECURSO\n\n"
        documento += "### MOTIVOS DE CASACIÓN\n\n"

        documento += "**MOTIVO PRIMERO.- Por infracción de ley (art. 849.1 LECrim)**\n\n"
        documento += f"{datos.get('motivo_infraccion_ley', 'Infracción de ley por aplicación indebida/inaplicación/interpretación errónea de preceptos penales.')}\n\n"

        documento += "**MOTIVO SEGUNDO.- Por quebrantamiento de forma (art. 850 LECrim)**\n\n"
        documento += f"{datos.get('motivo_quebrantamiento_forma', 'Quebrantamiento de forma por vulneración de derechos fundamentales.')}\n\n"

        # Suplico
        documento += "## SUPLICO AL TRIBUNAL SUPREMO\n\n"
        documento += "Que tenga por interpuesto en tiempo y forma RECURSO DE CASACIÓN, lo admita a trámite, "
        documento += "y previos los trámites legales, dicte sentencia por la que se case y anule la recurrida, "
        documento += "dictando nueva sentencia conforme a Derecho.\n\n"

        documento += f"{datos.get('ciudad', '[CIUDAD]')}, a {self._fecha_actual()}\n\n"
        documento += f"Fdo.: {datos.get('letrado', '[LETRADO]')}\n"

        return self._guardar_documento(documento, "recurso_casacion")

    def generar_escrito_defensa(self, datos: Dict) -> str:
        """Genera escrito de defensa"""
        documento = self._header_documento("ESCRITO DE DEFENSA")

        documento += f"AL JUZGADO DE INSTRUCCIÓN/PENAL {datos.get('juzgado', '[NÚMERO]')} DE {datos.get('ciudad', '[CIUDAD]').upper()}\n"
        documento += f"Procedimiento: {datos.get('procedimiento', '[TIPO Y NÚMERO]')}\n\n"

        documento += f"{datos['defendido']['nombre']}, representado por el Procurador D./Dña. {datos.get('procurador', '[PROCURADOR]')} "
        documento += f"y asistido por el Letrado D./Dña. {datos.get('letrado', '[LETRADO]')}, "
        documento += "ante el Juzgado comparezco y como mejor proceda en Derecho, DIGO:\n\n"

        documento += "## HECHOS\n\n"
        documento += f"{datos.get('hechos', 'Los hechos descritos en el escrito de acusación...')}\n\n"

        documento += "## FUNDAMENTOS DE DERECHO\n\n"
        documento += "**PRIMERO.- Presunción de inocencia**\n\n"
        documento += "Mi representado goza de la presunción de inocencia reconocida en el art. 24.2 de la Constitución Española, "
        documento += "correspondiendo a la acusación la carga de desvirtuar dicha presunción mediante prueba de cargo "
        documento += "válida, lícita y suficiente.\n\n"

        documento += "**SEGUNDO.- Insuficiencia probatoria**\n\n"
        documento += f"{datos.get('argumentos_defensa', 'La prueba aportada es insuficiente para destruir la presunción de inocencia...')}\n\n"

        documento += "**TERCERO.- Calificación jurídica**\n\n"
        documento += "En el caso de que el Tribunal estimara probados los hechos (lo que se niega), la calificación jurídica "
        documento += "debería ser [calificación alternativa más favorable].\n\n"

        documento += "**CUARTO.- Circunstancias atenuantes**\n\n"
        documento += f"{datos.get('atenuantes', 'Concurren las siguientes circunstancias atenuantes...')}\n\n"

        documento += "## SUPLICO AL JUZGADO\n\n"
        documento += "Que tenga por presentado este escrito, lo admita y, previos los trámites oportunos, "
        documento += "dicte sentencia por la que:\n\n"
        documento += "- Con carácter principal: Se absuelva a mi representado por aplicación del principio de presunción de inocencia.\n"
        documento += "- Subsidiariamente: Se apliquen las circunstancias atenuantes solicitadas.\n\n"

        documento += f"{datos.get('ciudad', '[CIUDAD]')}, a {self._fecha_actual()}\n\n"
        documento += f"Fdo.: {datos.get('letrado', '[LETRADO]')}\n"

        return self._guardar_documento(documento, "escrito_defensa")

    def generar_informe_juridico(self, datos: Dict) -> str:
        """Genera un informe jurídico"""
        documento = self._header_documento("INFORME JURÍDICO")

        documento += f"**ASUNTO:** {datos.get('asunto', '[DESCRIPCIÓN DEL ASUNTO]')}\n"
        documento += f"**FECHA:** {self._fecha_actual()}\n"
        documento += f"**DESTINATARIO:** {datos.get('destinatario', '[CLIENTE/ENTIDAD]')}\n"
        documento += f"**EMITIDO POR:** {datos.get('letrado', '[LETRADO]')}\n\n"

        documento += "---\n\n"

        documento += "## I. ANTECEDENTES\n\n"
        documento += f"{datos.get('antecedentes', '[Descripción de los antecedentes del caso]')}\n\n"

        documento += "## II. HECHOS\n\n"
        documento += f"{datos.get('hechos', '[Relato de los hechos relevantes]')}\n\n"

        documento += "## III. CUESTIONES PLANTEADAS\n\n"
        if isinstance(datos.get('cuestiones', []), list):
            for i, cuestion in enumerate(datos['cuestiones'], 1):
                documento += f"{i}. {cuestion}\n"
        else:
            documento += f"{datos.get('cuestiones', '[Cuestiones a analizar]')}\n"
        documento += "\n"

        documento += "## IV. ANÁLISIS JURÍDICO\n\n"
        documento += f"{datos.get('analisis', '[Análisis jurídico detallado de las cuestiones planteadas]')}\n\n"

        documento += "## V. NORMATIVA APLICABLE\n\n"
        documento += f"{datos.get('normativa', '[Código Penal, LECrim, jurisprudencia aplicable]')}\n\n"

        documento += "## VI. JURISPRUDENCIA\n\n"
        documento += f"{datos.get('jurisprudencia', '[Sentencias del TS y TC relevantes]')}\n\n"

        documento += "## VII. CONCLUSIONES\n\n"
        if isinstance(datos.get('conclusiones', []), list):
            for i, conclusion in enumerate(datos['conclusiones'], 1):
                documento += f"{i}. {conclusion}\n"
        else:
            documento += f"{datos.get('conclusiones', '[Conclusiones del informe]')}\n"
        documento += "\n"

        documento += "## VIII. RECOMENDACIONES\n\n"
        documento += f"{datos.get('recomendaciones', '[Recomendaciones de actuación]')}\n\n"

        documento += "---\n\n"
        documento += f"{datos.get('ciudad', '[CIUDAD]')}, a {self._fecha_actual()}\n\n"
        documento += f"Fdo.: {datos.get('letrado', '[LETRADO]')}\n"
        documento += f"Letrado\n"

        return self._guardar_documento(documento, "informe_juridico")

    def _header_documento(self, tipo: str) -> str:
        """Genera el encabezado del documento"""
        header = "=" * 80 + "\n"
        header += f"{tipo.center(80)}\n"
        header += "=" * 80 + "\n\n"
        return header

    def _fecha_actual(self) -> str:
        """Retorna la fecha actual en formato español"""
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

        hoy = datetime.now()
        return f"{hoy.day} de {meses[hoy.month - 1]} de {hoy.year}"

    def _numero_ordinal(self, num: int) -> str:
        """Convierte número a ordinal en español"""
        ordinales = {
            1: "PRIMERO", 2: "SEGUNDO", 3: "TERCERO", 4: "CUARTO", 5: "QUINTO",
            6: "SEXTO", 7: "SÉPTIMO", 8: "OCTAVO", 9: "NOVENO", 10: "DÉCIMO"
        }
        return ordinales.get(num, f"{num}º")

    def _numero_romano(self, num: int) -> str:
        """Convierte número a romano"""
        valores = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        resultado = ""

        for valor, letra in valores:
            while num >= valor:
                resultado += letra
                num -= valor

        return resultado

    def _guardar_documento(self, contenido: str, tipo: str) -> str:
        """Guarda el documento en archivo"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{tipo}_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(contenido)

        return filepath
