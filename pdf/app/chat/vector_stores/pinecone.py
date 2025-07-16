import os
import pinecone
# from langchain.vectorstores.pinecone import Pinecone
from langchain_pinecone import Pinecone  # Novo import!
from app.chat.embeddings.openai import embeddings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("🚀 Initializing Pinecone vector store...")
logger.info("🚀 Pinecone API Key: %s", os.getenv("PINECONE_API_KEY"))


pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME", "us-east-1"),
)

index_name = os.getenv("PINECONE_INDEX_NAME", "docs")
namespace = os.getenv("PINECONE_NAMESPACE", "default")


logging.info("✅ Connecting to Pinecone index: %s", os.getenv("PINECONE_INDEX_NAME"))


vector_store = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
    namespace=namespace,
)

def build_retriever(chat_args):
    search_kargs = {"filter": { "pdf_id": chat_args.pdf_id}} 
    # retorna um objeto capaz de buscar apenas os vetores que correspondem ao filtro (ou seja, só os chunks daquele PDF).
    return vector_store.as_retriever(
        search_kargs=search_kargs
    )
