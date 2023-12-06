import openai
from ..models.user import *
from ..models.projects import *

def generate_learning_resource_prompt(talent, project):
    team = Team.objects.filter(project=project)
    tech_stack = project.related_techstacks
    tech_stack = ", ".join(tech_stack)
    skills_string = ""
    for user in team.members.all():
        talent = Talent.objects.filter(user=user)
        if talent:
            skills = (
                ", ".join(talent.skills)
                if talent.skills
                else "No skills listed"
            )
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
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
    )
    answer=response.choices[0].text.strip()
    return answer