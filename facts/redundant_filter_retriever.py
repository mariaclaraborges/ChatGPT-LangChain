from langchain.embeddings.base import Embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.schema import BaseRetriever

class RedundantFilterRetriever(BaseRetriever):

    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        '''
        Calculate embeddings for the query string

        Take embeddings and feed them into that max_marginal_relevance_search_by_vector method of the Chroma vector store.
        This will return a list of documents that are relevant to the query.
        '''

        emb = self.embeddings.embed_query(query)
                
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8,  # Adjust this value to control the balance between relevance and diversity
        )

    async def aget_relevant_documents(self):
        return []