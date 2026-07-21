# 網站 — 部署與維護

這個網站一次解決四件事：

1. **隱私權政策**（Chrome 上架的硬性要求，必須放在公開網址）
2. **旅遊合作連結**的揭露頁面
3. **意見回饋**的落腳處
4. **擴充的說明頁**，而且有搜尋流量價值

內容涵蓋實際訂票時會遇到的規則：14 天預訂窗口、週五規則、06:00 開賣、遊樂區套票的張數對應。

---

## 檔案結構

```
train_ticket_buyer_web/       ← 這個資料夾就是 repo 根目錄
  index.html          繁體中文首頁（訂票攻略）
  privacy.html        繁體中文隱私權政策
  en/index.html       English
  en/privacy.html
  ja/index.html       日本語
  ja/privacy.html
  donate/index.html   贊助轉址頁（擴充指這裡，再轉到收款平台）
  style.css           共用樣式（零外部資源）

  _build.py           產生器：共用外殼與導覽
  _content_zh.py      中文內容
  _content_en.py      英文內容
  _content_ja.py      日文內容
  _gen.py             執行這支就會重新產生所有 HTML
```

**改內容不要直接改 HTML** —— 改 `_content_*.py` 然後跑：

```bash
python3 _gen.py
```

這樣三個語言版本不會走鐘。

---

## 設定集中在 `_build.py` 最上面

```python
STORE  = "..."   # ⚠ 還是 placeholder，擴充上架後要換成商店網址
FEEDBK = "..."   # Google 表單 ✔
DONATE = "..."   # Ko-fi ✔（改這行就等於改了 /donate 轉址目標）

AFF_ID, AFF_SID = "...", "..."   # Trip.com 聯盟，與擴充端相同
AFF_SUB1 = "web"                 # 流量來源；擴充端用 "ext"，不要留空
```

改完跑 `python3 _gen.py` 重新產生。

**聯盟連結兩個地雷：**

- `trip_sub1` 不要留空 —— 它是分辨「擴充 vs 網站」流量的唯一依據。
- 不要用 Trip.com 短網址（`trip.com/t/xxxx`），實測會把 `trip_sub1` 洗成空值。

> 擴充專案裡也有一份同樣的連結（`extension/content.js` 的 `LINKS` 常數）。
> Allianceid / SID 兩邊要一致，只有 `trip_sub1` 不同。

---

## `/donate` 轉址頁

擴充的贊助連結指向本站的 `/donate/`，再由它轉到 Ko-fi。這樣日後換收款平台
只要改 `_build.py` 的 `DONATE` 重跑產生器，**擴充不用改、不必重送商店審核**。

> GitHub Pages 是純靜態的，發不出真正的 302，所以 `/donate/` 用的是
> meta refresh + JS 轉址（HTTP 狀態碼是 200）。對上述目的效果相同。
> 若哪天需要真正的 302，得把站台搬到 Cloudflare Pages 或 Netlify。

---

## 部署到 GitHub Pages

1. 在 GitHub 建一個 public repo
2. 這個資料夾本身就是 git 倉庫，直接 `git remote add origin ...` 然後 push
3. repo → **Settings → Pages**
4. Source 選 **Deploy from a branch**，Branch 選 `main`、資料夾選 `/ (root)`
5. 存檔，等一兩分鐘

網址會是：

```
https://<你的帳號>.github.io/<repo名稱>/
隱私權政策：https://<你的帳號>.github.io/<repo名稱>/privacy.html
```

**隱私權政策那個網址就是 Chrome 開發者後台要填的。**

---

## 設計上的幾個決定

**零外部資源。** 沒有 Google Fonts、沒有 CDN、沒有分析腳本。理由跟擴充一致：載入外部資源就是把訪客的 IP 交給第三方。也因為這樣，隱私權政策可以誠實寫「不收集任何資料」，而不是一堆但書。

**三語言用同一份產生器。** 避免改了中文忘記改日文 —— 這在前面的擴充開發裡已經發生過一次。

**攻略內容放在聯盟連結前面。** 使用者先得到有用的東西，合作連結放在最後且明確標示。這符合 Chrome 對聯盟連結的要求（相關利益、使用者主動、明確揭露），也比較不討人厭。
