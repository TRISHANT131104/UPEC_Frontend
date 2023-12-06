import openai
from ..models.user import *
from ..models.projects import *
import pprint
import google.generativeai as palm
from dotenv import load_dotenv
import os

load_dotenv()


def generate_learning_resource_prompt(talent, project):
    team = Team.objects.filter(project=project)
    tech_stack = project.related_techstacks
    tech_stack = ", ".join(tech_stack)
    skills_string = ""
    for user in team.members.all():
        talent = Talent.objects.filter(user=user)
        if talent:
            skills = ", ".join(talent.skills) if talent.skills else "No skills listed"
            skills_string += f"{user.first_name}'s skills: {skills}\n"

    prompt = f"""
        You have to recomment learning resources to the team members based on the project's required tech stacks and the team members' skills. 
        The project's required tech stacks are {tech_stack}.
        The team members' skills are as follows: {skills_string}.

        ### Learning Resources:
        Please provide detailed learning resources and include all the necessary links if possible.
        """

    return prompt


def learning_resource(talent, project):
    prompt = generate_learning_resource_prompt(talent, project)
    palm.configure(api_key=os.environ.get("PALM_API_KEY"))
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
    #     engine="davinci",
    #     prompt=prompt,
    #     max_tokens=1000,  # Adjust as needed
    #     temperature=0.7,  # Adjust as needed
    # )
    # answer = response.choices[0].text.strip()
    return answer
