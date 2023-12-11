import pinecone
from langchain.vectorstores import Pinecone
import os
from .load_embedding_model import load_embedding_model
from dotenv import load_dotenv

load_dotenv()

def initiate_pinecone(api_key, index_name):
    pinecone.init(
        api_key=api_key,
        environment=os.environ.get("PINECONE_ENVIRONMENT")
    )

    index = pinecone.Index(index_name)
    embed_model = load_embedding_model()
    text_field = "text"  # field in metadata that contains text content
    return index, embed_model