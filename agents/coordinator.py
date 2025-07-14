from core.agent import Agent
from core.message import Message

class Coordinator(Agent):
    """
    The coordinator agent responsible for managing the workflow.

    This agent orchestrates the entire process, from initiating the
    "Discover" phase to receiving the final output from the "Deliver" phase.
    """
    def __init__(self, name, message_bus):
        super().__init__(name, message_bus)
        self.original_problem = None

    async def start_process(self, problem: str):
        """
        Starts the Double Diamond process with the given problem.

        Args:
            problem (str): The initial problem description.
        """
        self.original_problem = problem
        print(f"Coordinator starting process with problem: {problem}")
        await self.send_message("discover", problem)

    async def process_message(self, message: Message):
        """
        Processes the final message from the Deliver agent.

        Args:
            message (Message): The message from the Deliver agent.
        """
        print(f"Coordinator received final output: {message.content}")
        # In a real application, you might want to do something more here,
        # like notifying the user or saving the result.
        print("Process complete.")
