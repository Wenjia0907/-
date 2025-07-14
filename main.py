import asyncio
from core.message_bus import MessageBus
from agents.coordinator import Coordinator
from agents.discover_agent import DiscoverAgent
from agents.define_agent import DefineAgent
from agents.develop_agent import DevelopAgent
from agents.deliver_agent import DeliverAgent

async def main():
    """
    The main function to run the multi-agent system.
    """
    message_bus = MessageBus()

    # Create agents
    coordinator = Coordinator(name="coordinator", message_bus=message_bus)
    discover_agent = DiscoverAgent(name="discover", message_bus=message_bus)
    define_agent = DefineAgent(name="define", message_bus=message_bus)
    develop_agent = DevelopAgent(name="develop", message_bus=message_bus)
    deliver_agent = DeliverAgent(name="deliver", message_bus=message_bus)

    # Start agents as asyncio tasks
    tasks = [
        asyncio.create_task(coordinator.run()),
        asyncio.create_task(discover_agent.run()),
        asyncio.create_task(define_agent.run()),
        asyncio.create_task(develop_agent.run()),
        asyncio.create_task(deliver_agent.run()),
    ]

    # Get user input and start the process
    problem_description = input("Enter the problem description: ")
    await coordinator.start_process(problem_description)

    # In a real application, you would have a more robust way to end
    # the process. For this example, we'll just wait for a short time
    # to allow the messages to be processed.
    await asyncio.sleep(5)

    # Cancel all tasks
    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
