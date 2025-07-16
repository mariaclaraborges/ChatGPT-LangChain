
# We import langchain and langchain imports openai.
# Whenever we feed some text into the model, it sent off an HTTP request to the OpenAI API.
# We are not running a language model locally. It is hosted on OpenAI's servers.

Two Big Goals of LangChain

Provide tools to automate each step of a tect generation pipeline

Make it easy to connect tools together


# O objeto agent_executor executa todo o fluxo do agente:

# Recebe a pergunta,
# O agente decide se precisa usar a ferramenta SQL,
# Executa a consulta se necessário,
# O modelo de linguagem processa a resposta da ferramenta,
# E então gera a resposta final.