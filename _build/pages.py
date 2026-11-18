"""Build the Elite Immigration concept site (no dependencies).

    python3 _build/pages.py && python3 _build/fonts.py

English at /, Traditional Chinese (Hong Kong) at /zh/. Every string is written as L(english, chinese).
"""
import json
import os

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
V = "7"  # cache-bust: bump on every CSS/JS change

LANG = "en"


def L(en, zh):
    return en if LANG == "en" else zh


# ------------------------------------------------------------------ facts (source: eliteimmigration.co.uk, Nov 2026)
PHONE = "0113 866 2868"
TEL = "+441138662868"
MOB = "07801 195794"
MOB_TEL = "+447801195794"
WECHAT = "Immigration_UK"
EMAIL = "Rob@eliteimmigration.co.uk"
IAA = "F201700014"
ADDR = "Vicarage Chambers, 9 Park Square East, Leeds LS1 2LH"
OFFICIAL = "https://eliteimmigration.co.uk/"
UXC = "https://ux-circles.com/professionals"
HOME = [-1.55065, 53.79895]
BASE = "https://uxcircles.github.io/eliteimmigration/"
ROUTE = json.load(open(os.path.join(BUILD, "routes.json")))[0]

PFX = ""  # prefix to the site root ("" or "../")


def mark(cls="mark"):
    return f'<img class="{cls}" src="{PFX}assets/img/mark.svg" width="64" height="64" alt="" aria-hidden="true">'


def swoosh(cls="swoosh"):
    """The red crescent from the logo, drawn on its own: the site's divider."""
    return (f'<svg class="{cls}" viewBox="0 0 240 40" aria-hidden="true" focusable="false">'
            '<path d="M2 6c70 34 160 34 236 0-50 30-112 36-160 30C46 32 20 22 2 6z"/></svg>')


PAGES = [
    ("individual.html", ("Families &amp; settlement", "家庭及定居")),
    ("bno.html", ("BN(O)", "BN(O)")),
    ("business.html", ("Employers &amp; business", "僱主及商業")),
    ("about.html", ("About", "關於我們")),
]


def head(slug, title, desc):
    en = BASE + slug.replace("index.html", "")
    zh = BASE + "zh/" + slug.replace("index.html", "")
    return f'''<!doctype html>
<html lang="{L('en-GB', 'zh-Hant-HK')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="en" href="{en}">
<link rel="alternate" hreflang="zh-Hant-HK" href="{zh}">
<link rel="icon" type="image/svg+xml" href="{PFX}assets/img/mark.svg">
<link rel="icon" type="image/png" href="{PFX}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{PFX}assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#29286c">
<link rel="preload" href="{PFX}assets/fonts/sora.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{PFX}assets/fonts/onest.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{PFX}assets/site.css?v={V}">
<script defer src="{PFX}assets/site.js?v={V}"></script>
</head>
'''


def switch_href(slug):
    s = "" if slug == "index.html" else slug
    if slug == "404.html":
        return PFX + ("zh/" if LANG == "en" else "")
    return ("zh/" + s) if LANG == "en" else ("../" + s)


def header(slug):
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if h == slug else ""}>{L(*t)}</a>' for h, t in PAGES
    )
    home = "index.html" if slug != "404.html" else PFX + ("" if LANG == "en" else "zh/")
    if slug == "404.html":
        links = "".join(f'<a href="{PFX}{"" if LANG == "en" else "zh/"}{h}">{L(*t)}</a>' for h, t in PAGES)
    sw_lang = L("zh-Hant-HK", "en")
    return f'''<body>
<a class="skip" href="#main">{L("Skip to content", "跳至內容")}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-in">
    <p><span class="concept-tag">{L("Concept", "概念")}</span><span class="concept-long">{L('Redesign concept. Not the <a href="' + OFFICIAL + '" target="_blank" rel="noopener">official Elite Immigration website</a>.', '網站概念設計，並非 <a href="' + OFFICIAL + '" target="_blank" rel="noopener">Elite Immigration 官方網站</a>。')}</span></p>
    <a class="concept-by" href="{UXC}" target="_blank" rel="noopener">{L("Designed by ", "設計：")}<strong>UX CIRCLES</strong> ↗</a>
  </div>
</div>
<header class="head" id="top">
  <div class="wrap head-in">
    <a class="brand" href="{home}" aria-label="{L('Elite Immigration, home', 'Elite Immigration 首頁')}">
      <img src="{PFX}assets/img/logo.png" width="800" height="273" alt="Elite Immigration">
    </a>
    <nav class="nav" aria-label="{L('Main', '主選單')}">{links}</nav>
    <a class="lang" href="{switch_href(slug)}" lang="{sw_lang}" hreflang="{sw_lang}">{L("中文", "English")}</a>
    <a class="head-call" href="tel:{TEL}">{PHONE}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{L('Menu', '選單')}</button>
  </div>
  <div class="menu" id="menu" hidden>
    <nav class="wrap" aria-label="{L('Menu', '選單')}">
      {links}
      <a href="{home}#contact">{L('Free consultation', '免費初步諮詢')}</a>
      <a href="tel:{TEL}">{L('Call', '致電')} {PHONE}</a>
      <a href="{switch_href(slug)}" lang="{sw_lang}">{L("中文", "English")}</a>
    </nav>
  </div>
</header>
'''


