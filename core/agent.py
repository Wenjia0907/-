import asyncio
from .message import Message
from .message_bus import MessageBus

class Agent:
    """
    The base class for all agents in the multi-agent system.

    Each agent has a unique name, an inbox for receiving messages, and a
    reference to the central message bus. Agents run in an asyncio event loop,
    continuously processing incoming messages.

    Attributes:
        name (str): The unique name of the agent.
        message_bus (MessageBus): The central message bus for communication.
        inbox (asyncio.Queue): A queue for receiving messages.
    """
    def __init__(self, name: str, message_bus: MessageBus):
        self.name = name
        self.message_bus = message_bus
        self.inbox = asyncio.Queue()
        self.message_bus.register_agent(self)

    async def send_message(self, recipient: str, content: any):
        """
        Sends a message to another agent.

        Args:
            recipient (str): The name of the recipient agent.
            content (any): The content of the message.
        """
        message = Message(sender=self.name, recipient=recipient, content=content)
        await self.message_bus.dispatch(message)

    async def receive_message(self) -> Message:
        """
        Waits for and receives a message from the inbox.

        Returns:
            Message: The received message.
        """
        return await self.inbox.get()

    async def run(self):
        """
        The main loop for the agent.

        Continuously receives and processes messages from the inbox.
        This method should be overridden by subclasses to implement
        the agent's specific logic.
        """
        while True:
            message = await self.receive_message()
            await self.process_message(message)

    async def process_message(self, message: Message):
        """
        Processes a received message.

        This method should be implemented by subclasses to define the
        agent's behavior.

        Args:
            message (Message): The message to process.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")
