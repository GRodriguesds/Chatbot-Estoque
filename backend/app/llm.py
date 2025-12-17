import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def gerar_resposta(produto: dict, pergunta: str) -> str:
    nome = produto["nome"]
    quantidade = produto["quantidade"]

    if quantidade == 0:
        contexto = f"O produto {nome} está esgotado."
    else:
        contexto = f"O produto {nome} possui {quantidade} unidades em estoque."

    prompt = f"""
Você é um atendente de loja.
Responda usando APENAS a informação abaixo:
-Diga sempre a quantidade do produto no estoque.
-Esqueça o item da última pergunta

{contexto}

Pergunta do cliente:
{pergunta}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    return response.choices[0].message.content