def footer(slug):
    home = "index.html" if slug != "404.html" else PFX + ("" if LANG == "en" else "zh/")
    lp = "" if slug != "404.html" else home
    return f'''<footer class="foot">
  {swoosh("swoosh foot-swoosh")}
  <div class="wrap foot-grid">
    <div>
      <img class="foot-logo" src="{PFX}assets/img/logo.png" width="800" height="273" alt="Elite Immigration">
      <p>{ADDR}</p>
      <p>{L('Regulated by the Immigration Advice Authority (IAA). Registration number', '受英國移民顧問管理局（IAA）監管，註冊編號')} <span class="mono">{IAA}</span></p>
    </div>
    <div>
      <p><a href="tel:{TEL}">{PHONE}</a> · {L('Leeds office', '列斯辦公室')}</p>
      <p><a href="tel:{MOB_TEL}">{MOB}</a> · {L('mobile', '手提電話')}</p>
      <p>WeChat <span class="mono">{WECHAT}</span></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <p>{" · ".join(f'<a href="{lp}{h}">{L(*t)}</a>' for h, t in PAGES)}</p>
      <p><a href="{lp}privacy.html">{L('Privacy and accessibility', '私隱及無障礙')}</a> · <a href="{switch_href(slug)}" lang="{L('zh-Hant-HK', 'en')}">{L('中文', 'English')}</a></p>
      <p class="small">{L('The settlement tool gives an estimate, not legal advice. Rules checked against GOV.UK and the earned settlement announcement of 2 November 2026.', '定居計算工具只提供估算，並非法律意見。規則已按 GOV.UK 及 2026 年 11 月 2 日公布的「積分定居」改革核對。')}</p>
      <p class="small">{L('Unofficial redesign concept by ', '非官方概念設計：')}<a href="{UXC}" target="_blank" rel="noopener">UX CIRCLES</a></p>
    </div>
  </div>
</footer>
<nav class="mbar" aria-label="{L('Quick actions', '快捷操作')}">
  <a href="tel:{TEL}">{L('Call', '致電')}</a>
  <button type="button" data-copy="{WECHAT}" data-done="{L('ID copied', '已複製')}">WeChat</button>
  <a href="{home}#contact">{L('Free consultation', '免費諮詢')}</a>
</nav>
<div class="toast" role="status" aria-live="polite"></div>
</body>
</html>
'''


def write(slug, title, desc, body):
    global PFX
    out = os.path.join(ROOT, "" if LANG == "en" else "zh", slug)
    PFX = "" if LANG == "en" else "../"
    if slug == "404.html":
        PFX = "/eliteimmigration/"
    html = head(slug, title, desc) + header(slug) + f'<main id="main">\n{body()}\n</main>\n' + footer(slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)


# ------------------------------------------------------------------ settlement tool
def tool():
    routes = [
        ("bno", L("BN(O) visa (Hong Kong)", "BN(O) 簽證（香港）")),
        ("partner", L("Partner of a British citizen or settled person", "英國公民或定居人士的配偶／伴侶")),
        ("skilled", L("Skilled Worker", "技術工作簽證（Skilled Worker）")),
        ("innovator", L("Innovator Founder", "創新創業者簽證（Innovator Founder）")),
        ("long", L("Long residence (any lawful visas)", "長期合法居留（任何合法簽證）")),
    ]
    opts = "".join(f'<option value="{v}">{t}</option>' for v, t in routes)
    return f'''<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <p class="hero-place">{L('Immigration advisers on Park Square, Leeds', '列斯 Park Square 移民顧問')}</p>
    <div class="hero-top"><h1 id="h1">{L('When can you apply to settle?', 'BN(O)、配偶、工作簽證，幾時可以申請永居？')}</h1>
    <p class="hero-lede">{L('Pick your visa and the date your time in the UK started. The arc shows the earliest dates for indefinite leave to remain and British citizenship under the rules in force today, and what the changes announced on 2 November 2026 mean for your route.',
      '揀選你的簽證，再輸入在英國居留的開始日期。弧線會按現行規則，顯示最早可申請永久居留（ILR）及入籍的日期，並說明 2026 年 11 月 2 日公布的改革對你的簽證途徑有何影響。')}</p></div>
    <form class="tool" id="tool" novalidate>
      <div class="tool-fields">
        <label class="f f-route"><span>{L('Your visa route', '簽證途徑')}</span>
          <select id="t-route">{opts}</select></label>
        <label class="f f-date"><span>{L('Start date of your route', '開始日期')}</span>
          <input id="t-start" type="date" required min="2005-01-01"></label>
        <label class="f f-pay" hidden><span>{L('Your salary (gross a year)', '年薪（稅前）')}</span>
          <select id="t-pay">
            <option value="low">{L('Under £50,271', '低於 £50,271')}</option>
            <option value="mid">{L('£50,271 or more', '£50,271 或以上')}</option>
            <option value="high">{L('£125,141 or more', '£125,141 或以上')}</option>
          </select></label>
        <label class="f f-brit" hidden><span>{L('Married to a British citizen?', '配偶是英國公民？')}</span>
          <select id="t-brit"><option value="yes">{L('Yes', '是')}</option><option value="no">{L('No, settled person', '否，是定居人士')}</option></select></label>
      </div>
      <div class="arc" aria-hidden="true">
        <svg viewBox="0 0 1000 200" preserveAspectRatio="none"><path class="arc-path" d="M30 180 C 250 -30, 750 -30, 970 180"/></svg>
        <span class="dot d0"></span><span class="dot d1"></span><span class="dot d2"></span>
      </div>
      <ol class="stops" id="t-stops" aria-live="polite">
        <li class="stop s0"><span class="stop-k">{L('Route started', '開始居留')}</span><span class="stop-d" id="t-d0">—</span></li>
        <li class="stop s1"><span class="stop-k">{L('Settlement (ILR)', '永久居留 ILR')}</span><span class="stop-d" id="t-d1">—</span><span class="stop-n" id="t-n1"></span></li>
        <li class="stop s2"><span class="stop-k">{L('Citizenship', '入籍英國')}</span><span class="stop-d" id="t-d2">—</span><span class="stop-n" id="t-n2"></span></li>
      </ol>
      <div class="change" id="t-change"></div>
      <p class="tool-foot">{L('An estimate, not legal advice. Absences, gaps between visas, English and Life in the UK requirements can all move these dates.', '以上只屬估算，並非法律意見。離境日數、簽證之間的空檔、英語及「英國生活」考試要求，都可能影響日期。')}
        <a href="#contact" id="t-ask">{L('Ask Jennie or Rob to check your dates', '請 Jennie 或 Rob 替你核對日期')}</a></p>
    </form>
  </div>
</section>'''


