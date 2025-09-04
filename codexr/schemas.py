from typing import List, Dict, Any, Literal
from pydantic import BaseModel, HttpUrl, Field

Difficulty = Literal["easy", "medium", "hard"]

class CodeXRResponse(BaseModel):
    category: Literal["Unity", "Unreal", "Shader", "General"]
    subtasks: List[str] = Field(default_factory=list)
    code: str = ""
    best_practices: List[str] = Field(default_factory=list)
    gotchas: List[str] = Field(default_factory=list)
    difficulty: Difficulty = "medium"
    docs: List[HttpUrl] = Field(default_factory=list)
    raw: Dict[str, Any] = Field(default_factory=dict)
