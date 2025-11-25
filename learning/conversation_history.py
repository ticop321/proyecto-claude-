"""
Sistema de Historial de Conversaciones
Almacena el contexto de cada conversación por caso
"""

import json
import os
from typing import List, Dict
from datetime import datetime


class ConversationHistory:
    """
    Gestiona el historial de conversaciones
    Mantiene contexto entre sesiones
    """

    def __init__(self, data_dir: str = "conversations"):
        self.data_dir = data_dir
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Crea el directorio de conversaciones"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def guardar_mensaje(self, case_id: str, rol: str, mensaje: str, metadata: Dict = None):
        """
        Guarda un mensaje en el historial

        Args:
            case_id: ID del caso/conversación
            rol: 'user' o 'assistant'
            mensaje: Contenido del mensaje
            metadata: Información adicional (emoción detectada, tipo de consulta, etc.)
        """
        filepath = os.path.join(self.data_dir, f"{case_id}.json")

        # Cargar historial existente
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                historial = json.load(f)
        else:
            historial = {
                "case_id": case_id,
                "fecha_inicio": datetime.now().isoformat(),
                "mensajes": []
            }

        # Agregar nuevo mensaje
        entrada = {
            "timestamp": datetime.now().isoformat(),
            "rol": rol,
            "mensaje": mensaje,
            "metadata": metadata or {}
        }

        historial["mensajes"].append(entrada)
        historial["ultima_actualizacion"] = datetime.now().isoformat()

        # Guardar
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(historial, f, ensure_ascii=False, indent=2)

    def cargar_historial(self, case_id: str) -> List[Dict]:
        """Carga el historial de un caso"""
        filepath = os.path.join(self.data_dir, f"{case_id}.json")

        if not os.path.exists(filepath):
            return []

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("mensajes", [])

    def obtener_contexto_reciente(self, case_id: str, num_mensajes: int = 5) -> List[Dict]:
        """Obtiene los últimos N mensajes como contexto"""
        historial = self.cargar_historial(case_id)
        return historial[-num_mensajes:] if historial else []

    def listar_casos(self) -> List[str]:
        """Lista todos los casos con conversaciones guardadas"""
        archivos = [f.replace('.json', '') for f in os.listdir(self.data_dir) if f.endswith('.json')]
        return archivos
