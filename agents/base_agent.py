from abc import ABC, abstractmethod

from config.llm import llm


class BaseAgent(ABC):
    """
    Parent class for every AI agent.
    """

    def __init__(self):
        self.llm = llm

    @abstractmethod
    def build_prompt(self, state):
        pass

    def process_response(self, state, response):
        return response

    def run(self, state):
        prompt = self.build_prompt(state)

        response = self.llm.invoke(prompt)

        return self.process_response(state, response.content)