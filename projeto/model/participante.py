from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ParticipanteCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nome: str = Field(min_length=1, examples=["Maria Silva"])
    email: EmailStr
    curso: str = Field(min_length=1, examples=["Ciência da Computação"])


class Participante(ParticipanteCreate):
    id: int
