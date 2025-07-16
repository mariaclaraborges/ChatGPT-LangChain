from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from langchain_openai import OpenAI 
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat = OpenAI()

memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("chat_history.json"),
    memory_key="messages", 
    return_messages=True
    )
#memory_key é o nome da variável que será usada para armazenar as mensagens na memória
#return_messages=True faz com que as mensagens sejam retornadas como uma lista de mensagens, o que é útil para depuração e visualização (HumanMesage e AIMessage)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory
)

while True:
    content = input(">> ")

    result = chain.invoke({"content": content})
    print(result["text"])