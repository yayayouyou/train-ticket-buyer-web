# -*- coding: utf-8 -*-
"""三語言網站產生器 —— 內容集中管理，避免各語言版本走鐘。
   輸出：index.html / privacy.html / en/*.html / ja/*.html"""
import os, io, json

# ===== 上架前要換掉的網址 =====
STORE  = "https://chromewebstore.google.com/"   # TODO: 上架後換成擴充實際網址
FEEDBK = "https://forms.gle/dLrvJ3eKrvngnvsg6"  # Google 表單（與擴充端同一份）

# 贊助頁。網站自己的連結直接指這裡；擴充則指向本站的 /donate/ 轉址頁，
# 這樣日後換收款平台只要改這一行重跑產生器，擴充不必改、不必重送商店審核。
DONATE = "https://ko-fi.com/traingogogo"

# ===== 聯盟連結（Trip.com）=====
# Allianceid 與 SID 是分潤追蹤參數，缺任一個都不會計佣。
#
# trip_sub1 用來分辨流量來源：網站一律 "web"，擴充一律 "ext"。
#   這是之後判斷「擴充到底值不值得繼續維護」的唯一依據，不要留空。
#
# ⚠ 不要用 Trip.com 的短網址（trip.com/t/xxxx）——實測會把 trip_sub1 洗成空值，
#   分不出流量來源。一律用下面組出來的完整網址。
AFF_ID   = "9409583"
AFF_SID  = "325182901"
AFF_SUB1 = "web"          # 擴充端在 extension/content.js 用 "ext"

# 各語言導到對應的 Trip.com 站別與幣別 ——
# 否則日文使用者會看到繁體中文頁面與美金報價，轉換率會很難看。
TRIP_HOST = {"zh": "tw.trip.com", "en": "www.trip.com", "ja": "jp.trip.com"}
TRIP_CURR = {"zh": "TWD",         "en": "USD",          "ja": "JPY"}

# 商品路徑（從 Trip.com 聯盟後台取得的三條連結展開而來）
P_TOUR  = "/things-to-do/list?searchkey=5152&searchtype=1"
P_STAY1 = "/hotels/chiayi-county-hotel-detail-1229576/alishan-shermuh-international-tourist-hotel/"
P_STAY2 = "/hotels/chiayi-county-hotel-detail-1303945/ho-fong-villa-hotel/"
SUB3_TOUR = "D18798999"
SUB3_STAY = "D18799279"

def aff(lang, path, sub3, sub1=None):
    sep = "&" if "?" in path else "?"
    return (f"https://{TRIP_HOST[lang]}{path}{sep}"
            f"Allianceid={AFF_ID}&SID={AFF_SID}"
            f"&trip_sub1={sub1 or AFF_SUB1}&trip_sub3={sub3}"
            f"&curr={TRIP_CURR[lang]}")

def aff_links(lang, sub1=None):
    return {"tour":  aff(lang, P_TOUR,  SUB3_TOUR, sub1),
            "stay1": aff(lang, P_STAY1, SUB3_STAY, sub1),
            "stay2": aff(lang, P_STAY2, SUB3_STAY, sub1)}

LANGS = ["zh", "en", "ja"]
LABEL = {"zh": "繁體中文", "en": "English", "ja": "日本語"}
DIR   = {"zh": "", "en": "en/", "ja": "ja/"}
HTMLL = {"zh": "zh-Hant-TW", "en": "en", "ja": "ja"}
SITE  = {"zh": "阿里山林鐵訂票小幫手", "en": "Alishan Railway Booking Helper",
         "ja": "阿里山森林鉄道 予約アシスタント"}
T = {
 "guide":   {"zh": "訂票攻略", "en": "Booking guide", "ja": "予約ガイド"},
 "privacy": {"zh": "隱私權政策", "en": "Privacy policy", "ja": "プライバシーポリシー"},
 "feedback":{"zh": "意見回饋", "en": "Feedback", "ja": "ご意見"},
 "foot":    {"zh": "本站為個人製作的非官方說明，與阿里山林業鐵路及文化資產管理處無關。訂票請以官方網站為準。",
             "en": "An independent, unofficial guide. Not affiliated with the Alishan Forest Railway and Cultural Heritage Office. Always follow the official site.",
             "ja": "個人が作成した非公式のガイドです。阿里山林業鉄路及文化資産管理処とは関係ありません。予約は公式サイトをご確認ください。"},
}

