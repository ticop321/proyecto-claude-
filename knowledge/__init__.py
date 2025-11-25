"""
Módulo de Conocimiento Legal
Gestión de base de datos legal española (Código Penal, LECrim, Jurisprudencia)
"""

from .codigo_penal import CodigoPenal
from .jurisprudencia import Jurisprudencia
from .lecrim import LECrim

__all__ = ['CodigoPenal', 'Jurisprudencia', 'LECrim']
