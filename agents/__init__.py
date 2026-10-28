from .custom_agent import CustomKnowledgeAgent
from .research_agent import ResearchAgent
from .writer_agent import WriterAgent

AVAILABLE_AGENTS = {
    "research": ResearchAgent,
    "writer": WriterAgent,
    "knowledge": CustomKnowledgeAgent,  # ✅ เพิ่ม Agent ของคุณ
}

def get_agent(name: str, llm):
    """เรียกใช้ Agent ตามชื่อ"""
    agent_class = AVAILABLE_AGENTS.get(name.lower())
    if not agent_class:
        raise ValueError(f"ไม่พบ Agent ชื่อ: {name}")
    return agent_class(llm)
