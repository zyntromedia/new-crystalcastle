from typing import Callable


def create_outline(prompt: str, context: List[str], llm_func: Callable[[str], str]) -> str:
    """
    เครื่องมือ: สร้างโครงร่างเนื้อหา
    """
    context_block = "\n".join([f"- {note}" for note in context]) if context else "ไม่มีบริบทเพิ่มเติม"

    prompt_text = f"""
คุณเป็นนักเขียนโครงร่างมืออาชีพ
โจทย์:
{prompt}

บริบทที่มีอยู่:
{context_block}

ให้สร้างโครงร่างที่ชัดเจน มีหัวข้อหลัก + หัวข้อย่อย
อย่าเขียนเนื้อหาเต็มทันที
"""
    return llm_func(prompt_text)


def write_draft(outline: str, prompt: str, context: List[str], llm_func: Callable[[str], str]) -> str:
    """
    เครื่องมือ: เขียนร่างเต็มตามโครงร่าง
    """
    context_block = "\n".join([f"- {note}" for note in context]) if context else "ไม่มีบริบทเพิ่มเติม"

    prompt_text = f"""
คุณเป็นนักเขียนเนื้อหา
โจทย์:
{prompt}

โครงร่าง:
{outline}

บริบท:
{context_block}

ให้เขียนร่างเต็มตามโครงร่าง
รักษาโทนให้เหมาะสมกับคลังความรู้ / Obsidian Note
"""
    return llm_func(prompt_text)


def revise_draft(draft: str, validation_notes: List[str], llm_func: Callable[[str], str]) -> str:
    """
    เครื่องมือ: ปรับแก้ร่างตาม Validation Notes
    """
    notes_block = "\n".join([f"- {note}" for note in validation_notes]) if validation_notes else "ไม่มีข้อเสนอแนะเพิ่มเติม"

    prompt_text = f"""
คุณเป็นนักแก้ไขเนื้อหา
ร่างเดิม:
{draft}

ข้อเสนอแนะจาก Validator:
{notes_block}

ให้แก้ไขร่างให้ดีขึ้น
รักษาโครงสร้างเดิม
"""
    return llm_func(prompt_text)
