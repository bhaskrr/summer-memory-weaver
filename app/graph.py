from services.memory_parser import MemoryParserAgent
from services.narrative_planner import NarrativePlannerAgent
from services.story_generator import StoryGeneratorAgent

from langgraph.graph import StateGraph
from langgraph.graph import START, END
from typing import TypedDict, List


class State(TypedDict):
    input_memories: List[dict]
    extracted_info: List[dict]
    narrative_plan: dict
    output: str


def memory_parser_node(state: State):
    parser_agent = MemoryParserAgent()
    print("MemoryParserAgent: Starting parsing memories...")
    extracted_details = [
        parser_agent.parse_memory(mem["type"], mem["original_text"])
        for mem in state["input_memories"]
    ]
    print("MemoryParserAgent: Parsing memories completed.")
    print("MemoryParserAgent: Parsed memories: ", extracted_details)
    return {"extracted_info": extracted_details}


def narrative_planner_node(state: State):
    narrative_planner_agent = NarrativePlannerAgent()
    plan = narrative_planner_agent.plan_narrative(state["extracted_info"])
    return {"narrative_plan": plan}


def story_generator_node(state: State):
    story_generator_agent = StoryGeneratorAgent()
    print(f"StoryGeneratorAgent: Generating story...")
    generated_story = story_generator_agent.generate_story(
        state["extracted_info"], state["narrative_plan"]
    )
    print("Story generation complete.")
    return {"output": generated_story}


# Initialize the builder with state
builder = StateGraph(State)

# Add nodes
builder.add_node("memory_parser", memory_parser_node)
builder.add_node("narrative_planner", narrative_planner_node)
builder.add_node("story_generator", story_generator_node)

# Add edges
builder.add_edge(START, "memory_parser")
builder.add_edge("memory_parser", "narrative_planner")
builder.add_edge("narrative_planner", "story_generator")
builder.add_edge("story_generator", END)

# Compile the graph
graph = builder.compile()