def tool_strings():
    """Text the JS needs, in the page language."""
    s = {
        "locale": L("en-GB", "zh-HK"),
        "apply": L("apply from {d}", "{d} 起可申請"),
        "years": L("{n} years", "{n} 年"),
        "afterIlr": L("12 months after ILR", "取得 ILR 後 12 個月"),
        "withIlr": L("as soon as you have ILR", "取得 ILR 後即可申請"),
        "pick": L("Enter a date", "請輸入日期"),
        "now": L("Rules today", "現行規則"),
        "plan": L("Announced 2 Nov 2026", "2026 年 11 月 2 日公布"),
        "c": {
            "bno": L("BN(O) holders keep the 5-year route to settlement. The Home Secretary named Hong Kong BN(O) among the groups whose path stays as it is today.",
                     "BN(O) 持有人維持 5 年定居途徑。內政大臣表明，香港 BN(O) 屬於定居途徑「維持現狀」的群組之一。"),
            "partner": L("Partners of British citizens keep the 5-year route (the &ldquo;British connection&rdquo; group). Partners of people who are settled but not British should check with us: the announcement does not spell this out.",
                         "英國公民的配偶維持 5 年途徑（「英國聯繫」群組）。如配偶只是定居人士而非英國公民，公布內容未有清楚說明，請先向我們查詢。"),
            "skilled_low": L("Under the announced plan the baseline becomes <strong>10 years</strong> for most routes, so this date could move to <strong>{d}</strong>. The new rules are expected to be laid from December 2026 and phased in through 2027. People already on the route are not exempt unless they hold ILR when the rules start.",
                             "按已公布的方案，大部分途徑的基本年期將改為 <strong>10 年</strong>，即日期或會延至 <strong>{d}</strong>。新規則預計由 2026 年 12 月起提交國會，並於 2027 年分階段實施。除非新規則生效時已取得 ILR，現時持簽人士並不獲豁免。"),
            "skilled_mid": L("Earning £50,271 or more for 3 of the last 5 years keeps a <strong>5-year</strong> route under the announced plan. You will also need at least 3 years of National Insurance contributions.",
                             "按已公布的方案，過去 5 年中有 3 年年薪達 £50,271 或以上，可維持 <strong>5 年</strong>途徑，另須至少 3 年國民保險供款。"),
            "skilled_high": L("Earning £125,141 or more for 3 years opens a <strong>3-year</strong> route under the announced plan, so you could reach settlement as early as <strong>{d}</strong> once the rules are in force.",
                              "按已公布的方案，3 年年薪達 £125,141 或以上，可走 <strong>3 年</strong>途徑；新規則生效後，最早或可於 <strong>{d}</strong> 申請定居。"),
            "innovator": L("Innovator Founder settlement is 3 years today. The announcement does not say clearly what happens to this route, so talk to us before you plan around the date.",
                           "現時 Innovator Founder 3 年可申請定居。公布內容未有清楚說明此途徑的安排，計劃前請先向我們查詢。"),
            "long": L("Long residence already needs 10 years of continuous lawful residence. Check your absences: long gaps or overstays can break the 10 years.",
                      "長期居留本身已須連續 10 年合法居留。請留意離境紀錄：長時間離開英國或逾期居留，都可能中斷 10 年的計算。"),
        },
    }
    return json.dumps(s, ensure_ascii=False)


# ------------------------------------------------------------------ home
def two_ways():
    return f'''<section class="ways" aria-labelledby="ways-h">
  <div class="wrap">
    <h2 id="ways-h">{L('Two ways to work with us', '兩種服務方式')}</h2>
    <div class="ways-grid">
      <article class="way">
        <h3>{L('Full representation', '全面代表')}</h3>
        <p>{L('We handle the whole application and every message with the Home Office.', '由我們處理整個申請，以及與內政部的所有聯絡。')}</p>
        <ul>
          <li>{L('Advice on eligibility and documents', '評估資格及所需文件')}</li>
          <li>{L('We complete and submit the application for you', '代你填寫及遞交申請')}</li>
          <li>{L('Covering letter and legal representations', '撰寫申請信及法律陳述')}</li>
          <li>{L('We deal with UKVI until a decision arrives', '與 UKVI 聯絡，直至獲得決定')}</li>
        </ul>
      </article>
      <article class="way way-alt">
        <h3>{L('Full document check', '文件全面檢查')}</h3>
        <p>{L('You prepare the application yourself; we check it before you pay the Home Office fees.', '你自行準備申請，我們在你繳交內政部費用前替你把關。')}</p>
        <ul>
          <li>{L('A line-by-line review of the form and evidence', '逐項檢查申請表及證明文件')}</li>
          <li>{L('Missing or wrongly formatted evidence flagged', '指出缺漏或格式錯誤的文件')}</li>
          <li>{L('A covering letter that sets out how you meet the rules', '撰寫申請信，說明你如何符合移民規則')}</li>
          <li>{L('Costs less than full representation', '費用低於全面代表服務')}</li>
        </ul>
        <p class="small">{L('For partner, points-based, ILR and citizenship applications.', '適用於配偶、計分制、永久居留及入籍申請。')}</p>
      </article>
    </div>
    <p class="ways-note">{L('Fixed fees where available. The first consultation is free and we usually reply within 1 working day.', '在可行情況下提供固定收費。首次諮詢免費，我們一般於 1 個工作天內回覆。')}</p>
  </div>
</section>'''


