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

        Your task is to craft a vivid, immersive narrative based on the real-life summer memories, central themes, and story outline provided below.

        Memories:
        {memory_texts}

        Themes:
        {themes}

        Story Outline:
        {outline_sections}

        Instructions:
        - Seamlessly weave the memories into a single cohesive and emotionally engaging story that closely follows the provided outline.
        - Make the central themes feel organic and deeply woven into the narrative, so they naturally emerge rather than feel forced.
        - Use rich sensory details, authentic dialogue, and emotional nuance to bring scenes and characters to life.
        - Evoke the nostalgic, heartfelt feeling of reminiscing about a cherished summer experience.
        - Write in a natural, flowing narrative voice that feels both personal and reflective.
        - Keep the pacing balanced, ensuring the story builds momentum and emotional depth toward a satisfying conclusion.

        Output:
        Only the complete final story. Do not include notes, explanations, or any additional commentary.
        Strictly follow these instructions.
        """

        response = self.llm_for_generation.invoke(story_generation_prompt)
        response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
        return response
