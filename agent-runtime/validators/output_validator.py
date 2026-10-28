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
