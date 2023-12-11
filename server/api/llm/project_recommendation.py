from ..utils import *
from dotenv import load_dotenv
import os

load_dotenv()

def project_recomendation(skills):
    # Define the prompt based on parameters
    index, embed_model = initiate_pinecone(os.environ.get("PINECONE_API_KEY"), "projects")
    result = []
    v = embed_model.embed_documents(skills)
    result = index.query(
        vector=v[0],
        top_k=3,
        include_values=True,
    )
    response = []
    for i in result["matches"]:
        response.append(i["id"])
    return response
