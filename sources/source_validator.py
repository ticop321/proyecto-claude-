"""
Validador de Fuentes Legales
Proporciona enlaces verificables a fuentes oficiales
"""

from typing import Dict, List


class SourceValidator:
    """
    Validador y generador de enlaces a fuentes oficiales
    """

    def __init__(self):
        self.fuentes_oficiales = self._cargar_fuentes()

    def _cargar_fuentes(self) -> Dict[str, Dict]:
        """Carga las URLs de fuentes oficiales"""
        return {
            "boe": {
                "nombre": "Boletín Oficial del Estado",
                "url_base": "https://www.boe.es",
                "descripcion": "Legislación oficial española",
                "fiabilidad": "Oficial"
            },
            "cendoj": {
                "nombre": "Centro de Documentación Judicial (CENDOJ)",
                "url_base": "https://www.poderjudicial.es/search/indexAN.jsp",
                "descripcion": "Jurisprudencia del Poder Judicial",
                "fiabilidad": "Oficial"
            },
            "codigo_penal": {
                "nombre": "Código Penal (LO 10/1995)",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444",
                "descripcion": "Código Penal vigente con todas las reformas",
                "fiabilidad": "Oficial"
            },
            "lecrim": {
                "nombre": "Ley de Enjuiciamiento Criminal",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1882-6036",
                "descripcion": "LECrim vigente",
                "fiabilidad": "Oficial"
            },
            "constitucion": {
                "nombre": "Constitución Española",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229",
                "descripcion": "Constitución Española de 1978",
                "fiabilidad": "Oficial"
            },
            "tribunal_constitucional": {
                "nombre": "Tribunal Constitucional",
                "url": "https://www.tribunalconstitucional.es/",
                "descripcion": "Sentencias y doctrina del TC",
                "fiabilidad": "Oficial"
            },
            "eur_lex": {
                "nombre": "EUR-Lex",
                "url": "https://eur-lex.europa.eu/",
                "descripcion": "Legislación de la Unión Europea",
                "fiabilidad": "Oficial"
            }
        }

    def generar_enlace_articulo_cp(self, numero: str) -> str:
        """Genera enlace al artículo del Código Penal"""
        base_url = "https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444"
        return f"{base_url}#a{numero}"

    def generar_enlace_boe(self, identificador: str) -> str:
        """Genera enlace a documento BOE"""
        return f"https://www.boe.es/buscar/doc.php?id={identificador}"

    def generar_enlace_cendoj(self, tribunal: str, numero: str, año: str) -> str:
        """
        Genera enlace a sentencia en CENDOJ

        Ejemplo:
        tribunal = "TS"
        numero = "531"
        año = "2022"
        """
        return f"https://www.poderjudicial.es/search/AN/openDocument/{tribunal}{numero}{año}"

    def obtener_fuentes_codigo_penal(self) -> List[Dict]:
        """Obtiene fuentes para verificar el Código Penal"""
        return [
            {
                "fuente": "BOE - Código Penal (LO 10/1995)",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444",
                "tipo": "Oficial"
            },
            {
                "fuente": "Reforma LO 1/2015",
                "url": "https://www.boe.es/buscar/doc.php?id=BOE-A-2015-3439",
                "tipo": "Oficial"
            },
            {
                "fuente": "Reforma LO 10/2022 (Ley 'solo sí es sí')",
                "url": "https://www.boe.es/buscar/doc.php?id=BOE-A-2022-14630",
                "tipo": "Oficial"
            }
        ]

    def obtener_fuentes_jurisprudencia(self, materia: str = None) -> List[Dict]:
        """Obtiene fuentes para consultar jurisprudencia"""
        fuentes = [
            {
                "fuente": "CENDOJ - Centro de Documentación Judicial",
                "url": "https://www.poderjudicial.es/search/indexAN.jsp",
                "descripcion": "Búsqueda de sentencias del TS, TC y AP",
                "tipo": "Oficial"
            },
            {
                "fuente": "Tribunal Constitucional - Buscador",
                "url": "https://hj.tribunalconstitucional.es/",
                "descripcion": "Sentencias y autos del TC",
                "tipo": "Oficial"
            },
            {
                "fuente": "Tribunal Supremo",
                "url": "https://www.poderjudicial.es/search/indexAN.jsp",
                "descripcion": "Doctrina jurisprudencial del TS",
                "tipo": "Oficial"
            }
        ]

        return fuentes

    def validar_cita_legal(self, cita: str) -> Dict:
        """
        Valida una cita legal y proporciona el enlace oficial

        Args:
            cita: Ej. "Art. 138 CP", "STS 531/2022"

        Returns:
            Dict con información de validación
        """
        cita_lower = cita.lower()

        if "art" in cita_lower and "cp" in cita_lower:
            # Artículo del Código Penal
            import re
            match = re.search(r'(\d+)', cita)
            if match:
                numero = match.group(1)
                return {
                    "valida": True,
                    "tipo": "Artículo Código Penal",
                    "enlace": self.generar_enlace_articulo_cp(numero),
                    "fuente": "BOE - Código Penal"
                }

        elif "sts" in cita_lower:
            # Sentencia Tribunal Supremo
            return {
                "valida": True,
                "tipo": "Sentencia Tribunal Supremo",
                "enlace": "https://www.poderjudicial.es/search/indexAN.jsp",
                "fuente": "CENDOJ",
                "nota": "Buscar por número y año en CENDOJ"
            }

        elif "stc" in cita_lower:
            # Sentencia Tribunal Constitucional
            return {
                "valida": True,
                "tipo": "Sentencia Tribunal Constitucional",
                "enlace": "https://hj.tribunalconstitucional.es/",
                "fuente": "Tribunal Constitucional",
                "nota": "Buscar en el buscador del TC"
            }

        return {
            "valida": False,
            "tipo": "Desconocido",
            "nota": "No se pudo validar la cita"
        }

    def generar_bibliografia(self) -> str:
        """Genera una bibliografía de fuentes recomendadas"""
        bibliografia = """
# BIBLIOGRAFÍA Y FUENTES

## LEGISLACIÓN OFICIAL

1. **Código Penal (LO 10/1995)**
   https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444

2. **Ley de Enjuiciamiento Criminal**
   https://www.boe.es/buscar/act.php?id=BOE-A-1882-6036

3. **Constitución Española**
   https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229

## JURISPRUDENCIA

4. **CENDOJ - Centro de Documentación Judicial**
   https://www.poderjudicial.es/search/indexAN.jsp

5. **Tribunal Constitucional**
   https://hj.tribunalconstitucional.es/

## DOCTRINA (Autores de referencia)

- Mir Puig, Santiago. *Derecho Penal - Parte General*
- Muñoz Conde, Francisco. *Derecho Penal - Parte Especial*
- Gimbernat Ordeig, Enrique. *Estudios de Derecho Penal*
- Cerezo Mir, José. *Curso de Derecho Penal Español*

## RECURSOS ADICIONALES

- BOE (Boletín Oficial del Estado): https://www.boe.es
- Noticias Jurídicas: https://noticias.juridicas.com
- Consejo General del Poder Judicial: https://www.poderjudicial.es
"""
        return bibliografia
