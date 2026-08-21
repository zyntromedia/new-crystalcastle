```markdown
# Contributing to New Crystal Castle

ยินดีต้อนรับสู่การมีส่วนร่วมในโปรเจค New Crystal Castle!  
เรายินดีรับ contribution ทุกรูปแบบ ไม่ว่าจะเป็น bug report, feature request, documentation หรือ code contribution

---

## 🚀 การตั้งค่า Environment

### ความต้องการเบื้องต้น
- [Node.js](https://nodejs.org/) เวอร์ชัน 18 ขึ้นไป
- [npm](https://www.npmjs.com/) หรือ [yarn](https://yarnpkg.com/)
- [Git](https://git-scm.com/)

### ขั้นตอนการติดตั้ง
1. Fork repository นี้ไปยัง GitHub account ของคุณ
2. Clone repository ที่ fork มาเครื่อง:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/new-crystalcastle.git
   cd new-crystalcastle
   ```

3. ติดตั้ง dependencies:
   
```bash
   npm install
   ```

4. รัน dev server:
   
```bash
   npm run dev
   ```

---

🌿 ขั้นตอนการ Contribute

1. สร้าง Branch ใหม่

```bash
git checkout -b feature/ชื่อ-feature-ของคุณ
# หรือ
git checkout -b fix/ชื่อ-bug-ที่แก้
```

2. Commit Changes
เขียน commit message ให้ชัดเจน ตาม [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add new crystal rendering engine"
git commit -m "fix: resolve login redirect issue"
```

3. Push และสร้าง Pull Request

```bash
git push origin feature/ชื่อ-feature-ของคุณ
```

จากนั้นไปที่ GitHub และสร้าง Pull Request เข้า `main` branch

---

📋 มาตรฐานการเขียนโค้ด

- ใช้ ESLint และ Prettier ที่ตั้งค่าไว้ในโปรเจค
- เขียน JSDoc สำหรับฟังก์ชันที่ซับซ้อน
- ตรวจสอบให้แน่ใจว่าโค้ดรันผ่านก่อน push:
  
```bash
  npm run lint
  npm run build
  ```

- หากแก้ไข UI กรุณาแนบ screenshot ใน Pull Request

---

🐛 การรายงาน Bug

กรุณาเปิด Issue ใหม่และระบุรายละเอียดดังนี้:
- หัวข้อ: สรุปปัญหาสั้นๆ
- รายละเอียด: อธิบายพฤติกรรมที่เกิดขึ้น vs ที่คาดหวัง
- ขั้นตอนการ reproduce: ทำตามขั้นตอนไหนถึงเจอบั๊ก
- Environment: OS, Browser, Node version
- Screenshot/Video: ถ้ามี

---

✨ การเสนอ Feature

เปิด Issue ใหม่และติดแท็ก `enhancement` พร้อมอธิบาย:
- ทำไม feature นี้จึงมีประโยชน์
- Use case ที่ชัดเจน
- ไอเดียการ implement เบื้องต้น (ถ้ามี)

---

🤝 Code of Conduct

ผู้มีส่วนร่วมทุกคนต้องปฏิบัติตามหลักเกณฑ์ต่อไปนี้:
- ให้เกียรติและเคารพซึ่งกันและกัน
- ยอมรับ feedback อย่างสร้างสรรค์
- มุ่งเน้นประโยชน์ของชุมชนและโปรเจค

---

❓ มีคำถาม?

หากมีข้อสงสัย สามารถเปิด Discussion ใน repository นี้ หรือติดต่อทีมผู้พัฒนาได้

---

ขอบคุณที่สนใจมีส่วนร่วมในการพัฒนา New Crystal Castle! 🏰✨

```

---

### 💡 คำแนะนำเพิ่มเติม

หากต้องการให้เอกสารสมบูรณ์ยิ่งขึ้น คุณอาจเพิ่มส่วนเหล่านี้:
- **Testing Guide** – หากมี test suite (`npm test`)
- **Architecture Overview** – อธิบายโครงสร้าง `src/` สั้นๆ
- **Release Process** – หากมี versioning ที่ชัดเจน

ต้องการให้ปรับแต่งส่วนไหนเพิ่มเติมไหมครับ? เช่น เพิ่มส่วนการเขียน test, กฎการตั้งชื่อ branch, หรือ template สำหรับ PR?
