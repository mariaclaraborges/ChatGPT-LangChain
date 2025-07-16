# ChatGPT-LangChain PDF App

## Visão Geral

Este projeto é uma aplicação completa para análise, busca e chat com PDFs, integrando IA generativa (OpenAI), armazenamento vetorial (Pinecone), banco de dados SQL, interface web (Svelte) e processamento assíncrono (Celery). Ele permite que usuários façam upload de PDFs, gerem embeddings, realizem buscas semânticas e conversem com o conteúdo dos documentos.

---

## Principais Funcionalidades

- **Upload e Gerenciamento de PDFs:**  
  Usuários podem enviar PDFs, que são processados e armazenados para análise posterior.

- **Geração de Embeddings:**  
  O texto dos PDFs é extraído, dividido em chunks e convertido em embeddings usando modelos da OpenAI.

- **Armazenamento Vetorial (Pinecone):**  
  Os embeddings são armazenados no Pinecone, permitindo buscas semânticas rápidas e filtradas por documento.

- **Busca e Chat com PDFs:**  
  Usuários podem fazer perguntas sobre o conteúdo dos PDFs. O sistema busca os chunks mais relevantes e utiliza um LLM (ChatOpenAI) para gerar respostas contextuais.

- **Memória de Conversa Persistente:**  
  O histórico de conversas é salvo em banco SQL, permitindo continuidade e contexto em múltiplas sessões.

- **Interface Web Moderna:**  
  Frontend em Svelte, com autenticação, visualização de PDFs, chat, dashboards e gerenciamento de documentos.

- **Processamento Assíncrono:**  
  Tarefas pesadas (como geração de embeddings) são processadas em background usando Celery.

---

## Estrutura de Pastas

- **app/**  
  Backend Python (Flask, LangChain, Celery, Pinecone, SQL, APIs, lógica de chat, embeddings, memories, etc.)

- **client/**  
  Frontend Svelte (componentes, rotas, autenticação, chat, visualização de PDFs, etc.)

- **instance/**  
  Banco de dados SQLite.

- **static/**  
  Arquivos estáticos (favicon, specs, etc.)

---

## Principais Tecnologias

- **Python 3.11**
- **Flask** (API backend)
- **LangChain** (orquestração de LLMs, chains, retrievers, memories)
- **OpenAI** (embeddings, chat)
- **Pinecone** (vector store)
- **Celery** (tarefas assíncronas)
- **Svelte** (frontend)
- **SQLite** (banco de dados)
- **Redis** (opcional, para filas/tarefas)

---

## Fluxo Básico

1. **Upload do PDF:**  
   Usuário faz upload via interface web.

2. **Processamento:**  
   O backend extrai o texto, divide em chunks, gera embeddings e armazena no Pinecone.

3. **Chat/Busca:**  
   Usuário faz perguntas sobre o PDF. O sistema busca os chunks relevantes, envia para o LLM e retorna a resposta.

4. **Memória:**  
   O histórico da conversa é salvo e pode ser recuperado em sessões futuras.

---

## Como Rodar

1. Instale as dependências (use `pipenv install` ou `pip install -r requirements.txt`).
2. Configure as variáveis de ambiente no `.env` (OpenAI, Pinecone, etc.).
3. Inicie o backend Flask e o worker Celery.
4. Inicie o frontend Svelte.
5. Acesse a interface web para usar o sistema.

---

## Observações de Segurança

- **NUNCA** suba arquivos `.env` ou chaves de API para o GitHub.
- Use `.gitignore` para proteger arquivos sensíveis e dados grandes.

---

## Créditos

Projeto baseado em LangChain, OpenAI, Pinecone, Flask, Svelte e
