from core.agent import Agent
from core.message import Message

class DevelopAgent(Agent):
    """
    The agent for the "Develop" phase of the Double Diamond model.

    This agent is responsible for developing the concept into a detailed
    prompt for image generation.
    """
    async def process_message(self, message: Message):
        """
        Processes a message containing the refined concept.

        Args:
            message (Message): The message from the Define agent.
        """
        print(f"Develop Agent received: {message.content}")
        # In a real implementation, this would involve calling a LLM
        # to expand the concept into a detailed prompt.
        prompt = f"A detailed prompt for '{message.content}'"
        await self.send_message("deliver", prompt)
