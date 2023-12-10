import openai
import docx
from ..models.user import *
from ..models.projects import *
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


def generate_prompt(team, project):
    prd = project.prd
    prd = model_to_dict(prd)
    prd = {
        key: prd[key]
        for key in prd.keys()
        & {
            "project_overview",
            "original_requirements",
            "project_goals",
            "tech_stacks",
            "development_methodology",
        }
    }
    skills_string = ""
    for user in team.values_list("members"):
        talent = get_object_or_404(Talent, id=user[0])
        if talent:
            skills = ", ".join(talent.skills) if talent.skills else "No skills listed"
            skills_string += f"{talent.user.username}'s skills: {skills}\n"
    prompt = f"""
        You have to assign roles and tasks of different aspects of the project to different members of the team based on the project's requirements and overview and team members skillset. 
        
        The project's details are as follows: {prd}

        The team members' skills are as follows: {skills_string}.

        I need you to divide tasks among users based on their skills and project's requirements. Please provide a json format with username and their responsibilites for the completion of this project.
        give it in this format username : "roles":"","tasks":""
        """

    return prompt


def generate_management(team, project):
    prompt = generate_prompt(team, project)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
    )
    answer = response.choices[0].text.strip()

    return answer
