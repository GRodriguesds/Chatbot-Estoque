import re

def normalizar(texto: str) -> list[str]:
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", "", texto) 
    palavras = texto.split()

    palavras = [p[:-1] if p.endswith("s") else p for p in palavras]

    return palavras

def buscar_nomes_produtos():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nome FROM estoque")
    return [row[0].lower() for row in cursor.fetchall()]

    conn.close()
    return nomes

def extrair_produtos(pergunta: str, produtos: list[dict]) -> list[dict]:
    palavras_pergunta = normalizar(pergunta)

    encontrados = []

    for produto in produtos:
        palavras_produto = normalizar(produto["nome"])

        if any(p in palavras_pergunta for p in palavras_produto):
            encontrados.append(produto)

    return encontrados
