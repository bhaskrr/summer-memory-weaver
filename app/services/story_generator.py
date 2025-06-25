from langchain_ollama import OllamaLLM
import re


class StoryGeneratorAgent:
    def __init__(self, llm_for_generation="deepseek-r1:1.5b", temperature=0.8):
        """Initializes the StoryGeneratorAgent"""
        self.llm_for_generation = OllamaLLM(
            model=llm_for_generation,
            temperature=temperature,
        )

    def generate_story(self, memories: list[dict], narrative_plan: dict):
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
        You are an expert storyteller.

        Your task is to craft a vivid, immersive narrative based on the real-life memories, central themes, and story structure provided below.

        Memories:
        {memory_texts}

        Themes:
        {themes}

        Story Outline:
        {outline_sections}

        Instructions:
        - Seamlessly weave the memories into a cohesive and engaging story, closely following the outline.
        - Highlight the specified themes throughout, ensuring they resonate emotionally.
        - Employ rich, sensory descriptions and authentic emotional depth to bring each scene to life.
        - Evoke the feeling of reminiscing about a cherished summer adventure, making the story feel personal and heartfelt.
        - Maintain a natural flow and narrative voice.

        Output only the completed story—do not include explanations or any extraneous text.
        """

        response = self.llm_for_generation.invoke(story_generation_prompt)
        response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
        return response
