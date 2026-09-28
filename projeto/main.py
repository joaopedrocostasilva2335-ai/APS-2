from fastapi import FastAPI
from controller import evento_controller, participante_controller

app = FastAPI(title="API de Eventos Acadêmicos")

app.include_router(evento_controller.router)
app.include_router(participante_controller.router)
