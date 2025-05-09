import os
from dotenv import load_dotenv
from mistralai import Mistral
from agents import *


# Load environment variables from .env file
load_dotenv()

class Themis:
    def __init__(self, agents=None):
        """
        Themis is the orchestrator (headmaster) of a multi-agent system called DeepSearch.
        Its responsibilities include:
        - Reformulating user questions for better agent understanding.
        - Delegating the task to the most appropriate specialized agent.
        - Collecting and returning the final answer to the user.

        This class acts as a bridge between user intent and agent-level execution.
        """
        self.agents = agents
        self.history = []
        self.agent = Mistral(os.environ["MISTRAL_API_KEY"])
        self.agent_name = "Themis"

    def answer(self, question):
        return self.reformulate(question)
    
    def reformulate(self, question):
        """
        Reformulate the question to make it more understandable for the agent.
        """
        reformulated_response = self.agent.chat.complete(
            messages=[
                {
                    "role": "system",
                    "content": "You are Themis, the headmaster of a multi-agent system called DeepSearch. "
                               "Your role is to reformulate user questions for better agent understanding."
                },
                {
                    "role": "user", 
                    "content": question
                }
            ],
            model="mistral-large-latest",
            temperature=0.7
        )

        return reformulated_response.choices[0].message.content

    def select_agent(self, question):
        """
        Select the best agents to handle the question based on keywords or other criteria.
        """
       