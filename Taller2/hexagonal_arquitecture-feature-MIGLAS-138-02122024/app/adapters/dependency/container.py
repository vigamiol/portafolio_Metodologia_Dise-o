from functools import lru_cache
from adapters.repositories.inmemory_pago_repository import InMemoryPagoRepository
from usecases.pago_usecases import (
    RegistrarPagoUseCase,
    ListarPagosUseCase,
    BuscarPagosPorClienteUseCase,
    EliminarPagoUseCase
)


class DependencyContainer:
    """Contenedor de dependencias para inyección"""
    
    def __init__(self):
        # Repositorio (singleton para mantener datos en memoria)
        self._pago_repository = InMemoryPagoRepository()
        
        # Casos de uso
        self._registrar_pago_usecase = RegistrarPagoUseCase(self._pago_repository)
        self._listar_pagos_usecase = ListarPagosUseCase(self._pago_repository)
        self._buscar_pagos_por_cliente_usecase = BuscarPagosPorClienteUseCase(self._pago_repository)
        self._eliminar_pago_usecase = EliminarPagoUseCase(self._pago_repository)
    
    def get_registrar_pago_usecase(self) -> RegistrarPagoUseCase:
        return self._registrar_pago_usecase
    
    def get_listar_pagos_usecase(self) -> ListarPagosUseCase:
        return self._listar_pagos_usecase
    
    def get_buscar_pagos_por_cliente_usecase(self) -> BuscarPagosPorClienteUseCase:
        return self._buscar_pagos_por_cliente_usecase
    
    def get_eliminar_pago_usecase(self) -> EliminarPagoUseCase:
        return self._eliminar_pago_usecase


# Singleton del contenedor
@lru_cache()
def get_dependency_container() -> DependencyContainer:
    return DependencyContainer()
