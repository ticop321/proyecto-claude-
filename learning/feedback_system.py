"""
Sistema de Retroalimentación
Captura y analiza feedback del usuario para mejorar
"""

import json
import os
from typing import Dict, List
from datetime import datetime


class FeedbackSystem:
    """
    Sistema de feedback y mejora continua
    """

    def __init__(self, data_dir: str = "feedback"):
        self.data_dir = data_dir
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Crea el directorio de feedback"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def registrar_feedback(self, user_id: str, case_id: str,
                          puntuacion: int, comentario: str = "",
                          aspecto: str = "general"):
        """
        Registra feedback del usuario

        Args:
            user_id: ID del usuario
            case_id: ID del caso
            puntuacion: 1-5 estrellas
            comentario: Comentario opcional
            aspecto: 'precision', 'utilidad', 'claridad', 'empatia', 'general'
        """
        feedback = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "case_id": case_id,
            "aspecto": aspecto,
            "puntuacion": puntuacion,
            "comentario": comentario
        }

        filepath = os.path.join(self.data_dir, "feedback_log.json")

        # Cargar log existente
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                log = json.load(f)
        else:
            log = []

        log.append(feedback)

        # Guardar
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(log, f, ensure_ascii=False, indent=2)

    def obtener_estadisticas(self) -> Dict:
        """Obtiene estadísticas de feedback"""
        filepath = os.path.join(self.data_dir, "feedback_log.json")

        if not os.path.exists(filepath):
            return {"promedio": 0, "total": 0}

        with open(filepath, 'r', encoding='utf-8') as f:
            log = json.load(f)

        if not log:
            return {"promedio": 0, "total": 0}

        puntuaciones = [f["puntuacion"] for f in log]
        promedio = sum(puntuaciones) / len(puntuaciones)

        return {
            "promedio": round(promedio, 2),
            "total": len(log),
            "distribucion": {
                "5_estrellas": sum(1 for p in puntuaciones if p == 5),
                "4_estrellas": sum(1 for p in puntuaciones if p == 4),
                "3_estrellas": sum(1 for p in puntuaciones if p == 3),
                "2_estrellas": sum(1 for p in puntuaciones if p == 2),
                "1_estrella": sum(1 for p in puntuaciones if p == 1)
            }
        }
