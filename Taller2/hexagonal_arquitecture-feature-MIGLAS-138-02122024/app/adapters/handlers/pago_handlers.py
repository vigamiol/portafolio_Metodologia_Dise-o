from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from adapters.schemas.pago_schemas import (
    RegistrarPagoRequest,
    PagoResponse,
    ErrorResponse,
    ListaPagosResponse
)
from adapters.dependency.container import get_dependency_container, DependencyContainer
from usecases.pago_usecases import (
    RegistrarPagoUseCase,
    ListarPagosUseCase,
    BuscarPagosPorClienteUseCase,
    EliminarPagoUseCase
)

router = APIRouter(prefix="/api/pagos", tags=["pagos"])


def get_registrar_pago_usecase(
    container: DependencyContainer = Depends(get_dependency_container)
) -> RegistrarPagoUseCase:
    return container.get_registrar_pago_usecase()


def get_listar_pagos_usecase(
    container: DependencyContainer = Depends(get_dependency_container)
) -> ListarPagosUseCase:
    return container.get_listar_pagos_usecase()


def get_buscar_pagos_por_cliente_usecase(
    container: DependencyContainer = Depends(get_dependency_container)
) -> BuscarPagosPorClienteUseCase:
    return container.get_buscar_pagos_por_cliente_usecase()


def get_eliminar_pago_usecase(
    container: DependencyContainer = Depends(get_dependency_container)
) -> EliminarPagoUseCase:
    return container.get_eliminar_pago_usecase()


@router.post(
    "/",
    response_model=PagoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un nuevo pago",
    description="Registra un nuevo pago realizado por un cliente"
)
async def registrar_pago(
    request: RegistrarPagoRequest,
    usecase: RegistrarPagoUseCase = Depends(get_registrar_pago_usecase)
):
    """RF1. Registrar un Pago"""
    try:
        pago = usecase.ejecutar(request.nombre_cliente, request.monto)
        return PagoResponse(
            id=pago.id,
            nombre_cliente=pago.nombre_cliente,
            monto=pago.monto,
            fecha=pago.fecha,
            estado=pago.estado
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=ListaPagosResponse,
    summary="Listar todos los pagos",
    description="Obtiene la lista completa de pagos registrados"
)
async def listar_pagos(
    usecase: ListarPagosUseCase = Depends(get_listar_pagos_usecase)
):
    """RF2. Listar todos los Pagos"""
    pagos = usecase.ejecutar()
    return ListaPagosResponse(
        pagos=[
            PagoResponse(
                id=pago.id,
                nombre_cliente=pago.nombre_cliente,
                monto=pago.monto,
                fecha=pago.fecha,
                estado=pago.estado
            ) for pago in pagos
        ],
        total=len(pagos)
    )


@router.get(
    "/cliente/{nombre_cliente}",
    response_model=ListaPagosResponse,
    summary="Buscar pagos por cliente",
    description="Consulta todos los pagos realizados por un cliente específico"
)
async def buscar_pagos_por_cliente(
    nombre_cliente: str,
    usecase: BuscarPagosPorClienteUseCase = Depends(get_buscar_pagos_por_cliente_usecase)
):
    """RF3. Buscar Pagos por Cliente"""
    pagos = usecase.ejecutar(nombre_cliente)
    return ListaPagosResponse(
        pagos=[
            PagoResponse(
                id=pago.id,
                nombre_cliente=pago.nombre_cliente,
                monto=pago.monto,
                fecha=pago.fecha,
                estado=pago.estado
            ) for pago in pagos
        ],
        total=len(pagos)
    )


@router.delete(
    "/{pago_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un pago",
    description="Elimina un pago registrado si cumple las reglas de negocio"
)
async def eliminar_pago(
    pago_id: str,
    usecase: EliminarPagoUseCase = Depends(get_eliminar_pago_usecase)
):
    """RF4. Eliminar un Pago"""
    try:
        eliminado = usecase.ejecutar(pago_id)
        if not eliminado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pago no encontrado"
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
