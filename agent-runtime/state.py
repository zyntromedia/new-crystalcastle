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
