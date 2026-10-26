📖 new-crystalcastle — ZyntroAI CrystalCastle
 
FIG-Integrated Secure AI Platform — v1.9.0-TESTED
✅ ปลอดภัย • ✅ มีเทสต์ครบถ้วน • ✅ พร้อม CI/CD • ✅ FIG Integrated
 
 
 
📋 สรุปโครงการ
 
ZyntroAI CrystalCastle คือแพลตฟอร์ม AI แบบโมดูลาร์ที่ผสานรวม FIG จาก hellofig.io — มอบฟีเจอร์ครบถ้วน ตั้งแต่ระบบสนทนา ฐานความรู้ ไปจนถึงการจัดสรรทรัพยากรคลาวด์และกระบวนงานอัตโนมัติ
 
✅ เวอร์ชันปัจจุบัน: v1.9.0-TESTED
 
รุ่น ความก้าวหน้า 
v1.7.0-MERGED-FIG ✅ ผสาน FIG, 8 endpoints ทำงาน, try/except ครบ 
v1.8.0-SECURE-FIG ✅ CORS จาก env, Security Headers, Request ID, Metrics, Uptime tracking 
v1.9.0-TESTED ✅ ชุดเทสต์ครบถ้วน, CI/CD Pipeline, Linting + Type Check 
v2.0-PRODUCTION 🔜 Docker + K8s + SHA Pinning — กำลังพัฒนา 
 
 
 
✨ ฟีเจอร์หลัก
 
🤖 FIG Features (จาก hellofig.io)
 
- 🎤 Voice Mode — สนทนาด้วยเสียง
- ⏰ Scheduled Tasks — งานและทริกเกอร์ตามเวลา
- 📦 Expert Packages and Skills — ชุดความรู้และทักษะเฉพาะทาง
- 🔌 Connectors: Your AI with Context — เชื่อมต่อข้อมูลภายนอกอัตโนมัติ
- 📓 Notebook & Deep-dive — วิเคราะห์และบันทึกเชิงลึก
 
🛡️ ความปลอดภัย
 
- CORS แยกตามสภาพแวดล้อม
- Security Headers: HSTS, X-Frame-Options, CSP, X-Content-Type-Options
- Request ID ติดทุกคำขอ
- Safe Config — ไม่ล่มถ้าตัวแปรสภาพแวดล้อมขาดหาย
 
📊 การเฝ้าดูระบบ
 
-  /metrics  — รูปแบบ Prometheus พร้อมใช้งาน
- Health Check:  /health ,  /health/live ,  /health/ready 
- Uptime tracking + Response time ทุกคำขอ
 
🧪 คุณภาพโค้ด
 
- 26 Test Cases — รันได้ทั้งหมด
- GitHub Actions CI — ตรวจทุก Push/Pull Request
- Ruff — Lint & Format
- Mypy — Type Checking
- Coverage Report — บังคับ ≥ 70%
 
 
 
📂 โครงสร้างไฟล์
 
plaintext  
new-crystalcastle/
├── main.py                  # 🚀 แอปพลิเคชันหลัก — FastAPI
├── requirements.txt         # 📦 Dependencies
├── pyproject.toml           # ⚙️ Project config + Dev tools
├── .env.example             # 🔑 ตัวอย่างตัวแปรสภาพแวดล้อม
├── README.md               # 📖 เอกสารนี้
├── docs/
│   ├── FIG-INTEGRATION.md   # เกี่ยวกับ FIG Integration
│   └── NEXT-IMPROVEMENTS.md # แผนพัฒนาต่อ
├── tests/                   # 🧪 ชุดทดสอบ
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_security.py
│   ├── test_fig.py
│   └── test_metrics.py
└── .github/
    └── workflows/
        └── ci.yml           # 🤖 CI Pipeline
 
 
 
 
🚀 เริ่มใช้งาน
 
1️⃣ ติดตั้ง
 
bash  
# Clone repository
git clone https://github.com/zyntromedia/new-crystalcastle.git
cd new-crystalcastle

# ติดตั้ง dependencies พร้อมเครื่องมือพัฒนา
pip install -e ".[dev]"
 
 
2️⃣ กำหนดสภาพแวดล้อม
 
