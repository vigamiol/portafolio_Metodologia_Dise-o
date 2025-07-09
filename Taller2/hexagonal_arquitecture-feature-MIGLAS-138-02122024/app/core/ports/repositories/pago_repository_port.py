from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.pago import Pago


class PagoRepositoryPort(ABC):
    """Puerto para el repositorio de pagos"""
    
    @abstractmethod
    def guardar(self, pago: Pago) -> Pago:
        """Guarda un pago en el repositorio"""
        pass
    
    @abstractmethod
    def obtener_todos(self) -> List[Pago]:
        """Obtiene todos los pagos"""
        pass
    
    @abstractmethod
    def obtener_por_id(self, pago_id: str) -> Optional[Pago]:
        """Obtiene un pago por su ID"""
        pass
    
    @abstractmethod
    def obtener_por_cliente(self, nombre_cliente: str) -> List[Pago]:
        """Obtiene todos los pagos de un cliente"""
        pass
    
    @abstractmethod
    def eliminar(self, pago_id: str) -> bool:
        """Elimina un pago por su ID. Retorna True si fue eliminado"""
        pass
