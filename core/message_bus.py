import asyncio
from typing import Dict
from .message import Message

class MessageBus:
    """
    A central message bus for routing messages between agents.

    The message bus is responsible for registering agents and dispatching
    messages to the appropriate recipient.
    """
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        """
        Registers an agent with the message bus.

        Args:
            agent (Agent): The agent to register.
        """
        self.agents[agent.name] = agent

    async def dispatch(self, message: Message):
        """
        Dispatches a message to the recipient agent.

        If the recipient is found, the message is put into the agent's
        inbox. Otherwise, a warning is printed.

        Args:
            message (Message): The message to dispatch.
        """
        recipient_agent = self.agents.get(message.recipient)
        if recipient_agent:
            await recipient_agent.inbox.put(message)
        else:
            print(f"Warning: Agent '{message.recipient}' not found.")
