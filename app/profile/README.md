---
title: Profile Module
version: 1.0.0
status: active
category: module
tags:
  - profile
  - user
  - management
created: 2026-10-04
---

# 👤 Profile Module

จัดการข้อมูลสาธารณะของผู้ใช้ — ชื่อ, ประวัติ, รูปประจำตัว

## 📋 Endpoints

| วิธี | เส้นทาง | หน้าที่ |
|---|---|---|
| `GET` | `/profile/{user_id}` | ดึงข้อมูลโปรไฟล์ |
| `POST` | `/profile/` | สร้างโปรไฟล์ใหม่ |
| `PATCH` | `/profile/{user_id}` | แก้ไขบางส่วน |

## 📐 โครงสร้างข้อมูล
- `user_id` — รหัสอ้างอิงจากระบบสมาชิก
- `display_name` — ชื่อที่แสดงต่อสาธารณะ
- `bio` — ข้อความแนะนำตัว
- `avatar_url` — ลิงก์รูปภาพ
- `created_at` / `updated_at` — เวลาอ้างอิง
