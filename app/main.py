from graph import graph

memories = [
    {
        "type": "text",
        "original_text": "Went to Goa with friends. Beaches were amazing!",
    },
    {
        "type": "text",
        "original_text": "Learned to surf on July 10th. So much fun.",
    },
    {
        "type": "text",
        "original_text": "Ate the best seafood at Calangute beach.",
    },
    {
        "type": "text",
        "original_text": "Visited a historical fort near Panjim. Beautiful architecture.",
    },
    {
        "type": "text",
        "original_text": "Relaxed by the pool all day.",
    }
]

result = graph.invoke({"input_memories": memories})
print(result["output"])
