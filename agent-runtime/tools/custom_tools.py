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
