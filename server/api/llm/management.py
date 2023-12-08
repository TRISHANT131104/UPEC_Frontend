import openai
import docx
from ..models.user import *
from ..models.projects import *
from django.shortcuts import get_object_or_404

def generate_prompt(team, project):
    prd = project.prd
    skills_string = ""
    for user in team.values_list('members'):
        print(user)
        talent = get_object_or_404(Talent, id=user[0])
        print(talent)
        if talent:
            skills = ", ".join(talent.skills) if talent.skills else "No skills listed"
            skills_string += f"{talent.user.username}'s skills: {skills}\n"
    print("prd", prd)
    print("skills", skills_string)
    prompt = f"""
        You have to assign roles and tasks of different aspects of the project to different members of the team based on the project's prd and team members skillset. 
        The project's prd is as follows: {prd}
        The team members' skills are as follows: {skills_string}.

        ### Project Management Breakdown:
        Please provide detailed breakdown of the project management.
        """

    return prompt


def generate_management(team, project):
    prompt = generate_prompt(team, project)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1000,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
    )
    answer = response.choices[0].text.strip()

    return answer
