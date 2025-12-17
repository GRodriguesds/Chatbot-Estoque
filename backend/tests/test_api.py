#Testar a API
#Para validar o endpoint /chat retornando resposta quando o produto é encontrado, utilizando mocks

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_retorna_resposta_com_produto(monkeypatch):
    # Mock do RAG
    def mock_buscar_produtos():
        return [{"nome": "notebook gamer", "quantidade": 3}]

    # Mock do LLM
    def mock_gerar_resposta(produto, pergunta):
        return "O produto notebook gamer possui 3 unidades em estoque."

    monkeypatch.setattr("app.main.buscar_produtos", mock_buscar_produtos)
    monkeypatch.setattr("app.main.gerar_resposta", mock_gerar_resposta)

    response = client.post(
        "/chat",
        json={"mensagem": "Tem notebook?"}
    )

    assert response.status_code == 200
    assert "notebook gamer" in response.json()["resposta"]