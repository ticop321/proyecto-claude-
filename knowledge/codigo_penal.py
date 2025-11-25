"""
Código Penal Español - LO 10/1995
Base de conocimiento del Código Penal con todos los tipos penales, penas y circunstancias
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ArticuloCP:
    """Artículo del Código Penal"""
    numero: str
    titulo: str
    contenido: str
    libro: str
    titulo_grupo: str
    capitulo: str
    seccion: Optional[str] = None
    vigencia: str = "Vigente"
    ultima_modificacion: Optional[str] = None
    notas: Optional[str] = None


@dataclass
class TipoPenal:
    """Tipo penal con elementos y consecuencias"""
    nombre: str
    articulos: List[str]
    bien_juridico: str
    elementos_objetivos: List[str]
    elementos_subjetivos: List[str]
    pena_minima: str
    pena_maxima: str
    tipo: str  # Básico, Agravado, Atenuado, Privilegiado
    gravedad: str  # Leve, Menos Grave, Grave
    prescripcion_delito: str
    prescripcion_pena: str


@dataclass
class CircunstanciaModificativa:
    """Circunstancia atenuante o agravante"""
    tipo: str  # atenuante, agravante, eximente
    articulo: str
    nombre: str
    descripcion: str
    efectos: str
    ejemplos: List[str]


class CodigoPenal:
    """
    Base de conocimiento del Código Penal Español
    LO 10/1995 y reformas posteriores
    """

    def __init__(self):
        self.articulos = self._cargar_articulos()
        self.tipos_penales = self._cargar_tipos_penales()
        self.circunstancias = self._cargar_circunstancias()
        self.version = "LO 10/1995 (actualizado 2024)"

    def _cargar_articulos(self) -> Dict[str, ArticuloCP]:
        """Carga los artículos del Código Penal"""
        articulos = {}

        # LIBRO I - Disposiciones generales
        articulos["10"] = ArticuloCP(
            numero="10",
            titulo="Penas graves, menos graves y leves",
            contenido="""Son penas graves:
a) La prisión permanente revisable.
b) La prisión superior a cinco años.
c) La inhabilitación absoluta.
d) Las inhabilitaciones especiales por tiempo superior a cinco años.
e) La suspensión de empleo o cargo público por tiempo superior a cinco años.
f) La privación del derecho a conducir vehículos a motor y ciclomotores por tiempo superior a ocho años.
g) La privación del derecho a la tenencia y porte de armas por tiempo superior a ocho años.

Son penas menos graves:
a) La prisión de tres meses hasta cinco años.
b) Las inhabilitaciones especiales hasta cinco años.
c) La suspensión de empleo o cargo público hasta cinco años.
d) La privación del derecho a conducir vehículos a motor y ciclomotores de un año y un día a ocho años.
e) La privación del derecho a la tenencia y porte de armas de un año y un día a ocho años.
f) La multa de más de tres meses.
g) Los trabajos en beneficio de la comunidad de treinta y uno a ciento ochenta días.

Son penas leves:
a) La privación del derecho a conducir vehículos a motor y ciclomotores de tres meses a un año.
b) La privación del derecho a la tenencia y porte de armas de tres meses a un año.
c) La multa de hasta tres meses.
d) La localización permanente de un día a tres meses.
e) Los trabajos en beneficio de la comunidad de uno a treinta días.""",
            libro="I",
            titulo_grupo="Disposiciones generales sobre los delitos, las personas responsables, las penas, medidas de seguridad y demás consecuencias de la infracción penal",
            capitulo="I",
            seccion="De las penas, sus clases y efectos",
            ultima_modificacion="LO 1/2015"
        )

        # Eximentes (Art. 20)
        articulos["20"] = ArticuloCP(
            numero="20",
            titulo="Causas de exención de responsabilidad criminal",
            contenido="""Están exentos de responsabilidad criminal:
1.º El que al tiempo de cometer la infracción penal, a causa de cualquier anomalía o alteración psíquica, no pueda comprender la ilicitud del hecho o actuar conforme a esa comprensión.
2.º El que al tiempo de cometer la infracción penal se halle en estado de intoxicación plena por el consumo de bebidas alcohólicas, drogas tóxicas, estupefacientes, sustancias psicotrópicas u otras que produzcan efectos análogos, siempre que no haya sido buscado con el propósito de cometerla o no se hubiese previsto o debido prever su comisión, o se halle bajo la influencia de un síndrome de abstinencia, a causa de su dependencia de tales sustancias, que le impida comprender la ilicitud del hecho o actuar conforme a esa comprensión.
3.º El que, por sufrir alteraciones en la percepción desde el nacimiento o desde la infancia, tenga alterada gravemente la conciencia de la realidad.
4.º El que obre en defensa de la persona o derechos propios o ajenos, siempre que concurran los requisitos siguientes:
    a) Agresión ilegítima.
    b) Necesidad racional del medio empleado para impedirla o repelerla.
    c) Falta de provocación suficiente por parte del defensor.
5.º El que, en estado de necesidad, para evitar un mal propio o ajeno lesione un bien jurídico de otra persona o infrinja un deber, siempre que concurran los siguientes requisitos:
    a) Que el mal causado no sea mayor que el que se trate de evitar.
    b) Que la situación de necesidad no haya sido provocada intencionadamente por el sujeto.
    c) Que el necesitado no tenga, por su oficio o cargo, obligación de sacrificarse.
