from core.agent import Agent
from core.message import Message

class DefineAgent(Agent):
    """
    The agent for the "Define" phase of the Double Diamond model.

    This agent is responsible for refining the initial ideas into a
    more concrete concept.
    """
    async def process_message(self, message: Message):
        """
        Processes a message containing the initial ideas.

        Args:
            message (Message): The message from the Discover agent.
        """
        print(f"Define Agent received: {message.content}")
        # In a real implementation, this would involve calling a LLM
        # to synthesize and define the concept.
        concept = f"Refined concept based on '{message.content}'"
        await self.send_message("develop", concept)
