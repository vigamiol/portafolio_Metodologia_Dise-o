from typing import List, Optional, Dict
from core.entities.pago import Pago
from core.ports.repositories.pago_repository_port import PagoRepositoryPort


class InMemoryPagoRepository(PagoRepositoryPort):
    """Implementación en memoria del repositorio de pagos"""
    
    def __init__(self):
        self._pagos: Dict[str, Pago] = {}
    
    def guardar(self, pago: Pago) -> Pago:
        """Guarda un pago en memoria"""
        self._pagos[pago.id] = pago
        return pago
    
    def obtener_todos(self) -> List[Pago]:
        """Obtiene todos los pagos"""
        return list(self._pagos.values())
    
    def obtener_por_id(self, pago_id: str) -> Optional[Pago]:
        """Obtiene un pago por su ID"""
        return self._pagos.get(pago_id)
    
    def obtener_por_cliente(self, nombre_cliente: str) -> List[Pago]:
        """Obtiene todos los pagos de un cliente (búsqueda insensible a mayúsculas)"""
        nombre_lower = nombre_cliente.lower().strip()
        return [
            pago for pago in self._pagos.values() 
            if pago.nombre_cliente.lower() == nombre_lower
        ]
    
    def eliminar(self, pago_id: str) -> bool:
        """Elimina un pago por su ID"""
        if pago_id in self._pagos:
            del self._pagos[pago_id]
            return True
        return False
