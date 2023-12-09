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
    return index,embed_model
def project_recomendation(skills):
    # Define the prompt based on parameters
    index,embed_model=initiate_pinecone()
    result = []
    v=embed_model.embed_documents(skills)
    result = index.query(
        vector=v[0],
        top_k=3,
        include_values=True,
    )
    return result['matches'][0]['id']


