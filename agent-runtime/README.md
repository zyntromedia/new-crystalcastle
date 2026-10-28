🚀 ZyntroAI — คู่มือการพัฒนา Agent แบบกำหนดเอง
 
yaml  
---
title: 🛠️ คู่มือการพัฒนา Agent แบบกำหนดเอง — ZyntroAI
aliases:
  - Custom Agent Development
  - พัฒนา AI Agent ด้วย LangGraph
tags:
  - type/guide
  - zyntroai
  - advanced
  - agent-development
created: 2026-10-12T13:31:00+07:00
---
 
 
 
 
📑 สารบัญ
 
- 10.1 แนวคิดพื้นฐานของ Agent
- 10.2 โครงสร้างไฟล์ของ Agent
- 10.3 เขียน Agent แบบพื้นฐาน
- 10.4 การใช้เครื่องมือ (Tools)
- 10.5 การสร้าง Validator Layer
- 10.6 ทดสอบและดีบัก Agent
- 10.7 นำไปใช้งานจริง
- 10.8 แม่แบบ Agent พร้อมใช้งาน
 
 
 
10.1 แนวคิดพื้นฐานของ Agent
 
🧠 Agent คืออะไรในบริบทของ ZyntroAI?
 
Agent = สถานะ + ความรู้ + เครื่องมือ + ตรรกะการตัดสินใจ
 
ไม่ใช่แค่เรียก LLM ตอบกลับ แต่สามารถ วางแผน → เลือกเครื่องมือ → ปฏิบัติ → ตรวจสอบ → ปรับแผนใหม่ ได้ด้วยตัวเอง
 
🔄 วงจรชีวิตของ Agent ทุกประเภท
 
plaintext  
📥 รับคำขอจากผู้ใช้
    ↓
🧠 วิเคราะห์: ต้องทำอะไรบ้าง?
    ↓
📋 วางแผน: ขั้นตอนอะไรบ้าง?
    ↓
🔧 ปฏิบัติ: เรียกใช้เครื่องมือ/ค้นหา/อ่านไฟล์
    ↓
✅ ตรวจสอบ: ผลลัพธ์ถูกต้องไหม?
    ↓
    ├ ✅ ถ้าถูกต้อง → 📤 ส่งผลลัพธ์ + บันทึกความรู้
    └ ❌ ถ้าไม่ถูกต้อง → 🔄 ปรับแผนใหม่ → กลับไปวางแผน
 
 
📦 ส่วนประกอบที่ต้องเขียน
 
ส่วน หน้าที่ 
State (สถานะ) ข้อมูลที่ส่งผ่านระหว่างขั้นตอน 
Nodes (โหนด) ฟังก์ชันแต่ละขั้นตอนการทำงาน 
Edges (เส้นเชื่อม) กฎการไหล — จะไปขั้นตอนถัดไปหรือวนกลับ 
Tools (เครื่องมือ) ฟังก์ชันที่ Agent เรียกใช้ได้ 
Validator ตรวจสอบคุณภาพก่อนส่งผลลัพธ์ 
 
 
 
10.2 โครงสร้างไฟล์ของ Agent
 
plaintext  
agent-runtime/
├── agents/
│   ├── __init__.py
│   ├── base.py              # คลาสพื้นฐานของทุก Agent
│   ├── research_agent.py    # ตัวอย่าง: Agent รวบรวมข้อมูล
│   ├── writer_agent.py      # ตัวอย่าง: Agent เขียนเนื้อหา
│   └── custom_agent.py      # ← Agent แบบกำหนดเองของคุณ
├── tools/
│   ├── __init__.py
│   ├── vault_tools.py       # เครื่องมืออ่าน/เขียนโน้ต
│   ├── search_tools.py      # เครื่องมือค้นหา
│   └── file_tools.py        # เครื่องมือจัดการไฟล์
├── state.py                 # คำนิยามสถานะร่วมกัน
├── config.py                # การตั้งค่า
└── main.py                  # จุดเริ่มต้นเรียกใช้ Agent
 
 
 
 
10.3 เขียน Agent แบบพื้นฐาน
 
📄 ขั้นที่ 1: กำหนด State (สถานะ)
 
