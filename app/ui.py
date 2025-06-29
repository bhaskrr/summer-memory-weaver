import streamlit as st
from graph import graph

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
    }
    .stApp {
        font-family: 'Segoe UI', sans-serif;
    }
    .title-style {
        color: #2b2d42;
        font-size: 2.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 0.5em;
    }
    .memory-box textarea {
        background: #f1f5f9;
        border-radius: 10px;
        border: 1.5px solid #a5b4fc;
        font-size: 1.1rem;
        padding: 1em;
        margin-bottom: 1em;
    }
    .sidebar .sidebar-content {
        background: #e0e7ff;
        border-radius: 12px;
        padding: 1em;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #60a5fa 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.7em 2em;
        font-size: 1.1rem;
        border: none;
        margin-top: 1em;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #818cf8 0%, #38bdf8 100%);
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="title-style">🌞 Summer Memory <em>Weaver</em></div>',
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color:#475569; font-size:1.2rem; margin-bottom:2em;'>Relive your summer memories as a beautiful story. Enter your favorite moments below!</p>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("<h4 style='color:#3730a3;'>Settings</h4>", unsafe_allow_html=True)
    num_text_options = st.selectbox(
        "Number of memory chunks:",
        (1, 2, 3, 4, 5),
    )

memories = []
for i in range(num_text_options):
    text_input = st.text_area(
        "...",
        value="",
        height=80,
        max_chars=300,
        placeholder=f"Memory #{i+1} (e.g., 'Watched the sunset at the beach...')",
        key=f"text_{i}",
        label_visibility="collapsed",
        help=None,
        disabled=False,
        args=None,
        kwargs=None,
    )
    if text_input.strip():
        memories.append({"type": "text", "original_text": text_input.strip()})

st.markdown("---")

if st.button("✨ Generate Story"):
    if not memories:
        st.warning("Please enter at least one memory to generate your story.")
    else:
        with st.spinner("Weaving your summer story..."):
            result = graph.invoke({"input_memories": memories})
            st.markdown(
                "<h4 style='color:#2563eb; margin-top:2em;'>Your Summer Story:</h4>",
                unsafe_allow_html=True,
            )
            st.markdown(result["output"])
