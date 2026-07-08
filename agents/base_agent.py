from abc import ABC, abstractmethod

from config.llm import llm


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    def __init__(self):
        self.llm = llm

    @abstractmethod
    def build_prompt(self, state):
        """Return the prompt for the LLM."""
        pass

    def run(self, state):
        """
        Execute the agent.
        """

        prompt = self.build_prompt(state)

        response = self.llm.invoke(prompt)

        return self.process_response(state, response.content)

    def process_response(self, state, response):
        """
        Override this if an agent needs custom response handling.
        """
        return response