สร้างไฟล์  state.py :
 
python  
from typing import TypedDict, List, Optional
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    """สถานะที่ส่งผ่านทุกขั้นตอนของ Agent"""
    # คำขอจากผู้ใช้
    user_query: str
    
    # ข้อมูลที่รวบรวม
    context_notes: List[str]
    
    # ผลลัพธ์
    draft_output: Optional[str]
    final_output: Optional[str]
    
    # ข้อมูลอ้างอิง
    sources: List[dict]
    
    # สถานะการตรวจสอบ
    review_comments: List[str]
    needs_revision: bool = False
 
 
📄 ขั้นที่ 2: สร้าง Agent พื้นฐาน
 
สร้างไฟล์  agents/custom_agent.py :
 
python  
from typing import Literal
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from state import AgentState
from tools.vault_tools import search_notes, read_note

class CustomKnowledgeAgent:
    """Agent แบบกำหนดเอง — ค้นหาและสรุปความรู้จากคลังความรู้"""
    
    def __init__(self, llm):
        self.llm = llm
        self.graph = self._build_graph()
    
    # ─── Nodes: แต่ละขั้นตอนการทำงาน ───
    
    def analyze_request(self, state: AgentState):
        """วิเคราะห์คำขอ: ต้องการอะไร ต้องหาข้อมูลอะไร"""
        system_prompt = """
        คุณเป็นผู้ช่วยวิเคราะห์คำขอ ระบุว่าผู้ใช้ต้องการทราบหัวข้ออะไร 
        และต้องค้นหาข้อมูลเพิ่มเติมหรือไม่
        ตอบในรูปแบบ JSON เท่านั้น: {"topic": "...", "needs_search": true/false}
        """
        
        response = self.llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=state["user_query"])
        ])
        
        # ในทางปฏิบัติควร parse JSON ที่นี่
        return {"user_query": state["user_query"]}
    
    def gather_context(self, state: AgentState):
        """ค้นหาข้อมูลที่เกี่ยวข้องจากคลังความรู้"""
        query = state["user_query"]
        
        # ใช้เครื่องมือค้นหาโน้ต
        results = search_notes(query, limit=5)
        
        # อ่านเนื้อหาแต่ละโน้ต
        context = []
        sources = []
        for path, metadata in results:
            content = read_note(path)
            context.append(content)
            sources.append({"path": path, "title": metadata.get("title", "")})
        
        return {
            "context_notes": context,
            "sources": sources
        }
    
    def generate_response(self, state: AgentState):
        """สร้างผลลัพธ์จากข้อมูลที่รวบรวมได้"""
        context = "\n\n---\n\n".join(state["context_notes"])
        query = state["user_query"]
        
        prompt = f"""
        คำถาม: {query}
        
        ข้อมูลที่มี:
        {context}
        
        คำแนะนำ:
        1. ตอบตามข้อมูลที่ให้มาเท่านั้น
        2. ถ้าข้อมูลไม่พอ ให้แจ้งอย่างชัดเจน
        3. อ้างอิงแหล่งที่มา
        """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        return {"draft_output": response.content}
    
    def review_output(self, state: AgentState):
        """ตรวจสอบผลลัพธ์ก่อนส่งให้ผู้ใช้"""
        draft = state["draft_output"]
        
        # เรียกใช้ Validator Layer
        review_prompt = f"""
        ตรวจสอบเนื้อหานี้:
        {draft}
        
        ตรวจสอบ:
        - ถูกต้องตามข้อมูลหรือไม่
        - ชัดเจนและเข้าใจง่ายไหม
        - มีข้อมูลที่ไม่ควรแชร์ไหม
        
        ตอบในรูปแบบ JSON:
        {{
          "approved": true/false,
          "comments": "...",
          "needs_revision": true/false
        }}
        """
        
        review = self.llm.invoke([HumanMessage(content=review_prompt)])
        
        # ตรวจสอบง่ายๆ ในตัวอย่างนี้
        approved = len(draft) > 10 and "ไม่มีข้อมูล" not in draft
        return {
            "final_output": draft if approved else "ขออภัย ไม่พบข้อมูลที่เพียงพอ",
            "review_comments": ["ตรวจสอบแล้ว"],
            "needs_revision": not approved
        }
    
    # ─── Edges: กฎการไหล ───
    
    def should_continue(self, state: AgentState) -> Literal["gather_context", "generate_response"]:
        """ตัดสินใจว่าต้องค้นหาข้อมูลเพิ่มหรือไม่"""
        if state.get("context_notes"):
            return "generate_response"
        return "gather_context"
    
    def should_revise(self, state: AgentState) -> Literal["generate_response", END]:
        """ตัดสินใจว่าต้องแก้ไขหรือเสร็จสิ้น"""
        if state.get("needs_revision"):
            return "generate_response"
        return END
    
    # ─── ประกอบเข้าด้วยกัน ───
    
    def _build_graph(self):
        graph = StateGraph(AgentState)
        
        # เพิ่มโหนด
        graph.add_node("analyze", self.analyze_request)
        graph.add_node("gather_context", self.gather_context)
        graph.add_node("generate", self.generate_response)
        graph.add_node("review", self.review_output)
        
        # กำหนดจุดเริ่มต้น
        graph.set_entry_point("analyze")
        
        # เชื่อมโหนด
        graph.add_edge("analyze", "gather_context")
        graph.add_edge("gather_context", "generate")
        graph.add_edge("generate", "review")
        
        # เส้นทางแบบมีเงื่อนไข
        graph.add_conditional_edges(
            "review",
            self.should_revise,
            {
                "generate_response": "generate",
                END: END
            }
        )
        
        return graph.compile()
    
    # ─── เรียกใช้งาน ───
    
    def run(self, query: str):
        """เรียกใช้ Agent ด้วยคำถาม"""
        result = self.graph.invoke({
            "user_query": query,
            "context_notes": [],
            "sources": [],
            "review_comments": []
        })
        return result
 
 
 
 
