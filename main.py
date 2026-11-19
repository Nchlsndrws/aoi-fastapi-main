from fastapi import FastAPI
import models
from database import engine
from routers import planos, modalidades, cadastros
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(planos.router)
app.include_router(modalidades.router)
app.include_router(cadastros.router)

@app.get("/")
def inicio():
    return {"mensagem": "socorro!"}