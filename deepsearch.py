from agents.themis import Themis


class DeepSearch:
    def __init__(self):
        """
        Classe for the DeepSearch agent.
        This agent is designed to help you find information quickly and efficiently
        """
        self.themis = Themis()

    def answer(self, question):
        return self.themis.answer(question)