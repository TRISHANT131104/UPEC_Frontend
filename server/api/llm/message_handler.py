import openai
import os
import pinecone
from langchain.chains import RetrievalQA
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from torch import cuda
from server.settings import embed_model

class MessageHandler:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.roles = "Alumni: Project Owner, Project Owner: Project Manager, Project Manager: Technical Lead, Technical Lead: Developer, Developer: QA Engineer, QA Engineer: Project Manager, Web Developer, Mobile Developer, Desktop Developer, Embedded Systems Developer, Game Developer, Database Developer, DevOps, Quality Assurance and Testing, Artificial Intelligence and Machine Learning, Cloud Computing, Cybersecurity, UI UX Design, API Development, Augmented Reality and Virtual Reality, Robotics, Financial Technology, Education Technology, Blockchain"
        self.role = "Alumni"

    def __is__question__answerable__(self, question):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Is this question answerable by any of the above roles {self.roles}? If it is a general question say no. The question is as follows: {question} .Just Return Yes Or No.",
            max_tokens=50,
        )

        answer = response.choices[0].text.strip()
        answer = answer.lower()
        return answer == "yes"

    def decide_role(self, question):
        if self.__is__question__answerable__(question):
            # if the question is answerable by any of the above roles , then it goes into this for loop
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=f"Which role among {self.roles} should handle this question? The question is as follows: {question}. Give your response in just the name of the role.",
                max_tokens=50,
            )

            role = response.choices[0].text.strip()
            return role
        else:
            # if the question is not answerable by any of the above roles , then it goes into this for loop , here AI answers it on its own
            return None

    def is_question_project_related(question):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Will this question require some context before you can answer it? The question is as follows: {question}. Just Return Yes Or No.",
            max_tokens=50,
        )

        answer = response.choices[0].text.strip()
        answer = answer.lower()
        return answer == "yes"

    def handle_context_required_message(question):
        llm = openai()
        # llm = HuggingFaceTextGenInference(
        #     inference_server_url=API_URL,
        #     max_new_tokens=512,
        #     top_k=10,
        #     top_p=0.95,
        #     typical_p=0.95,
        #     temperature=0.01,
        #     repetition_penalty=1.03,
        # )
        rag_pipeline = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
        )
        answer = rag_pipeline(question)
        return answer["result"]

    def handle_message(self, user_question):
        role = self.decide_role(user_question)
        print(role)
        if role == None:
            print("role is none")
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=f"{user_question}. Give your response as you are best in that field and you really want to help the user .",
                max_tokens=50,
            )
        else:
            print(self.is_question_project_related(user_question))
            if self.is_question_project_related(user_question):
                response = self.handle_context_required_message(user_question)
            else:
                response = openai.Completion.create(
                    engine="gpt-3.5-turbo-instruct",
                    prompt=f"As a {role}, {user_question}. Give your response as you are best in that field and you really want to help the user .",
                    max_tokens=50,
                )
        print(response)
        answer = response.choices[0].text.strip()
        return answer
