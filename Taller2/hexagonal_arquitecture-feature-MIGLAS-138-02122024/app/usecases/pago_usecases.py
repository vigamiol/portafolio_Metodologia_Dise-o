from typing import List, Optional
from core.entities.pago import Pago
from core.ports.repositories.pago_repository_port import PagoRepositoryPort


class RegistrarPagoUseCase:
    """Caso de uso: Registrar un pago"""
    
    def __init__(self, pago_repository: PagoRepositoryPort):
        self._pago_repository = pago_repository
    
    def ejecutar(self, nombre_cliente: str, monto: float) -> Pago:
        """
        Registra un nuevo pago
        
        Args:
            nombre_cliente: Nombre del cliente
            monto: Monto del pago
            
        Returns:
            Pago creado
            
        Raises:
            ValueError: Si los datos no son válidos
        """
        # Crear el pago (las validaciones están en la entidad)
        pago = Pago.crear_nuevo(nombre_cliente, monto)
        
        # Guardar en el repositorio
        return self._pago_repository.guardar(pago)


class ListarPagosUseCase:
    """Caso de uso: Listar todos los pagos"""
    
    def __init__(self, pago_repository: PagoRepositoryPort):
        self._pago_repository = pago_repository
    
    def ejecutar(self) -> List[Pago]:
        """Obtiene todos los pagos registrados"""
        return self._pago_repository.obtener_todos()


class BuscarPagosPorClienteUseCase:
    """Caso de uso: Buscar pagos por cliente"""
    
    def __init__(self, pago_repository: PagoRepositoryPort):
        self._pago_repository = pago_repository
    
    def ejecutar(self, nombre_cliente: str) -> List[Pago]:
        """
        Busca todos los pagos de un cliente específico
        
        Args:
            nombre_cliente: Nombre del cliente a buscar
            
        Returns:
            Lista de pagos del cliente
        """
        # Búsqueda insensible a mayúsculas/minúsculas
        return self._pago_repository.obtener_por_cliente(nombre_cliente.strip())


class EliminarPagoUseCase:
    """Caso de uso: Eliminar un pago"""
    
    def __init__(self, pago_repository: PagoRepositoryPort):
        self._pago_repository = pago_repository
    
    def ejecutar(self, pago_id: str) -> bool:
        """
        Elimina un pago si cumple las reglas de negocio
        
        Args:
            pago_id: ID del pago a eliminar
            
        Returns:
            True si fue eliminado, False si no existe
            
        Raises:
            ValueError: Si el pago no puede ser eliminado
        """
        # Obtener el pago
        pago = self._pago_repository.obtener_por_id(pago_id)
        
        if not pago:
            return False
        
        # Verificar reglas de negocio
        if not pago.puede_ser_eliminado():
            raise ValueError(f"El pago con estado '{pago.estado}' no puede ser eliminado")
        
        # Eliminar
        return self._pago_repository.eliminar(pago_id)
