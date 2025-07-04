![banner-image](./media/banner.png)

# 🧠 Summer Memory Weaver

An AI-powered storytelling agent that transforms fragmented summer memories—text, audio, and images—into beautiful, coherent narratives using NLP, RAG, and multi-agent orchestration.

## 📌 Table of Contents <!-- omit in toc -->

- [🧠 Summer Memory Weaver](#-summer-memory-weaver)
  - [🌞 Introduction](#-introduction)
  - [✨ Features](#-features)
  - [🧠 Agents Implemented](#-agents-implemented)
    - [📝 1. Memory Parser Agent](#-1-memory-parser-agent)
    - [📜 2. Narrative Planner Agent](#-2-narrative-planner-agent)
    - [✏️ 3. Story Generator Agent](#️-3-story-generator-agent)

## 🌞 Introduction

Summer is a collection of moments — scattered journal entries, late-night voice notes, unforgettable trips, and photos lost in your camera roll.

Summer Memory Weaver is your AI-powered personal historian that takes these fragmented memories and weaves them into a beautiful, enriched narrative.

## ✨ Features

- 📜 Accepts textual memory fragments (notes, social posts, keywords)
- 🎤 (Optional) Converts voice notes into text using Whisper ASR
- 🖼️ (Optional) Generates image tags/captions via open-source image models
- 🧠 Uses spaCy-based NLP to extract key events, people, and places
- ✍️ Generates a narrative that feels deeply personal and human
- 🧩 Modular agent-based architecture powered by LangChain + LangGraph

Stay tuned for further updates!

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
