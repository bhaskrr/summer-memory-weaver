import en_core_web_sm


class MemoryParserAgent:
    def __init__(self):
        """
        Initializes the MemoryParserAgent with necessary NLP models and tools.
        """
        self.nlp = en_core_web_sm.load()

    def parse_text_memory(self, text: str):
        """Parses a raw text memory."""

        doc = self.nlp(text)

        extracted_info = {
            "original_text": text,
            "entities": [],
            "keywords": [],
            "main_verbs": [],
            "date_info": [],
            "location_info": [],
            "event_info": [],
        }

        # Named Entity Recognition
        for ent in doc.ents:
            extracted_info["entities"].append({"text": ent.text, "label": ent.label_})
            if ent.label_ == "DATE":
                extracted_info["date_info"].append(ent.text)
            elif ent.label_ in ["GPE", "LOC"]:
                extracted_info["location_info"].append(ent.text)
            elif ent.label_ == "EVENT":
                extracted_info["event_info"].append(ent.text)
            # ? More entity types may be needed

        # keywords
        keywords = [
            token.text.lower()
            for token in doc
            if token.pos_ in ["NOUN", "PROPN", "ADJ"]
            and not token.is_stop
            and not token.is_punct
        ]
        extracted_info["keywords"] = list(set(keywords))  # * Remove duplicates

        # main verbs/actions
        main_verbs = [
            token.lemma_
            for token in doc
            if token.pos_ == "VERB" and token.dep_ in ["ROOT", "acl", "advcl", "conj"]
        ]
        extracted_info["main_verbs"] = list(set(main_verbs)) # * Remove duplicates

        return extracted_info

    def parse_memory(self, input_type: str, input_data: str):
        """Main entry point for parsing any type of memory."""
        if input_type.lower() == "text":
            return self.parse_text_memory(input_data)
        else:
            raise ValueError(f"Unsupported memory input type: {input_type}")
