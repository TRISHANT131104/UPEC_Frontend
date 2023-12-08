import openai
import json
from langchain.vectorstores import Pinecone
import pinecone
# from server.settings import embed_model
from ..utils.load_embedding_model import load_embedding_model

def initiate_pinecone():
    pinecone.init(
        api_key="663983e5-451f-4d33-bf74-6a7b8dbc4bcb",
        environment="gcp-starter",
    )

    index_name = "projects"
    index = pinecone.Index(index_name)
    embed_model = load_embedding_model()
    text_field = 'text'  # field in metadata that contains text content

    vectorstore = Pinecone(
        index, embed_model.embed_query, text_field
    )
    return vectorstore
def project_recomendation(skills):

    # Define the prompt based on parameters
    vectorstore=initiate_pinecone()
    result = vectorstore.similarity_search(
        skills,  # the search query
        k=3  # returns top 3 most relevant chunks of text
    )

    return result


