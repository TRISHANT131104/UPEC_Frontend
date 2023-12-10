import os

import pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from torch import cuda

from server.settings import embed_model


def load_embedding_model():
    embed_model_id = "sentence-transformers/all-MiniLM-L6-v2"

    device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"

    embed_model = HuggingFaceEmbeddings(
        model_name=embed_model_id,
        model_kwargs={"device": device},
        encode_kwargs={"device": device, "batch_size": 32},
    )
    return embed_model
