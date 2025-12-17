# Chatbot de Estoque

Um assistente virtual para funcionários de loja que permite consultar rapidamente a disponibilidade de produtos no estoque. O chatbot recebe perguntas sobre itens, verifica a base de dados e retorna se o produto está disponível, facilitando o atendimento e agilizando a gestão de inventário.

## Execução do Projeto

### Requisitos do Sistema
- **Python** 3.10 – 3.13 ([download](https://www.python.org/downloads/))
- **Node.js** 18+ ([download](https://nodejs.org/))
- NPM 9+ (vem junto com Node.js)

### Clone o repositório

```bash
git clone https://github.com/GRodriguesds/Chatbot-Estoque
cd chatbot-estoque
```

### Obtenha a chave da Groq para o LLM

* Acesse o site da Groq: [https://console.groq.com](https://console.groq.com)
* Crie uma conta ou faça login
* No painel, gere uma API Key
* Copie a chave gerada

### Configure a chave Groq

Na raiz do projeto, crie um arquivo `.env` usando o `.env.example` como base:

```env
GROQ_API_KEY=sua_chave_groq
```

### BackEnd (FastAPI)

Entre na pasta do backend (no terminal, uma linha por vez):

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse:

```
http://127.0.0.1:8000/docs
```

### FrontEnd (React + Vite)

Abra outro terminal e entre na pasta do frontend (no terminal, uma linha por vez):

```bash
cd frontend
npm install
npm run dev
```

Acesse:

```
http://localhost:5173
```

### Para realizar os testes

Garanta que o diretório esteja na pasta backend

```
cd backend (caso não esteja na pasta)
pytest -v
```