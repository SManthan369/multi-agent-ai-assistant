import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from graphs.workflow import graph

# =============================
# Page Configuration
# =============================

st.set_page_config(page_title="Multi-Agent AI Assistant", page_icon="🤖", layout="wide")

# =============================
# Session State
# =============================

if "history" not in st.session_state:
    st.session_state.history = []

# =============================
# Header
# =============================

st.title("🤖 Multi-Agent AI Assistant")
st.caption("Research • Planning • Writing • Data Analysis")

# =============================
# Sidebar
# =============================

st.sidebar.header("⚙️ Controls")

query = st.sidebar.text_area(
    "Research Topic",
    height=150,
    placeholder="Example: Explain Retrieval Augmented Generation",
)

dataset = st.sidebar.file_uploader("Upload CSV (Optional)", type=["csv"])

run = st.sidebar.button("🚀 Run Assistant", use_container_width=True)

# History
st.sidebar.divider()
st.sidebar.subheader("🕘 Recent Searches")

if st.session_state.history:

    for item in st.session_state.history:

        with st.sidebar.expander(item["query"][:35]):

            st.write(item["report"][:250] + "...")

if st.sidebar.button("🗑 Clear History"):
    st.session_state.history = []
    st.rerun()

# About
st.sidebar.divider()

st.sidebar.markdown("### ℹ️ About")

st.sidebar.info("""
**Multi-Agent AI Assistant**

✅ Research Agent

✅ Planning Agent

✅ Writer Agent

✅ Data Analysis Agent

✅ LangGraph Workflow

✅ Ollama LLM

✅ Streamlit UI
""")

# =============================
# Empty State
# =============================

if not run:

    st.info("👈 Enter a research topic in the sidebar and click **Run Assistant**.")

# =============================
# Run Workflow
# =============================
workflow_start = time.perf_counter()

result = graph.invoke(state)

workflow_time = time.perf_counter() - workflow_start

st.metric("Total Workflow Time", f"{workflow_time:.2f} sec")
if run:

    if not query.strip():
        st.error("Please enter a research topic.")
        st.stop()

    state = {
        "query": query,
        "dataset": "",
        "research": "",
        "plan": "",
        "report": "",
        "analysis": "",
        "messages": [],
        "approval": True,
    }

    if dataset:

        os.makedirs("sample_data", exist_ok=True)

        path = f"sample_data/{dataset.name}"

        with open(path, "wb") as f:
            f.write(dataset.getbuffer())

        state["dataset"] = path

    progress = st.progress(0)

    with st.spinner("🤖 AI Agents are working..."):

        progress.progress(20)

        start = time.time()

        result = graph.invoke(state)

        progress.progress(100)

        elapsed = time.time() - start

    # Save history
    st.session_state.history.insert(0, {"query": query, "report": result["report"]})

    st.session_state.history = st.session_state.history[:10]

    st.success("✅ Workflow Completed")

    st.metric("⏱ Execution Time", f"{elapsed:.2f} sec")

    # =============================
    # Tabs
    # =============================

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📚 Research", "🗺️ Plan", "📊 Analysis", "📝 Report"]
    )

    with tab1:
        st.markdown(result["research"])

    with tab2:
        st.markdown(result["plan"])

    with tab3:

        if result.get("analysis"):
            st.markdown(result["analysis"])
        else:
            st.info("No dataset uploaded.")

    with tab4:

        st.markdown(result["report"])

        st.download_button(
            "⬇ Download Report",
            data=result["report"],
            file_name="report.md",
            mime="text/markdown",
            use_container_width=True,
        )

    # =============================
    # Statistics
    # =============================

    st.divider()

    st.subheader("📈 Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Research Words", len(result["research"].split()))

    with col2:
        st.metric("Plan Lines", len(result["plan"].splitlines()))

    with col3:
        st.metric("Report Words", len(result["report"].split()))

    # =============================
    # Workflow Log
    # =============================

    st.divider()

    st.subheader("📋 Workflow Log")

    for i, msg in enumerate(result["messages"], start=1):
        st.write(f"{i}. ✅ {msg}")

    # =============================
    # Debug
    # =============================

    with st.expander("🛠 Debug Information"):

        st.json(
            {
                "Query": state["query"],
                "Dataset": state["dataset"] if state["dataset"] else "None",
                "Execution Time": f"{elapsed:.2f} sec",
            }
        )

# =============================
# Footer
# =============================

st.divider()

st.caption("Built with ❤️ using Python • LangGraph • Ollama • Streamlit")
