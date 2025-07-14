from core.agent import Agent
from core.message import Message

class DiscoverAgent(Agent):
    """
    The agent for the "Discover" phase of the Double Diamond model.

    This agent is responsible for brainstorming and generating initial ideas
    based on a given problem description.
    """
    async def process_message(self, message: Message):
        """
        Processes a message containing the problem description.

        Args:
            message (Message): The message from the Coordinator agent.
        """
        print(f"Discover Agent received: {message.content}")
        # In a real implementation, this would involve calling a LLM
        # to brainstorm ideas. For now, we'll use a simple placeholder.
        ideas = f"Initial ideas for '{message.content}'"
        await self.send_message("define", ideas)
