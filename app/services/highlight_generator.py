from langchain_ollama import OllamaLLM


class HighlightGeneratorAgent:
    """Generates the highlight of the story."""

    def __init__(self, llm_for_highlight="llama3.2:1b"):
        """Initialize the highlight generator agent"""
        self.llm_for_highlight_generation = OllamaLLM(
            model=llm_for_highlight,
            temperature=0.5,
            top_k=50,
            top_p=0.8,
        )

    def generate_highlight(self, story: str, tone: str, num_sentences: int = 3):
        """Generate the story highlight"""

        prompt = f"""You are an expert storyteller and editor.\n\n
            Your task is to craft a vivid, emotionally engaging highlight that captures the very essence of the following story.\n\n
            Story:\n{story}\n\n
            Instructions:\n
            - Identify and extract the most powerful, memorable, or emotionally resonant moments.\n
            - Summarize these into a single cohesive highlight with a {tone} tone of no more than {num_sentences} sentences.\n
            - Make the highlight vivid and compelling, so it feels like a captivating teaser to someone who hasn’t read the story.\n
            - Output only the highlight text—do not add any explanations, commentary, or formatting."""
        try:
            print("HighlightGeneratorAgent: Generating highlight...")

            # Generate response from a local llm
            response = self.llm_for_highlight_generation.invoke(prompt)

            print("HighlightGeneratorAgent: Highlight generation complete.")
        except Exception as e:
            print(f"Error generating highlight: {e}. Falling back to defaults.")

            story_sentences = story.split(".")
            response = ".".join([story_sentences[0], story_sentences[-2], ""])

        # Remove any leading and trailing whitespaces if reponse is a string
        if type(response) == str:
            response = response.strip()

        return response
