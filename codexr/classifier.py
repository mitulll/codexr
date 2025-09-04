from enum import Enum

class Category(str, Enum):
    Unity = "Unity"
    Unreal = "Unreal"
    Shader = "Shader"
    General = "General"

UNITY_KEYWORDS = [
    "unity", "xr interaction toolkit", "c#", "monobehaviour", "teleport", "xr rig", "ovr",
    "vive", "oculus integration", "unity xr"
]
UNREAL_KEYWORDS = [
    "unreal", "ue", "ue5", "blueprint", "c++", "multiplayer", "replication", "pawn", "actor"
]
SHADER_KEYWORDS = [
    "shader", "hlsl", "glsl", "shadergraph", "pbr", "occlusion", "fragment", "vertex"
]

def classify_query(q: str) -> Category:
    ql = (q or "").lower()
    if any(k in ql for k in UNITY_KEYWORDS):
        return Category.Unity
    if any(k in ql for k in UNREAL_KEYWORDS):
        return Category.Unreal
    if any(k in ql for k in SHADER_KEYWORDS):
        return Category.Shader
    return Category.General
