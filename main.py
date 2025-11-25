#!/usr/bin/env python3
"""
ASISTENTE LEGAL PENAL ESPAÑOL
Sistema experto de asistencia jurídica en Derecho Penal Español

Autor: Sistema de IA Legal
Versión: 1.0.0
"""

import os
import sys
from datetime import datetime

# Importar módulos del sistema
from knowledge.codigo_penal import CodigoPenal
from knowledge.jurisprudencia import Jurisprudencia
from knowledge.lecrim import LECrim

from analysis.case_analyzer import CaseAnalyzer
from analysis.legal_reasoning import LegalReasoning
from analysis.strategic_advisor import StrategicAdvisor

from drafting.document_generator import DocumentGenerator

from emotional.emotion_detector import EmotionDetector
from emotional.response_adapter import ResponseAdapter

from learning.user_profile import UserProfileManager
from learning.conversation_history import ConversationHistory
from learning.feedback_system import FeedbackSystem


class AsistenteLegalCLI:
    """
    Interfaz CLI del Asistente Legal Penal Español
    """

    def __init__(self):
        # Inicializar módulos
        self.codigo_penal = CodigoPenal()
        self.jurisprudencia = Jurisprudencia()
        self.lecrim = LECrim()

        self.case_analyzer = CaseAnalyzer()
        self.legal_reasoning = LegalReasoning()
        self.strategic_advisor = StrategicAdvisor()

        self.doc_generator = DocumentGenerator()

        self.emotion_detector = EmotionDetector()
        self.response_adapter = ResponseAdapter()

        self.profile_manager = UserProfileManager()
        self.conversation_history = ConversationHistory()
        self.feedback_system = FeedbackSystem()

        # Estado de la sesión
        self.user_id = None
        self.case_id = None
        self.perfil_usuario = None

    def mostrar_banner(self):
        """Muestra el banner de bienvenida"""
        print("\n" + "=" * 80)
        print(" " * 15 + "ASISTENTE LEGAL PENAL ESPAÑOL")
        print(" " * 10 + "Sistema Experto de Asesoramiento Jurídico Penal")
        print("=" * 80)
        print("\n🎓 Simulación de abogado penalista senior (20+ años de experiencia)")
        print("📚 Base de conocimiento: Código Penal, LECrim, Jurisprudencia TS/TC")
        print("⚖️  Especialización: Derecho Penal Español\n")
        print("⚠️  DISCLAIMER: Esta información es orientativa y no sustituye")
        print("   el asesoramiento de un abogado colegiado.\n")
        print("=" * 80 + "\n")

    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\n╔════════════════════════════════════════════════════════════════╗")
        print("║                      MENÚ PRINCIPAL                            ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║  1. 📋 Analizar un caso penal                                  ║")
        print("║  2. 📝 Redactar documento legal                                ║")
        print("║  3. 📚 Consultar normativa (Código Penal, LECrim)              ║")
        print("║  4. ⚖️  Consultar jurisprudencia                               ║")
        print("║  5. 📖 Explicar concepto legal                                 ║")
        print("║  6. 🎯 Asesoramiento estratégico                               ║")
        print("║  7. 📊 Ver historial de casos                                  ║")
        print("║  8. ⚙️  Configuración y preferencias                           ║")
        print("║  9. ℹ️  Ayuda e información                                     ║")
        print("║  0. 🚪 Salir                                                    ║")
        print("╚════════════════════════════════════════════════════════════════╝\n")

    def inicializar_sesion(self):
        """Inicializa la sesión del usuario"""
        print("\n🔐 INICIALIZACIÓN DE SESIÓN\n")

        # Solicitar ID de usuario
        user_id = input("Ingrese su ID de usuario (o presione Enter para sesión anónima): ").strip()

        if not user_id:
            user_id = f"anonimo_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            print(f"✓ Sesión anónima iniciada: {user_id}")
        else:
            # Intentar cargar perfil existente
            self.perfil_usuario = self.profile_manager.cargar_perfil(user_id)

            if self.perfil_usuario:
                print(f"✓ Bienvenido de nuevo, {self.perfil_usuario.nombre}!")
                self.profile_manager.actualizar_ultima_interaccion(user_id)
            else:
                # Crear nuevo perfil
                nombre = input("Nombre (opcional): ").strip() or "Usuario"
                print("\n¿Cuál es su situación?")
                print("1. Soy víctima de un delito")
                print("2. He sido acusado/investigado")
                print("3. Consulta general/académica")
                print("4. Profesional del derecho")

                rol_opcion = input("Seleccione (1-4): ").strip()
                roles = {"1": "victima", "2": "acusado", "3": "consulta_general", "4": "profesional"}
                rol = roles.get(rol_opcion, "consulta_general")

                self.perfil_usuario = self.profile_manager.crear_perfil(user_id, nombre, rol)
                print(f"✓ Perfil creado para {nombre}")

        self.user_id = user_id

    def opcion_analizar_caso(self):
        """Analiza un caso penal completo"""
        print("\n" + "="*80)
        print(" " * 25 + "ANÁLISIS DE CASO PENAL")
        print("="*80 + "\n")

        # Crear ID de caso
        self.case_id = f"caso_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        print("Por favor, describa los HECHOS del caso de forma detallada:")
        print("(Presione Enter dos veces para finalizar)\n")

        lineas = []
        while True:
            linea = input()
            if linea == "" and lineas and lineas[-1] == "":
                break
            lineas.append(linea)

        hechos = "\n".join(lineas).strip()

        if not hechos:
            print("❌ No se ingresaron hechos. Operación cancelada.")
            return

        # Guardar mensaje del usuario
        self.conversation_history.guardar_mensaje(self.case_id, "user", hechos)

        # Detectar emoción
        print("\n🧠 Analizando contexto emocional...")
        estado_emocional = self.emotion_detector.detectar_emocion(hechos)

        # Si es crisis, derivar inmediatamente
        if estado_emocional.requiere_derivacion:
            respuesta = self.response_adapter._respuesta_contencion(estado_emocional)
            print("\n" + respuesta)
            self.conversation_history.guardar_mensaje(
                self.case_id, "assistant", respuesta,
                {"tipo": "derivacion_emergencia", "emocion": estado_emocional.emocion_principal}
            )
            return

        # Solicitar información adicional
        print("\nInformación adicional (opcional):")
        fecha_hechos = input("Fecha de los hechos (DD/MM/AAAA) [Enter para omitir]: ").strip()
        antecedentes = input("¿Existen antecedentes penales? (s/n) [Enter para omitir]: ").strip().lower() == 's'

        contexto = {}
        if fecha_hechos:
            contexto["fecha_hechos"] = fecha_hechos
        if antecedentes:
            contexto["antecedentes"] = True

        # Analizar caso
        print("\n⚖️  Analizando caso... Por favor espere.\n")
        analisis = self.case_analyzer.analizar_caso(hechos, contexto)

        # Generar respuesta
        respuesta = self._generar_informe_analisis(analisis)

        # Adaptar tono según emoción
        respuesta_adaptada = self.response_adapter.adaptar_respuesta(respuesta, estado_emocional)

        # Mostrar resultado
        print("\n" + "="*80)
        print(respuesta_adaptada)
        print("="*80 + "\n")

        # Guardar en historial
        self.conversation_history.guardar_mensaje(
            self.case_id, "assistant", respuesta_adaptada,
            {
                "tipo": "analisis_caso",
                "tipo_penal": analisis.tipo_principal.nombre if analisis.tipo_principal else None,
                "emocion": estado_emocional.emocion_principal
            }
        )

        # Guardar en perfil
        if self.perfil_usuario:
            self.profile_manager.agregar_caso(self.user_id, {
                "case_id": self.case_id,
                "tipo": analisis.tipo_principal.nombre if analisis.tipo_principal else "No determinado",
                "fecha": datetime.now().isoformat()
            })

        # Ofrecer opciones adicionales
        self._ofrecer_acciones_posteriores(analisis)

    def _generar_informe_analisis(self, analisis) -> str:
        """Genera el informe de análisis del caso"""
        informe = "## 📋 INFORME DE ANÁLISIS JURÍDICO-PENAL\n\n"

        # Calificación jurídica
        if analisis.tipo_principal:
            informe += analisis.calificacion_juridica + "\n"
        else:
            informe += "⚠️ No se ha podido determinar un tipo penal claro a partir de los hechos descritos.\n\n"
            return informe

        # Pena estimada
        informe += "## ⚖️  MARCO PENAL Y CONSECUENCIAS\n\n"
        informe += analisis.pena_estimada + "\n\n"

        # Prescripción
        if analisis.prescripcion:
            informe += "## ⏰ PRESCRIPCIÓN\n\n"
            informe += f"- Prescripción del delito: {analisis.prescripcion.get('delito', 'No determinado')}\n"
            informe += f"- Prescripción de la pena: {analisis.prescripcion.get('pena', 'No determinado')}\n"
            if analisis.prescripcion.get('estado'):
                informe += f"- Estado: {analisis.prescripcion['estado']}\n"
            informe += "\n"

        # Advertencias
        if analisis.advertencias:
            informe += "## ⚠️  ADVERTENCIAS IMPORTANTES\n\n"
            for adv in analisis.advertencias:
                informe += f"{adv}\n"
            informe += "\n"

        # Alternativas jurídicas
        if analisis.alternativas_juridicas:
            informe += "## 🔄 CALIFICACIONES ALTERNATIVAS\n\n"
            for alt in analisis.alternativas_juridicas[:3]:  # Mostrar máximo 3
                informe += f"- {alt}\n"
            informe += "\n"

        return informe

    def _ofrecer_acciones_posteriores(self, analisis):
        """Ofrece acciones posteriores al análisis"""
        print("\n¿Qué desea hacer ahora?\n")
        print("1. Ver fundamentación jurídica completa")
        print("2. Consultar jurisprudencia aplicable")
        print("3. Obtener asesoramiento estratégico")
        print("4. Generar documento legal")
        print("5. Volver al menú principal")

        opcion = input("\nSeleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\n" + "="*80)
            print(analisis.fundamentacion)
            print("="*80)
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            if analisis.tipo_principal:
                sentencias = self.jurisprudencia.buscar_por_tipo_penal(analisis.tipo_principal.nombre)
                if sentencias:
                    print(f"\n📚 Jurisprudencia sobre {analisis.tipo_principal.nombre}:\n")
                    for sent in sentencias[:3]:
                        print(f"- {sent.numero}: {sent.resumen}")
                        print(f"  Doctrina: {sent.doctrina[:200]}...")
                        print()
                else:
                    print(f"\nNo se encontró jurisprudencia específica sobre {analisis.tipo_principal.nombre}")
                input("\nPresione Enter para continuar...")

        elif opcion == "3":
            self._asesoramiento_estrategico_caso(analisis)

        elif opcion == "4":
            self._generar_documento_caso(analisis)

    def _asesoramiento_estrategico_caso(self, analisis):
        """Proporciona asesoramiento estratégico"""
        print("\n¿Cuál es su rol en este caso?")
        print("1. Defensa del acusado")
        print("2. Acusación particular (víctima)")
        print("3. Acusación pública (Fiscal)")

        rol_opcion = input("Seleccione (1-3): ").strip()
        roles = {"1": "defensa", "2": "acusacion_particular", "3": "acusacion_publica"}
        rol = roles.get(rol_opcion, "defensa")

        # Generar recomendaciones
        if rol == "defensa":
            recomendaciones = self.strategic_advisor.recomendar_estrategia_defensa({})
        else:
            recomendaciones = self.strategic_advisor.recomendar_estrategia_acusacion({})

        print(f"\n## 🎯 ESTRATEGIA RECOMENDADA PARA {rol.upper().replace('_', ' ')}\n")

        for i, rec in enumerate(recomendaciones, 1):
            print(f"### {i}. {rec.accion} (Prioridad: {rec.prioridad})\n")
            print(f"**Fundamento:** {rec.fundamento}\n")
            print(f"**Beneficios:**")
            for ben in rec.beneficios:
                print(f"  ✓ {ben}")
            print(f"\n**Riesgos:**")
            for riesgo in rec.riesgos:
                print(f"  ⚠️  {riesgo}")
            print("\n" + "-"*80 + "\n")

        input("\nPresione Enter para continuar...")

    def _generar_documento_caso(self, analisis):
        """Genera un documento legal basado en el caso"""
        print("\n¿Qué tipo de documento desea generar?\n")
        print("1. Querella criminal")
        print("2. Denuncia")
        print("3. Escrito de defensa")
        print("4. Informe jurídico")

        tipo_doc = input("Seleccione (1-4): ").strip()

        print("\n📝 Generando documento... (se solicitarán datos adicionales)\n")

        if tipo_doc == "1":
            datos = self._solicitar_datos_querella(analisis)
            filepath = self.doc_generator.generar_querella(datos)
            print(f"\n✓ Querella generada: {filepath}")

        elif tipo_doc == "2":
            datos = self._solicitar_datos_denuncia()
            filepath = self.doc_generator.generar_denuncia(datos)
            print(f"\n✓ Denuncia generada: {filepath}")

        elif tipo_doc == "3":
            datos = self._solicitar_datos_defensa(analisis)
            filepath = self.doc_generator.generar_escrito_defensa(datos)
            print(f"\n✓ Escrito de defensa generado: {filepath}")

        elif tipo_doc == "4":
            datos = self._solicitar_datos_informe(analisis)
            filepath = self.doc_generator.generar_informe_juridico(datos)
            print(f"\n✓ Informe jurídico generado: {filepath}")

        input("\nPresione Enter para continuar...")

    def _solicitar_datos_querella(self, analisis):
        """Solicita datos para generar querella"""
        datos = {}

        print("DATOS DEL QUERELLANTE:")
        datos["querellante"] = {
            "nombre": input("Nombre completo: "),
            "dni": input("DNI: "),
            "domicilio": input("Domicilio: ")
        }

        print("\nDATOS DEL QUERELLADO:")
        datos["querellado"] = {
            "nombre": input("Nombre (o 'Desconocido'): ")
        }

        datos["juzgado"] = input("\nJuzgado competente (número): ")
        datos["ciudad"] = input("Ciudad: ")

        # Usar análisis para calificación
        if analisis.tipo_principal:
            datos["calificacion_juridica"] = analisis.calificacion_juridica
        else:
            datos["calificacion_juridica"] = "[Calificación a determinar]"

        # Hechos del caso actual
        historial = self.conversation_history.cargar_historial(self.case_id)
        if historial:
            datos["hechos"] = historial[0]["mensaje"]
        else:
            datos["hechos"] = "[Descripción de los hechos]"

        datos["peticiones"] = [
            "Se admita a trámite la presente querella",
            "Se practiquen las diligencias de investigación pertinentes",
            "Se cite al querellado para su declaración",
            "Se dicte auto de procesamiento y, en su momento, se abra el juicio oral",
            "Se condene al querellado como autor del delito descrito"
        ]

        return datos

    def _solicitar_datos_denuncia(self):
        """Solicita datos para generar denuncia"""
        datos = {}

        print("DATOS DEL DENUNCIANTE:")
        datos["denunciante"] = {
            "nombre": input("Nombre completo: "),
            "dni": input("DNI: "),
            "domicilio": input("Domicilio: ")
        }

        print("\nHECHOS:")
        print("Describa brevemente los hechos a denunciar:")
        datos["hechos"] = input()

        datos["ciudad"] = input("\nCiudad: ")

        return datos

    def _solicitar_datos_defensa(self, analisis):
        """Solicita datos para escrito de defensa"""
        datos = {}

        datos["defendido"] = {
            "nombre": input("Nombre del defendido: ")
        }

        datos["juzgado"] = input("Juzgado (número): ")
        datos["ciudad"] = input("Ciudad: ")
        datos["procedimiento"] = input("Número de procedimiento: ")

        # Usar análisis
        if analisis.tipo_principal:
            datos["argumentos_defensa"] = "La prueba aportada es insuficiente para acreditar la concurrencia de todos los elementos del tipo penal."

            if analisis.circunstancias_atenuantes:
                atenuantes_texto = "\n".join([f"- {at.nombre} ({at.articulo} CP)" for at in analisis.circunstancias_atenuantes])
                datos["atenuantes"] = atenuantes_texto

        return datos

    def _solicitar_datos_informe(self, analisis):
        """Solicita datos para informe jurídico"""
        datos = {}

        datos["asunto"] = input("Asunto del informe: ")
        datos["destinatario"] = input("Destinatario: ")
        datos["letrado"] = input("Nombre del letrado: ")
        datos["ciudad"] = input("Ciudad: ")

        # Usar análisis del caso
        if analisis.fundamentacion:
            datos["analisis"] = analisis.fundamentacion

        if analisis.tipo_principal:
            datos["conclusiones"] = [
                f"Los hechos son constitutivos del delito de {analisis.tipo_principal.nombre}",
                f"La pena aplicable oscila entre {analisis.tipo_principal.pena_minima} y {analisis.tipo_principal.pena_maxima}",
                "Se recomienda asesoramiento legal especializado"
            ]

        return datos

    def opcion_redactar_documento(self):
        """Menú de redacción de documentos"""
        print("\n📝 REDACCIÓN DE DOCUMENTOS LEGALES\n")
        print("1. Querella criminal")
        print("2. Denuncia")
        print("3. Recurso de apelación")
        print("4. Recurso de casación")
        print("5. Escrito de defensa")
        print("6. Informe jurídico")
        print("0. Volver")

        opcion = input("\nSeleccione tipo de documento (0-6): ").strip()

        if opcion == "0":
            return

        print("\nNOTA: Para generar documentos completos, es recomendable primero")
        print("analizar el caso (opción 1 del menú principal).\n")

        # Implementación simplificada
        print("Esta funcionalidad requiere datos específicos del caso.")
        print("Use la opción 1 (Analizar caso) para generar documentos automáticamente.")

        input("\nPresione Enter para continuar...")

    def opcion_consultar_normativa(self):
        """Consulta de normativa"""
        print("\n📚 CONSULTA DE NORMATIVA\n")
        print("1. Buscar artículo del Código Penal")
        print("2. Buscar tipo penal")
        print("3. Consultar circunstancias modificativas")
        print("4. Información sobre procedimiento (LECrim)")
        print("0. Volver")

        opcion = input("\nSeleccione (0-4): ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            numero = input("\nNúmero de artículo del CP: ").strip()
            articulo = self.codigo_penal.buscar_articulo(numero)

            if articulo:
                print(f"\n{'='*80}")
                print(f"Artículo {articulo.numero} - {articulo.titulo}")
                print(f"{'='*80}\n")
                print(f"**Libro:** {articulo.libro} - {articulo.titulo_grupo}")
                print(f"**Capítulo:** {articulo.capitulo}")
                if articulo.seccion:
                    print(f"**Sección:** {articulo.seccion}")
                print(f"\n**Contenido:**\n{articulo.contenido}\n")
                if articulo.ultima_modificacion:
                    print(f"**Última modificación:** {articulo.ultima_modificacion}")
                print(f"**Vigencia:** {articulo.vigencia}")
            else:
                print(f"\n❌ No se encontró el artículo {numero}")

        elif opcion == "2":
            print("\nTipos penales disponibles:")
            print("- homicidio, asesinato")
            print("- lesiones_basicas")
            print("- hurto, robo_fuerza, robo_violencia")
            print("- estafa")
            print("- agresion_sexual, violacion")
            print("- violencia_genero")
            print("- trafico_drogas")
            print("- conduccion_temeraria")

            nombre = input("\nIngrese el nombre del tipo penal: ").strip()
            tipo = self.codigo_penal.buscar_tipo_penal(nombre)

            if tipo:
                print(f"\n{'='*80}")
                print(f"TIPO PENAL: {tipo.nombre.upper()}")
                print(f"{'='*80}\n")
                print(f"**Artículos:** {', '.join(tipo.articulos)} CP")
                print(f"**Bien jurídico:** {tipo.bien_juridico}")
                print(f"**Gravedad:** {tipo.gravedad}")
                print(f"\n**Pena:** {tipo.pena_minima} a {tipo.pena_maxima}")
                print(f"\n**Elementos objetivos:**")
                for elem in tipo.elementos_objetivos:
                    print(f"  - {elem}")
                print(f"\n**Elementos subjetivos:**")
                for elem in tipo.elementos_subjetivos:
                    print(f"  - {elem}")
                print(f"\n**Prescripción delito:** {tipo.prescripcion_delito}")
                print(f"**Prescripción pena:** {tipo.prescripcion_pena}")
            else:
                print(f"\n❌ No se encontró el tipo penal '{nombre}'")

        elif opcion == "3":
            print("\n¿Qué tipo de circunstancia?")
            print("1. Eximentes")
            print("2. Atenuantes")
            print("3. Agravantes")

            tipo_circ = input("Seleccione (1-3): ").strip()

            if tipo_circ == "1":
                print("\nCIRCUNSTANCIAS EXIMENTES (Art. 20 CP):")
                print("- Anomalía o alteración psíquica")
                print("- Intoxicación plena / síndrome de abstinencia")
                print("- Alteraciones de la percepción")
                print("- Legítima defensa")
                print("- Estado de necesidad")
                print("- Miedo insuperable")
                print("- Cumplimiento de un deber")

            elif tipo_circ == "2":
                print("\nCIRCUNSTANCIAS ATENUANTES (Art. 21 CP):")
                print("- Eximentes incompletas")
                print("- Grave adicción")
                print("- Arrebato, obcecación u otro estado pasional")
                print("- Confesión")
                print("- Reparación del daño")
                print("- Atenuante analógica")

            elif tipo_circ == "3":
                print("\nCIRCUNSTANCIAS AGRAVANTES (Art. 22 CP):")
                print("- Alevosía")
                print("- Disfraz, abuso de superioridad o aprovechamiento de circunstancias")
                print("- Precio, recompensa o promesa")
                print("- Motivos discriminatorios")
                print("- Ensañamiento")
                print("- Abuso de confianza")
                print("- Prevalerse del carácter público")
                print("- Reincidencia")

        elif opcion == "4":
            print("\n¿Qué información procesal necesita?")
            print("1. Esquema de procedimiento abreviado")
            print("2. Esquema de procedimiento ordinario")
            print("3. Plazos de recursos")

            proc = input("Seleccione (1-3): ").strip()

            if proc == "1":
                print(self.lecrim.generar_esquema_procedimiento("abreviado"))
            elif proc == "2":
                print(self.lecrim.generar_esquema_procedimiento("ordinario"))
            elif proc == "3":
                print("\nPLAZOS DE RECURSOS:")
                print("- Recurso de reforma: 3 días")
                print("- Recurso de apelación (preparación): 5 días")
                print("- Recurso de apelación (interposición): 10 días")
                print("- Recurso de casación (preparación): 5 días")
                print("- Recurso de casación (interposición): 20 días")
                print("- Recurso de amparo: 30 días")

        input("\nPresione Enter para continuar...")

    def opcion_consultar_jurisprudencia(self):
        """Consulta de jurisprudencia"""
        print("\n⚖️  CONSULTA DE JURISPRUDENCIA\n")

        materia = input("Ingrese la materia o tipo penal a buscar: ").strip()

        sentencias = self.jurisprudencia.buscar_por_materia(materia)

        if sentencias:
            print(f"\n📚 Se encontraron {len(sentencias)} sentencia(s) sobre '{materia}':\n")

            for i, sent in enumerate(sentencias, 1):
                print(f"{i}. {sent.numero} - {sent.fecha}")
                print(f"   {sent.tribunal}")
                print(f"   Materia: {sent.materia}")
                print(f"   {sent.resumen}")
                print(f"\n   Doctrina: {sent.doctrina[:300]}...")
                print(f"\n   Enlace CENDOJ: {sent.enlace_cendoj}")
                print("\n" + "-"*80 + "\n")

        else:
            print(f"\n❌ No se encontró jurisprudencia sobre '{materia}'")
            print("Intente con otros términos como: homicidio, estafa, hurto, etc.")

        input("\nPresione Enter para continuar...")

    def opcion_explicar_concepto(self):
        """Explica conceptos legales"""
        print("\n📖 EXPLICACIÓN DE CONCEPTOS LEGALES\n")

        concepto = input("¿Qué concepto desea que le explique? ").strip()

        # Diccionario simplificado de conceptos
        explicaciones = {
            "dolo": """
**DOLO**

Es la intención de cometer el delito, es decir, conocer lo que se hace y querer hacerlo.

Para que haya dolo se necesita:
1. **Conocimiento:** Saber que lo que haces es un delito
2. **Voluntad:** Querer hacerlo de todas formas

**Tipos de dolo:**
- **Dolo directo:** Quieres causar ese resultado (ej: disparas para matar)
- **Dolo eventual:** No quieres el resultado pero lo aceptas si ocurre (ej: conduces muy rápido sabiendo que puedes matar a alguien, y lo aceptas)

**Diferencia con la culpa/imprudencia:**
- Culpa = No quieres el resultado, pero eres descuidado
- Dolo = Sabes lo que haces y lo aceptas
""",
            "presuncion de inocencia": """
**PRESUNCIÓN DE INOCENCIA**

Es un derecho fundamental (art. 24.2 Constitución) que significa:

**Toda persona es inocente hasta que se demuestre su culpabilidad**

Consecuencias:
- La carga de la prueba la tiene la acusación (no el acusado)
- El acusado NO tiene que demostrar su inocencia
- Si hay dudas, se absuelve (in dubio pro reo)
- La prueba debe ser sólida, válida y obtenida con garantías

Solo se puede condenar si la acusación demuestra la culpabilidad "más allá de toda duda razonable".
""",
            "legitima defensa": """
**LEGÍTIMA DEFENSA**

Es una causa que elimina la responsabilidad penal cuando te defiendes de una agresión.

Requisitos (art. 20.4 CP):
1. **Agresión ilegítima:** Alguien te ataca de forma injusta
2. **Necesidad racional del medio:** Tu defensa es proporcionada al ataque
3. **Falta de provocación:** Tú no provocaste la situación

Ejemplos:
✓ Te atacan con un cuchillo y te defiendes con otro cuchillo
✓ Alguien entra en tu casa a robar y lo empujas para defenderte

✗ Te insultan y tú le pegas (no hay agresión física)
✗ Te empujan y tú sacas un arma (desproporción)
""",
            "prescripcion": """
**PRESCRIPCIÓN DEL DELITO**

Es el plazo máximo para juzgar un delito. Si pasa ese tiempo, ya no se puede juzgar.

Plazos (según gravedad del delito):
- Delitos leves: 1 año
- Delitos menos graves: 5 años
- Delitos graves: 10-20 años (según pena máxima)

¿Cuándo empieza a contar?
- Desde el día que se cometió el delito

¿Cuándo se interrumpe?
- Cuando se abre un procedimiento judicial contra el investigado
- Tras la interrupción, el plazo vuelve a empezar

**Diferencia:**
- Prescripción del DELITO: plazo para juzgarlo
- Prescripción de la PENA: plazo para cumplir condena ya dictada
"""
        }

        explicacion = explicaciones.get(concepto.lower())

        if explicacion:
            print(explicacion)
        else:
            print(f"\n❌ No tengo una explicación preparada sobre '{concepto}'")
            print("\nConceptos disponibles:")
            print("- dolo")
            print("- presuncion de inocencia")
            print("- legitima defensa")
            print("- prescripcion")
            print("\n(O haga una búsqueda más específica en el menú de normativa)")

        input("\nPresione Enter para continuar...")

    def opcion_asesoramiento_estrategico(self):
        """Asesoramiento estratégico"""
        print("\n🎯 ASESORAMIENTO ESTRATÉGICO PROCESAL\n")

        print("¿Cuál es su rol?")
        print("1. Defensa del acusado")
        print("2. Acusación (víctima)")
        print("3. Análisis general")

        rol_op = input("Seleccione (1-3): ").strip()

        if rol_op == "1":
            recomendaciones = self.strategic_advisor.recomendar_estrategia_defensa({})
            print("\n## ESTRATEGIA DE DEFENSA\n")

            for i, rec in enumerate(recomendaciones, 1):
                print(f"### {i}. {rec.accion}\n")
                print(f"**Prioridad:** {rec.prioridad}")
                print(f"**Fundamento:** {rec.fundamento}\n")
                print(f"**Beneficios:**")
                for ben in rec.beneficios:
                    print(f"  ✓ {ben}")
                print(f"\n**Riesgos:**")
                for riesgo in rec.riesgos:
                    print(f"  ⚠️  {riesgo}")
                print("\n" + "-"*80 + "\n")

        elif rol_op == "2":
            recomendaciones = self.strategic_advisor.recomendar_estrategia_acusacion({})
            print("\n## ESTRATEGIA DE ACUSACIÓN\n")

            for i, rec in enumerate(recomendaciones, 1):
                print(f"### {i}. {rec.accion}\n")
                print(f"**Prioridad:** {rec.prioridad}")
                print(f"**Fundamento:** {rec.fundamento}\n")
                print(f"**Beneficios:**")
                for ben in rec.beneficios:
                    print(f"  ✓ {ben}")
                print(f"\n**Riesgos:**")
                for riesgo in rec.riesgos:
                    print(f"  ⚠️  {riesgo}")
                print("\n" + "-"*80 + "\n")

        input("\nPresione Enter para continuar...")

    def opcion_ver_historial(self):
        """Ver historial de casos"""
        print("\n📊 HISTORIAL DE CASOS\n")

        if not self.perfil_usuario:
            print("❌ No hay perfil de usuario. Inicie sesión con un ID para mantener historial.")
            input("\nPresione Enter para continuar...")
            return

        casos = self.profile_manager.obtener_historial_casos(self.user_id)

        if not casos:
            print("No hay casos registrados en su historial.")
        else:
            print(f"Total de casos: {len(casos)}\n")
            for i, caso in enumerate(casos, 1):
                print(f"{i}. Caso: {caso.get('case_id', 'N/A')}")
                print(f"   Tipo: {caso.get('tipo', 'No determinado')}")
                print(f"   Fecha: {caso.get('fecha', 'N/A')}")
                print()

        input("\nPresione Enter para continuar...")

    def opcion_configuracion(self):
        """Configuración y preferencias"""
        print("\n⚙️  CONFIGURACIÓN\n")

        if not self.perfil_usuario:
            print("❌ No hay perfil de usuario. Inicie sesión con un ID para configurar preferencias.")
            input("\nPresione Enter para continuar...")
            return

        print("1. Cambiar tono de respuesta preferido")
        print("2. Cambiar nivel de tecnicismo")
        print("3. Ver estadísticas de uso")
        print("0. Volver")

        opcion = input("\nSeleccione (0-3): ").strip()

        if opcion == "1":
            print("\nTonos disponibles:")
            print("1. Empático (cálido, comprensivo)")
            print("2. Técnico (profesional, objetivo)")
            print("3. Pedagógico (didáctico, explicativo)")

            tono_op = input("Seleccione (1-3): ").strip()
            tonos = {"1": "empatico", "2": "tecnico", "3": "pedagogico"}
            tono = tonos.get(tono_op, "tecnico")

            self.profile_manager.actualizar_tono_preferido(self.user_id, tono)
            print(f"\n✓ Tono actualizado a: {tono}")

        elif opcion == "2":
            print("\nNivel de tecnicismo:")
            print("1. Bajo (lenguaje muy simple)")
            print("2. Medio (equilibrado)")
            print("3. Alto (términos técnicos completos)")

            nivel_op = input("Seleccione (1-3): ").strip()
            niveles = {"1": "bajo", "2": "medio", "3": "alto"}
            nivel = niveles.get(nivel_op, "medio")

            preferencias = {"nivel_tecnico": nivel}
            self.profile_manager.actualizar_preferencias(self.user_id, preferencias)
            print(f"\n✓ Nivel de tecnicismo actualizado a: {nivel}")

        elif opcion == "3":
            stats = self.feedback_system.obtener_estadisticas()
            print("\n## ESTADÍSTICAS\n")
            print(f"- Valoración promedio: {stats['promedio']}/5.0")
            print(f"- Total valoraciones: {stats['total']}")

        input("\nPresione Enter para continuar...")

    def opcion_ayuda(self):
        """Muestra información de ayuda"""
        print("\n" + "="*80)
        print(" " * 30 + "AYUDA E INFORMACIÓN")
        print("="*80 + "\n")

        print("""
Este sistema es un asistente de asesoramiento jurídico-penal basado en IA,
diseñado para proporcionar orientación sobre Derecho Penal Español.

**FUNCIONALIDADES PRINCIPALES:**

1. **Análisis de casos:** Analiza hechos y determina tipos penales aplicables
2. **Redacción de documentos:** Genera querellas, denuncias, recursos e informes
3. **Consulta normativa:** Acceso al Código Penal y LECrim
4. **Jurisprudencia:** Base de datos de sentencias del TS y TC
5. **Explicaciones:** Conceptos legales en lenguaje accesible
6. **Estrategia procesal:** Recomendaciones tácticas de defensa/acusación

**IMPORTANTE - LIMITACIONES:**

⚠️  Este sistema NO sustituye a un abogado colegiado
⚠️  La información es orientativa, no constituye asesoramiento legal oficial
⚠️  Para casos reales, consulte con un profesional del derecho
⚠️  En situaciones de crisis, contacte con servicios de emergencia (112, 016, 024)

**RECURSOS DE AYUDA:**

- Colegio de Abogados: Turno de oficio gratuito
- Justicia Gratuita: Si cumple requisitos económicos
- 016: Violencia de género
- 024: Atención conducta suicida
- 112: Emergencias generales

**BASES LEGALES:**

- Código Penal (LO 10/1995 y reformas)
- Ley de Enjuiciamiento Criminal
- Constitución Española (derechos fundamentales)
- Jurisprudencia TS y TC

Para más información, visite:
- www.boe.es (BOE - Legislación oficial)
- www.poderjudicial.es/cendoj (Jurisprudencia)
        """)

        input("\nPresione Enter para continuar...")

    def ejecutar(self):
        """Bucle principal de ejecución"""
        self.mostrar_banner()
        self.inicializar_sesion()

        while True:
            self.mostrar_menu_principal()

            opcion = input("Seleccione una opción (0-9): ").strip()

            if opcion == "1":
                self.opcion_analizar_caso()
            elif opcion == "2":
                self.opcion_redactar_documento()
            elif opcion == "3":
                self.opcion_consultar_normativa()
            elif opcion == "4":
                self.opcion_consultar_jurisprudencia()
            elif opcion == "5":
                self.opcion_explicar_concepto()
            elif opcion == "6":
                self.opcion_asesoramiento_estrategico()
            elif opcion == "7":
                self.opcion_ver_historial()
            elif opcion == "8":
                self.opcion_configuracion()
            elif opcion == "9":
                self.opcion_ayuda()
            elif opcion == "0":
                print("\n👋 Gracias por usar el Asistente Legal Penal Español")
                print("Recuerde: Esta información es orientativa. Consulte con un abogado colegiado.")
                print("\n¡Hasta pronto!\n")
                break
            else:
                print("\n❌ Opción no válida. Por favor seleccione 0-9.\n")
                input("Presione Enter para continuar...")


def main():
    """Función principal"""
    try:
        app = AsistenteLegalCLI()
        app.ejecutar()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupción detectada. Saliendo...\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reporte este error.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
