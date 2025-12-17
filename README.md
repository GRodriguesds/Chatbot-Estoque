# Chatbot de Estoque

Este projeto é um chatbot inteligente desenvolvido em Python para auxiliar no gerenciamento e consulta de um inventário de produtos. Ele utiliza FastAPI para criar a API, o modelo de linguagem Groq (LLM) para gerar respostas naturais e a técnica RAG (Retrieval-Augmented Generation) para integrar dados do inventário nas respostas do modelo.

### Funcionalidades

Consulta de quantidade de produtos específicos no inventário.

Retorna o total de produtos cadastrados.

Respostas curtas e diretas, simulando um assistente de atendimento.

Integração do modelo LLM com os dados da loja usando RAG, garantindo respostas precisas e contextualizadas.

Fácil expansão para novos tipos de perguntas e dados.

### Execução do Projeto

### Requisitos do Sistema
- **Python** 3.10 – 3.13 ([download](https://www.python.org/downloads/))
- pip (gerenciador de pacotes Python)
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
