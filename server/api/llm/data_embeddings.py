from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from torch import cuda
from langchain.vectorstores import Pinecone
import os
import pinecone
from models.projects import Project
from models.projects import ProjectRequirementDocument


embed_model_id = "sentence-transformers/all-MiniLM-L6-v2"

device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"

embed_model = HuggingFaceEmbeddings(
    model_name=embed_model_id,
    model_kwargs={"device": device},
    encode_kwargs={"device": device, "batch_size": 32},
)

pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_ENVIRONMENT") or "gcp-starter",
)

index_name = "projects"
index = pinecone.Index(index_name)

text_field = "text"
vectorstore = Pinecone(index, embed_model.embed_query, text_field)

projects = Project.objects.all()
batch_size = 32

for i in range(0, len(projects)):
    project = projects[i]
    if project.prd is not None:
        metadata = [
            {
                "id": project.id,
                "title": project.title,
                "description": project.description,
                "start_date": project.start_date,
                "end_date": project.end_date,
                "bid_price": project.bid_price,
                "status": project.status,
                "project_doc": project.project_doc,
                "prd": project.prd,
                "learning_resource": project.learning_resource,
                "related_techstacks": project.related_techstacks,
            }
        ]
        embeddings = embed_model.embed_documents(metadata)
        index.upsert(vectors = zip(project.id, embeddings, metadata))

        
