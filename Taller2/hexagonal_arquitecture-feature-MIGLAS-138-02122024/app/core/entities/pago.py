from datetime import datetime
from dataclasses import dataclass
from typing import Optional
import uuid


@dataclass
class Pago:
    """Entidad Pago del dominio"""
    id: str
    nombre_cliente: str
    monto: float
    fecha: datetime
    estado: str = "COMPLETADO"
    
    def __post_init__(self):
        """Validaciones de negocio"""
        if self.monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        if not self.nombre_cliente or not self.nombre_cliente.strip():
            raise ValueError("El nombre del cliente es requerido")
    
    @classmethod
    def crear_nuevo(cls, nombre_cliente: str, monto: float) -> 'Pago':
        """Factory method para crear un nuevo pago"""
        return cls(
            id=str(uuid.uuid4()),
            nombre_cliente=nombre_cliente.strip(),
            monto=monto,
            fecha=datetime.now(),
            estado="COMPLETADO"
        )
    
    def puede_ser_eliminado(self) -> bool:
        """Regla de negocio: solo se puede eliminar si está COMPLETADO"""
        return self.estado == "COMPLETADO"
