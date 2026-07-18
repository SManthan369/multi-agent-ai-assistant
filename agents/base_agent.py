from abc import ABC, abstractmethod
import time

from config.llm import llm
from config.logger import logger


class BaseAgent(ABC):

    def __init__(self):
        self.llm = llm

    @abstractmethod
    def build_prompt(self, state):
        pass

    def process_response(self, state, response):
        return response

    def run(self, state):

        try:
            logger.info(f"{self.__class__.__name__} started")

            total_start = time.perf_counter()

            # Prompt creation
            prompt_start = time.perf_counter()
            prompt = self.build_prompt(state)
            prompt_time = time.perf_counter() - prompt_start
            logger.info(
                f"{self.__class__.__name__} prompt length: {len(prompt)} characters"
            )
            # LLM call
            llm_start = time.perf_counter()
            response = self.llm.invoke(prompt)
            llm_time = time.perf_counter() - llm_start

            total_time = time.perf_counter() - total_start

            logger.info(
                f"{self.__class__.__name__} | "
                f"Prompt: {prompt_time:.2f}s | "
                f"LLM: {llm_time:.2f}s | "
                f"Total: {total_time:.2f}s"
            )

            state["messages"].append(f"{self.__class__.__name__}: {total_time:.2f}s")

            return self.process_response(state, response.content)

        except Exception as e:
            logger.error(f"{self.__class__.__name__} failed: {e}")
            state["messages"].append(f"{self.__class__.__name__} failed")
            return state