def areas():
    items = [
        ("bno.html", L("BN(O) visas", "BN(O) 簽證"),
         L("From first entry clearance to ILR and citizenship, including adult children under the household member route.", "由首次入境許可到永居及入籍，包括以「同住家庭成員」途徑申請的成年子女。")),
        ("individual.html", L("Partners and families", "配偶及家庭"),
         L("Spouse, unmarried partner and fiancé(e) visas, parents and other dependent relatives.", "配偶、未婚伴侶、未婚夫／妻簽證，以及父母和其他受養親屬。")),
        ("individual.html#settle", L("Settlement and citizenship", "定居及入籍"),
         L("Indefinite leave to remain, long residence, naturalisation and British passports.", "永久居留、長期居留、歸化入籍及英國護照。")),
        ("business.html", L("Sponsor licences", "擔保牌照"),
         L("Licence applications, Skilled Worker sponsorship and Home Office compliance audits.", "牌照申請、技術工作簽證擔保及內政部合規審查。")),
        ("business.html#founders", L("Founders and expansion", "創業及海外擴展"),
         L("Innovator Founder, UK Expansion Worker and other Global Business Mobility routes.", "創新創業者、英國擴展工作者及其他全球商業流動途徑。")),
        ("individual.html#visit", L("Visits and EU status", "探訪及歐盟身份"),
         L("Visit visas, EU Settlement Scheme, Frontier Worker permits and UK Ancestry.", "探訪簽證、歐盟定居計劃、邊境工作者許可及英國祖籍簽證。")),
    ]
    lis = "".join(f'<li><a href="{h}"><h3>{t}</h3><p>{d}</p><span class="arrow" aria-hidden="true">→</span></a></li>' for h, t, d in items)
    return f'''<section class="areas" aria-labelledby="areas-h">
  <div class="wrap">
    {swoosh()}
    <h2 id="areas-h">{L('What we advise on', '服務範圍')}</h2>
    <ul class="area-list">{lis}</ul>
  </div>
</section>'''


def people():
    return f'''<section class="people" aria-labelledby="people-h">
  <div class="wrap">
    <h2 id="people-h">{L('Who you will speak to', '負責你個案的顧問')}</h2>
    <div class="people-grid">
      <article class="person">
        <p class="mono person-id">JC</p>
        <h3>Jennie Chau</h3>
        <p class="role">{L('Senior Immigration Consultant · LLB (Hons), LPC', '高級移民顧問 · LLB（榮譽）、LPC')}</p>
        <p>{L('Advising since 2015, with a focus on sponsor licences, Skilled Worker planning, partner routes, ILR and citizenship. Authorised by the IAA; complex or reserved matters run through Truth Legal.', '2015 年起執業，專注擔保牌照、技術工作簽證規劃、配偶途徑、永居及入籍。獲 IAA 授權；較複雜或屬保留法律服務的個案，經 Truth Legal 處理。')}</p>
        <p class="langs">{L('English · Cantonese · Mandarin', '英語 · 廣東話 · 普通話')}</p>
      </article>
      <article class="person">
        <p class="mono person-id">RW</p>
        <h3>Rob Waugh</h3>
        <p class="role">{L('Immigration Consultant · IAA Level 1', '移民顧問 · IAA 第一級')}</p>
        <p>{L('With the team since 2018. Partner and fiancé(e) visas, ILR, citizenship, EU Settlement Scheme, UK Ancestry and BN(O) applications, with full representation or a document check.', '2018 年加入團隊。處理配偶及未婚夫／妻簽證、永居、入籍、歐盟定居計劃、英國祖籍及 BN(O) 申請，提供全面代表或文件檢查服務。')}</p>
        <p class="langs">{L('English', '英語')}</p>
      </article>
    </div>
    <p><a class="more" href="about.html">{L('About the firm', '關於本所')} →</a></p>
  </div>
</section>'''


def quotes():
    return f'''<section class="quotes" aria-labelledby="q-h">
  <div class="wrap">
    <h2 id="q-h">{L('What clients have written', '客戶評語')}</h2>
    <div class="q-grid">
      <figure class="q">
        <blockquote><p>{L('&ldquo;Thank you Jennie for helping me to sort out my fiancée settlement visa with no hassle at all. From Entry Clearance Visa to Renewal, Jennie has offered 24 hours 7 days service whenever we have questions about our application.&rdquo;', '「多謝 Jennie 協助我處理未婚妻定居簽證，過程毫不麻煩。由入境簽證到續簽，每當我們對申請有疑問，Jennie 都全天候提供協助。」')}</p></blockquote>
        <figcaption>Hing Wan · {L('takeaway owner', '外賣店東主')}</figcaption>
      </figure>
      <figure class="q">
        <blockquote><p lang="pt">&ldquo;Nos fomos ajudados pela Jennie para o nosso caso de imigração. A experiência foi totalmente positiva, o processo foi concluído com total sucesso e sem demora.&rdquo;</p>
        <p class="q-tr">{L('&ldquo;We have instructed Jennie as our Immigration Consultant, our experience with Jennie was extremely positive. The application process was smooth and successful.&rdquo;', '「我們委託 Jennie 擔任移民顧問，體驗非常正面，申請過程順利並獲批。」')}</p></blockquote>
        <figcaption>Rafael Pereira da Silva &amp; family · {L('former Manchester United and Brazil footballer', '前曼聯及巴西國家隊球員')}</figcaption>
      </figure>
      <figure class="q">
        <blockquote><p>{L('&ldquo;Very professional! Jenny helped me so much in the process of getting my residency, everything went through fine and she was always in contact with me to keep me updated.&rdquo;', '「非常專業！Jenny 在我申請居留期間幫了很多，一切順利，她亦一直與我保持聯絡，讓我知道最新進度。」')}</p></blockquote>
        <figcaption>Tatiana Pereira · {L('Google review', 'Google 評價')}</figcaption>
      </figure>
    </div>
    <p class="small">{L('Quoted from the testimonials and Google reviews published on eliteimmigration.co.uk.', '摘自 eliteimmigration.co.uk 刊登的客戶評語及 Google 評價。')}{L('', '（中文為譯文）')}</p>
  </div>
</section>'''