10.4 การใช้เครื่องมือ (Tools)
 
📄 สร้างเครื่องมือใหม่
 
สร้างไฟล์  tools/custom_tools.py :
 
python  
from langchain_core.tools import tool
from typing import Optional, List, Dict
import os

@tool
def search_vault(query: str, limit: int = 5) -> List[Dict]:
    """
    ค้นหาโน้ตในคลังความรู้
    
    Args:
        query: คำที่ต้องการค้นหา
        limit: จำนวนผลลัพธ์ที่ต้องการ
    
    Returns:
        รายการผลลัพธ์ที่ตรงกับคำค้นหา
    """
    # ใส่ตรรกะการค้นหาจริงที่นี่
    results = []
    vault_path = os.getenv("VAULT_PATH", "./ZyntroAI-Vault")
    
    # ตัวอย่าง: ค้นหาไฟล์ที่มีคำอยู่
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md") and len(results) < limit:
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        results.append({
                            "path": full_path,
                            "title": file.replace(".md", ""),
                            "snippet": content[:100] + "..."
                        })
    return results

@tool
def save_note(title: str, content: str, folder: str = "Research") -> str:
    """
    บันทึกเนื้อหาเป็นโน้ตใหม่ในคลังความรู้
    
    Args:
        title: ชื่อโน้ต
        content: เนื้อหาโน้ต
        folder: โฟลเดอร์ที่ต้องการบันทึก
    
    Returns:
        ข้อความยืนยันผลการบันทึก
    """
    vault_path = os.getenv("VAULT_PATH", "./ZyntroAI-Vault")
    target_folder = os.path.join(vault_path, folder)
    os.makedirs(target_folder, exist_ok=True)
    
    # ทำให้ชื่อไฟล์ปลอดภัย
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).strip()
    file_path = os.path.join(target_folder, f"{safe_title}.md")
    
    # เขียนเนื้อหาพร้อม YAML Frontmatter
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"""---
title: {title}
type: note
created: 2026-10-12
source: AI Agent
---

{content}
""")
    
    return f"✅ บันทึกสำเร็จ: {file_path}"
 
 
📄 วิธีให้ Agent ใช้เครื่องมือ
 
python  
# ใน Agent __init__
from tools.custom_tools import search_vault, save_note