6.º El que obre impulsado por miedo insuperable.
7.º El que obre en cumplimiento de un deber o en el ejercicio legítimo de un derecho, oficio o cargo.""",
            libro="I",
            titulo_grupo="Disposiciones generales",
            capitulo="II",
            seccion="De las causas que eximen de la responsabilidad criminal"
        )

        # Atenuantes (Art. 21)
        articulos["21"] = ArticuloCP(
            numero="21",
            titulo="Circunstancias atenuantes",
            contenido="""Son circunstancias atenuantes:
1.ª Las causas expresadas en el artículo anterior, cuando no concurrieren todos los requisitos necesarios para eximir de responsabilidad en sus respectivos casos.
2.ª La de actuar el culpable a causa de su grave adicción a las sustancias mencionadas en el número 2.º del artículo anterior.
3.ª La de obrar por causas o estímulos tan poderosos que hayan producido arrebato, obcecación u otro estado pasional de entidad semejante.
4.ª La de haber procedido el culpable, antes de conocer que el procedimiento judicial se dirige contra él, a confesar la infracción a las autoridades.
5.ª La de haber procedido el culpable a reparar el daño ocasionado a la víctima, o disminuir sus efectos, en cualquier momento del procedimiento y con anterioridad a la celebración del acto del juicio oral.
6.ª Cualquier otra circunstancia de análoga significación que las anteriores (atenuante analógica).""",
            libro="I",
            titulo_grupo="Disposiciones generales",
            capitulo="II",
            seccion="De las circunstancias que atenúan la responsabilidad criminal"
        )

        # Agravantes (Art. 22)
        articulos["22"] = ArticuloCP(
            numero="22",
            titulo="Circunstancias agravantes",
            contenido="""Son circunstancias agravantes:
1.ª Ejecutar el hecho con alevosía.
2.ª Ejecutar el hecho mediante disfraz, con abuso de superioridad o aprovechando las circunstancias de lugar, tiempo o auxilio de otras personas que debiliten la defensa del ofendido o faciliten la impunidad del delincuente.
3.ª Ejecutar el hecho mediante precio, recompensa o promesa.
4.ª Cometer el delito por motivos racistas, antisemitas u otra clase de discriminación referente a la ideología, religión o creencias de la víctima, la etnia, raza o nación a la que pertenezca, su sexo, orientación o identidad sexual, razones de género, la enfermedad que padezca o su discapacidad.
5.ª Aumentar deliberada e inhumanamente el sufrimiento de la víctima, causando a ésta padecimientos innecesarios para la ejecución del delito.
6.ª Obrar con abuso de confianza.
7.ª Prevalerse del carácter público que tenga el culpable.
8.ª Ser reincidente.""",
            libro="I",
            titulo_grupo="Disposiciones generales",
            capitulo="II",
            seccion="De las circunstancias que agravan la responsabilidad criminal"
        )

        # LIBRO II - Delitos y sus penas

        # HOMICIDIO
        articulos["138"] = ArticuloCP(
            numero="138",
            titulo="Homicidio",
            contenido="El que matare a otro será castigado, como reo de homicidio, con la pena de prisión de diez a quince años.",
            libro="II",
            titulo_grupo="Delitos contra las personas",
            capitulo="I",
            seccion="Del homicidio y sus formas"
        )

        articulos["139"] = ArticuloCP(
            numero="139",
            titulo="Asesinato",
            contenido="""Será castigado con la pena de prisión de quince a veinticinco años, como reo de asesinato, el que matare a otro concurriendo alguna de las circunstancias siguientes:
1.ª Con alevosía.
2.ª Por precio, recompensa o promesa.
3.ª Con ensañamiento, aumentando deliberada e inhumanamente el dolor del ofendido.
4.ª Para facilitar la comisión de otro delito o para evitar que se descubra.""",
            libro="II",
            titulo_grupo="Delitos contra las personas",
            capitulo="I",
            seccion="Del homicidio y sus formas"
        )

        # LESIONES
        articulos["147"] = ArticuloCP(
            numero="147",
            titulo="Lesiones",
            contenido="""1. El que, por cualquier medio o procedimiento, causare a otro una lesión que menoscabe su integridad corporal o su salud física o mental, será castigado, como reo del delito de lesiones con la pena de prisión de tres meses a tres años o multa de seis a doce meses, siempre que la lesión requiera objetivamente para su sanidad, además de una primera asistencia facultativa, tratamiento médico o quirúrgico. La simple vigilancia o seguimiento facultativo del curso de la lesión no se considerará tratamiento médico.
2. No obstante, el hecho descrito en el apartado anterior será castigado con la pena de prisión de uno a tres años si concurre alguna de las circunstancias siguientes:
a) Si la víctima fuere menor de catorce años o persona con discapacidad necesitada de especial protección.
b) Si la lesión se produce mediante el uso de armas, instrumentos, objetos, medios, métodos o formas concretamente peligrosas para la vida o salud, física o psíquica, del lesionado.
c) Si existiere relación de parentesco del art. 23.""",
            libro="II",
            titulo_grupo="Delitos contra las personas",
            capitulo="III",
            seccion="De las lesiones"
        )

        articulos["148"] = ArticuloCP(
            numero="148",
            titulo="Lesiones graves",
            contenido="""Las lesiones previstas en el apartado 1 del artículo anterior podrán ser castigadas con la pena de prisión de dos a cinco años, atendiendo al resultado causado o riesgo producido:
