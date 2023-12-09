from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from torch import cuda
from langchain.vectorstores import Pinecone
import os
import pinecone
from ..models import (
    Workflow,
    ProjectRequirementDocument,
    Project
)
# from server.settings import embed_model
from ..utils.load_embedding_model import load_embedding_model

def initiate_pinecone():
    pinecone.init(
        api_key="663983e5-451f-4d33-bf74-6a7b8dbc4bcb",
        environment="gcp-starter",
    )

    index_name = "projects"
    index = pinecone.Index(index_name)
    return index


def store_project_requirement_document_embeddings(project):
    embed_model=load_embedding_model()
    index = initiate_pinecone()
    prd = project.prd
    text =[f"""
    "project_id": {project.id},
    "project_title": {project.title},
    "project_description": {project.description},
    "project_start_date": {project.start_date},
    "project_end_date": {project.end_date},
    "project_bid_price": {project.bid_price},
    "project_status": {project.status},
    "project_related_techstacks": {tuple(project.related_techstacks)}
    "project_created_at": {project.created_at},
    "project_updated_at": {project.updated_at},
    "project_created_by": {project.created_by},
    "project_overview": {prd.project_overview},
    "original_requirements": {prd.original_requirements},
    "project_goals": {prd.project_goals},
    "user_stories": {prd.user_stories},
    "system_architecture": {prd.system_architecture},
    "tech_stacks": {prd.tech_stacks},
    "requirement_pool": {prd.requirement_pool},
    "ui_ux_design": {prd.ui_ux_design},
    "development_methodology": {prd.development_methodology},
    "security_measures": {prd.security_measures},
    "testing_strategy": {prd.testing_strategy},
    "scalability_and_performance": {prd.scalability_and_performance},
    "deployment_plan": {prd.deployment_plan},
    "maintenance_and_support": {prd.maintenance_and_support},
    "risks_and_mitigations": {prd.risks_and_mitigations},
    "compliance_and_regulations": {prd.compliance_and_regulations},
    "budget_and_resources": {prd.budget_and_resources},
    "timeline_and_milestones": {prd.timeline_and_milestones},
    "communication_plan": {prd.communication_plan},
    "anything_unclear": {prd.anything_unclear},
    """]
    embeddings = embed_model.embed_documents(text)
    print(len(embeddings[0]))
    record_metadatas = [{
        "text": str(text), 'ID': project.id,
    }]
    index.upsert(vectors = zip([f'{project.id}'], embeddings,record_metadatas))
        
def update_project_workflow(workflow):
    embed_model=load_embedding_model()
    index = initiate_pinecone()
    project = Project.objects.get(workflow=workflow)
    prd=project.prd
    text =[
    f"""
    "project_id": {project.id},
    "project_title": {project.title},
    "project_description": {project.description},
    "project_start_date": {project.start_date},
    "project_end_date": {project.end_date},
    "project_bid_price": {project.bid_price},
    "project_status": {project.status},
    "project_related_techstacks": {project.related_techstacks}
    "project_created_at": {project.created_at},
    "project_updated_at": {project.updated_at},
    "project_created_by": {project.created_by},
    "project_overview": {prd.project_overview},
    "original_requirements": {prd.original_requirements},
    "project_goals": {prd.project_goals},
    "user_stories": {prd.user_stories},
    "system_architecture": {prd.system_architecture},
    "tech_stacks": {prd.tech_stacks},
    "requirement_pool": {prd.requirement_pool},
    "ui_ux_design": {prd.ui_ux_design},
    "development_methodology": {prd.development_methodology},
    "security_measures": {prd.security_measures},
    "testing_strategy": {prd.testing_strategy},
    "scalability_and_performance": {prd.scalability_and_performance},
    "deployment_plan": {prd.deployment_plan},
    "maintenance_and_support": {prd.maintenance_and_support},
    "risks_and_mitigations": {prd.risks_and_mitigations},
    "compliance_and_regulations": {prd.compliance_and_regulations},
    "budget_and_resources": {prd.budget_and_resources},
    "timeline_and_milestones": {prd.timeline_and_milestones},
    "communication_plan": {prd.communication_plan},
    "anything_unclear": {prd.anything_unclear},
    "workflow": {workflow}
        """
    ]
    embeddings = embed_model.embed_documents(text)
    record_metadatas = [{
        "text": str(text), 'ID': project.id,
    }]
    update_response = index.update(
    id=f"{project.id}",
    values=embeddings,
    set_metadata=record_metadatas,
    )

