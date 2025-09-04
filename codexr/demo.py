from .classifier import Category, classify_query
from .schemas import CodeXRResponse

def language_hint_for(category: Category) -> str:
        if category == Category.Unity:
            return "csharp"
        if category == Category.Unreal:
            return "cpp"
        if category == Category.Shader:
            return "hlsl"
        return "text"

def example_docs(category: Category):
        if category == Category.Unity:
            return ["https://docs.unity3d.com/Manual/XR.html"]
        if category == Category.Unreal:
            return ["https://docs.unrealengine.com/"]
        if category == Category.Shader:
            return ["https://learnopengl.com/Advanced-Lighting/Normal-Mapping"]
        return ["https://developer.mozilla.org/"]

def make_demo_response(query: str) -> CodeXRResponse:
        category = classify_query(query)
        # Minimal placeholder content; we will replace this with real LLM + search later
        subtasks_map = {
            Category.Unity: [
                "Install XR Interaction Toolkit in Package Manager",
                "Add XR Origin (Action-based) to the scene",
                "Add Teleportation Area and set input actions",
                "Test in Play Mode and tweak turn/strafe settings"
            ],
            Category.Unreal: [
                "Create a new C++ project with VR template",
                "Enable replication on PlayerPawn and key components",
                "Set up GameMode for listen server",
                "Test with two clients using PIE"
            ],
            Category.Shader: [
                "Decide occlusion approach (depth mask vs stencil)",
                "Sample camera depth texture in fragment stage",
                "Compare scene depth against virtual object depth",
                "Discard pixels when real depth is closer"
            ],
            Category.General: [
                "Clarify engine and platform",
                "Break the task into features and steps",
                "Identify required packages/plugins",
                "Prototype and iterate"
            ],
        }
        code_map = {
            Category.Unity: """// C# (Unity) — Teleport example (placeholder)
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class SetupTeleport : MonoBehaviour
{
    public TeleportationProvider provider;
    public TeleportationArea area;
    void Start() {
        if (provider == null) provider = FindObjectOfType<TeleportationProvider>();
        if (area == null) area = FindObjectOfType<TeleportationArea>();
        // Assign input via XR Interaction Toolkit Input Actions (in editor)
    }
}""",
            Category.Unreal: """// C++ (Unreal) — Replication setup (placeholder)
void AMyActor::GetLifetimeReplicatedProps(TArray< FLifetimeProperty >& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    DOREPLIFETIME(AMyActor, ReplicatedVar);
}""",
            Category.Shader: """// HLSL (Shader) — Depth-based occlusion (conceptual placeholder)
float sceneDepth = SAMPLE_DEPTH_TEXTURE(_CameraDepthTexture, i.uv);
if (sceneDepth < i.objDepth) { clip(-1); } // hide pixel when real world is closer
""",
            Category.General: "// Provide engine-specific details for tailored code."
        }
        best_practices_map = {
            Category.Unity: [
                "Use the Action-based XR rig to avoid legacy input issues",
                "Define input actions for Teleport Select and Cancel",
                "Bake NavMesh if using Teleportation Areas"
            ],
            Category.Unreal: [
                "Use Server RPCs for authoritative gameplay",
                "Replicate only what’s needed to reduce bandwidth",
                "Test with different network emulation settings"
            ],
            Category.Shader: [
                "Mind platform-specific depth ranges and precision",
                "Avoid branching in hot paths; prefer step/smoothstep",
                "Profile on target device (mobile vs desktop)"
            ],
            Category.General: [
                "Keep tasks small and testable",
                "Document assumptions and references",
                "Automate builds as early as possible"
            ],
        }
        gotchas_map = {
            Category.Unity: [
                "NullReferenceException if TeleportationProvider is not assigned",
                "Input mappings must match the XR Interaction default actions"
            ],
            Category.Unreal: [
                "For LAN tests, ensure firewall allows UE editor",
                "Remember to set Net Mode to Play As Client/Server in PIE"
            ],
            Category.Shader: [
                "Depth textures can be reversed (0..1 vs 1..0) depending on API",
                "AR pipelines may require special camera feed sampling"
            ],
            Category.General: [
                "Ambiguous requirements slow you down",
                "Premature optimization can hide bugs"
            ],
        }
        resp = CodeXRResponse(
            category=category.value,
            subtasks=subtasks_map[category],
            code=code_map[category],
            best_practices=best_practices_map[category],
            gotchas=gotchas_map[category],
            difficulty="medium",
            docs=example_docs(category),
            raw={"note": "demo content only — will be replaced by LLM + grounded docs in later steps"}
        )
        return resp
