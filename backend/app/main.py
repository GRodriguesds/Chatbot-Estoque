from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import buscar_produtos
from app.llm import gerar_resposta
from app.utils import extrair_produtos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pergunta(BaseModel):
    mensagem: str

@app.post("/chat")
def chat(pergunta: Pergunta):
    produtos = buscar_produtos()  # 🔎 Retrieval

    produtos_encontrados = extrair_produtos(pergunta.mensagem, produtos)

    if not produtos_encontrados:
        return {"resposta": "Nenhum produto correspondente encontrado no estoque."}

    # Se encontrar mais de um, responda todos
    respostas = [
        gerar_resposta(produto, pergunta.mensagem)
        for produto in produtos_encontrados
    ]

    return {"resposta": " ".join(respostas)}
