# -*- coding: utf-8 -*-
import sys, io, os
sys.path.insert(0, '.')
from _build import shell, write, SITE, donate_page, promo_json
import _content_zh as ZH, _content_en as EN, _content_ja as JA

C = {"zh": ZH, "en": EN, "ja": JA}
TITLE = {
  "zh": ("阿里山林鐵訂票攻略 — 開賣時間、遊樂區套票、票種完整說明",
         "阿里山林業鐵路網路訂票的完整規則：什麼時候開賣、遊樂區套票怎麼配、票種資格與票價，並提供免費的 Chrome 訂票小幫手。"),
  "en": ("Alishan Forest Railway booking guide — release times, package tickets, ticket types",
         "The complete rules for booking the Alishan Forest Railway online: when tickets open, how the recreation area package works, ticket types and prices, plus a free Chrome extension."),
  "ja": ("阿里山森林鉄道 予約ガイド — 発売時刻・遊園地パッケージ・券種の完全解説",
         "阿里山森林鉄道のネット予約の全ルール：いつ発売されるか、遊園地パッケージの仕組み、券種と料金。無料の Chrome 拡張機能もご紹介。"),
}
PTITLE = {
  "zh": ("隱私權政策 — 阿里山林鐵訂票小幫手", "本擴充不上傳你的任何個人資料、不追蹤、不含分析或廣告；輸入的資料只存在你的瀏覽器。"),
  "en": ("Privacy policy — Alishan Railway Booking Helper", "This extension never uploads your personal data, does not track you, and contains no analytics or ads."),
  "ja": ("プライバシーポリシー — 阿里山森林鉄道 予約アシスタント", "本拡張機能は個人情報をアップロードせず、追跡もアナリティクスも広告もありません。"),
}
DIRS = {"zh": ".", "en": "en", "ja": "ja"}

print("產生網頁：")
for lang in ("zh", "en", "ja"):
    d = DIRS[lang]
    depth = 0 if lang == "zh" else 1
    m = C[lang]
    t, desc = TITLE[lang]
    write(os.path.join(d, "index.html"),
          shell(lang, depth, t, desc, m.HERO + m.BODY))
    pt, pdesc = PTITLE[lang]
    write(os.path.join(d, "privacy.html"),
          shell(lang, depth, pt, pdesc, m.PRIVACY))

# 擴充指向的贊助轉址頁（換收款平台只需改 _build.py 的 DONATE）
write(os.path.join("donate", "index.html"), donate_page())

# 擴充完成頁的遠端促銷資料（擴充 PROMO_URL 指向本站的 promo.json）
write("promo.json", promo_json())
print("完成")
