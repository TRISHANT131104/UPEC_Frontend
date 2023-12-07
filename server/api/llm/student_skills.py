import openai
from ..models import Talent
from dotenv import load_dotenv
import os

load_dotenv()


def generate_learning_reasources(student, projects):
    skills = student.skills
    tech_stacks = projects.prd.tech_stacks
    prompt = f"""
        You are a student.
        You already have {skills} knowledge.
        Based on the projects you are assigned that needed {tech_stacks} knowledge.
        Tell me what all I need to learn to complete the project and its learning resources too.
    """
    # response = openai.Completion.create(
    #     engine="gpt-3.5-turbo-instruct",
    #     prompt=prompt,
    #     max_tokens=50,
    #     temperature=0.7,
    # )
    # output = query({
    #     "inputs": prompt,
    # })

    palm.configure(api_key=os.environ.get("PALM_API_KEY"))
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    model = models[0].name

    response = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )
    student.learning_resources = response
    student.save()
    return response
