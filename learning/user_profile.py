"""
Gestor de Perfiles de Usuario
Almacena preferencias, historial y contexto de cada usuario
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class UserProfile:
    """Perfil de usuario"""
    user_id: str
    nombre: str
    rol: str  # victima, acusado, profesional, consulta_general
    preferencias: Dict
    historial_casos: List[Dict]
    tono_preferido: str
    nivel_tecnico: str  # alto, medio, bajo
    fecha_creacion: str
    ultima_interaccion: str


class UserProfileManager:
    """
    Gestor de perfiles de usuario
    Mantiene contexto y preferencias de cada usuario
    """

    def __init__(self, data_dir: str = "user_data"):
        self.data_dir = data_dir
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Crea el directorio de datos si no existe"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def crear_perfil(self, user_id: str, nombre: str, rol: str = "consulta_general") -> UserProfile:
        """Crea un nuevo perfil de usuario"""
        perfil = UserProfile(
            user_id=user_id,
            nombre=nombre,
            rol=rol,
            preferencias={
                "idioma": "es",
                "formato_documentos": "txt",
                "notificaciones": True
            },
            historial_casos=[],
            tono_preferido="empatico" if rol in ["victima"] else "tecnico",
            nivel_tecnico="medio",
            fecha_creacion=datetime.now().isoformat(),
            ultima_interaccion=datetime.now().isoformat()
        )

        self._guardar_perfil(perfil)
        return perfil

    def cargar_perfil(self, user_id: str) -> Optional[UserProfile]:
        """Carga un perfil de usuario existente"""
        filepath = os.path.join(self.data_dir, f"{user_id}.json")

        if not os.path.exists(filepath):
            return None

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return UserProfile(**data)
        except Exception as e:
            print(f"Error cargando perfil: {e}")
            return None

    def _guardar_perfil(self, perfil: UserProfile):
        """Guarda el perfil de usuario"""
        filepath = os.path.join(self.data_dir, f"{perfil.user_id}.json")

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(asdict(perfil), f, ensure_ascii=False, indent=2)

    def actualizar_ultima_interaccion(self, user_id: str):
        """Actualiza la fecha de última interacción"""
        perfil = self.cargar_perfil(user_id)
        if perfil:
            perfil.ultima_interaccion = datetime.now().isoformat()
            self._guardar_perfil(perfil)

    def agregar_caso(self, user_id: str, caso: Dict):
        """Agrega un caso al historial del usuario"""
        perfil = self.cargar_perfil(user_id)
        if perfil:
            caso["fecha"] = datetime.now().isoformat()
            perfil.historial_casos.append(caso)
            self._guardar_perfil(perfil)

    def actualizar_preferencias(self, user_id: str, preferencias: Dict):
        """Actualiza las preferencias del usuario"""
        perfil = self.cargar_perfil(user_id)
        if perfil:
            perfil.preferencias.update(preferencias)
            self._guardar_perfil(perfil)

    def obtener_historial_casos(self, user_id: str) -> List[Dict]:
        """Obtiene el historial de casos del usuario"""
        perfil = self.cargar_perfil(user_id)
        return perfil.historial_casos if perfil else []

    def obtener_tono_preferido(self, user_id: str) -> str:
        """Obtiene el tono preferido del usuario"""
        perfil = self.cargar_perfil(user_id)
        return perfil.tono_preferido if perfil else "tecnico"

    def actualizar_tono_preferido(self, user_id: str, tono: str):
        """Actualiza el tono preferido del usuario"""
        perfil = self.cargar_perfil(user_id)
        if perfil:
            perfil.tono_preferido = tono
            self._guardar_perfil(perfil)
