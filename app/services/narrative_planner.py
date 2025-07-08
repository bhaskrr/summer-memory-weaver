from schemas.llm_schemas import ThemeResponseSchema
from langchain_ollama import OllamaLLM
from typing import List
import json
import re


class NarrativePlannerAgent:
    def __init__(self, llm_for_planning="qwen3:1.7b"):
        """
        Initializes the NarrativePlannerAgent.
        Args:
            llm_for_planning: A lightweight LLM for narrative reasoning.
        """
        self.llm_for_planning = OllamaLLM(
            model=llm_for_planning,
            temperature=0.8,
            top_k=50,
            top_p=0.8,
        )

    def _extract_themes(self, memories: List[dict]):
        """
        Analyzes parsed memories to identify dominant themes.
        Uses LLM for nuanced theme extraction.
        """

        memory_summary = "\n".join(
            [
                memory["original_text"]
                for memory in memories
                if "original_text" in memory
            ]
        )

        prompt = f"""
You are an expert narrative analyst. Given a summary of summer memories, identify the most prominent overarching themes that best capture the emotional or experiential essence of the memories.

Focus on broad, meaningful themes such as:
- Adventure
- Relaxation
- Family Bonding
- Learning Journey
- Cultural Exploration
- Personal Growth
- Nature Connection
(These are just examples — choose only what fits the content.)

Be **concise** and output **only the themes** that are most strongly represented.

Input:
\"\"\"
{memory_summary}
\"\"\"

Respond strictly in the following format (JSON-like):
{{
  "themes": <relevant themes here>
}}
"""

        try:
            response = self.llm_for_planning.invoke(prompt)
            # * To remove the <think>...</think> block from the output
            response = re.sub(
                r"<think>.*?</think>", "", response, flags=re.DOTALL
            ).strip()
            # Validate using the schema
            output = ThemeResponseSchema.model_validate_json(response)
            # return
            return (
                output.themes
                if output.themes and len(output.themes) > 0
                else ["Summer Memories"]
            )
        except Exception as e:
            print(f"Error analyzing themes: {e}. Falling back to default.")
            return ["Summer Memories"]

    def plan_narrative(self, memories: List[dict], narrative_style: str = "first_person"):
        """Generates a detailed narrative plan based on memories.
        This involves theme analysis and outlining.
        """

        print("NarrativePlannerAgent: Starting narrative planning...")

        # * Step 1
        themes = self._extract_themes(memories)
        print(f"NarrativePlannerAgent: Identified themes: {themes}")

        # * Step 2
        narrative_plan = {"themes": themes, "outline": []}

        if self.llm_for_planning:
            thematic_prompt = f"""
                Based on the following themes: {', '.join(themes)}
                and the raw memory texts: {', '.join([m['original_text'] for m in memories if 'original_text' in m])}

                Suggest a detailed thematic outline for a summer story.
                Use {narrative_style} narrative style.
                For each section, suggest a title and briefly mention which types of memories it would cover.
                Format as JSON array of objects:
                [
                    {{"section_title": "Theme A: <name>", "description": "<a suitable description>"}},
                    {{"section_title": "Theme B: <name>", "description": "<a suitable description>"}},
                    ...
                ]
                """
            try:
                llm_response = self.llm_for_planning.invoke(thematic_prompt)
                llm_response = re.sub(
                    r"<think>.*?</think>", "", llm_response, flags=re.DOTALL
                ).strip()
                parsed_outline = json.loads(llm_response)
                narrative_plan["outline"] = parsed_outline
            except Exception as e:
                print(
                    f"Error generating thematic outline with LLM: {e}. Falling back to simple thematic sections."
                )
                # Fallback: Simple sections based on primary themes
                narrative_plan["outline"] = [
                    {
                        "section_title": f"The {theme} of Summer",
                        "description": f"Memories related to {theme.lower()}",
                    }
                    for theme in themes
                ]
        else:
            narrative_plan["outline"] = [
                {
                    "section_title": f"The {theme} of Summer",
                    "description": f"Memories related to {theme.lower()}",
                }
                for theme in themes
            ]

        # Last step: Reflect (Optional) - Self-critique the plan (e.g., check for balance, missing sections)
        # This could involve another LLM call asking: "Is this outline comprehensive for the given memories?"

        print("NarrativePlannerAgent: Narrative plan generated.")
        return narrative_plan
