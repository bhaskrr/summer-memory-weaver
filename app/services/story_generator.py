from langchain_ollama import OllamaLLM
import re


class StoryGeneratorAgent:
    def __init__(self, llm_for_generation="llama3.2:1b", temperature=0.5):
        """Initializes the StoryGeneratorAgent"""
        self.llm_for_generation = OllamaLLM(
            model=llm_for_generation,
            temperature=temperature,
        )

    def generate_story(self, memories: list[dict], narrative_plan: dict, tone: str, preferred_length: str):
        """Generates the story using the memories and narrative plan."""
        memory_texts = "\n".join(
            [f"- {m['original_text']}" for m in memories if "original_text" in m]
        )
        themes = ", ".join(narrative_plan.get("themes", []))
        outline_sections = "\n".join(
            [
                f"{i+1}. {section['section_title']}: {section['description']}"
                for i, section in enumerate(narrative_plan.get("outline", []))
            ]
        )

        story_generation_prompt = f"""
        You are a masterful storyteller renowned for your ability to transform real-life memories into captivating narratives.

        Your task is to weave the following summer memories, themes, and story outline into a single, immersive story.

        Memories:
        {memory_texts}

        Themes:
        {themes}

        Story Outline:
        {outline_sections}

        Guidelines:
        - Integrate the memories naturally and seamlessly, ensuring each one contributes meaningfully to the story's progression.
        - Let the central themes emerge organically through the characters, events, and emotions—avoid making them feel forced or artificial.
        - Write in a {tone} tone, and ensure the story is {preferred_length}.
        - Use vivid sensory details, authentic dialogue, and emotional nuance to bring scenes and characters to life.
        - Maintain a natural, flowing narrative voice that feels personal and genuine.
        - Balance the pacing, building emotional depth and momentum toward a satisfying conclusion.
        - Follow the provided outline closely, but feel free to enhance transitions and add creative touches that enrich the narrative.

        Output Instructions:
        - Output only the complete, final story.
        - Do not include any notes, explanations, or commentary.
        - Strictly adhere to these instructions.
        """

        response = self.llm_for_generation.invoke(story_generation_prompt)
        return response
