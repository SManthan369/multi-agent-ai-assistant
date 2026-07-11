from abc import ABC, abstractmethod

from config.llm import llm
from config.logger import logger


class BaseAgent(ABC):
    """
    Parent class for every AI agent.
    """

    def __init__(self):
        self.llm = llm

    @abstractmethod
    def build_prompt(self, state):
        """
        Every child agent must implement this method.
        """
        pass

    def process_response(self, state, response):
        """
        Override in child classes if additional processing is required.
        """
        return response

    def run(self, state):

        try:
            logger.info(f"{self.__class__.__name__} started")

            prompt = self.build_prompt(state)

            response = self.llm.invoke(prompt)

            logger.info(f"{self.__class__.__name__} completed")

            return self.process_response(state, response.content)

        except Exception as e:

            logger.error(f"{self.__class__.__name__} failed: {str(e)}")

            state["messages"].append(f"{self.__class__.__name__} failed")

            return state
