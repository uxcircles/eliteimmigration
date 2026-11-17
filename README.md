# Elite Immigration 網站概念設計

UX CIRCLES 為列斯 Elite Immigration（IAA 註冊編號 F201700014）製作的非官方網站改版概念，英文版在 `/`，繁體中文（香港）版在 `/zh/`。每頁頂部都有「概念」標示及官方網站連結，並設有 `noindex` 及 `robots.txt`，不會被搜尋引擎收錄。

網址：https://uxcircles.github.io/eliteimmigration/

## 頁面

| 頁面 | 英文 | 中文 |
| --- | --- | --- |
| 首頁：定居日期計算工具、兩種服務方式、服務範圍、顧問、客戶評語、聯絡及地圖 | `index.html` | `zh/index.html` |
| BN(O) 簽證 | `bno.html` | `zh/bno.html` |
| 家庭及定居（含文件檢查） | `individual.html` | `zh/individual.html` |
| 僱主及商業（擔保牌照） | `business.html` | `zh/business.html` |
| 關於我們（Jennie Chau、Rob Waugh） | `about.html` | `zh/about.html` |
| 私隱及無障礙（草稿） | `privacy.html` | `zh/privacy.html` |
| 404 | `404.html` | |

## 如何修改

所有頁面由 `_build/pages.py` 產生，中英文並排寫成 `L(英文, 中文)`；聯絡資料集中在檔案開頭。

```bash
python3 _build/pages.py      # 重建所有 HTML
python3 _build/fonts.py      # 修改中文字後，重新抽取 Noto Sans TC 子集字型
```

修改 CSS 或 JS 後，請把 `pages.py` 的 `V` 加一（cache-bust）。

## 設計概念

- **標誌元素**：商標地球上的紅色弧線。網站把它變成「定居路線弧」：由開始居留 → 永久居留（ILR）→ 入籍。首頁工具、分隔線（`.swoosh`）、地圖標記、favicon 及 404 頁都用上它。
- **首屏類型**：`tool-first`。客戶最常問「我幾時可以申請永居？」，首屏直接讓他們揀選簽證途徑及開始日期，即時計算日期，並說明 2026 年 11 月 2 日公布的「積分定居」（earned settlement）改革對該途徑的影響。
- **字型**：Sora（標題，幾何寬身大寫，呼應商標字款）、Onest（內文）、DM Mono（日期及註冊編號）、Noto Sans TC（中文）。
- **顏色**：全部取自商標：靛藍 `#29286c`、紅 `#bb2025`，配冷灰藍底 `#eef1f7`。
- **標題**：When can you apply to settle? ／ BN(O)、配偶、工作簽證，幾時可以申請永居？
- **與之前的律師／移民網站不同之處**：沒有左文右圖、沒有拱形相框、沒有人像卡；首屏就是工具；色調冷而飽和，而非米色＋深藍。

## 資料來源

全部取自 eliteimmigration.co.uk（2026 年 11 月 17 日）：服務列表、BN(O) 中英文內容、Jennie Chau 及 Rob Waugh 簡介、地址、電話、WeChat、電郵、IAA 註冊編號、客戶評語及 Google 評價。步行路線來自 routing.openstreetmap.de（列斯火車站 550 米，約 7 分鐘）。

定居規則：現行年期按 GOV.UK；改革內容按 2026 年 11 月 2 日內政大臣聲明（EIN、FSP Law 等報導）。新規則預計 2026 年 12 月起提交，2027 年分階段實施，細節或會改變，請事務所在使用前核實。

## 需要事務所確認

1. **定居工具的內容**：特別是 Innovator Founder 及「定居人士（非英國公民）配偶」在改革下的安排，公布內容未有清楚說明。
2. **語言**：首頁寫英語、廣東話、普通話；關於我們頁寫英語及廣東話；中文頁另提葡萄牙語。網站暫寫「英語、廣東話、普通話」。
3. **辦公時間**：現有網站沒有列出，網站暫寫「需預約，到訪前請先致電」。
4. **WhatsApp**：現有網站沒有列出，所以手機底部列用「致電／WeChat／免費諮詢」。
5. **地圖位置**：9 Park Square East 的確切位置按 OpenStreetMap 估算。
6. **客戶評語中文**為 UX CIRCLES 翻譯。
7. **私隱聲明**為草稿：現有網站的條款頁仍多處寫著另一間公司「PinSupreme」。
8. 已關閉的簽證（Tier 1 Investor／Entrepreneur、Start-up、海外公司代表）改列為「只處理續簽及定居」。

網站沒有使用任何圖庫相片，也沒有後端：查詢表格只會開啟預先填好的電郵。

非官方概念設計：UX CIRCLES · https://ux-circles.com/professionals
