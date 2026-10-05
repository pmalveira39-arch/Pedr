from fastapi import FastAPI
import uvicorn

app = FastAPI(title="minha API python")

@app.get("/")
def home():
    return {
        "status":"online",
        "mensagem":"Sua API estar a funcionar"
    }

@app.get("/saudacao/{nome}")
def saudara(nome: str):
    return {
        "mensagem": f"Olà, {nome}! Bem-vindo a API. "
    }

@app.get("/somar")
def somar(a: int = 0, b: int= 0):
    resultado = a + b
    return {
        "operaçao": "soma",
        "a": a,
        "b": b,
        "resultado": resultado
    }

if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)