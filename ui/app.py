import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from graphs.workflow import graph

st.set_page_config(
    page_title="Multi-Agent AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Assistant")
st.caption("Research • Planning • Writing • Data Analysis")

# ================= Sidebar =================

st.sidebar.header("⚙️ Controls")

query = st.sidebar.text_area(
    "Research Topic",
    height=150
)

dataset = st.sidebar.file_uploader(
    "Upload CSV (Optional)",
    type=["csv"]
)

run = st.sidebar.button(
    "🚀 Run Assistant",
    use_container_width=True
)

# ================ Output ====================

if run:

    state = {
        "query": query,
        "dataset": "",
        "research": "",
        "plan": "",
        "report": "",
        "analysis": "",
        "messages": [],
        "approval": True
    }

    if dataset:

        os.makedirs("sample_data", exist_ok=True)

        path = f"sample_data/{dataset.name}"

        with open(path, "wb") as f:
            f.write(dataset.getbuffer())

        state["dataset"] = path

    with st.spinner("🤖 Running AI Workflow..."):

        result = graph.invoke(state)

    st.success("Workflow Completed ✅")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📚 Research",
            "🗺️ Plan",
            "📊 Analysis",
            "📝 Report"
        ]
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

    st.divider()

    st.subheader("📋 Workflow Log")

    for msg in result["messages"]:
        st.success(msg)

    st.download_button(
        "⬇ Download Report",
        result["report"],
        file_name="report.txt"
    )