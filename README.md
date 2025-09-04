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

Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create a .env file in the root folder and add your Hugging Face API key:

HF_API_KEY=your_token_here


Run the app:

streamlit run streamlit_app.py

Example Queries

How do I add teleport locomotion in Unity VR?

How do I set up multiplayer in Unreal VR?

Which shader works best for AR occlusion?

Notes

This is an MVP version, so the outputs are not always perfect.

In the future, I would like to add voice input and proper web search grounding.

Author

This project was developed by Mitul Chitkara as part of my coursework.
I set up Streamlit, connected it to Hugging Face models, and made the app show structured results.
