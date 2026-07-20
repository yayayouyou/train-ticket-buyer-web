# 網站 — 部署與維護

這個網站一次解決四件事：

1. **隱私權政策**（Chrome 上架的硬性要求，必須放在公開網址）
2. **聯盟行銷申請**（你卡住的那關 —— 審核方要看到有內容的網站）
3. **意見回饋**的落腳處
4. **擴充的說明頁**，而且有搜尋流量價值

內容不是為了填版面而寫的 —— 那些訂票規則是我們這半年從站方實測逆向出來的（14 天窗口、週五規則、06:00 開賣、遊樂區套票的張數對應），網路上沒幾個地方寫得這麼完整。這正是聯盟審核想看到的「真的有相關內容」。

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

## 上架前一定要換的網址

全部集中在 `_build.py` 最上面：

```python
STORE    = "..."   # 擴充上架後的商店網址
FEEDBK   = "..."   # Google 表單
DONATE   = "..."   # Ko-fi / Buy Me a Coffee
AFF_STAY = "..."   # 聯盟追蹤網址（住宿）
AFF_TOUR = "..."   # 聯盟追蹤網址（行程）
```

改完跑 `python3 _gen.py` 重新產生。

> 擴充裡也有一份同樣的連結，在 `D:\train_ticket_buyer\extension\content.js` 的 `LINKS` 常數。兩邊要一起換。

---

## 部署到 GitHub Pages

詳細步驟看 `部署步驟.md`。摘要：

1. 在 GitHub 建一個 repo（例如 `alishan-booking`）
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

## 申請聯盟時怎麼說

網站有了之後，申請時**主動說明這是搭配 Chrome 擴充的網站**，不要只填網址就送出。建議這樣寫：

> 本站提供阿里山林業鐵路的訂票規則說明，並發布一個免費的 Chrome 擴充功能協助填寫訂票表單。
> 旅遊合作連結顯示於網站頁面與擴充的「訂票完成」畫面，均明確標示為合作連結，
> **由使用者主動點擊，不自動導轉，且不覆蓋或修改任何既有的聯盟參數。**

最後那句是重點。Honey 事件（擴充偷偷覆蓋別人的聯盟碼）之後，聯盟網路對擴充最在意的就是這件事 —— 你主動聲明不做，比被問到才解釋好得多。

---

## 設計上的幾個決定

**零外部資源。** 沒有 Google Fonts、沒有 CDN、沒有分析腳本。理由跟擴充一致：載入外部資源就是把訪客的 IP 交給第三方。也因為這樣，隱私權政策可以誠實寫「不收集任何資料」，而不是一堆但書。

**三語言用同一份產生器。** 避免改了中文忘記改日文 —— 這在前面的擴充開發裡已經發生過一次。

**攻略內容放在聯盟連結前面。** 使用者先得到有用的東西，合作連結放在最後且明確標示。這符合 Chrome 對聯盟連結的要求（相關利益、使用者主動、明確揭露），也比較不討人厭。