def contact():
    data = {
        "home": HOME,
        "mark": PFX + "assets/img/mark.svg",
        "label": "Elite Immigration",
        "routes": [{"name": L("Leeds station", "列斯火車站"), "min": ROUTE["min"], "start": ROUTE["start"], "coords": ROUTE["coords"]}],
    }
    topics = [L("BN(O)", "BN(O)"), L("Partner or family visa", "配偶或家庭簽證"), L("Settlement (ILR) or citizenship", "永居或入籍"),
              L("Sponsor licence or Skilled Worker", "擔保牌照或技術工作簽證"), L("Business or founder visa", "商業或創業簽證"),
              L("Visit visa", "探訪簽證"), L("Document check", "文件檢查"), L("Something else", "其他")]
    opts = "".join(f"<option>{t}</option>" for t in topics)
    return f'''<section class="contact" id="contact" aria-labelledby="c-h">
  <div class="wrap contact-grid">
    <div class="c-text">
      <h2 id="c-h">{L('Free first consultation', '免費初步諮詢')}</h2>
      <p class="c-phone"><a href="tel:{TEL}">{PHONE}</a></p>
      <p>{L('Mobile', '手提電話')} <a href="tel:{MOB_TEL}">{MOB}</a> · WeChat <button type="button" class="copy mono" data-copy="{WECHAT}" data-done="{L('ID copied', '已複製')}">{WECHAT}</button><br>
      <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <form class="form" id="enquiry" novalidate data-email="{EMAIL}" data-subject="{L('Free consultation request', '免費諮詢查詢')}">
        <div class="row2">
          <label class="f"><span>{L('Name', '姓名')}</span><input name="name" autocomplete="name" required></label>
          <label class="f"><span>{L('Phone', '電話')}</span><input name="phone" type="tel" autocomplete="tel" required></label>
        </div>
        <label class="f"><span>{L('Email', '電郵')}</span><input name="email" type="email" autocomplete="email"></label>
        <label class="f"><span>{L('What is it about?', '查詢事項')}</span><select name="topic">{opts}</select></label>
        <label class="f"><span>{L('Your situation, in a few lines', '簡述你的情況')}</span><textarea name="msg" rows="4"></textarea></label>
        <input type="hidden" name="dates" id="f-dates">
        <p class="f-err" role="alert" hidden>{L('Please add your name and a phone number.', '請填寫姓名及電話號碼。')}</p>
        <button class="btn" type="submit">{L('Open in my email app', '以電郵程式發送')}</button>
        <p class="small">{L('This opens a pre-filled email to Elite Immigration. Nothing is stored on this website.', '按下後會開啟已填好內容的電郵，寄給 Elite Immigration。本網站不會儲存任何資料。')}</p>
      </form>
    </div>
    <div class="c-map">
      <div class="map" data-map>
        <svg class="map-sketch" viewBox="0 0 400 360" role="img" aria-label="{L('Sketch map: Park Square is about 7 minutes walk north-west of Leeds station', '示意地圖：Park Square 位於列斯火車站西北面，步行約 7 分鐘')}">
          <rect width="400" height="360" fill="#e6e9f2"/>
          <rect x="60" y="70" width="120" height="100" rx="6" fill="#d7e3cf"/>
          <text x="120" y="125" text-anchor="middle" font-size="13" fill="#4a4a7a">Park Square</text>
          <path d="M0 250h400M230 0v360" stroke="#fff" stroke-width="14"/>
          <rect x="250" y="270" width="130" height="40" rx="4" fill="#cfd3e3"/>
          <text x="315" y="295" text-anchor="middle" font-size="12" fill="#4a4a7a">Leeds station</text>
          <path d="M300 270 C 280 210, 220 190, 190 130" fill="none" stroke="#bb2025" stroke-width="4" stroke-dasharray="6 6"/>
          <circle cx="186" cy="122" r="9" fill="#29286c"/>
        </svg>
      </div>
      <address class="addr">
        <strong>Vicarage Chambers</strong><br>9 Park Square East, Leeds LS1 2LH<br>
        {L(f'About {ROUTE["min"]} minutes on foot from Leeds station ({ROUTE["m"]} m).', f'由列斯火車站步行約 {ROUTE["min"]} 分鐘（{ROUTE["m"]} 米）。')}
        <a href="https://www.google.com/maps/search/?api=1&amp;query=Elite+Immigration+9+Park+Square+East+Leeds" target="_blank" rel="noopener">{L('Directions', '路線')} ↗</a>
      </address>
      <p class="small">{L('By appointment. Please call before visiting.', '需預約，到訪前請先致電。')}</p>
      <script type="application/json" id="map-data">{json.dumps(data, ensure_ascii=False)}</script>
    </div>
  </div>
</section>'''


