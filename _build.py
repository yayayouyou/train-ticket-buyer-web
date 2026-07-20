# -*- coding: utf-8 -*-
"""三語言網站產生器 —— 內容集中管理，避免各語言版本走鐘。
   輸出：index.html / privacy.html / en/*.html / ja/*.html"""
import os, io

# ===== 上架前要換掉的網址 =====
STORE  = "https://chromewebstore.google.com/"   # TODO: 上架後換成擴充實際網址
FEEDBK = "https://forms.gle/"                   # TODO: 換成 Google 表單
DONATE = "https://ko-fi.com/"                   # TODO: 換成 Ko-fi / Buy Me a Coffee
AFF_STAY = "https://www.booking.com/"           # TODO: 換成聯盟追蹤網址（住宿）
AFF_TOUR = "https://www.kkday.com/"             # TODO: 換成聯盟追蹤網址（行程）

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

def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  {path}  ({len(text)} bytes)")
