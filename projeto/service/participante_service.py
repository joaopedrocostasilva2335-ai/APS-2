from fastapi import HTTPException
from model.participante import Participante, ParticipanteCreate

participantes: list[Participante] = []
_proximo_id = 1


def listar():
    return participantes


def buscar(participante_id: int) -> Participante:
    for p in participantes:
        if p.id == participante_id:
            return p
    raise HTTPException(status_code=404, detail="Participante não encontrado.")


def criar(dados: ParticipanteCreate) -> Participante:
    global _proximo_id
    novo = Participante(id=_proximo_id, **dados.model_dump())
    _proximo_id += 1
    participantes.append(novo)
    return novo


def atualizar(participante_id: int, dados: ParticipanteCreate) -> Participante:
    existente = buscar(participante_id)
    atualizado = Participante(id=existente.id, **dados.model_dump())
    participantes[participantes.index(existente)] = atualizado
    return atualizado


def excluir(participante_id: int):
    from service import evento_service
    participantes.remove(buscar(participante_id))
    evento_service.remover_inscricoes_do_participante(participante_id)