def iaa_band():
    return f'''<section class="reg" aria-label="{L('Regulation', '監管')}">
  <div class="wrap reg-in">
    <p class="reg-num"><span>{L('IAA registration', 'IAA 註冊編號')}</span><span class="mono">{IAA}</span></p>
    <p>{L('Elite Immigration is regulated by the <a href="https://www.gov.uk/government/organisations/immigration-advice-authority" target="_blank" rel="noopener">Immigration Advice Authority</a>, which requires our advisers to keep their immigration law knowledge current. Advice in English, Cantonese and Mandarin.',
       'Elite Immigration 受<a href="https://www.gov.uk/government/organisations/immigration-advice-authority" target="_blank" rel="noopener">英國移民顧問管理局（IAA）</a>監管，顧問須持續更新移民法律知識。提供英語、廣東話及普通話服務。')}</p>
  </div>
</section>'''


def home():
    return (tool() + f'<script type="application/json" id="tool-text">{tool_strings()}</script>'
            + iaa_band() + two_ways() + areas() + people() + quotes() + contact())


# ------------------------------------------------------------------ inner pages
def page_head(h1, lede, kicker=None):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    return f'''<section class="page-head">
  <div class="wrap">{k}<h1>{h1}</h1><p class="lede">{lede}</p>{swoosh()}</div>
</section>'''


def cta():
    return f'''<section class="cta">
  <div class="wrap cta-in">
    <h2>{L('Free first consultation', '免費初步諮詢')}</h2>
    <p>{L('Fixed fees where available. We usually reply within 1 working day.', '在可行情況下提供固定收費，一般於 1 個工作天內回覆。')}</p>
    <p class="cta-btns"><a class="btn" href="tel:{TEL}">{L('Call', '致電')} {PHONE}</a> <a class="btn btn-line" href="index.html#contact">{L('Send your details', '填寫查詢')}</a></p>
  </div>
</section>'''


def ul(items):
    return "<ul class='ticks'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def bno():
    return page_head(
        L("BN(O) visas, from entry clearance to a British passport", "BN(O) 簽證：由入境許可到英國護照"),
        L("Specialist advice and representation for Hong Kong BN(O) status holders and their families, in English, Cantonese and Mandarin.", "為香港 BN(O) 身份持有人及其家人提供專業法律意見及代表服務，可用英語、廣東話及普通話溝通。"),
    ) + f'''<section class="body">
  <div class="wrap cols">
    <div>
      <h2>{L('Why BN(O) applications are refused', 'BN(O) 申請為何會被拒')}</h2>
      <p>{L('The route is meant to be flexible, but applications are often delayed or refused because of misunderstandings about eligibility, family relationships or documents. We make sure each application is assessed, evidenced and presented in line with the Immigration Rules and Home Office guidance.', 'BN(O) 途徑原意具彈性，但申請常因誤解資格、家庭關係證明不足或文件不全而延誤甚至被拒。我們確保每宗申請均按《移民規則》及內政部指引作出評估、充分舉證及妥善呈交。')}</p>
      <h2>{L('Who we act for', '服務對象')}</h2>
      {ul([L('BN(O) status holders applying from overseas or in the UK', '於海外或英國境內申請的 BN(O) 身份持有人'),
           L('Spouses, partners and dependent children', '配偶、伴侶及受養子女'),
           L('Adult children and other household members under the BN(O) Household Member route', '以「BN(O) 同住家庭成員」途徑申請的成年子女及其他家庭成員'),
           L('Families with complex living arrangements or dependency histories', '居住安排或依賴關係較複雜的家庭')])}
    </div>
    <div>
      <h2>{L('What we do', '服務內容')}</h2>
      {ul([L('Assess BN(O) status and family eligibility', '評估 BN(O) 身份及家庭成員資格'),
           L('Advise on the best route and timing', '建議最合適的途徑及遞交時間'),
           L('Prepare and submit entry clearance and in-country applications', '準備及遞交入境許可及英國境內申請'),
           L('Evidence household membership, dependency and residence', '證明同住關係、經濟依賴及居住要求'),
           L('Switching, extensions and continuous residence', '轉換簽證、續期及連續居留'),
           L('ILR and British citizenship', '永久居留及入籍'),
           L('Advice after a refusal, including administrative review', '被拒後的法律意見，包括行政覆核')])}
      <div class="note">
        <h3>{L('The 2 November 2026 announcement', '2026 年 11 月 2 日的公布')}</h3>
        <p>{L('BN(O) holders keep the 5-year route to settlement while most other routes move to a 10-year baseline. If you are on another visa, we can tell you whether switching into the BN(O) route is worth it.', 'BN(O) 持有人維持 5 年定居途徑，而大部分其他途徑的基本年期將改為 10 年。如你現時持有其他簽證，我們可分析轉用 BN(O) 途徑是否值得。')}</p>
        <p><a href="index.html#tool">{L('Work out your dates', '計算你的日期')} →</a></p>
      </div>
    </div>
  </div>
</section>''' + cta()


