---

## 📄 Document 4: `localizer/README.md`

```markdown
# 🌍 Localized Tools — AgentTools/Localizer
> **Primary Function:** Automatic regional adaptation — currency, language, formats, and data sources

## 📌 Purpose
Ensure agents communicate and operate correctly regardless of region — automatically adapting formats, units, language, and reference data without manual configuration.

## ✨ Key Features
- **Language Adaptation:** Switch interface/output language automatically
- **Format Conversion:** Dates, time, addresses, phone numbers, measurement units
- **Currency Handling:** Auto‑convert display values; preserve original values internally
- **Regional Data Routing:** Use correct local regulations, holidays, time zones
- **Standardization Layer:** Convert all regional inputs to a canonical internal format for consistency

## 🔄 Conversion Flow
Input (Local Format)  →  [Localizer]  →  Standard Internal Format
↓
Response (Standard)  ←  [Localizer]  ←  Processing
↳ Converted back to requester's region format
## 📐 Supported Adaptations
| Category | From → To Examples |
|---|---|
| **Dates** | MM/DD/YYYY ↔ DD/MM/YYYY ↔ YYYY‑MM‑DD |
| **Time** | 12‑hour ↔ 24‑hour format |
| **Currency** | USD → THB → SGD (display only; preserve base value) |
| **Units** | Miles ↔ Kilometers, lbs ↔ kg, °F ↔ °C |
| **Numbers** | Decimal/comma separators |
| **Addresses** | Local postal format standards |

**Status:** ✅ Integrated into Core