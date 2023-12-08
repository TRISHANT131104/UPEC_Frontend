import openai
import os
import pinecone
from langchain.chains import RetrievalQA
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import HuggingFaceTextGenInference
from torch import cuda
import json
from server.settings import embed_model


class MessageHandler:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.roles = " Project Owner: Project Manager, Project Manager: Technical Lead, Technical Lead: Developer, Developer: QA Engineer, QA Engineer: Project Manager, Web Developer, Mobile Developer, Desktop Developer, Embedded Systems Developer, Game Developer, Database Developer, DevOps, Quality Assurance and Testing, Artificial Intelligence and Machine Learning, Cloud Computing, Cybersecurity, UI UX Design, API Development, Augmented Reality and Virtual Reality, Robotics, Financial Technology, Education Technology, Blockchain"
        self.role = "Alumni"
        index = "project"
        text_field = "text"
        if embed_model:
            self.vectorstore = Pinecone(index, embed_model.embed_query, text_field)

    def prechecks(self, question):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"""
            I have a Question : {question} and The Current Roles i have is : {self.roles}. 
            Now i have 3 questions for you . 
            Qn1) Is this question answerable by any of the above mentioned roles Just Return yes or no and nothing else , 
            Qn2) If the question is answerable by any of the above roles then which role should take up the question just return the role If no role is decided then return None , 
            Qn3) Will this question require some context / project details before you can answer it Just Return yes or no and nothing else. 
            Return the answer of all 3 questions In this format : qn1's_answer,qn2's_answer,qn3's_answer . 
            Remmber to answer to the point and only 3 answers splitted with comma's must be returned
            """,
            max_tokens=50,
        )

        answer = response.choices[0].text.strip()
        answer = answer.lower()
        return answer

    def handle_context_required_message(self, question):
        # llm = openai()
        llm = HuggingFaceTextGenInference(
            inference_server_url="https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha",
            max_new_tokens=512,
            top_k=10,
            top_p=0.95,
            typical_p=0.95,
            temperature=0.01,
            repetition_penalty=1.03,
        )
        rag_pipeline = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=self.vectorstore.as_retriever()
        )
        answer = rag_pipeline(question)
        return answer["result"]

    def handle_message(self, user_question):
        print("user_question", user_question)
        precheck_json = self.prechecks(user_question)
        print(precheck_json)
        arr = precheck_json.split(",")
        print("arr", arr)
        arr = [i.replace(".", "") for i in arr]
        is_question_answerable = arr[0]
        role = arr[1]
        is_question_project_related = arr[2]
        if is_question_answerable.lower().replace(" ", "").replace(
            ".", ""
        ) == "no" or "no" in is_question_project_related.lower().replace(
            " ", ""
        ).replace(
            ".", ""
        ):
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=f"{user_question}. Give your response as you are best in that field and you really want to help the user .",
                max_tokens=50,
            )
        elif is_question_answerable.lower().replace(" ", "").replace(
            ".", ""
        ) == "yes" or "yes" in is_question_project_related.lower().replace(
            " ", ""
        ).replace(
            ".", ""
        ):
            if (
                role == None
                or role == "none"
                or role.replace(" ", "").replace(".", "") == "none"
                or "none" in role.replace(" ", "").replace(".", "")
                and is_question_project_related.lower()
                .replace(" ", "")
                .replace(".", "")
                == "no"
                or "no"
                in is_question_project_related.lower().replace(" ", "").replace(".", "")
            ):
                response = openai.Completion.create(
                    engine="gpt-3.5-turbo-instruct",
                    prompt=f"{user_question}. Give your response as you are best in that field and you really want to help the user .",
                    max_tokens=50,
                )
            else:
                if is_question_project_related.lower().replace(" ", "").replace(
                    ".", ""
                ) == "no" or "no" in is_question_project_related.lower().replace(
                    " ", ""
                ).replace(
                    ".", ""
                ):
                    response = openai.Completion.create(
                        engine="gpt-3.5-turbo-instruct",
                        prompt=f"As a {role}, {user_question}. Give your response as you are best in that field and you really want to help the user.",
                        max_tokens=50,
                    )
                elif is_question_project_related.lower().replace(" ", "").replace(
                    ".", ""
                ) == "yes" or "yes" in is_question_project_related.lower().replace(
                    " ", ""
                ).replace(
                    ".", ""
                ):
                    response = self.handle_context_required_message(user_question)
                else:
                    response = openai.Completion.create(
                        engine="gpt-3.5-turbo-instruct",
                        prompt=f"{user_question}. Give your response as you are best in that field and you really want to help the user .",
                        max_tokens=50,
                    )
        return response.choices[0].text.strip()
