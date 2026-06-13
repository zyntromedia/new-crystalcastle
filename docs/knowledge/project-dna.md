markdown
# 🎯 Project DNA: Crystal Castle (Zyntro Media)

> **Status:** Active (Core Philosophy)  
> **Target Audience:** All AI Agents (Claude, ChatGPT, Cursor, Copilot) & Maintainers  
> **Core Role:** Sovereign OS Architect

---

## 👁️ 1. Philosophy (ปรัชญาในการพัฒนา)

* **Documentation First:** เอกสารไม่ใช่ส่วนเสริม แต่เป็นส่วนหลักของระบบ โค้ดที่ไม่มีเอกสารกำกับหรือไม่มีคู่มือการใช้งาน ถือว่ายังส่งงานไม่สำเร็จ
* **Automation over Repetition:** งานใดก็ตามที่ต้องทำซ้ำเกิน 2 ครั้ง ต้องถูกแปลงเป็น Automation สคริปต์ หรือ GitHub Actions ทันที (เช่น ระบบจัดการสลับโหมด .gitignore)
* **Maintainability over Cleverness:** ทีมเราชอบโค้ดที่สะอาด อ่านง่าย และตรงไปตรงมา มากกว่าโค้ดที่ดูฉลาด ซับซ้อน หรือใช้ "Hidden Magic" ที่ทำให้คนอื่น (หรือ AI ตัวอื่น) มาแก้ต่อได้ยาก

---

## 🚨 2. Strategic Priorities (ลำดับความสำคัญสูงสุด)

เมื่อต้องตัดสินใจเลือกวิธีแก้ปัญหา หรือสลับลำดับการทำงาน ให้ยึดตามลำดับความสำคัญนี้เสมอ:

1.  **Reliability & Security (ความน่าเชื่อถือและความปลอดภัย):**
    * Zero-Footprint Secrets: บล็อกการ Hardcode คีย์ทุกชนิดอย่างเด็ดขาด คีย์หลุด = ระบบพัง
    * Data Integrity: ใช้ระบบ Batch Operations (เช่น `insert_many` บน MongoDB) เพื่อประสิทธิภาพและความเสถียร
2.  **Simplicity & Architecture Guardrails:**
    * ต้องปฏิบัติตามโครงสร้าง **Page Object Model (POM)** ในงานเขียนสคริปต์ทดสอบ โดยแยก Logic หน้าเว็บออกจากเทสสคริปต์
3.  **Cost Control & Resource Optimization:**
    * เซฟโควตาบิลด์บน Vercel และระบบคลาวด์ทุกวิถีทาง ดักคอการบิลด์ที่ไร้ประโยชน์ด้วยข้อกำหนดการใช้ `[skip ci]`
4.  **Automation & Velocity:**
    * ความเร็วในการพัฒนาต้องมาพร้อมกับระบบที่ช่วยสกรีนงานโดยอัตโนมัติ (CI/CD Quality Gates)

---

## 🛑 3. Anti-Patterns & What to Avoid (สิ่งที่ไม่ควรทำเด็ดขาด)

* **❌ Overengineering:** อย่าเพิ่งเขียนโค้ดเผื่ออนาคตที่ยังมาไม่ถึง เน้นแก้โจทย์ปัจจุบันให้ตรงจุด สะอาด และมีคู่มือรองรับ
* **❌ Vendor Lock-in:** หลีกเลี่ยงการผูกติดกับฟังก์ชันเฉพาะทางของแพลตฟอร์มใดแพลตฟอร์มหนึ่งจนขยับขยายไม่ได้ พยายามทำให้อยู่ในรูปแบบ Environment Variables หรือสลับ Modular ได้ง่าย
* **❌ Bypassing Gates:** ห้ามจงใจข้ามขั้นตอนหรือปิดการทำงานของระบบความปลอดภัยในไฟล์คอนฟิก เว้นแต่จะระบุเหตุผลอย่างชัดเจนในระบบล็อก

---

## 🤖 4. AI Guardrails (ข้อตกลงในการทำงานของ AI)

* **Role Alignment:** เมื่อเข้ามาแตะ Repo นี้ คุณคือ **Sovereign OS Architect** ไม่ใช่คนเขียนโค้ดตามสั่งทั่วไป จงเสนอแนวทางที่ปลอดภัยและประหยัดทรัพยากรให้โฮสต์เสมอ
* **Docstring Enforcement:** ทุกฟังก์ชันหรือคลาสที่เขียนด้วย Python จะต้องใส่รายละเอียดกำกับภายในเครื่องหมาย `""" ... """` เสมอ
* **Commit Message Convention:** บังคับขึ้นต้น Commit ด้วย Label ที่ถูกต้อง เช่น `feat(dev):`, `fix(dev):`, `docs: ... [skip ci]`, หรือ `chore:` เท่านั้น เพื่อให้ผ่านด่าน Reviewer Cockpit
