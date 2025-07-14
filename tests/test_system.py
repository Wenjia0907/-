import asyncio
import unittest
from unittest.mock import patch, MagicMock

from core.message_bus import MessageBus
from agents.coordinator import Coordinator
from agents.discover_agent import DiscoverAgent
from agents.define_agent import DefineAgent
from agents.develop_agent import DevelopAgent
from agents.deliver_agent import DeliverAgent

class TestSystem(unittest.TestCase):
    def test_full_workflow(self):
        # Mock the input function
        with patch('builtins.input', return_value="a futuristic car"):
            # Run the asyncio event loop
            with patch('agents.deliver_agent.generate_image', return_value="output/test_image.png") as mock_generate_image:
                asyncio.run(self.async_test_full_workflow(mock_generate_image))

    async def async_test_full_workflow(self, mock_generate_image):
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

        # Start the process
        await coordinator.start_process("a futuristic car")

        # Wait for the process to complete
        await asyncio.sleep(1)

        # Assert that the image generator was called with the correct prompt
        mock_generate_image.assert_called_with("A detailed prompt for 'Refined concept based on 'Initial ideas for 'a futuristic car'''")

        # Cancel all tasks
        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    unittest.main()
