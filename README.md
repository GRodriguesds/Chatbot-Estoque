##Execução do Projeto

- Clone o repositório:
-git clone https://github.com/seu-usuario/chatbot-estoque.git
-cd chatbot-estoque

- Obtenha a chave da Groq para o LLM:
-Acesse o site da Groq: https://console.groq.com
-Crie uma conta ou faça login
-No painel, gere uma API Key
-Copie a chave gerada

- Configure a chave Groq:
-Na raiz do projeto, crie um arquivo .env usando o .env.example como base:
-GROQ_API_KEY=sua_chave_groq

## BackEnd (FastAPI):
-Entre na pasta do backend:
-(No terminal, uma linha por vez)

-cd backend 
-pip install -r requirements.txt
-uvicorn app.main:app --reload
-http://127.0.0.1:8000/docs (acesse)

##  FrontEnd(React + Vite)
-Abra outro terminal e entre na pasta do frontend:
-(No terminal, uma linha por vez)

-cd frontend
-npm install
-npm run dev
-http://localhost:5173 (acesse)