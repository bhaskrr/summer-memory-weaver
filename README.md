![banner-image](./media/banner.png)

# Summer Memory Weaver

An AI-powered storytelling agent that transforms fragmented summer memories into beautiful, coherent narratives using NLP and multi-agent orchestration - privately, on your machine.

## 📌 Table of Contents <!-- omit in toc -->

- [Summer Memory Weaver](#summer-memory-weaver)
  - [🌞 Introduction](#-introduction)
  - [🌱 Why?](#-why)
  - [✨ Features](#-features)
  - [🛠️ Built with](#️-built-with)
  - [🧠 Agents Implemented](#-agents-implemented)
    - [📝 1. Memory Parser Agent](#-1-memory-parser-agent)
    - [📜 2. Narrative Planner Agent](#-2-narrative-planner-agent)
    - [✏️ 3. Story Generator Agent](#️-3-story-generator-agent)
    - [✨ 4. Highlight Generator Agent](#-4-highlight-generator-agent)
  - [🧠 How it works](#-how-it-works)
  - [🛠️ Customization Features](#️-customization-features)
  - [⚡ Built for](#-built-for)
  - [🎯 What's next?](#-whats-next)
  - [📦 Installation \& Usage](#-installation--usage)
  - [⚠️ Limitations](#️-limitations)
  - [🙏 Acknowledgments](#-acknowledgments)
  - [📬 Contact](#-contact)
  - [📜 License](#-license)

## 🌞 Introduction

Summer is a collection of moments — scattered journal entries, late-night voice notes, unforgettable trips, and photos lost in your camera roll.

Summer Memory Weaver is your AI-powered personal historian that takes these fragmented memories and weaves them into a beautiful, enriched narrative.

## 🌱 Why?

Every summer, we collect moments — quick notes, snippets of conversations, scattered photos — but they stay fragmented.

**Summer Memory Weaver** reimagines how we remember:

- Uses **local LLM agents** to analyze, summarize, and narrate your memories.
- Creates a **personal story** from real moments.
- Works fully offline, ensuring your memories stay **private and secure**.

## ✨ Features

- 📜 Accepts textual memory fragments (notes, social posts, keywords)
- 🎤 (Optional) Converts voice notes into text using Whisper ASR
- 🖼️ (Optional) Generates image tags/captions via open-source image models
- 🧠 Uses spaCy-based NLP to extract key events, people, and places
- ✍️ Generates a narrative that feels deeply personal and human
- 🧩 Modular agent-based architecture powered by LangChain + LangGraph
- 🔒 **Runs fully locally** — No API calls; keeps your data private.

## 🛠️ Built with

- Python 🐍
- SpaCy (NLP)
- Ollama (local LLM serving)
- Langchain & Langgraph (multi-agent orchastration)
- Streamlit (UI)

## 🧠 Agents Implemented

This app uses multiple local LLM-powered agents, each designed to handle a specific creative or analytical task in the storytelling process:

### 📝 1. Memory Parser Agent

Purpose: Parses the input memory chunks using named entity recognition to extract entities relevant to the memory chunk.

How it works:

- Uses spaCy to perform named entity recognition
- Extracts key entities from each memory chunk

### 📜 2. Narrative Planner Agent

Purpose: Generates the themes and the narrative outline for the story.

How it works:

- Extracts relevant themes from memories using a local llm.
- Generates a detailed thematic outline for a summer story using themes along with memories.

### ✏️ 3. Story Generator Agent

Purpose:
Crafts the final immersive narrative by weaving together memories, themes, and the outline.

How it works:

- Uses rich sensory language and emotional depth.
- Closely follows the generated outline.
- Produces a cohesive, personal, and engaging summer story.

### ✨ 4. Highlight Generator Agent

Purpose:
Summarizes the generated story into a short, emotionally impactful highlight that captures its essence.

How it works:

- Extracts the most memorable, vivid, or emotionally resonant moments from the story.
- Produces a concise highlight (e.g., in 3–4 sentences) designed to quickly convey what makes the story special.
- Writes in an engaging, descriptive style to make the highlight feel appealing, as if introducing the story to someone who hasn’t read it.
- Avoids commentary or explanation, focusing purely on the story’s most striking moments.

## 🧠 How it works

1. **You input memory fragments** (texts, notes).
2. **Memory parser agent** extracts.
3. **Narrative planner agent** drafts a story structure.
4. **Story generator agent** generates the final narrative.

**All powered by local LLMs running with Ollama — no internet required.**

## 🛠️ Customization Features

Users can:

- 📚 **Choose number of memory chunks** (up to 5)
- 🎭 **Enable creative storytelling mode**: let AI add creative details and metaphors
- 📝 **Select tone**: nostalgic, humorous, reflective, cinematic, poetic
- 👤 **Select narrative style**: first-person or third-person
- ✨ **Toggle highlight generation**: get a short summary of the story

All features controlled via a clean **Streamlit sidebar**.

## ⚡ Built for

Summer Memory Weaver was built specifically with the spirit of Fusion Hacks 2 in mind:

- ✅ Summer-Inspired: At its heart, the app turns fragmented summer memories into rich, emotionally resonant narratives—helping users relive and preserve the essence of their summer adventures.

- 🔀 Cross-Disciplinary Fusion:
  - Combines:
    - 🧠 AI & NLP: Local LLMs for story generation, thematic analysis, and highlight summarization.
    - 📖 Storytelling & Creative Writing: Narrative crafting based on real memories and user-selected tones.
    - 🛠 User-Centric Design: Interactive Streamlit frontend with customizations like tone, style, and creative storytelling.

  - 🏡 Built fully local: No external APIs—runs entirely on your machine, showcasing practical AI development.

By blending AI + storytelling + user creativity, it aligns perfectly with Fusion Hacks' vision to fuse diverse ideas into something unique and meaningful.

## 🎯 What's next?

- 🖼️ Add support for images & audio memories.
- 📊 Richer analytics on summer themes.
- 🧪 Experiment with fine-tuned local models for storytelling.

## 📦 Installation & Usage

⚠️ Requires [Ollama](https://ollama.com/) installed and running locally.

The models used are:

- qwen3:1.7b
- llama3.2:1b

Make sure these models are downloaded via ollama.

```bash
# Clone the repository
git clone https://github.com/bhaskrr/summer-memory-weaver.git

# Navigate to the repository root
cd summer-memory-weaver

# Install the dependencies using uv (make sure uv is installed)
uv sync

# Run the app
streamlit run app/ui.py
```

## ⚠️ Limitations

While Summer Memory Weaver aims to provide a deeply personal and creative storytelling experience, there are a few current limitations:

- **Local Model Constraints:** Running local LLMs can be resource-intensive; story generation may become slower on machines with limited RAM or CPU.
- **Memory Handling:** The app currently accepts up to five memory chunks; supporting larger, complex narratives could require optimization.
- **Highlight Accuracy:** Generated highlights rely on the model's interpretation and may sometimes miss subtle emotional moments.
- **Language Support:** The app currently supports only English narratives.
- **Limited Guardrails:** AI guardrails are not implemented due to latency add-ons.

Despite these, the app demonstrates the potential of agentic local AI systems for creative, user-driven storytelling.

## 🙏 Acknowledgments

- Fusion Hacks 2 team for organizing the hackathon.
- Streamlit for the frontend framework.
- Ollama and open‑source local LLM projects.
- Inspiration from summer stories, creative writing, and AI communities.

## 📬 Contact

Created by [Bhaskar Bordoloi](https://github.com/bhaskrr) — feel free to connect!

## 📜 License

This project is licensed under the MIT License.
