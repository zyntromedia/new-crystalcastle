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
