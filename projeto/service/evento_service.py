from fastapi import HTTPException
from model.evento import Evento, EventoCreate
from service import participante_service

eventos: list[Evento] = []
inscricoes: list[dict] = []  # {"evento_id": int, "participante_id": int}
_proximo_id = 1


def listar():
    return eventos


def buscar(evento_id: int) -> Evento:
    for e in eventos:
        if e.id == evento_id:
            return e
    raise HTTPException(status_code=404, detail="Evento não encontrado.")


def criar(dados: EventoCreate) -> Evento:
    global _proximo_id
    novo = Evento(id=_proximo_id, **dados.model_dump())
    _proximo_id += 1
    eventos.append(novo)
    return novo


def atualizar(evento_id: int, dados: EventoCreate) -> Evento:
    existente = buscar(evento_id)
    total = len([i for i in inscricoes if i["evento_id"] == evento_id])
    if dados.capacidade < total:
        raise HTTPException(
            status_code=400,
            detail="A capacidade não pode ser menor que o número de inscritos.",
        )
    atualizado = Evento(id=existente.id, **dados.model_dump())
    eventos[eventos.index(existente)] = atualizado
    return atualizado


def excluir(evento_id: int):
    eventos.remove(buscar(evento_id))
    inscricoes[:] = [i for i in inscricoes if i["evento_id"] != evento_id]


def remover_inscricoes_do_participante(participante_id: int):
    inscricoes[:] = [i for i in inscricoes if i["participante_id"] != participante_id]


def inscrever(evento_id: int, participante_id: int):
    evento = buscar(evento_id)                          # 1. evento existe?
    participante = participante_service.buscar(participante_id)  # 2. participante existe?

    ja_inscrito = any(
        i["evento_id"] == evento_id and i["participante_id"] == participante_id
        for i in inscricoes
    )
    if ja_inscrito:                                     # 3. já inscrito?
        raise HTTPException(
            status_code=400, detail="Participante já está inscrito neste evento."
        )

    total = len([i for i in inscricoes if i["evento_id"] == evento_id])
    if total >= evento.capacidade:                      # 4. há vagas?
        raise HTTPException(
            status_code=400, detail="Não existem vagas disponíveis para este evento."
        )

    inscricoes.append({"evento_id": evento_id, "participante_id": participante_id})
    return {
        "mensagem": "Inscrição realizada com sucesso.",
        "evento": evento.titulo,
        "participante": participante.nome,
    }


def listar_inscritos(evento_id: int):
    buscar(evento_id)
    ids = [i["participante_id"] for i in inscricoes if i["evento_id"] == evento_id]
    return [p for p in participante_service.listar() if p.id in ids]
