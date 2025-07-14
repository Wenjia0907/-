from core.agent import Agent
from core.message import Message
from utils.image_generator import generate_image

class DeliverAgent(Agent):
    """
    The agent for the "Deliver" phase of the Double Diamond model.

    This agent is responsible for generating the final output, which in
    this case will be an image.
    """
    async def process_message(self, message: Message):
        """
        Processes a message containing the final prompt.

        Args:
            message (Message): The message from the Develop agent.
        """
        print(f"Deliver Agent received: {message.content}")
        image_path = generate_image(message.content)
        print(f"Image generated: {image_path}")
        await self.send_message("coordinator", f"Image generated at {image_path}")
