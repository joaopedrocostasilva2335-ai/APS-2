# API de Eventos Acadêmicos

API RESTful feita com **Python + FastAPI + Pydantic** para gerenciar eventos acadêmicos,
participantes e inscrições. Os dados ficam em memória (listas Python) e são perdidos ao reiniciar.

Arquitetura MVC:
- `controller/` – rotas HTTP
- `model/` – modelos e validação (Pydantic)
- `service/` – regras de negócio

## Instalação
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Execução
```bash
uvicorn main:app --reload
```
Swagger: http://127.0.0.1:8000/docs

## Rotas
| Método | Rota | Descrição | Status |
|---|---|---|---|
| POST | /eventos | Cadastrar evento | 201 |
| GET | /eventos | Listar eventos | 200 |
| GET | /eventos/{id} | Consultar evento | 200 / 404 |
| PUT | /eventos/{id} | Atualizar evento | 200 / 404 |
| DELETE | /eventos/{id} | Excluir evento | 204 / 404 |
| POST | /participantes | Cadastrar participante | 201 |
| GET | /participantes | Listar participantes | 200 |
| GET | /participantes/{id} | Consultar participante | 200 / 404 |
| PUT | /participantes/{id} | Atualizar participante | 200 / 404 |
| DELETE | /participantes/{id} | Excluir participante | 204 / 404 |
| POST | /eventos/{evento_id}/inscricoes/{participante_id} | Inscrever participante | 201 / 400 / 404 |
| GET | /eventos/{evento_id}/inscricoes | Listar inscritos | 200 / 404 |

Dados inválidos retornam **422**.

## Exemplos

### Cadastrar evento — `POST /eventos`
```json
{
  "titulo": "Palestra de IA",
  "descricao": "Introdução à inteligência artificial",
  "data": "2026-11-10",
  "horario": "19:00:00",
  "local": "Auditório A",
  "capacidade": 1,
  "categoria": "Palestra"
}
```
Resposta (201): o mesmo JSON com `"id": 1`.

### Cadastrar participante — `POST /participantes`
```json
{ "nome": "Maria Silva", "email": "maria@email.com", "curso": "Ciência da Computação" }
```

### Inscrever — `POST /eventos/1/inscricoes/1`
```json
{ "mensagem": "Inscrição realizada com sucesso.", "evento": "Palestra de IA", "participante": "Maria Silva" }
```

### Erros
```json
{ "detail": "Evento não encontrado." }
{ "detail": "Participante já está inscrito neste evento." }
{ "detail": "Não existem vagas disponíveis para este evento." }
```
