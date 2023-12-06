import openai
from ..models import Talent
from .message_handler import query    

def generate_learning_reasources(student,projects):
    skills = student.skills
    tech_stacks = projects.prd.tech_stacks
    prompt = f"""
        You are a student.
        You already have {skills} knowledge.
        Based on the projects you are assigned that needed {tech_stacks} knowledge.
        Tell me what all I need to learn to complete the project and its learning resources too.
    """
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
    )
    # output = query({
    #     "inputs": prompt,
    # })
    student.learning_resources = response.choices[0].text.strip()
    student.save()
    return response.choices[0].text.strip()