1.º Si en la agresión se hubieren utilizado instrumentos, armas o medios peligrosos para la vida o salud.
2.º Si hubiere mediado alevosía o ensañamiento.
3.º Si la víctima fuere menor de doce años o persona con discapacidad necesitada de especial protección.
4.º Si la víctima fuere o hubiere sido esposa o mujer ligada al autor por análoga relación de afectividad, aun sin convivencia.""",
            libro="II",
            titulo_grupo="Delitos contra las personas",
            capitulo="III"
        )

        # HURTO
        articulos["234"] = ArticuloCP(
            numero="234",
            titulo="Hurto",
            contenido="""1. El que, con ánimo de lucro, tomare las cosas muebles ajenas sin la voluntad de su dueño será castigado, como reo de hurto, con la pena de prisión de seis a dieciocho meses si la cuantía de lo sustraído excediese de 400 euros.
2. Con la misma pena se castigará al que en el plazo de un año realice tres veces la acción descrita en el artículo 234.1, siempre que el montante acumulado de las infracciones sea superior al mínimo de la referida figura del delito.""",
            libro="II",
            titulo_grupo="Delitos contra el patrimonio y el orden socioeconómico",
            capitulo="I",
            seccion="De los hurtos"
        )

        # ROBO
        articulos["237"] = ArticuloCP(
            numero="237",
            titulo="Robo con fuerza en las cosas",
            contenido="Son reos del delito de robo los que, con ánimo de lucro, se apoderaren de las cosas muebles ajenas empleando fuerza en las cosas para acceder o abandonar el lugar donde éstas se encuentran o violencia o intimidación en las personas, sea al cometer el delito, para proteger la huida, o sobre los que acudiesen en auxilio de la víctima o que le persiguieren.",
            libro="II",
            titulo_grupo="Delitos contra el patrimonio",
            capitulo="II",
            seccion="De los robos"
        )

        articulos["242"] = ArticuloCP(
            numero="242",
            titulo="Robo con violencia o intimidación",
            contenido="""El culpable de robo con violencia o intimidación en las personas será castigado con la pena de prisión de dos a cinco años, sin perjuicio de la que pudiera corresponder a los actos de violencia física que realizase.
Cuando el robo se cometa en casa habitada, edificio público o cualquiera de sus dependencias, se impondrá la pena de prisión de tres años y seis meses a cinco años.""",
            libro="II",
            titulo_grupo="Delitos contra el patrimonio",
            capitulo="II",
            seccion="De los robos"
        )

        # ESTAFA
        articulos["248"] = ArticuloCP(
            numero="248",
            titulo="Estafa",
            contenido="""1. Cometen estafa los que, con ánimo de lucro, utilizaren engaño bastante para producir error en otro, induciéndolo a realizar un acto de disposición en perjuicio propio o ajeno.
2. También se consideran reos de estafa:
a) Los que, con ánimo de lucro y valiéndose de alguna manipulación informática o artificio semejante, consigan una transferencia no consentida de cualquier activo patrimonial en perjuicio de otro.
b) Los que fabricaren, introdujeren, poseyeren o facilitaren programas informáticos específicamente destinados a la comisión de las estafas previstas en este artículo.
c) Los que utilizando tarjetas de crédito o débito, o cheques de viaje, o los datos obrantes en cualquiera de ellos, realicen operaciones de cualquier clase en perjuicio de su titular o de un tercero.""",
            libro="II",
            titulo_grupo="Delitos contra el patrimonio",
            capitulo="VI",
            seccion="De las estafas"
        )

        articulos["249"] = ArticuloCP(
            numero="249",
            titulo="Penas de la estafa",
            contenido="""Los reos de estafa serán castigados con la pena de prisión de seis meses a tres años, si la cuantía de lo defraudado excediese de 400 euros.""",
            libro="II",
            titulo_grupo="Delitos contra el patrimonio",
            capitulo="VI"
        )

        # DELITOS CONTRA LA LIBERTAD SEXUAL
        articulos["178"] = ArticuloCP(
            numero="178",
            titulo="Agresión sexual",
            contenido="""1. El que realizare actos que atenten contra la libertad sexual de otra persona sin su consentimiento, será castigado, como responsable de agresión sexual, con la pena de prisión de uno a cuatro años.
