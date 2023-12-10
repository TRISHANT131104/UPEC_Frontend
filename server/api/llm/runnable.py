import os

import pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from torch import cuda

# from models.projects import Project
# from models.projects import ProjectRequirementDocument


embed_model_id = "sentence-transformers/all-MiniLM-L6-v2"

device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"

embed_model = HuggingFaceEmbeddings(
    model_name=embed_model_id,
    model_kwargs={"device": device},
    encode_kwargs={"device": device, "batch_size": 32},
)

pinecone.init(
    api_key="663983e5-451f-4d33-bf74-6a7b8dbc4bcb",
    environment="gcp-starter",
)

index_name = "projects"
index = pinecone.Index(index_name)

text_field = "text"
vectorstore = Pinecone(index, embed_model.embed_query, text_field)

# projects = Project.objects.all()
batch_size = 32

print(index.describe_index_stats())

batch_size = 4

for i in range(0, 1):  # Adjust the loop as needed
    text = [
        """
        "id": "1",
        "title": "project.title",
        "description": "project.description",
        "start_date": "project.start_date",
        "end_date": "project.end_date",
        "bid_price": "project.bid_price",
        "status": "project.status",
        "project_doc": "project.project_doc",
        "prd": "project.prd",
        "learning_resource": "project.learning_resource",
        "related_techstacks": "project.related_techstacks"
        """
    ]
    embeddings = embed_model.embed_documents(text)
    # Ensure metadata is a list of dictionaries
    metadata = {
        "id": 1,
        "title": "project.title",
        "description": "project.description",
        "start_date": "project.start_date",
        "end_date": "project.end_date",
        "bid_price": "project.bid_price",
        "status": "project.status",
        "project_doc": "project.project_doc",
        "prd": "project.prd",
        "learning_resource": "None",
        "related_techstacks": "None",
        "text": "project.related_techstacks",
    }

    update_response = index.update(
        id="1",
        values=embeddings,
        set_metadata=metadata,
    )
print(index.describe_index_stats())
