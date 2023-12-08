from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from torch import cuda
from langchain.vectorstores import Pinecone
import os
import pinecone
from ..models import (
    Post
)
from server.settings import embed_model

pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY2"),
    environment=os.environ.get("PINECONE_ENVIRONMENT") or "gcp-starter",
)

index_name = "user"
index = pinecone.Index(index_name)


def store_post_embeddings(post):
    user = post.user
    text =[f"""
        "User": {user.first_name} {user.last_name},
        "title": {post.title},
        "contect": {post.content},
        "date": {post.date}
    """]
    embeddings = embed_model.embed_documents(text)
    print(type(embeddings))
    # Ensure metadata is a list of dictionaries
    metadata = [{
        "User": f'{user.first_name} {user.last_name}',
        "title": {post.title},
        "contect": {post.content},
        "date": {post.date},
    }]
    index.upsert(vectors = zip([f'{post.id}'], embeddings,metadata))
        
def store_talent_data(talent):
    text =[
    f"""
        "User": {talent.user.first_name} {talent.user.last_name},
        "skills": {talent.skills},
        "learning_resources": {talent.learning_resources},
        "rating": {talent.rating},
        "no_projects_completed": {talent.no_projects_completed},
        "deadline_missed": {talent.deadline_missed},
        "project_cancelled": {talent.project_cancelled},
    """
    ]
    embeddings = embed_model.embed_documents(text)
    metadata = [{
        "User": f'{talent.user.first_name} {talent.user.last_name}',
        "skills": {talent.skills},
        "learning_resources": {talent.learning_resources},
        "rating": {talent.rating},
        "no_projects_completed": {talent.no_projects_completed},
        "deadline_missed": {talent.deadline_missed},
        "project_cancelled": {talent.project_cancelled},
    }]
    index.upsert(vectors = zip([f'{talent.user.id}'], embeddings,metadata))

def update_talent_data(talent):
    text =[
    f"""
        "User": {talent.user.first_name} {talent.user.last_name},
        "skills": {talent.skills},
        "learning_resources": {talent.learning_resources},
        "rating": {talent.rating},
        "no_projects_completed": {talent.no_projects_completed},
        "deadline_missed": {talent.deadline_missed},
        "project_cancelled": {talent.project_cancelled},
    """
    ]
    for i in talent.currently_working_on.all():
        text.append(f"""
            "currently_working_on": {i.title},
        """)
    embeddings = embed_model.embed_documents(text)
    metadata ={
        "User": f'{talent.user.first_name} {talent.user.last_name}',
        "skills": {talent.skills},
        "learning_resources": {talent.learning_resources},
        "rating": {talent.rating},
        "no_projects_completed": {talent.no_projects_completed},
        "deadline_missed": {talent.deadline_missed},
        "project_cancelled": {talent.project_cancelled},
    }
    for i in talent.currently_working_on.all():
        metadata["currently_working_on"] += i.title+","+i.content
    index.update(
        ids = [f'{talent.user.id}'],
        values = embeddings,
        set_metadata = metadata,
    )

def store_mentor_data(mentor):
    text =[
    f"""
        "User": {mentor.user.first_name} {mentor.user.last_name},
        "skills": {mentor.skills},
        "rating": {mentor.rating},
        "no_projects_mentored": {mentor.no_projects_mentored},
    """
    ]
    embeddings = embed_model.embed_documents(text)
    metadata = [{
        "User": f'{mentor.user.first_name} {mentor.user.last_name}',
        "skills": {mentor.skills},
        "rating": {mentor.rating},
        "no_projects_mentored": {mentor.no_projects_mentored},
    }]
    index.upsert(vectors = zip([f'{mentor.user.id}'], embeddings,metadata))

def update_mentor_data(mentor):
    text =[
    f"""
        "User": {mentor.user.first_name} {mentor.user.last_name},
        "skills": {mentor.skills},
        "rating": {mentor.rating},
        "no_projects_mentored": {mentor.no_projects_mentored},
    """
    ]
    for i in mentor.currently_mentoring.all():
        text.append(f"""
            "currently_mentoring": {i.title},
        """)
    embeddings = embed_model.embed_documents(text)
    metadata ={
        "User": f'{mentor.user.first_name} {mentor.user.last_name}',
        "skills": {mentor.skills},
        "rating": {mentor.rating},
        "no_projects_mentored": {mentor.no_projects_mentored},
    }
    for i in mentor.currently_mentoring.all():
        metadata["currently_mentoring"] += i.title+","+i.content
    index.update(
        ids = [f'{mentor.user.id}'],
        values = embeddings,
        set_metadata = metadata,
    )

def store_client_data(client):
    text =[
    f"""
        "User": {client.user.first_name} {client.user.last_name},
        "number_of_projects_given": {client.number_of_projects_given},
        "number_of_projects_completed": {client.number_of_projects_completed},
        "rating": {client.rating},
    """
    ]
    embeddings = embed_model.embed_documents(text)
    metadata = [{
        "User": f'{client.user.first_name} {client.user.last_name}',
        "number_of_projects_given": {client.number_of_projects_given},
        "number_of_projects_completed": {client.number_of_projects_completed},
        "rating": {client.rating},
    }]
    index.upsert(vectors = zip([f'{client.user.id}'], embeddings,metadata))

def update_client_data(client):
    text =[
    f"""
        "User": {client.user.first_name} {client.user.last_name},
        "number_of_projects_given": {client.number_of_projects_given},
        "number_of_projects_completed": {client.number_of_projects_completed},
        "rating": {client.rating},
    """
    ]
    for i in client.current_projects.all():
        text.append(f"""
            "current_projects": {i.title},
        """)
    embeddings = embed_model.embed_documents(text)
    metadata ={
        "User": f'{client.user.first_name} {client.user.last_name}',
        "number_of_projects_given": {client.number_of_projects_given},
        "number_of_projects_completed": {client.number_of_projects_completed},
        "rating": {client.rating},
    }
    for i in client.current_projects.all():
        metadata["current_projects"] += i.title+","+i.content
    index.update(
        ids = [f'{client.user.id}'],
        values = embeddings,
        set_metadata = metadata,
    )