2. Cuando la agresión sexual consista en acceso carnal por vía vaginal, anal o bucal, o introducción de miembros corporales u objetos por alguna de las dos primeras vías, el responsable será castigado como reo de violación con la pena de prisión de cuatro a doce años.""",
            libro="II",
            titulo_grupo="Delitos contra la libertad e indemnidad sexual",
            capitulo="I",
            ultima_modificacion="LO 10/2022 (Ley del 'solo sí es sí')"
        )

        # VIOLENCIA DE GÉNERO
        articulos["153"] = ArticuloCP(
            numero="153",
            titulo="Violencia de género",
            contenido="""1. El que por cualquier medio o procedimiento causare a otro menoscabo psíquico o una lesión de menor gravedad de las previstas en el apartado 2 del artículo 147, o golpeare o maltratare de obra a otro sin causarle lesión, cuando la ofendida sea o haya sido esposa, o mujer que esté o haya estado ligada a él por una análoga relación de afectividad aun sin convivencia, o persona especialmente vulnerable que conviva con el autor, será castigado con la pena de prisión de seis meses a un año o de trabajos en beneficio de la comunidad de treinta y uno a ochenta días y, en todo caso, privación del derecho a la tenencia y porte de armas de un año y un día a tres años, así como, cuando el juez o tribunal lo estime adecuado al interés del menor o persona con discapacidad necesitada de especial protección, inhabilitación especial para el ejercicio de la patria potestad, tutela, curatela, guarda o acogimiento hasta cinco años.""",
            libro="II",
            titulo_grupo="Delitos contra las personas",
            capitulo="III",
            ultima_modificacion="LO 1/2004"
        )

        # TRÁFICO DE DROGAS
        articulos["368"] = ArticuloCP(
            numero="368",
            titulo="Tráfico de drogas",
            contenido="""1. Los que ejecuten actos de cultivo, elaboración o tráfico, o de otro modo promuevan, favorezcan o faciliten el consumo ilegal de drogas tóxicas, estupefacientes o sustancias psicotrópicas, o las posean con aquellos fines, serán castigados con las penas de prisión de tres a seis años y multa del tanto al triplo del valor de la droga objeto del delito si se tratare de sustancias o productos que causen grave daño a la salud, y de prisión de uno a tres años y multa del tanto al duplo en los demás casos.
2. No obstante lo dispuesto en el apartado anterior, los tribunales podrán imponer la pena inferior en grado a las señaladas en atención a la escasa entidad del hecho y a las circunstancias personales del culpable.""",
            libro="II",
            titulo_grupo="Delitos contra la salud pública",
            capitulo="III"
        )

        # CONDUCCIÓN TEMERARIA
        articulos["379"] = ArticuloCP(
            numero="379",
            titulo="Conducción temeraria",
            contenido="""1. El que condujere un vehículo de motor o un ciclomotor a velocidad superior en sesenta kilómetros por hora en vía urbana o en ochenta kilómetros por hora en vía interurbana a la permitida reglamentariamente, será castigado con la pena de prisión de tres a seis meses o con la de multa de seis a doce meses o con la de trabajos en beneficio de la comunidad de treinta y uno a noventa días, y, en cualquier caso, con la de privación del derecho a conducir vehículos a motor y ciclomotores por tiempo superior a uno y hasta cuatro años.