def individual():
    return page_head(
        L("Partners, families and settlement", "配偶、家庭及定居"),
        L("Clear advice on personal immigration cases, simple or complex, with full representation or a document check.", "個人移民個案，無論簡單或複雜，都提供清晰意見；可選擇全面代表或文件檢查。"),
    ) + f'''<section class="body">
  <div class="wrap cols3">
    <div>
      <h2>{L('Partners and family', '配偶及家庭')}</h2>
      {ul([L('Spouse and civil partner visas', '配偶及民事伴侶簽證'), L('Unmarried partner visas', '未婚伴侶簽證'), L('Fiancé(e) visas', '未婚夫／妻簽證'),
           L('Parents and other dependent relatives', '父母及其他受養親屬'), L('Extensions and leave to remain', '續簽及居留許可')])}
    </div>
    <div id="settle">
      <h2>{L('Settlement and citizenship', '定居及入籍')}</h2>
      {ul([L('Indefinite leave to remain', '永久居留（ILR）'), L('10-year long residence', '10 年長期居留'), L('Naturalisation and British citizenship', '歸化及入籍'),
           L('British passport applications', '英國護照申請'), L('EU Settlement Scheme: pre-settled and settled status', '歐盟定居計劃：預定居及定居身份')])}
    </div>
    <div id="visit">
      <h2>{L('Visits and other routes', '探訪及其他途徑')}</h2>
      {ul([L('Visit visas for family and business', '探親及商務探訪簽證'), L('UK Ancestry visas', '英國祖籍簽證'), L('Frontier Worker permits', '邊境工作者許可'),
           L('Graduate, Youth Mobility and High Potential Individual', '畢業生、青年流動及高潛力人才簽證'), L('Global Talent', '全球人才簽證')])}
    </div>
  </div>
</section>
<section class="body alt">
  <div class="wrap cols">
    <div>
      <h2>{L('Already confident? Get a full document check', '有信心自己申請？可選文件全面檢查')}</h2>
      <p>{L('We go through your form and evidence before you submit to UK Visas and Immigration. If an answer could confuse the caseworker, or evidence is missing or in the wrong format, we tell you what to change. We also draft a covering letter showing how you meet the rules.', '在你向 UK Visas and Immigration 遞交前，我們會檢查申請表及證明文件。如有答案可能令審批人員混淆，或文件缺漏、格式不符，我們會指出應如何修改，並撰寫申請信，說明你如何符合規則。')}</p>
    </div>
    <div>
      <h2>{L('Changes to settlement', '定居規則的改變')}</h2>
      <p>{L('On 2 November 2026 the government confirmed a 10-year baseline for most routes, with 5 years kept for partners of British citizens and BN(O) holders. Rules are expected from December 2026. Until they are in force, today&rsquo;s qualifying periods apply.', '政府於 2026 年 11 月 2 日確認，大部分途徑的基本年期改為 10 年，英國公民配偶及 BN(O) 持有人維持 5 年。新規則預計由 2026 年 12 月起提交；生效前仍按現行年期計算。')}</p>
      <p><a href="index.html#tool">{L('Work out your dates', '計算你的日期')} →</a></p>
    </div>
  </div>
</section>''' + cta()


def business():
    return page_head(
        L("Sponsor licences and business immigration", "擔保牌照及商業移民"),
        L("Sponsorship is a major part of our practice. We help UK employers get and keep their licence, and help founders and overseas companies set up here.", "擔保牌照是本所的主要業務。我們協助英國僱主取得及維持牌照，亦協助創業者及海外公司在英國設立業務。"),
    ) + f'''<section class="body">
  <div class="wrap cols">
    <div>
      <h2>{L('For employers', '僱主服務')}</h2>
      {ul([L('Sponsor licence applications', '擔保牌照申請'), L('Skilled Worker visas and extensions', '技術工作簽證及續簽'),
           L('Recruiting from outside the UK', '海外招聘意見'), L('Preventing illegal working: right to work checks', '防止非法僱用：工作權利查核'),
           L('Compliance support and preparing for Home Office audits', '合規支援及內政部審查準備'), L('Temporary Worker routes', '臨時工作者途徑')])}
    </div>
    <div id="founders">
      <h2>{L('For founders and overseas companies', '創業者及海外公司')}</h2>
      {ul([L('Innovator Founder visas', '創新創業者簽證'), L('Global Business Mobility: Senior or Specialist Worker, Graduate Trainee, UK Expansion Worker, Service Supplier, Secondment Worker', '全球商業流動：高級或專業工作者、見習畢業生、英國擴展工作者、服務提供者、借調工作者'),
           L('Business plans written for the immigration rules', '按移民規則撰寫商業計劃書')])}
      <div class="note">
        <h3>{L('Closed routes: extensions and settlement only', '已關閉途徑：只處理續簽及定居')}</h3>
        <p>{L('Tier 1 Investor, Tier 1 Entrepreneur, Start-up and Sole Representative of an Overseas Business are closed to new applicants. If you are already on one of them, we advise on extensions and settlement.', 'Tier 1 投資者、Tier 1 企業家、Start-up 及海外公司代表簽證已不接受新申請。如你已持有這些簽證，我們可就續簽及定居提供意見。')}</p>
      </div>
    </div>
  </div>
</section>''' + cta()


def about():
    return page_head(
        L("An IAA-regulated immigration firm on Park Square", "Park Square 的 IAA 監管移民顧問"),
        L("We advise individuals, families and businesses across the UK and worldwide, with clients in Europe, the Americas and Asia.", "我們為英國及世界各地的個人、家庭及企業提供意見，客戶遍及歐洲、美洲及亞洲。"),
    ) + f'''<section class="body">
  <div class="wrap people-grid">
    <article class="person">
      <p class="mono person-id">JC</p>
      <h2>Jennie Chau</h2>
      <p class="role">{L('Senior Immigration Consultant · LLB (Hons), LPC', '高級移民顧問 · LLB（榮譽）、LPC')}</p>
      <p>{L('Jennie has advised individual and corporate clients since 2015. She holds an LLB and the Legal Practice Course and is authorised by the Immigration Advice Authority.', 'Jennie 自 2015 年起為個人及企業客戶提供意見，持有法學士學位及法律專業課程（LPC）資格，並獲英國移民顧問管理局授權。')}</p>
      {ul([L('Sponsor licence applications and compliance', '擔保牌照申請及合規'), L('Skilled Worker sponsorship and eligibility', '技術工作簽證擔保及資格規劃'), L('Global Business Mobility', '全球商業流動'),
           L('Partner, spouse and family routes', '配偶及家庭途徑'), L('ILR and British citizenship', '永居及入籍')])}
      <p>{L('Jennie practises through both Elite Immigration and Truth Legal; cases that need reserved legal services are handled under Truth Legal. She has written on immigration policy for Jurit, a Legal 500 recognised firm.', 'Jennie 同時在 Elite Immigration 及 Truth Legal 執業；涉及保留法律服務的個案，經 Truth Legal 處理。她亦曾為 Legal 500 推介律所 Jurit 撰寫移民政策文章。')}</p>
    </article>
    <article class="person">
      <p class="mono person-id">RW</p>
      <h2>Rob Waugh</h2>
      <p class="role">{L('Immigration Consultant · IAA Level 1', '移民顧問 · IAA 第一級')}</p>
      <p>{L('Rob joined Elite Immigration in 2018. With a background in media and teaching English to refugees, he is known for clear advice and for putting clients at ease.', 'Rob 於 2018 年加入 Elite Immigration。他曾從事傳媒工作，亦曾教導難民英語，以清晰的意見及令客戶安心見稱。')}</p>
      {ul([L('Spouse, unmarried partner and fiancé(e) visas', '配偶、未婚伴侶及未婚夫／妻簽證'), L('Other dependent relatives', '其他受養親屬'), L('ILR and British citizenship', '永居及入籍'),
           L('EU Settlement Scheme', '歐盟定居計劃'), L('Points-based work visas, UK Ancestry, Frontier Worker', '計分制工作簽證、英國祖籍、邊境工作者'), L('BN(O) and visit visas', 'BN(O) 及探訪簽證')])}
    </article>
  </div>
</section>''' + iaa_band() + cta()


