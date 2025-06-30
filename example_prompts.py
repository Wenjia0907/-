from prompt_library import PromptLibrary

def main():
    # 创建 PromptLibrary 实例
    library = PromptLibrary()

    # 添加 10 条示例 prompt
    prompts_data = [
        {"name": "Cyberpunk Cityscape", "prompt_text": "A sprawling cyberpunk cityscape at night, neon lights reflecting on wet streets, flying vehicles, towering skyscrapers with holographic ads. Style: Blade Runner, detailed, hyperrealistic."},
        {"name": "Enchanted Forest", "prompt_text": "A mystical enchanted forest, ancient trees with glowing runes, ethereal mist, a hidden pathway, magical creatures peeking from the shadows. Style: fantasy art, vibrant colors, atmospheric."},
        {"name": "Steampunk Airship", "prompt_text": "A magnificent steampunk airship soaring through a cloudy sky, intricate gears and pipes visible, brass and copper details, adventurers on deck. Style: steampunk, detailed mechanical design, dramatic lighting."},
        {"name": "Alien Planet Landscape", "prompt_text": "A breathtaking alien planet landscape, strange flora and fauna, two moons in the sky, unusual rock formations, a lone explorer in a spacesuit. Style: sci-fi concept art, otherworldly, sense of wonder."},
        {"name": "Underwater Kingdom", "prompt_text": "A vibrant underwater kingdom, coral castles, schools of exotic fish, merfolk swimming, sun rays filtering through the water. Style: fantasy, colorful, detailed marine life."},
        {"name": "Post-Apocalyptic Survivor", "prompt_text": "A lone survivor ब्याज-apocalyptic wasteland, tattered clothes, makeshift weapon, ruined city in the background, dust and debris. Style: gritty, realistic, emotional."},
        {"name": "Medieval Knight Duel", "prompt_text": "Two medieval knights in full armor engaged in a fierce duel, swords clashing, sparks flying, a castle courtyard setting. Style: historical realism, dynamic action, detailed armor."},
        {"name": "Abstract Geometric Shapes", "prompt_text": "A dynamic composition of abstract geometric shapes, vibrant colors, intersecting lines and planes, creating a sense of depth and movement. Style: abstract art, modern, minimalist."},
        {"name": "Cute Cartoon Animal", "prompt_text": "A cute and fluffy cartoon animal (e.g., a fox or a bunny) with big expressive eyes, holding a flower, set against a soft pastel background. Style: children's book illustration, adorable, heartwarming."},
        {"name": "Surreal Dream Sequence", "prompt_text": "A surreal dream sequence, melting clocks, floating islands, a figure walking on water, illogical and bizarre elements combined. Style: surrealism, Salvador Dali influence, thought-provoking."}
    ]

    for p in prompts_data:
        try:
            library.add_prompt(p["name"], p["prompt_text"])
        except ValueError as e:
            print(e) # Handle cases where a prompt name might be duplicated if script is run multiple times

    # 演示如何使用库
    print("\n--- Available Prompts ---")
    for prompt_name in library.list_prompts():
        print(prompt_name)

    print("\n--- Example: Getting a Prompt ---")
    example_prompt_name = "Cyberpunk Cityscape"
    retrieved_prompt = library.get_prompt(example_prompt_name)
    if retrieved_prompt:
        print(f"Name: {retrieved_prompt['name']}")
        print(f"Prompt Text: {retrieved_prompt['prompt_text']}")
    else:
        print(f"Prompt '{example_prompt_name}' not found.")

    # 演示更新 prompt
    print("\n--- Example: Updating a Prompt ---")
    try:
        library.update_prompt("Cute Cartoon Animal", "A very cute and fluffy cartoon panda munching on bamboo, with big innocent eyes, in a lush green bamboo forest. Style: Disney animation, adorable, detailed fur.")
        updated_prompt = library.get_prompt("Cute Cartoon Animal")
        if updated_prompt:
            print(f"Updated Prompt Text: {updated_prompt['prompt_text']}")
    except ValueError as e:
        print(e)


    # 演示删除 prompt
    print("\n--- Example: Removing a Prompt ---")
    try:
        library.remove_prompt("Abstract Geometric Shapes")
    except ValueError as e:
        print(e)

    print("\n--- All Prompts After Deletion ---")
    for prompt_name in library.list_prompts():
        print(prompt_name)


if __name__ == "__main__":
    main()