2. Con las mismas penas será castigado el que condujere un vehículo de motor o ciclomotor bajo la influencia de drogas tóxicas, estupefacientes, sustancias psicotrópicas o de bebidas alcohólicas. En todo caso será condenado con dichas penas el que condujere con una tasa de alcohol en aire espirado superior a 0,60 miligramos por litro o con una tasa de alcohol en sangre superior a 1,2 gramos por litro.""",
            libro="II",
            titulo_grupo="Delitos contra la seguridad vial",
            capitulo="IV"
        )

        return articulos

    def _cargar_tipos_penales(self) -> Dict[str, TipoPenal]:
        """Carga los tipos penales con sus elementos"""
        tipos = {}

        tipos["homicidio"] = TipoPenal(
            nombre="Homicidio",
            articulos=["138"],
            bien_juridico="Vida humana independiente",
            elementos_objetivos=[
                "Conducta: matar (causar la muerte)",
                "Sujeto pasivo: persona viva",
                "Nexo causal entre conducta y muerte",
                "Ausencia de circunstancias del asesinato"
            ],
            elementos_subjetivos=[
                "Dolo: conocimiento y voluntad de causar la muerte",
                "Cualquier forma de dolo (directo, eventual)"
            ],
            pena_minima="10 años de prisión",
            pena_maxima="15 años de prisión",
            tipo="Básico",
            gravedad="Grave",
            prescripcion_delito="15 años",
            prescripcion_pena="30 años"
        )

        tipos["asesinato"] = TipoPenal(
            nombre="Asesinato",
            articulos=["139"],
            bien_juridico="Vida humana independiente",
            elementos_objetivos=[
                "Matar a otra persona",
                "Concurrencia de alguna circunstancia cualificada: alevosía, precio, ensañamiento, o para facilitar/evitar descubrimiento de otro delito"
            ],
            elementos_subjetivos=[
                "Dolo de matar",
                "Conocimiento de la circunstancia cualificadora"
            ],
            pena_minima="15 años de prisión",
            pena_maxima="25 años de prisión (prisión permanente revisable en casos excepcionales)",
            tipo="Agravado",
            gravedad="Grave",
            prescripcion_delito="20 años",
            prescripcion_pena="40 años"
        )

        tipos["lesiones_basicas"] = TipoPenal(
            nombre="Lesiones básicas",
            articulos=["147.1"],
            bien_juridico="Integridad física y salud (física o mental)",
            elementos_objetivos=[
                "Causar a otro una lesión",
                "Menoscabo de integridad corporal o salud física/mental",
                "Necesidad objetiva de tratamiento médico o quirúrgico (además de primera asistencia)"
            ],
            elementos_subjetivos=[
                "Dolo de lesionar",
                "Conocimiento del menoscabo causado"
            ],
            pena_minima="3 meses de prisión o multa de 6 meses",
            pena_maxima="3 años de prisión o multa de 12 meses",
            tipo="Básico",
            gravedad="Menos grave",
            prescripcion_delito="5 años",
            prescripcion_pena="10 años"
        )

        tipos["hurto"] = TipoPenal(
            nombre="Hurto",
            articulos=["234"],
            bien_juridico="Patrimonio (propiedad y posesión)",
            elementos_objetivos=[
                "Tomar cosas muebles ajenas",
                "Sin voluntad del dueño",
                "Cuantía superior a 400 euros",
                "Sin violencia, intimidación ni fuerza en las cosas"
            ],
            elementos_subjetivos=[
                "Ánimo de lucro",
                "Conocimiento de ajenidad de la cosa"
            ],
            pena_minima="6 meses de prisión",
            pena_maxima="18 meses de prisión",
            tipo="Básico",
            gravedad="Menos grave",
            prescripcion_delito="5 años",
            prescripcion_pena="10 años"
        )

        tipos["robo_fuerza"] = TipoPenal(
            nombre="Robo con fuerza en las cosas",
            articulos=["237", "238", "239", "240", "241"],
            bien_juridico="Patrimonio y, en su caso, inviolabilidad domicilio",
            elementos_objetivos=[
                "Apoderamiento de cosas muebles ajenas",
                "Empleo de fuerza en las cosas",
                "Para acceder, permanecer o abandonar el lugar"
            ],
            elementos_subjetivos=[
                "Ánimo de lucro",
                "Conocimiento del empleo de fuerza"
            ],
            pena_minima="1 año de prisión",
            pena_maxima="3 años de prisión (mayor si es en casa habitada)",
            tipo="Básico",
            gravedad="Menos grave a Grave (según modalidad)",
            prescripcion_delito="5-10 años",
            prescripcion_pena="10-15 años"
        )

        tipos["robo_violencia"] = TipoPenal(
            nombre="Robo con violencia o intimidación",
            articulos=["242", "243"],
            bien_juridico="Patrimonio, libertad y seguridad personal",
            elementos_objetivos=[
                "Apoderamiento de cosas muebles ajenas",
                "Empleo de violencia o intimidación en las personas",
                "Al cometer el delito, para proteger huida o sobre quienes auxilien"
            ],
            elementos_subjetivos=[
                "Ánimo de lucro",
                "Conocimiento de violencia/intimidación"
            ],
            pena_minima="2 años de prisión",
            pena_maxima="5 años de prisión (más pena por violencia física)",
            tipo="Agravado",
            gravedad="Grave",
            prescripcion_delito="10 años",
            prescripcion_pena="15 años"
        )

        tipos["estafa"] = TipoPenal(
            nombre="Estafa",
            articulos=["248", "249"],
            bien_juridico="Patrimonio (mediante engaño)",
            elementos_objetivos=[
                "Engaño bastante",
                "Error en la víctima",
                "Acto de disposición patrimonial perjudicial",
                "Cuantía superior a 400 euros"
            ],
            elementos_subjetivos=[
                "Ánimo de lucro",
                "Conocimiento del engaño y del perjuicio"
            ],
            pena_minima="6 meses de prisión",
            pena_maxima="3 años de prisión",
            tipo="Básico",
            gravedad="Menos grave",
            prescripcion_delito="5 años",
            prescripcion_pena="10 años"
        )

        tipos["agresion_sexual"] = TipoPenal(
            nombre="Agresión sexual",
            articulos=["178.1"],
            bien_juridico="Libertad e indemnidad sexual",
            elementos_objetivos=[
                "Actos que atenten contra libertad sexual",
                "Sin consentimiento de la víctima",
                "Actos de contenido sexual pero sin acceso carnal"
            ],
            elementos_subjetivos=[
                "Dolo: conocimiento de ausencia de consentimiento",
                "Voluntad de realizar acto sexual"
            ],
            pena_minima="1 año de prisión",
            pena_maxima="4 años de prisión",
            tipo="Básico",
            gravedad="Menos grave a Grave",
            prescripcion_delito="10 años",
            prescripcion_pena="15 años"
        )

        tipos["violacion"] = TipoPenal(
            nombre="Violación (agresión sexual con acceso carnal)",
            articulos=["178.2"],
            bien_juridico="Libertad e indemnidad sexual",
            elementos_objetivos=[
                "Acceso carnal vía vaginal, anal o bucal",
                "O introducción de miembros corporales u objetos por vía vaginal/anal",
                "Sin consentimiento"
            ],
            elementos_subjetivos=[
                "Dolo: conocimiento de ausencia de consentimiento",
                "Voluntad de acceso carnal"
            ],
            pena_minima="4 años de prisión",
            pena_maxima="12 años de prisión",
            tipo="Agravado",
            gravedad="Grave",
            prescripcion_delito="15 años",
            prescripcion_pena="25 años"
        )

        tipos["violencia_genero"] = TipoPenal(
            nombre="Violencia de género (maltrato art. 153)",
            articulos=["153"],
            bien_juridico="Integridad física y moral, dignidad",
            elementos_objetivos=[
                "Causar menoscabo psíquico, lesión leve, golpear o maltratar",
                "Víctima: esposa, exesposa, mujer ligada por relación de afectividad",
                "Contexto de violencia de género"
            ],
            elementos_subjetivos=[
                "Dolo de causar el menoscabo/maltrato",
                "Conocimiento de la relación con la víctima"
            ],
            pena_minima="6 meses de prisión o TBC 31 días",
            pena_maxima="1 año de prisión o TBC 80 días + privación armas",
            tipo="Específico",
            gravedad="Menos grave",
            prescripcion_delito="5 años",
            prescripcion_pena="10 años"
        )

        tipos["trafico_drogas"] = TipoPenal(
            nombre="Tráfico de drogas",
            articulos=["368"],
            bien_juridico="Salud pública",
            elementos_objetivos=[
                "Actos de cultivo, elaboración, tráfico",
                "Promover, favorecer o facilitar consumo ilegal",
                "Posesión con fines de tráfico",
                "Sustancias: drogas tóxicas, estupefacientes, psicotrópicas"
            ],
            elementos_subjetivos=[
                "Dolo: conocimiento de la sustancia",
                "Finalidad de promover/facilitar consumo ajeno"
            ],
            pena_minima="1-3 años prisión (sustancias no graves) o 3-6 años (graves)",
            pena_maxima="3 años + multa (no graves) o 6 años + multa (graves)",
            tipo="Básico",
            gravedad="Grave",
            prescripcion_delito="10 años",
            prescripcion_pena="15 años"
        )

        tipos["conduccion_temeraria"] = TipoPenal(
            nombre="Conducción temeraria/bajo influencia",
            articulos=["379"],
            bien_juridico="Seguridad vial",
            elementos_objetivos=[
                "Conducir vehículo de motor o ciclomotor",
                "Exceso velocidad (+60 km/h urbana o +80 km/h interurbana)",
                "O bajo influencia drogas/alcohol (>0,60 mg/l aire o >1,2 g/l sangre)"
            ],
            elementos_subjetivos=[
                "Dolo: conocimiento de la conducción en esas condiciones",
                "Voluntad de conducir"
            ],
            pena_minima="3 meses prisión, multa 6 meses o TBC 31 días + privación conducir 1 año",
            pena_maxima="6 meses prisión, multa 12 meses o TBC 90 días + privación conducir 4 años",
            tipo="Básico",
            gravedad="Menos grave",
            prescripcion_delito="5 años",
            prescripcion_pena="10 años"
        )

        return tipos

    def _cargar_circunstancias(self) -> Dict[str, CircunstanciaModificativa]:
        """Carga las circunstancias modificativas de la responsabilidad"""
        circunstancias = {}

        # EXIMENTES
        circunstancias["eximente_anomalia_psiquica"] = CircunstanciaModificativa(
            tipo="eximente",
            articulo="20.1",
            nombre="Anomalía o alteración psíquica",
            descripcion="El que al tiempo de cometer la infracción penal, a causa de cualquier anomalía o alteración psíquica, no pueda comprender la ilicitud del hecho o actuar conforme a esa comprensión.",
            efectos="Exención total de responsabilidad criminal (puede aplicarse medida de seguridad)",
            ejemplos=[
                "Esquizofrenia paranoide en brote",
                "Trastorno bipolar en fase maníaca grave",
                "Demencia avanzada",
                "Retraso mental profundo"
            ]
        )

        circunstancias["eximente_legitima_defensa"] = CircunstanciaModificativa(
            tipo="eximente",
            articulo="20.4",
            nombre="Legítima defensa",
            descripcion="El que obre en defensa de la persona o derechos propios o ajenos, con agresión ilegítima, necesidad racional del medio empleado y falta de provocación suficiente.",
            efectos="Exención total de responsabilidad criminal",
            ejemplos=[
                "Repeler agresión con arma blanca usando fuerza proporcional",
                "Defensa de tercero ante agresión sexual",
                "Protección del domicilio ante entrada violenta"
            ]
        )

        circunstancias["eximente_estado_necesidad"] = CircunstanciaModificativa(
            tipo="eximente",
            articulo="20.5",
            nombre="Estado de necesidad",
            descripcion="El que, en estado de necesidad, para evitar un mal propio o ajeno lesione un bien jurídico de otra persona, siempre que el mal causado no sea mayor que el evitado, no haya provocación intencional y no tenga obligación de sacrificarse.",
            efectos="Exención total de responsabilidad criminal",
            ejemplos=[
                "Hurto de alimentos por hambre extrema (necesidad vital)",
                "Daños para evitar incendio",
                "Lesiones para salvar vida en accidente"
            ]
        )

        circunstancias["eximente_miedo_insuperable"] = CircunstanciaModificativa(
            tipo="eximente",
            articulo="20.6",
            nombre="Miedo insuperable",
            descripcion="El que obre impulsado por miedo insuperable.",
            efectos="Exención total de responsabilidad criminal",
            ejemplos=[
                "Coacción bajo amenaza de muerte inmediata",
                "Actuación bajo síndrome de Estocolmo",
                "Terror pánico ante situación de peligro extremo"
            ]
        )

        # ATENUANTES
        circunstancias["atenuante_incompleta"] = CircunstanciaModificativa(
            tipo="atenuante",
            articulo="21.1",
            nombre="Eximente incompleta",
            descripcion="Cuando no concurren todos los requisitos de una eximente pero sí la mayoría de ellos.",
            efectos="Rebaja de pena en uno o dos grados (según intensidad)",
            ejemplos=[
                "Anomalía psíquica que no anula totalmente la comprensión",
                "Legítima defensa con exceso en el medio empleado",
                "Estado de necesidad con mal causado ligeramente superior"
            ]
        )

        circunstancias["atenuante_adiccion"] = CircunstanciaModificativa(
            tipo="atenuante",
            articulo="21.2",
            nombre="Grave adicción",
            descripcion="Actuar el culpable a causa de su grave adicción a drogas, alcohol u otras sustancias.",
            efectos="Rebaja de pena en un grado",
            ejemplos=[
                "Toxicómano en síndrome de abstinencia cometiendo hurto",
                "Alcohólico crónico en estado de necesidad por adicción",
                "Ludópata con adicción acreditada"
            ]
        )

        circunstancias["atenuante_arrebato"] = CircunstanciaModificativa(
            tipo="atenuante",
            articulo="21.3",
            nombre="Arrebato, obcecación u otro estado pasional",
            descripcion="Obrar por causas o estímulos tan poderosos que hayan producido arrebato, obcecación u otro estado pasional de entidad semejante.",
            efectos="Rebaja de pena (habitualmente en un grado)",
            ejemplos=[
                "Reacción violenta inmediata tras descubrir infidelidad flagrante",
                "Estado de desesperación tras acoso prolongado",
                "Reacción emocional intensa ante provocación grave"
            ]
        )

        circunstancias["atenuante_confesion"] = CircunstanciaModificativa(
            tipo="atenuante",
            articulo="21.4",
            nombre="Confesión",
            descripcion="Haber confesado la infracción a las autoridades antes de conocer que el procedimiento se dirige contra él.",
            efectos="Rebaja de pena (habitualmente en un tercio en su mitad inferior)",
            ejemplos=[
                "Acudir voluntariamente a comisaría a confesar delito",
                "Confesar al ser preguntado como testigo, antes de ser imputado",
                "Autoinculpación espontánea"
            ]
        )

        circunstancias["atenuante_reparacion"] = CircunstanciaModificativa(
            tipo="atenuante",
            articulo="21.5",
            nombre="Reparación del daño",
            descripcion="Haber reparado el daño ocasionado a la víctima o disminuir sus efectos, antes del juicio oral.",
            efectos="Rebaja de pena (intensidad según grado de reparación)",
            ejemplos=[
                "Devolver lo sustraído antes del juicio",
                "Pagar indemnización completa",
                "Reparar daños materiales causados"
            ]
        )

        circunstancias["atenuante_analogica"] = CircunstanciaModificativa(
            tipo="atenuante",
            articulo="21.6",
            nombre="Atenuante analógica",
            descripcion="Cualquier otra circunstancia de análoga significación a las anteriores.",
            efectos="Rebaja de pena (variable según el caso)",
            ejemplos=[
                "Dilaciones indebidas en el proceso",
                "Colaboración con la justicia",
                "Conducta ejemplar posterior al delito",
                "Arrepentimiento sincero y activo"
            ]
        )

        # AGRAVANTES
        circunstancias["agravante_alevosa"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.1",
            nombre="Alevosía",
            descripcion="Ejecutar el hecho con alevosía (asegurando la ejecución sin riesgo para el autor que proceda de la defensa del ofendido).",
            efectos="Agrava la pena (puede cualificar delitos como asesinato)",
            ejemplos=[
                "Atacar a víctima dormida o indefensa",
                "Emboscada sorpresiva",
                "Ataque por la espalda sin aviso"
            ]
        )

        circunstancias["agravante_abuso_superioridad"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.2",
            nombre="Abuso de superioridad, disfraz o aprovechamiento de circunstancias",
            descripcion="Ejecutar el hecho mediante disfraz, con abuso de superioridad o aprovechando circunstancias de lugar, tiempo o auxilio que debiliten la defensa.",
            efectos="Agrava la pena",
            ejemplos=[
                "Varios agresores contra una víctima",
                "Aprovechamiento de lugar oscuro o solitario",
                "Uso de disfraz para ocultar identidad",
                "Ataque nocturno aprovechando oscuridad"
            ]
        )

        circunstancias["agravante_precio"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.3",
            nombre="Precio, recompensa o promesa",
            descripcion="Ejecutar el hecho mediante precio, recompensa o promesa.",
            efectos="Agrava la pena (puede cualificar asesinato)",
            ejemplos=[
                "Sicario contratado para matar",
                "Pago por comisión de delito",
                "Promesa de beneficio económico"
            ]
        )

        circunstancias["agravante_discriminacion"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.4",
            nombre="Discriminación (motivos racistas, sexistas, homófobos, etc.)",
            descripcion="Cometer el delito por motivos racistas, antisemitas, de discriminación por ideología, religión, etnia, raza, nación, sexo, orientación sexual, identidad de género, enfermedad o discapacidad.",
            efectos="Agrava la pena sustancialmente",
            ejemplos=[
                "Agresión por motivos racistas",
                "Delito de odio por orientación sexual",
                "Discriminación por discapacidad",
                "Violencia xenófoba"
            ]
        )

        circunstancias["agravante_ensanamiento"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.5",
            nombre="Ensañamiento",
            descripcion="Aumentar deliberada e inhumanamente el sufrimiento de la víctima, causando padecimientos innecesarios.",
            efectos="Agrava la pena (puede cualificar asesinato)",
            ejemplos=[
                "Tortura antes de causar la muerte",
                "Prolongación innecesaria del sufrimiento",
                "Múltiples agresiones cuando una sería suficiente"
            ]
        )

        circunstancias["agravante_abuso_confianza"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.6",
            nombre="Abuso de confianza",
            descripcion="Obrar con abuso de confianza.",
            efectos="Agrava la pena",
            ejemplos=[
                "Empleado que defrauda al empresario",
                "Amigo que aprovecha confianza para robar",
                "Profesional que traiciona secreto profesional"
            ]
        )

        circunstancias["agravante_prevalencia_caracter_publico"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.7",
            nombre="Prevalerse del carácter público",
            descripcion="Prevalerse del carácter público que tenga el culpable.",
            efectos="Agrava la pena",
            ejemplos=[
                "Policía que comete delito usando su condición",
                "Funcionario que abusa de autoridad",
                "Político que se prevalece de cargo público"
            ]
        )

        circunstancias["agravante_reincidencia"] = CircunstanciaModificativa(
            tipo="agravante",
            articulo="22.8",
            nombre="Reincidencia",
            descripcion="Ser reincidente (haber sido condenado por delito de la misma naturaleza, no cancelado ni prescrito).",
            efectos="Agrava la pena en un grado (con límites)",
            ejemplos=[
                "Condenado previo por hurto que comete nuevo hurto",
                "Antecedentes por delitos violentos y nueva condena por violencia",
                "Historial delictivo de la misma naturaleza"
            ]
        )

        return circunstancias

    def buscar_articulo(self, numero: str) -> Optional[ArticuloCP]:
        """Busca un artículo por número"""
        return self.articulos.get(numero)

    def buscar_tipo_penal(self, nombre: str) -> Optional[TipoPenal]:
        """Busca un tipo penal por nombre"""
        return self.tipos_penales.get(nombre.lower())

    def buscar_circunstancia(self, clave: str) -> Optional[CircunstanciaModificativa]:
        """Busca una circunstancia modificativa"""
        return self.circunstancias.get(clave)

    def identificar_tipos_por_palabras_clave(self, texto: str) -> List[TipoPenal]:
        """Identifica posibles tipos penales basándose en palabras clave del texto"""
        texto_lower = texto.lower()
        tipos_identificados = []

        # Mapeo de palabras clave a tipos penales
        mapeo = {
            "matar": ["homicidio", "asesinato"],
            "muerte": ["homicidio", "asesinato"],
            "asesinar": ["asesinato"],
            "alevosía": ["asesinato"],
            "lesion": ["lesiones_basicas"],
            "golpe": ["lesiones_basicas", "violencia_genero"],
            "herir": ["lesiones_basicas"],
            "robar": ["hurto", "robo_fuerza", "robo_violencia"],
            "hurto": ["hurto"],
            "sustraccion": ["hurto"],
            "robo": ["robo_fuerza", "robo_violencia"],
            "violencia": ["robo_violencia", "violencia_genero"],
            "intimidacion": ["robo_violencia"],
            "estafa": ["estafa"],
            "engaño": ["estafa"],
            "defraud": ["estafa"],
            "agresi": ["agresion_sexual"],
            "violacion": ["violacion"],
            "sexual": ["agresion_sexual", "violacion"],
            "droga": ["trafico_drogas"],
            "estupefaciente": ["trafico_drogas"],
            "trafico": ["trafico_drogas"],
            "conducir": ["conduccion_temeraria"],
            "alcohol": ["conduccion_temeraria"],
            "velocidad": ["conduccion_temeraria"],
            "maltrato": ["violencia_genero"],
            "mujer": ["violencia_genero"],
            "pareja": ["violencia_genero"]
        }

        for palabra_clave, tipos in mapeo.items():
            if palabra_clave in texto_lower:
                for tipo in tipos:
                    tipo_penal = self.tipos_penales.get(tipo)
                    if tipo_penal and tipo_penal not in tipos_identificados:
                        tipos_identificados.append(tipo_penal)

        return tipos_identificados

    def calcular_pena(self, tipo_penal: str, atenuantes: List[str] = None,
                     agravantes: List[str] = None) -> Tuple[str, str]:
        """
        Calcula el marco penal aplicable según tipo penal y circunstancias
        Retorna (pena_minima, pena_maxima) como strings
        """
        tipo = self.tipos_penales.get(tipo_penal.lower())
        if not tipo:
            return ("Tipo penal no encontrado", "")

        # Pena básica
        pena_info = f"Pena básica: {tipo.pena_minima} a {tipo.pena_maxima}"

        # Aplicar atenuantes (simplificado - en realidad requiere cálculo complejo)
        if atenuantes:
            pena_info += f"\n\nCon {len(atenuantes)} atenuante(s): Rebaja de pena en grado inferior"

        # Aplicar agravantes
        if agravantes:
            pena_info += f"\n\nCon {len(agravantes)} agravante(s): Posible agravación según art. 66"

        return (tipo.pena_minima, tipo.pena_maxima)

    def get_prescripcion(self, tipo_penal: str) -> Dict[str, str]:
        """Obtiene plazos de prescripción del delito y de la pena"""
        tipo = self.tipos_penales.get(tipo_penal.lower())
        if not tipo:
            return {}

        return {
            "prescripcion_delito": tipo.prescripcion_delito,
            "prescripcion_pena": tipo.prescripcion_pena
        }
