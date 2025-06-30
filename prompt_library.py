class PromptLibrary:
    def __init__(self):
        self.prompts = {}

    def add_prompt(self, name: str, prompt_text: str):
        """
        Adds a new prompt to the library.

        Args:
            name: The name of the prompt (must be unique).
            prompt_text: The text of the prompt.
        """
        if name in self.prompts:
            raise ValueError(f"Prompt with name '{name}' already exists.")
        self.prompts[name] = {"name": name, "prompt_text": prompt_text}
        print(f"Prompt '{name}' added.")

    def remove_prompt(self, name: str):
        """
        Removes a prompt from the library.

        Args:
            name: The name of the prompt to remove.
        """
        if name not in self.prompts:
            raise ValueError(f"Prompt with name '{name}' not found.")
        del self.prompts[name]
        print(f"Prompt '{name}' removed.")

    def get_prompt(self, name: str) -> dict:
        """
        Retrieves a prompt from the library.

        Args:
            name: The name of the prompt to retrieve.

        Returns:
            A dictionary containing the prompt's name and text,
            or None if the prompt is not found.
        """
        return self.prompts.get(name)

    def list_prompts(self) -> list[str]:
        """
        Lists the names of all prompts in the library.

        Returns:
            A list of prompt names.
        """
        return list(self.prompts.keys())

    def update_prompt(self, name: str, new_prompt_text: str):
        """
        Updates the text of an existing prompt.

        Args:
            name: The name of the prompt to update.
            new_prompt_text: The new text for the prompt.
        """
        if name not in self.prompts:
            raise ValueError(f"Prompt with name '{name}' not found.")
        self.prompts[name]["prompt_text"] = new_prompt_text
        print(f"Prompt '{name}' updated.")
