from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
banco_de_dados = [
    {"id": 1, "titulo":"Aprender FastAPI"},
    {"id": 2, "titulo":"Conectar Back-end com front-end "}
] 

class Tarefaschema(BaseModel):
    titulo:str

@app.get("/api/tarefas") 
def listar_tarefas():
    return banco_de_dados

@app.post("/api/tarefas")
def criar_tarefa(tarefa: Tarefaschema):
    nova_tarefa = {
        "id": len(banco_de_dados) + 1,
        "titulo": tarefa.titulo
    }
    banco_de_dados.append(nova_tarefa)
    return nova_tarefa

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)