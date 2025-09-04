# CodeXR — Phase 1 (MVP)

This is the starter scaffold for **CodeXR**, an AI coding assistant for AR/VR developers.

## 🧰 Prerequisites (macOS Apple Silicon – M1/M2/M3)
- macOS 13+ recommended
- Python 3.10+ (`python3 --version`)
- (Optional) Homebrew for managing dependencies: https://brew.sh/

## 🚀 Setup (recommended)
```bash
# 1) Unzip and cd into the project
cd codexr

# 2) Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # if you use fish: source .venv/bin/activate.fish

# 3) Upgrade pip and install dependencies
pip install -U pip
pip install -r requirements.txt

# 4) Run the app
streamlit run streamlit_app.py
```

Streamlit will print a local URL (usually http://localhost:8501). Open it in your browser.

## 🗂️ What’s included
- `streamlit_app.py` — Streamlit UI (with placeholders)
- `codexr/classifier.py` — simple Unity/Unreal/Shader/General classifier
- `codexr/schemas.py` — Pydantic schema for structured output
- `codexr/demo.py` — placeholder response generator
- `requirements.txt` — Python deps for Phase 1
- `.env.example` — where API keys will go in later steps

## ✅ Next steps (we’ll do together)
1. Add **LLM backend** (OpenAI or others) and a **prompt template** to return JSON that matches our schema.
2. Add **web search grounding** (Serper/Bing) and pass snippets to the LLM.
3. Swap the placeholder generator with the real pipeline.
4. Add syntax highlighting & UI polish (progress spinners, error states).
5. Create the 3 demo scenarios and record success.

---
_If anything fails, ensure your virtual environment is active and try `pip install -r requirements.txt` again._