def shell(lang, depth, title, desc, body):
    up = "../" * depth
    CUR = ' aria-current="page"'
    navs = "".join(
        '<a href="%s%s"%s>%s</a>' % (up, DIR[c], CUR if c == lang else "", LABEL[c])
        for c in LANGS)
    here = up + DIR[lang]
    return f"""<!DOCTYPE html>
<html lang="{HTMLL[lang]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<header><div class="wrap">
  <div class="logo">森</div>
  <div class="site">{SITE[lang]}</div>
  <nav>{navs}</nav>
</div></header>
{body}
<footer><div class="wrap">
  <div class="row">
    <a href="{here}">{T['guide'][lang]}</a>
    <a href="{here}privacy.html">{T['privacy'][lang]}</a>
    <a href="{FEEDBK}" target="_blank" rel="noopener noreferrer">{T['feedback'][lang]}</a>
  </div>
  <div>{T['foot'][lang]}</div>
</div></footer>
</body>
</html>
"""

def donate_page():
    """/donate/ 轉址頁 —— 擴充指向這裡，再轉到當前的收款平台。

    GitHub Pages 是純靜態的，發不出真正的 302，所以用 meta refresh + JS。
    對「換平台不用動擴充」這個目的來說效果一樣，差別只在 HTTP 狀態碼是 200。
    noscript 使用者會看到頁面上的按鈕，仍然可以手動點過去。
    """
    return f"""<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={DONATE}">
<title>前往贊助頁 / Redirecting to the tip jar</title>
<link rel="canonical" href="{DONATE}">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<main class="wrap" style="padding:64px 0;text-align:center">
  <p>正在前往贊助頁…<br>Redirecting to the tip jar…<br>支援ページに移動しています…</p>
  <p style="margin-top:24px">
    <a class="cta" href="{DONATE}" rel="noopener noreferrer">沒有自動跳轉？點這裡 / Continue / 続ける</a>
  </p>
</main>
<script>location.replace({DONATE!r});</script>
</body>
</html>
"""


def promo_json():
    """完成頁遠端促銷資料 —— 擴充的 PROMO_URL 指向本站的 /promo.json。

    改這裡重跑產生器即可更新擴充完成頁的推薦內容，擴充不必重上架、不必重送商店審核。
    聯盟連結沿用 aff_links()（trip_sub1=web），三語各一組（缺語言擴充會退回 en→zh）。

    圖片用「相對路徑」（相對於 promo.json 本身），擴充 background 會以 promo.json 的
    網址為基準解析再轉 data URI —— 所以這裡不必寫死 GitHub 網域，換帳號/改路徑都不用動。
    請把對應圖片放到本站的 promo/ 目錄（單張 < 400KB，否則擴充會略過該圖只顯示文字）。
    """
    L = {lang: aff_links(lang) for lang in LANGS}

    def item(image, key, title, sub):
        it = {"image": image}
        for lang in LANGS:
            it[lang] = {"title": title[lang], "sub": sub[lang], "url": L[lang][key]}
        return it

    data = {
        "_note": "由 _build.py 的 promo_json() 產生，勿手改；改內容請改該函式再跑 python _gen.py",
        "referral": {
            "zh": "想順便安排行程嗎？透過以下連結購買不會額外加價，純粹是導購 / 合作連結。",
            "en": "Planning the rest of your trip? Buying through these links costs you nothing extra — they are simply referral links.",
            "ja": "旅の予定も立てませんか？以下のリンクから購入しても追加料金はかかりません（紹介リンクです）。",
        },
        "items": [
            item("promo/stay-shermuh.jpg", "stay1",
                 {"zh": "阿里山神木賓館", "en": "Alishan Shermuh Hotel", "ja": "阿里山神木賓館"},
                 {"zh": "距阿里山車站約 400 公尺", "en": "About 400 m from Alishan Station", "ja": "阿里山駅から約 400 m"}),
            item("promo/stay-hofong.jpg", "stay2",
                 {"zh": "禾楓別墅", "en": "Ho-Fong Villa", "ja": "禾楓ヴィラ"},
                 {"zh": "阿里山鄉，近森林遊樂區", "en": "Near the recreation area, Alishan", "ja": "森林遊楽区の近く（阿里山郷）"}),
            item("promo/tour-sunrise.jpg", "tour",
                 {"zh": "阿里山日出・神木行程", "en": "Alishan sunrise & sacred-tree tours", "ja": "阿里山 日の出・神木ツアー"},
                 {"zh": "當地體驗，多為含接送", "en": "Local experiences, many with transfer", "ja": "送迎付きが多い現地体験"}),
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  {path}  ({len(text)} 字元)")   # 字元數，不是 bytes：中文一字 3 bytes
