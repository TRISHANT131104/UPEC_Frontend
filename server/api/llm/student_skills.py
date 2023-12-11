import os

import google.generativeai as palm
import openai
from dotenv import load_dotenv

from ..models import *

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_learning_resource_prompt(skills, tech_stack):
    """
    Generate the prompt for recommending learning resources to a student based on their skills and project's required tech stacks.

    Args:
        skills (str): The skills of the student.
        tech_stack (list): The required tech stacks for the project.

    Returns:
        str: The generated prompt.
    """
    prompt = f"""
        You have to recommend learning resources to the student based on the project's required tech stacks and the students skills. 
        
        The project's required tech stacks are {tech_stack}.
        The team members' skills are as follows: {skills}.

        ### Learning Resources:
        Please provide detailed learning resources and include all the necessary links if possible , Remember You Do have to Provide Learning Resources Compulsary .

        Note: Provide the output in html tags . use different html tags to make the output look good in the frontend .

        Note: Use Tailwind Classes for h1,h2 and other basic tags and make it professional . Colour the <a> tages , Kepp good spacing Between Each Line . Donot give <html>,<head> / <body> tags
        """

    return prompt

def generate_learning_reasources(talent, projects):
    """
    Generate learning resources based on the talent's skills and project's required tech stacks.

    Args:
        talent (Talent): The talent object containing the skills.
        projects (list): The list of projects.

    Returns:
        str: The generated learning resources.
    """
    skills = talent.skills
    tech_stacks=[]
    for project in projects:
        print(project.prd.tech_stacks)
        tech_stacks.append(project.prd.tech_stacks)

    prompt = generate_learning_resource_prompt(skills, tech_stacks)
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

    return response.result
