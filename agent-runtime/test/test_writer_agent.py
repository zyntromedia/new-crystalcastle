from agents.writer_agent import WriterAgent


def mock_llm_func(prompt: str) -> str:
    """
    Mock LLM สำหรับทดสอบเท่านั้น
    """
    if "สร้างโครงร่าง" in prompt or "โครงร่าง" in prompt:
        return """
# โครงร่าง
## บทนำ
## เนื้อหาหลัก
## บทสรุป
"""
    if "เขียนร่าง" in prompt or "ร่างเต็ม" in prompt:
        return """
# บทนำ
นี่คือร่างเนื้อหาตัวอย่าง

## เนื้อหาหลัก
- จุดที่ 1
- จุดที่ 2

## บทสรุป
นี่คือบทสรุป
"""
    if "แก้ไข" in prompt or "Revise" in prompt:
        return """
# บทนำ (แก้ไขแล้ว)
นี่คือร่างที่ผ่านการปรับปรุง

## เนื้อหาหลัก
- จุดที่ 1 ปรับชัดเจนขึ้น
- จุดที่ 2 ปรับชัดเจนขึ้น

## บทสรุป
นี่คือบทสรุปที่สมบูรณ์ขึ้น
"""
    return "ตอบกลับตัวอย่าง"


def test_writer_agent():
    agent = WriterAgent(
        llm_func=mock_llm_func,
        max_iterations=2
    )

    result = agent.run(
        prompt="เขียน Obsidian Note เกี่ยวกับ DevSecOps Basics",
        context_notes=[
            "DevSecOps = Security Shift Left",
            "CI/CD คือส่วนสำคัญ"
        ]
    )

    print("Status:", result.status)
    print("Outline:", result.outline)
    print("Final Output:", result.final_output)
    print("Validation Errors:", result.validation_errors)


if __name__ == "__main__":
    test_writer_agent()
