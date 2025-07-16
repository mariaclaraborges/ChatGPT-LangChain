from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

with open("facts.txt", "r", encoding="utf-8") as f:
    text = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0, 
)

embeddings = OpenAIEmbeddings()

chunks = text_splitter.split_text(text)
docs = [Document(page_content=chunk) for chunk in chunks]

#creating chroma instances
db = Chroma.from_documents(
    docs, #list of documents
    embedding=embeddings, #generates embeddings for each chunk
    persist_directory="emb"
)

results = db.similarity_search(
    "What is an interesting fact about the English language?", 
    )

for result in results:
    print("\n")
    print(result.page_content)