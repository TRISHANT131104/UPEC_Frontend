import openai
from ..models import  projects,Workflow
def generate_project_workflow_prompt(
    project_description, project_requirements, project_timeline, students_skills
):
    # Joining student information into a string
    students_info = ", ".join(
        [f"{student}: {skills}" for student, skills in students_skills.items()]
    )

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

        {students_info}

        ### Workflow Integration:
        Considering the skills of each student, outline a detailed workflow that leverages their expertise. Ensure efficient task allocation and collaboration among the team members.

        Note: Do not provide actual code; instead, create a narrative or bullet-point format suitable for a Word file.
    """
    return prompt


def make_workflow(project):
    # Get all the values from the database
    project_requirements = project.object.get("project_requirements")
    project_description = project.object.get("project_description")
    project_timeline = project.object.get("project_timeline")
    project_milestones = project.object.get("project_milestones")
    team = project.object.get("team")
    students_skills = {}
    for student in team.object.all():
        students_skills[student.object.get("name")] = student.object.get("skills")
    prompt = generate_project_workflow_prompt(
        project_description,
        project_requirements,
        project_timeline,
        project_milestones,
        students_skills,
    )
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
    )
    workflow=response.choices[0].text.strip()
    workflow_object=Workflow(
        description = workflow
    )
    workflow_object.save()
    project.object.update(workflow=workflow_object)
    project.save()
    return workflow