# รวมเครื่องมือเข้ากับ LLM
tools = [search_vault, save_note]
self.llm_with_tools = self.llm.bind_tools(tools)
 
 
 
 
10.5 การสร้าง Validator Layer
 
📄 ทำไมต้องมี?
 
ก่อนส่งผลลัพธ์ให้ผู้ใช้ ต้องตรวจสอบ:
 
- ✅ ข้อมูลถูกต้องไหม?
- ✅ ไม่มีข้อมูลลับรั่วไหลไหม?
- ✅ อยู่ในขอบเขตที่อนุญาตไหม?
 
📄 สร้าง Validator
 
สร้างไฟล์  validators/output_validator.py :
 
python  
from typing import Tuple, List
import re

class OutputValidator:
    """ตรวจสอบความปลอดภัยและคุณภาพของผลลัพธ์ Agent"""
    
    # รูปแบบข้อมูลที่ไม่อนุญาตให้แสดง
    PATTERNS_BLOCKED = [
        # ข้อมูลส่วนตัว
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # อีเมล
        r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',  # IP Address
        r'\b[0-9]{13}\b',  # เลขบัตรประชาชน
        
        # คำต้องห้าม
        r'password\s*=',
        r'api[_-]?key\s*=',
        r'secret\s*=',
    ]
    
    # คำเตือนที่ควรตรวจสอบ
    WARNING_KEYWORDS = [
        "ฉันไม่แน่ใจ", "อาจจะ", "ไม่แน่นอน", "คิดว่า", "เดาว่า"
    ]
    
    @classmethod
    def validate(cls, content: str) -> Tuple[bool, List[str]]:
        """
        ตรวจสอบเนื้อหา
        คืนค่า: (ผ่านไหม?, รายการข้อผิดพลาด/คำเตือน)
        """
        issues = []
        
        # ตรวจสอบข้อมูลที่ละเอียดอ่อน
        for pattern in cls.PATTERNS_BLOCKED:
            matches = re.findall(pattern, content)
            if matches:
                issues.append(f"⚠️ พบรูปแบบข้อมูลที่อาจเป็นความลับ: {matches[0]}")
        
        # ตรวจสอบความมั่นใจ
        for word in cls.WARNING_KEYWORDS:
            if word in content:
                issues.append(f"ℹ️ พบคำที่ลดความน่าเชื่อถือ: '{word}'")
        
        # ตรวจสอบความยาวขั้นต่ำ
        if len(content.strip()) < 10:
            issues.append("⚠️ เนื้อหาสั้นเกินไป อาจไม่มีข้อมูลที่เป็นประโยชน์")
        
        is_valid = len([i for i in issues if i.startswith("⚠️")]) == 0
        return is_valid, issues
 
 
📄 นำไปใช้งานใน Agent
 
python  
from validators.output_validator import OutputValidator

# ในส่วน review_output
is_valid, issues = OutputValidator.validate(draft)

if not is_valid:
    return {
        "final_output": "⚠️ ขออภัย ไม่สามารถแสดงเนื้อหานี้ได้",
        "review_comments": issues,
        "needs_revision": True
    }
 
 
 
 
10.6 ทดสอบและดีบัก Agent
 
📄 เขียนไฟล์ทดสอบ
 
สร้างไฟล์  test_agent.py :
 
python  
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from agents.custom_agent import CustomKnowledgeAgent

load_dotenv()

# เริ่มต้น LLM
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0.3
)

# สร้าง Agent
agent = CustomKnowledgeAgent(llm)

# ทดสอบ
if __name__ == "__main__":
    print("🤖 ทดสอบ Custom Knowledge Agent")
    print("─" * 50)
    
    queries = [
        "อธิบายความแตกต่างระหว่าง AI กับ Machine Learning",
        "สรุปหลักการของ Atomic Note ให้เข้าใจง่าย"
    ]
    
    for q in queries:
        print(f"\n📥 ถาม: {q}")
        result = agent.run(q)
        print(f"📤 ตอบ: {result.get('final_output', 'ไม่มีคำตอบ')}")
        if result.get("sources"):
            print(f"📚 แหล่งที่มา: {len(result['sources'])} แหล่ง")
        print("─" * 50)
 
 
