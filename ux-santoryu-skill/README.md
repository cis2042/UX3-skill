# UX 三刀流 — AI 產品體驗設計知識庫

## 這是什麼？

這是一份供 AI 使用的「設計知識 Skill」，萃取自 **UX 三刀流產品體驗設計課程**（共 40 堂課），重新依照設計師在實務中會遇到的問題情境組織，讓 AI 能夠在你提問時，快速調用正確的設計知識來協助你。

---

## 核心理念

UX 三刀流主張：產品體驗設計不能只看使用者，必須同時掌握三把刀：

| 刀 | 能力 | 關注 |
|---|---|---|
| 🗡 用戶流 | 使用者需求洞察 | 人與產品互動的需求與感受 |
| 🗡 商業流 | 商業思維與資源配置 | 企業利益、成本、市場競爭 |
| 🗡 數據流 | 數據分析與驗證 | 客觀證據、指標衡量、迭代方向 |

三刀並行，動態平衡，才是成熟的產品設計思維。

---

## 知識架構

這份 Skill 不是按課程章節排列，而是依照**設計師實際會遇到的問題**重新建構：

```
ux-santoryu-skill/
├── SKILL.md                                  ← AI 讀取的入口
└── references/
    ├── strategy-and-positioning.md           ← 策略、定位、競品、利害關係人
    ├── user-research-and-needs.md            ← 研究方法、需求分析、心智模型
    ├── prioritization-and-mvp.md             ← 需求取捨、MVP、商業模式
    ├── interaction-and-ui-design.md          ← 互動設計、資訊架構、UI 原則
    ├── growth-and-retention.md               ← 增長、留存、遊戲化、全鏈路
    ├── data-driven-design.md                 ← 數據指標、使用性、AI/UX
    ├── prd-and-dev-process.md                ← PRD 撰寫、開發流程、工程溝通
    └── iteration-and-lifecycle.md            ← 迭代策略、產品生命週期、S 曲線
```

---

## 涵蓋的設計知識

以下是 8 份 reference 檔案各自涵蓋的主題：

### 📋 策略與定位 (`references/strategy-and-positioning.md`)
- 商業策略與 UX 策略的對齊
- 市場定位分析框架
- 目標族群定義（人口統計 + 心理變數）
- UX 投資報酬率（ROI）說服術
- 利益關係人分析與價值交換
- 產品價值主張設計

### 🔍 使用者研究與需求 (`references/user-research-and-needs.md`)
- 心智模型（Don Norman）
- 以使用者為中心的設計（UCD）
- 設計思考五階段與盲區
- 人因工程與認知原則
- 使用者研究方法選擇指南
- 需求擷取、分析與排序技術

### ⚖️ 需求取捨與 MVP (`references/prioritization-and-mvp.md`)
- 需求排序的雙指標評估法
- 產品藍圖規劃
- 最小可行產品（MVP）設計原則
- 常見數位產品商業模式
- UX 品質與創新評估指標

### 🎨 互動與介面設計 (`references/interaction-and-ui-design.md`)
- 人機互動設計（HCI）
- 資訊架構四大核心問題
- UI 設計核心原則（一致性、簡約、可見性、容錯、動線）
- 控制元件選擇指南
- 原型設計與測試方法
- 設計評論的正確框架

### 📈 產品增長與留存 (`references/growth-and-retention.md`)
- 進入市場策略（Go-To-Market）
- AARRR 海盜指標
- 全鏈路思維與接觸點設計
- 首次使用體驗（Onboarding）
- 回訪動機與忠誠度迴圈
- RFM 模型
- 遊戲化設計框架

### 📊 數據驅動設計 (`references/data-driven-design.md`)
- 數據指標體系（產品級 / 功能級 / 商業級）
- 數據收集與漏斗分析設計
- 使用性工程方法
- AI 輔助 UX 設計
- Product-Market Fit 成效報告

### 📝 PRD 與開發流程 (`references/prd-and-dev-process.md`)
- 產品需求文件（PRD）完整模板
- 設計與工程的溝通原則
- 瀑布式 vs 敏捷式開發
- Scrum 框架中的設計師角色

### 🔄 迭代與生命週期 (`references/iteration-and-lifecycle.md`)
- 使用者回饋的取捨決策
- 運算式設計思考
- 產品生命週期五階段
- S 曲線創新策略（Dyson、Netflix 案例）
- 產品終結時的設計責任
- 從 UX → CX → HX 的格局提升

---

## 如何使用

### 方法一：放入 Claude Projects 的 Knowledge

1. 解壓縮 `../ux3_skill.zip`
2. 將整個 `ux-santoryu-skill/` 資料夾上傳到 Claude Project 的 Knowledge
3. AI 會在你提問時自動參考這份知識庫

### 方法二：放入 Claude 的 Skills 目錄

若你使用的環境支援 Skills（如 Claude Code 或自定義部署），將資料夾放入 skills 目錄即可。

### 方法三：直接在對話中使用

將 `SKILL.md` 的內容貼入系統提示詞（System Prompt），並在需要時將相關的 reference 檔案內容貼入對話。

---

## 使用情境範例

| 你的問題 | AI 會參考 |
|---|---|
| 「老闆不同意投入 UX 研究的預算，怎麼說服？」 | strategy-and-positioning → UX ROI |
| 「產品功能太多，不知道先做什麼」 | prioritization-and-mvp → 需求排序 |
| 「介面設計一直被打槍」 | interaction-and-ui-design → 設計原則 |
| 「產品上線後用戶留不住」 | growth-and-retention → 留存策略 |
| 「不知道怎麼寫 PRD」 | prd-and-dev-process → PRD 模板 |
| 「產品老化，需要找新方向」 | iteration-and-lifecycle → S 曲線 |

---

## 知識來源

**UX 三刀流產品體驗設計課程**
- 40 堂完整課程
- 融合用戶需求洞察、商業思維、數據分析
- 從基礎理論到實戰應用的完整知識體系

---

## 授權說明

本專案採用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 授權。

- ✅ 可自由使用、分享、修改
- ✅ 必須標註來源為「**UX 三刀流**」
- ❌ 不得用於商業用途

知識內容萃取自 UX 三刀流產品體驗設計課程。
