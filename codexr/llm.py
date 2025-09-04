import os
import json
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from .classifier import classify_query
from .schemas import CodeXRResponse

# Load environment variables
load_dotenv()

# Initialize Hugging Face client (Zephyr chat model)
client = InferenceClient(
    "HuggingFaceH4/zephyr-7b-beta",
    token=os.getenv("HF_API_KEY")
)

PROMPT_TEMPLATE = """
You are CodeXR, an AI coding assistant for AR/VR developers.
The user will ask a question about Unity (C#), Unreal (C++), or Shaders.
Break it into:
- subtasks
- code snippet
- best practices
- gotchas
- difficulty rating (easy, medium, hard)
- documentation links

Return JSON ONLY that matches this schema:
{{
  "category": "Unity|Unreal|Shader|General",
  "subtasks": ["step1", "step2"],
  "code": "code here",
  "best_practices": ["tip1", "tip2"],
  "gotchas": ["trap1", "trap2"],
  "difficulty": "easy|medium|hard",
  "docs": ["https://..."],
  "raw": {{}}
}}
"""

def run_llm(query: str) -> CodeXRResponse:
    category = classify_query(query)
    user_prompt = PROMPT_TEMPLATE + f"\n\nUser query: {query}\nCategory: {category.value}\n"

    # Use Hugging Face chat API
    response = client.chat_completion(
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=500,
        temperature=0.2
    )

    content = response.choices[0].message["content"]

    # --- Try extracting JSON ---
    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1:
        json_str = content[start:end+1]
    else:
        # No JSON at all → fallback mode
        return CodeXRResponse(
            category=category.value,
            subtasks=["Could not parse structured steps"],
            code="",
            best_practices=[],
            gotchas=[],
            difficulty="medium",
            docs=[],
            raw={"raw_text": content}
        )

    try:
        parsed = json.loads(json_str)
        return CodeXRResponse(**parsed)
    except Exception:
        # JSON was invalid → fallback mode
        return CodeXRResponse(
            category=category.value,
            subtasks=["Failed to parse model output"],
            code="",
            best_practices=[],
            gotchas=[],
            difficulty="medium",
            docs=[],
            raw={"raw_text": content}
        )
