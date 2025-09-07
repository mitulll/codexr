# CodeXR – AR/VR Coding Assistant

This is my mini-project for coursework.  
It is a coding assistant that helps with Unity, Unreal, and Shader programming.  
The app is made with **Streamlit** and uses a Hugging Face model as the backend.

---

## Features
- Ask a coding question in text form
- Classifies query into Unity, Unreal, Shader, or General
- Shows:
  - Subtasks
  - Code snippet
  - Best practices
  - Gotchas
  - Difficulty level
  - Documentation links
- Also shows the raw model output (JSON)

---

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/codexr.git
   cd codexr
   ```

2. Create a Virtual Environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```      

4. Create a .env file in the root folder and add your Hugging Face API key:
   ```bash
   HF_API_KEY=your_token_here
   ```

5. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ``` 