รันด้วย:
 
bash  
python test_agent.py
 
 
🐛 เคล็ดลับการดีบัก
 
- ✅ เพิ่ม  print()  หรือใช้  logging  ในแต่ละ Node เพื่อดูค่าที่ส่งผ่าน
- ✅ เรียกใช้ทีละ Node ไม่ต้องรันทั้งหมดในครั้งเดียว
- ✅ ลดความซับซ้อน: เริ่มจาก 2 Node ก่อน แล้วค่อยเพิ่ม
- ✅ ใช้โมเดลที่เร็วและราคาถูกตอนพัฒนา เช่น  gpt-4o-mini 
 
 
 
10.7 นำไปใช้งานจริง
 
📄 ลงทะเบียน Agent ให้ระบบรู้จัก
 
อัปเดตไฟล์  agents/__init__.py :
 
python  
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
 
 
📄 เพิ่มคำอธิบายในคลังความรู้
 
สร้างโน้ต  🤖 AI Agents/Custom-Knowledge-Agent.md :
 
markdown  
---
title: Custom Knowledge Agent
type: agent
description: ค้นหาและตอบคำถามจากคลังความรู้ภายในของเราเอง
tools: search_vault, save_note
validator: OutputValidator
---

# 🤖 Custom Knowledge Agent

## หน้าที่
ค้นหาข้อมูลจากโน้ตภายในคลังความรู้ สรุปและตอบคำถามโดยอ้างอิงแหล่งที่มา

## ขั้นตอนการทำงาน
1. วิเคราะห์คำขอ
2. ค้นหาโน้ตที่เกี่ยวข้อง
3. รวบรวมเนื้อหา
4. สร้างคำตอบ
5. ตรวจสอบความถูกต้อง
6. บันทึกผลลัพธ์ (ถ้าต้องการ)

## ขอบเขต
- ✅ ใช้ได้กับทุกโน้ตในคลังความรู้
- ✅ อ้างอิงแหล่งที่มาทุกครั้ง
- ❌ ไม่ตอบคำถามที่ไม่มีข้อมูลในคลัง
 
 
 
 
10.8 แม่แบบ Agent พร้อมใช้งาน
 
เลือกแม่แบบที่เหมาะกับความต้องการ แล้วปรับแต่ง:
 
ประเภท Agent กรณีใช้งานจริง ความยาก 
📝 Summary Agent รับไฟล์/ลิงก์ → สรุปเป็น Atomic Note ⭐ เริ่มต้น 
🔍 Search Agent ค้นหาข้อมูลภายนอก → สรุป + อ้างอิง ⭐⭐ ปานกลาง 
✍️ Writer Agent รับโจทย์ → ร่างเนื้อหา → ตรวจสอบ → ปรับปรุง ⭐⭐ ปานกลาง 
🧠 Analysis Agent รับข้อมูล → วิเคราะห์ → หาข้อสังเกต/รูปแบบ ⭐⭐⭐ ขั้นสูง 
📊 Report Agent ดึงข้อมูลหลายแห่ง → รวมเป็นรายงานสรุป ⭐⭐⭐ ขั้นสูง 
 
 
 
📋 เช็คลิสต์พัฒนา Agent
 
กำหนดวัตถุประสงค์และขอบเขตของ Agent ให้ชัดเจน ✅
ออกแบบ State — ข้อมูลอะไรที่ต้องส่งผ่าน ✅
เขียน Node แต่ละขั้นตอนทีละส่วน ✅
กำหนดกฎการไหล (Edges) ให้ชัดเจน ✅
สร้างเครื่องมือที่จำเป็นเท่าที่พอใช้ ✅
เพิ่ม Validator Layer ✅
เขียนเคสทดสอบครอบคลุม ✅
บันทึกเอกสารการใช้งานในคลังความรู้ ✅
ทดสอบกับผู้ใช้จริงและปรับปรุง ✅
 
 
 
ต้องการแม่แบบ Agent ประเภทไหนเพิ่มไหมครับ เช่น Agent วิเคราะห์ข้อมูล, Agent รายงาน, หรือ Agent ตรวจสอบคุณภาพเอกสาร 😊