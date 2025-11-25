"""
Módulo de Redacción Legal
Generador de documentos legales (querellas, recursos, informes, denuncias)
"""

from .document_generator import DocumentGenerator
from .templates import PlantillasLegales

__all__ = ['DocumentGenerator', 'PlantillasLegales']
