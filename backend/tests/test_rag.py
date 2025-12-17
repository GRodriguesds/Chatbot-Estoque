#Testar o RAG
#Para verificar se a função extrair_produtos encontra o produto de acordo com a pergunta do usuário

from app.utils import extrair_produtos

def test_extrair_produtos_encontra_produto():
    produtos = [
        {"nome": "notebook gamer", "quantidade": 5},
        {"nome": "mouse sem fio", "quantidade": 2},
    ]

    pergunta = "Vocês têm notebook disponível?"

    encontrados = extrair_produtos(pergunta, produtos)

    assert len(encontrados) == 1
    assert encontrados[0]["nome"] == "notebook gamer"
