from fastapi import APIRouter, Response, status
from model.evento import Evento, EventoCreate
from model.participante import Participante
from service import evento_service

router = APIRouter(prefix="/eventos", tags=["Eventos"])


@router.post("", response_model=Evento, status_code=status.HTTP_201_CREATED)
def cadastrar_evento(evento: EventoCreate):
    return evento_service.criar(evento)


@router.get("", response_model=list[Evento])
def listar_eventos():
    return evento_service.listar()


@router.get("/{evento_id}", response_model=Evento)
def consultar_evento(evento_id: int):
    return evento_service.buscar(evento_id)


@router.put("/{evento_id}", response_model=Evento)
def atualizar_evento(evento_id: int, evento: EventoCreate):
    return evento_service.atualizar(evento_id, evento)


@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_evento(evento_id: int):
    evento_service.excluir(evento_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{evento_id}/inscricoes/{participante_id}", status_code=status.HTTP_201_CREATED)
def inscrever_participante(evento_id: int, participante_id: int):
    return evento_service.inscrever(evento_id, participante_id)


@router.get("/{evento_id}/inscricoes", response_model=list[Participante])
def listar_inscritos(evento_id: int):
    return evento_service.listar_inscritos(evento_id)
