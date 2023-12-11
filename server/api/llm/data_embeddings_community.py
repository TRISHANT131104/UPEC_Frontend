import os

import pinecone
from dotenv import load_dotenv
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone

from ..utils import *

load_dotenv()

index, embed_model = initiate_pinecone(os.environ.get("PINECONE_API_KEY"), "user")


def store_post_embeddings(post):
    """
    Store the embeddings of a post in the Pinecone index.

    Args:
        post (Post): The post object.

    Returns:
        None
    """
    user = post.user
    text = [
        f"""
        "User": {user.first_name} {user.last_name},
        "title": {post.title},
        "contect": {post.content},
        "date": {post.date}
    """
    ]
    embeddings = embed_model.embed_documents(text)
    metadata = [
        {
            "text": str(text),
            "ID": post.id,
        }
    ]
    index.upsert(vectors=zip([f"{post.id}"], embeddings, metadata))


def store_talent_data(talent):
    """
    Store the embeddings of talent data in the Pinecone index.

    Args:
        talent (Talent): The talent object.

    Returns:
        None
    """
    text = [
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
    metadata = [
        {
            "text": str(text),
            "ID": talent.user.id,
        }
    ]
    index.upsert(vectors=zip([f"{talent.user.id}"], embeddings, metadata))


def update_talent_data(talent):
    """
    Update the embeddings of talent data in the Pinecone index.

    Args:
        talent (Talent): The talent object.

    Returns:
        None
    """
    text = [
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
        text.append(
            f"""
            "currently_working_on": {i.title},
        """
        )
    embeddings = embed_model.embed_documents(text)
    metadata = [
        {
            "text": str(text),
            "ID": talent.user.id,
        }
    ]
    index.upsert(vectors=zip([f"{talent.user.id}"], embeddings, metadata))


def store_mentor_data(mentor):
    """
    Store the embeddings of mentor data in the Pinecone index.

    Args:
        mentor (Mentor): The mentor object.

    Returns:
        None
    """
    text = [
        f"""
        "User": {mentor.user.first_name} {mentor.user.last_name},
        "skills": {mentor.skills},
        "rating": {mentor.rating},
        "no_projects_mentored": {mentor.no_projects_mentored},
    """
    ]
    embeddings = embed_model.embed_documents(text)
    metadata = [
        {
            "text": str(text),
            "ID": mentor.user.id,
        }
    ]
    index.upsert(vectors=zip([f"{mentor.user.id}"], embeddings, metadata))


def update_mentor_data(mentor):
    """
    Update the embeddings of mentor data in the Pinecone index.

    Args:
        mentor (Mentor): The mentor object.

    Returns:
        None
    """
    text = [
        f"""
        "User": {mentor.user.first_name} {mentor.user.last_name},
        "skills": {mentor.skills},
        "rating": {mentor.rating},
        "no_projects_mentored": {mentor.no_projects_mentored},
    """
    ]
    for i in mentor.currently_mentoring.all():
        text.append(
            f"""
            "currently_mentoring": {i.title},
        """
        )
    embeddings = embed_model.embed_documents(text)
    metadata = [
        {
            "text": str(text),
            "ID": mentor.user.id,
        }
    ]
    index.upsert(vectors=zip([f"{mentor.user.id}"], embeddings, metadata))


def store_client_data(client):
    """
    Store the embeddings of client data in the Pinecone index.

    Args:
        client (Client): The client object.

    Returns:
        None
    """
    text = [
        f"""
        "User": {client.user.first_name} {client.user.last_name},
        "number_of_projects_given": {client.number_of_projects_given},
        "number_of_projects_completed": {client.number_of_projects_completed},
        "rating": {client.rating},
    """
    ]
    embeddings = embed_model.embed_documents(text)
    metadata = [
        {
            "text": str(text),
            "ID": client.user.id,
        }
    ]
    index.upsert(vectors=zip([f"{client.user.id}"], embeddings, metadata))


def update_client_data(client):
    """
    Update the embeddings of client data in the Pinecone index.

    Args:
        client (Client): The client object.

    Returns:
        None
    """
    text = [
        f"""
        "User": {client.user.first_name} {client.user.last_name},
        "number_of_projects_given": {client.number_of_projects_given},
        "number_of_projects_completed": {client.number_of_projects_completed},
        "rating": {client.rating},
    """
    ]
    for i in client.current_projects.all():
        text.append(
            f"""
            "current_projects": {i.title},
        """
        )
    embeddings = embed_model.embed_documents(text)
    metadata = [
        {
            "text": str(text),
            "ID": client.user.id,
        }
    ]
    index.upsert(vectors=zip([f"{client.user.id}"], embeddings, metadata))