def privacy():
    return page_head(
        L("Privacy and accessibility", "私隱及無障礙"),
        L("Draft text for Elite Immigration to review. The current site&rsquo;s terms page still names another company.", "供 Elite Immigration 審閱的草稿。現有網站的條款頁仍然寫著另一間公司的名稱。"),
    ) + f'''<section class="body">
  <div class="wrap prose">
    <h2>{L('What this website collects', '本網站收集的資料')}</h2>
    <p>{L('Nothing. The enquiry form opens an email in your own email app; nothing is sent until you press send there. The map loads tiles from OpenFreeMap when you scroll to it.', '本網站不收集任何資料。查詢表格只會在你的電郵程式開啟一封電郵，你按下發送前不會傳送任何內容。地圖在你捲動至該處時，才會從 OpenFreeMap 載入。')}</p>
    <h2>{L('When you contact us', '當你聯絡我們')}</h2>
    <p>{L('Elite Immigration uses your details to answer your enquiry and, if you instruct us, to act on your case. Immigration cases can include special category data; we keep it confidential, share it only with the Home Office and others you agree to, and keep files only as long as our regulator and the law require. You can ask for a copy of your data or ask us to correct it at any time.', 'Elite Immigration 會使用你的資料回覆查詢；如你委託我們，亦會用於處理你的個案。移民個案可能涉及特殊類別個人資料，我們會保密處理，只會與內政部及你同意的其他機構分享，並只按監管機構及法律要求的期限保存。你可隨時要求索取或更正你的資料。')}</p>
    <h2>{L('Accessibility', '無障礙')}</h2>
    <p>{L('This site aims to meet WCAG 2.2 AA: text can be resized, every page works with a keyboard, and the settlement tool reads out its results to screen readers. If something does not work for you, call', '本網站以符合 WCAG 2.2 AA 為目標：文字可放大、所有頁面均可用鍵盤操作，定居計算工具的結果亦會由螢幕閱讀器讀出。如有任何不便，請致電')} <a href="tel:{TEL}">{PHONE}</a>.</p>
  </div>
</section>'''


def notfound():
    return f'''<section class="lost">
  <div class="wrap">
    {mark("lost-mark")}
    <h1>{L('This page has moved on', '找不到這個頁面')}</h1>
    <p class="lede">{L('Like a visa that has run out, this link no longer leads anywhere. Try the home page, or call us.', '這個連結已經失效，就像過期的簽證一樣。請返回首頁，或致電我們。')}</p>
    <p class="cta-btns"><a class="btn" href="{PFX}{'' if LANG == 'en' else 'zh/'}">{L('Home page', '返回首頁')}</a> <a class="btn btn-line" href="tel:{TEL}">{PHONE}</a></p>
  </div>
</section>'''


def build():
    global LANG
    for LANG in ("en", "zh"):
        write("index.html", L("Elite Immigration · UK immigration advisers in Leeds", "Elite Immigration · 列斯英國移民顧問"),
              L("IAA-regulated immigration advisers on Park Square, Leeds. Work out when you can apply to settle.", "受 IAA 監管的列斯移民顧問。計算你最早何時可申請永居。"), home)
        write("bno.html", L("BN(O) visas · Elite Immigration", "BN(O) 簽證 · Elite Immigration"), L("BN(O) visa advice in Leeds.", "列斯 BN(O) 簽證法律意見。"), bno)
        write("individual.html", L("Families and settlement · Elite Immigration", "家庭及定居 · Elite Immigration"), L("Partner, family, settlement and citizenship advice.", "配偶、家庭、定居及入籍意見。"), individual)
        write("business.html", L("Employers and business · Elite Immigration", "僱主及商業 · Elite Immigration"), L("Sponsor licences and business immigration.", "擔保牌照及商業移民。"), business)
        write("about.html", L("About · Elite Immigration", "關於我們 · Elite Immigration"), L("Jennie Chau and Rob Waugh, IAA-regulated advisers.", "Jennie Chau 及 Rob Waugh，IAA 監管顧問。"), about)
        write("privacy.html", L("Privacy and accessibility · Elite Immigration", "私隱及無障礙 · Elite Immigration"), L("Privacy notice and accessibility statement (draft).", "私隱聲明及無障礙聲明（草稿）。"), privacy)
    LANG = "en"
    write("404.html", "Page not found · Elite Immigration", "Page not found.", notfound)
    print("built")


if __name__ == "__main__":
    build()