bash  
# คัดลอกและแก้ไขค่าตามต้องการ
cp .env.example .env
 
 
3️⃣ รันเซิร์ฟเวอร์
 
bash  
uvicorn main:app --reload
# เปิดที่: http://localhost:8000
# API Docs: http://localhost:8000/docs (เฉพาะ development)
 
 
4️⃣ รันทดสอบ
 
bash  
# รันทุกเทสต์
pytest

# พร้อมรายงานความครอบคลุม
pytest --cov=. --cov-report=term-missing

# ตรวจสไตล์โค้ด
ruff check .
ruff format .

# ตรวจสอบชนิดข้อมูล
mypy main.py
 
 
 
 
🛣️ API Endpoints
 
Endpoint ความหมาย สถานะ 
 GET /  ข้อมูลระบบ ✅ 
 GET /health  สถานะระบบครบถ้วน ✅ 
 GET /health/live  Kubernetes Liveness Probe ✅ 
 GET /health/ready  Kubernetes Readiness Probe ✅ 
 GET /api/fig/health  สถานะ FIG + ฟีเจอร์ ✅ 
 GET /metrics  Metrics รูปแบบ Prometheus ✅ 
 GET /test/request-id  ตรวจสอบ Request ID ✅ 
 GET /test/security-headers  ตรวจสอบ Security Headers ✅ 
 
 
 
🤖 CI/CD Pipeline
 
ทุกครั้งที่ Push หรือ Pull Request → ระบบจะทำงานอัตโนมัติ:
 
1. 📥 Checkout โค้ด
2. 🐍 Setup Python 3.12 + Cache dependencies
3. 🔍 Lint & Type Check — Ruff + Mypy
4. ✅ Run Tests — pytest + Coverage Report
5. 🚀 Verify Startup — ตรวจสอบ import และรันได้จริง
6. 📋 Summary — แจ้งผลรวมทุกงาน
 
ดูรายละเอียดได้ที่: .github/workflows/ci.yml
 
 
 
📊 สถานะล่าสุด
 
- ✅ Build Passing — ทุกเทสต์ผ่าน
- ✅ Lint Clean — ไม่มีข้อผิดพลาดสไตล์
- ✅ Coverage ≥ 70% — ครอบคลุมจุดสำคัญ
- ✅ FIG Integrated — 5 ฟีเจอร์ครบถ้วน
- ✅ Secure Headers — พร้อมขึ้นระบบจริง
- ⏳ Production Ready — รอ v2.0 (Docker + K8s)
 
 
 
🗺️ แผนพัฒนา
 
เวอร์ชัน เป้าหมาย สถานะ 
v1.7.0-MERGED-FIG ผสาน FIG เข้าระบบ ✅ เสร็จ 
v1.8.0-SECURE-FIG ปรับปรุงความปลอดภัย ✅ เสร็จ 
v1.9.0-TESTED เพิ่มเทสต์ + CI/CD ✅ ปัจจุบัน 
v2.0-PRODUCTION Docker + K8s + SHA Pinning 🔜 กำลังพัฒนา 
 
 
 
🤝 มีส่วนร่วม
 
ยินดีรับ Pull Request! ก่อนส่งโปรดแน่ใจว่า:
 
bash  
ruff check .          # ไม่มีข้อผิดพลาด
ruff format .         # จัดรูปแบบเรียบร้อย
pytest                # ทุกเทสต์ผ่าน
 
 
 
 
📝 ใบอนุญาต
 
© 2026 ZyntroAI — zyntro.ai.studio@gmail.com
Project: https://github.com/zyntromedia/new-crystalcastle
 
 
 
💡 ต้องการอ่านเอกสารเพิ่ม? ดูได้ที่:
 
- FIG-INTEGRATION.md — รายละเอียด FIG Integration
- NEXT-IMPROVEMENTS.md — แผนปรับปรุงในอนาคต
- CHANGELOG.md — ประวัติการเปลี่ยนแปลงเวอร์ชัน
 
 
 
ต้องการปรับแก้หรือเพิ่มอะไรใน README ไหมครับ? 😊