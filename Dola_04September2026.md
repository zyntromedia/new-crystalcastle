🚀 พร้อมแล้วครับ! รวมทั้งชุด — PR Description + ไฟล์ครบถ้วน + ยื่น Marketplace ได้เลย 🔥
 
 
 
📋 Pull Request Description — Copy → Paste ได้เลย
 
markdown
  
# ✅ Dola AI — GitHub Marketplace Release Prep: Safety + Pricing + 1-Click Install

## 🎯 Overview
เพิ่ม 3 ฟีเจอร์สำคัญเพื่อเตรียมยื่น GitHub Marketplace — ปลอดภัยขึ้น, มีระบบรายได้, ติดตั้งง่ายสุดๆ

---

## 🆕 What's Added

### 🛡️ 1. Safety Guard — ป้องกันการแก้ไขที่อันตราย
- **ไฟล์: `.dola/safety.yml`** — กฎความปลอดภัยแบบกำหนดเอง
  - ❌ ไม่เคย Auto-Merge ถ้าแตะ DB, Config, Env
  - ⏳ ต้องขออนุญาตก่อน Delete / Billing / Env
  - ✅ Auto-Approve สำหรับแค่ Docs / Typo / Version bump
- **ไฟล์: `dola_fix.py`** — ตรวจสอบก่อน commit ทุกครั้ง
  - อ่านกฎจาก safety.yml → บล็อกถ้าฝ่าฝืน
  - Exit code 1 = บล็อก, 0 = ผ่าน
  - รองรับ path pattern + label + line count

### 💰 2. Pricing System — พร้อมขายจริง
- **ไฟล์: `dashboard/pricing.html`** — หน้าเลือกแผน 3 แบบ
  - **Hobby** — ฟรี · 50 PR/เดือน
  - **Pro** — $29/เดือน · 500 PR + Slack Bot
  - **Team** — $199/เดือน · ไม่จำกัด + Dashboard
- **ไฟล์: `dashboard/pricing.json`** — Backend config เชื่อม Stripe ได้เลย

### ⚙️ 3. 1-Click Install — ติดตั้งง่ายที่สุด
- **ไฟล์: `dola.yml`** — วางที่ root → ทำงานทันที
  - Auto Review / Auto Fix เปิดมาแล้ว
  - Slack Notify + Safety Guard พร้อมใช้
  - ไม่ต้องเขียน GitHub Actions เอง!

---

## ✅ Benefits for GitHub Marketplace
- 🔒 **Reviewer Love** — มี Safety Guard → ไม่กลัว AI พัง production
- 💰 **Monetization Ready** — มีแผนชัดเจน → GitHub ชอบ App ที่สร้างรายได้
- ⚡ **Zero Friction** — วางไฟล์เดียว → ใช้ได้ทันที → ยอดติดตั้งพุ่งแน่นอน

---

## 📁 Files Changed
| File | Change |
|---|---|
| `.dola/safety.yml` | ✅ New — Safety rules config |
| `dola_fix.py` | ✅ New — Pre-commit safety checker |
| `dola.yml` | ✅ New — 1-Click install config |
| `dashboard/pricing.html` | ✅ New — Pricing UI |
| `dashboard/pricing.json` | ✅ New — Pricing backend config |

---

## 🚀 Next Steps
- [ ] Merge this PR → ไปยื่น GitHub Marketplace
- [ ] ติดตั้ง Stripe Webhook → เปิดรับเงินจริง
- [ ] โพสต์ r/github / HackerNews / LinkedIn 📢
- [ ] เดือนหน้า → Linear/Jira Integration

---

**Ready to merge & submit! 🎉**
 
 
 
 
✅ Summary — ทุกอย่างครบแล้วครับ
 
ส่วน ไฟล์ Status 
🛡️ Safety Guard  .dola/safety.yml  +  dola_fix.py  ✅ พร้อม 
💰 Pricing Page  dashboard/pricing.html  +  .json  ✅ พร้อม 
⚙️ 1-Click Install  dola.yml  ✅ พร้อม 
📋 PR Description ด้านบน ↑ ✅ ก๊อปปี้ใช้ได้เลย 
 
 
 
🔥 เตรียมยื่น Marketplace ได้ทันทีครับ! ทั้ง 3 อย่างที่ Reviewer และลูกค้าชอบ — ปลอดภัย, มีราคา, ติดตั้งง่ายสุดๆ โอกาสติด Featured App สูงมาก!
 
ต่อไปต้องการทำอะไรต่อ?
 
- 🔗 เชื่อม Stripe → เปิดรับเงินจริง
- 📢 Post Launch → เขียนโพสต์ r/github + HackerNews
- 📊 Analytics Dashboard → ดูจำนวน users + รายได้
- 🚀 ยื่น Marketplace → พร้อมเลย!
 
บอกได้เลยครับ จัดให้ทันที ⚡
