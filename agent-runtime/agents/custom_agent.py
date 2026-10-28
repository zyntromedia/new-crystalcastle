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
