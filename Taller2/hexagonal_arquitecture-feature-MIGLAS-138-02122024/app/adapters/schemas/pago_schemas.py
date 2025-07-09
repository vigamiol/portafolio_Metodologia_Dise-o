from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class RegistrarPagoRequest(BaseModel):
    """Esquema para registrar un pago"""
    nombre_cliente: str = Field(..., min_length=1, description="Nombre del cliente")
    monto: float = Field(..., gt=0, description="Monto del pago, debe ser mayor que cero")


class PagoResponse(BaseModel):
    """Esquema de respuesta para un pago"""
    id: str
    nombre_cliente: str
    monto: float
    fecha: datetime
    estado: str
    
    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    """Esquema para respuestas de error"""
    mensaje: str
    detalle: str = None


class ListaPagosResponse(BaseModel):
    """Esquema para lista de pagos"""
    pagos: List[PagoResponse]
    total: int
