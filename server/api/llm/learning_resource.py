import openai
from ..models.user import *
from ..models.projects import *
import pprint
from dotenv import load_dotenv
import os
import google.generativeai as palm

load_dotenv()


def generate_learning_resource_prompt(talent, project):
    team = Team.objects.get(project=project)
    tech_stack = project.related_techstacks
    tech_stack = ", ".join(tech_stack)
    skills_string = ""
    print(team)
    for user in team.members.all():
        talent = Talent.objects.get(user=user)
        if talent:
            skills = ", ".join(talent.skills) if talent.skills else "No skills listed"
            skills_string += f"{user.username}'s skills: {skills}\n"
    print('tech_stack',tech_stack)
    print('skills_string',skills_string)
    prompt = f"""
        You have to recommend learning resources to the team members based on the project's required tech stacks and the team members' skills. 
        
        The project's required tech stacks are {tech_stack}.
        The team members' skills are as follows: {skills_string}.

        ### Learning Resources:
        Please provide detailed learning resources and include all the necessary links if possible , Remember You Do have to Provide Learning Resources Compulsary , Remember To Use <h1>,<p>,<a>,<b> tags To Make the output look good. .
        """

    return prompt


def learning_resource(talent, project):
    prompt = generate_learning_resource_prompt(talent, project)
    palm.configure(api_key='AIzaSyAJoZkh9TLWe7SJjfrRnyiO38B4dLNMfXM')
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    model = models[0].name

    answer = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )

    # response = openai.Completion.create(
    #     engine="gpt-3.5-turbo-instruct",
    #     prompt=prompt,
    #     max_tokens=80,  # Adjust as needed
    #     temperature=0.7,  # Adjust as needed
    # )
    # answer = response.choices[0].text.strip()
    
    return answer.result
