import streamlit as st
from codexr.llm import run_llm
from codexr.classifier import classify_query, Category
from codexr.demo import make_demo_response, language_hint_for
from pydantic import ValidationError

st.set_page_config(page_title="CodeXR — AR/VR Coding Assistant (MVP)", layout="wide")

st.title("🧠 CodeXR — AR/VR Coding Assistant (MVP)")
st.caption("Phase 1: Streamlit UI with classification + placeholder output. LLM + search come next.")

with st.sidebar:
    st.header("Settings")
    st.write("This MVP uses placeholder logic — no API keys needed yet.")
    st.info("Next steps will add LLM + web search and JSON validation.")
    st.divider()
    st.markdown("**Detected environment**: Streamlit running in Python venv is recommended.")

query = st.text_area("Describe what you want to build or fix (Unity/Unreal/Shader):", height=120,
                     placeholder="e.g., How do I add teleport locomotion in Unity VR?")
run = st.button("Get Solution")

if run:
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        cat = classify_query(query)
        st.subheader("Classification")
        st.write(f"**Category:** `{cat.value}`")

        # Demo response (placeholder). Later we'll call LLM + search here.
        try:
            resp = run_llm(query)
        except ValidationError as e:
            st.error("Output did not match expected schema.")
            st.exception(e)
            st.stop()

        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("✅ Subtasks")
            for step in resp.subtasks:
                st.checkbox(step, value=False, key=f"task-{step}")
            st.subheader("⚠️ Gotchas")
            st.markdown("\n".join([f"- {g}" for g in resp.gotchas]))
            st.subheader("🌟 Best Practices")
            st.markdown("\n".join([f"- {b}" for b in resp.best_practices]))

        with col2:
            st.subheader("🧩 Code Snippet")
            st.code(resp.code, language=language_hint_for(Category(resp.category)))
            st.subheader("📈 Difficulty")
            st.write(resp.difficulty.capitalize())
            st.subheader("🔗 Documentation")
            for url in resp.docs:
                st.markdown(f"- [{url}]({url})")

        st.divider()
        st.subheader("🧱 Raw JSON")
        st.json(resp.model_dump())

st.markdown("---")
st.markdown("Made with ❤️ for AR/VR devs. Phase 2: RAG-lite + Error Debugging. Phase 3: VS Code Extension.")
