import openai

from ..models import *


def generate_project_workflow_prompt(
    project_description, project_requirements, project_timeline, students_skills
):
    prompt = f"""
        As a Project Manager, your task is to generate a comprehensive workflow for a new project based on the skills of the assigned students. The project involves {project_description}. Below are the key details:

        ### Project Requirements:
        {project_requirements}

        ### Project Description:
        {project_description}

        ### Project Timeline:
        {project_timeline}

        ### Student Skills:
        The following students have been assigned to the project along with their respective skillsets:

        {students_skills}

        ### Workflow Integration:
        Considering the skills of each student, outline a detailed workflow , Divide The Whole Project Into Different Sections , Each Section Telling In Details What To Do.

        Note: Do not provide actual code; instead, create a narrative or bullet-point format suitable for a Word file.

        Note: Provide the output in html tags . use different html tags to make the output look good in the frontend .

        Note: Use Tailwind Classes for h1,h2 and other basic tags and make it professional
    """
    return prompt


def make_workflow(project):
    # Get all the values from the database
    project_techstacks = project.related_techstacks
    project_description = project.description
    project_timeline = f"{project.end_date} to {project.start_date}"
    team = Team.objects.get(project=project)
    skills_string = ""
    for user in team.members.all():
        talent = user
        if talent:
            skills = ", ".join(talent.skills) if talent.skills else "No skills listed"
            skills_string += f"{talent.user.username}'s skills: {skills}\n"

    prompt = generate_project_workflow_prompt(
        project_description, project_techstacks, project_timeline, skills_string
    )
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
    )
    workflow = response.choices[0].text.strip()
    workflow_object = Workflow(description=workflow)
    workflow_object.save()
    project.workflow = workflow_object
    project.save()
    return workflow
