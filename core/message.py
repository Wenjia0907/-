from dataclasses import dataclass, field
from typing import Any

@dataclass
class Message:
    """
    Represents a message exchanged between agents.

    Attributes:
        sender (str): The name of the agent sending the message.
        recipient (str): The name of the agent receiving the message.
        content (Any): The content of the message.
    """
    sender: str
    recipient: str
    content: Any
