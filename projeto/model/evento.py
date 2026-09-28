from datetime import date, time
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class Categoria(str, Enum):
    palestra = "Palestra"
    workshop = "Workshop"
    minicurso = "Minicurso"
    seminario = "Seminário"
    competicao = "Competição"


class EventoCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    titulo: str = Field(min_length=1, examples=["Palestra de IA"])
    descricao: str = Field(examples=["Introdução à inteligência artificial"])
    data: date
    horario: time
    local: str = Field(min_length=1, examples=["Auditório A"])
    capacidade: int = Field(gt=0, examples=[50])
    categoria: Categoria


class Evento(EventoCreate):
    id: int
