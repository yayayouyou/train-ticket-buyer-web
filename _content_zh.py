# -*- coding: utf-8 -*-
"""繁體中文內容。資料來源：站方售票說明 + 訂票系統實測（2026-07）。"""
from _build import STORE, FEEDBK, DONATE, aff_links
_A = aff_links("zh")
AFF_TOUR, AFF_STAY1, AFF_STAY2 = _A["tour"], _A["stay1"], _A["stay2"]

HERO = f"""
<div class="hero"><div class="wrap">
  <h1>阿里山林鐵訂票，<br>其實有一套規則</h1>
  <p>什麼時候開賣、為什麼一定要買遊樂區套票、票種怎麼配才不會被退 —— 這頁把官方分散在各處的規則整理成一份看得懂的說明，並提供一個免費的 Chrome 擴充幫你把表單填好。</p>
  <a class="cta" href="{STORE}" target="_blank" rel="noopener noreferrer">安裝免費擴充</a>
  <p class="cta-note">完全免費 · 不收集個人資料 · 不連線任何外部伺服器</p>
</div></div>
"""

BODY = f"""
<main><div class="wrap">

<section id="when">
<h2>一、什麼時候可以訂？</h2>
<p>這是最多人卡住的地方。官方規則是：<strong>乘車日起前 1 日至前 14 日</strong>可以預訂，但週末有例外。</p>
<table>
<tr><th>你在哪一天訂</th><th>最遠可以訂到</th></tr>
<tr><td>週一 ~ 週四</td><td>14 天後</td></tr>
<tr><td>週五</td><td><strong>次次週日</strong>（等於 16 天後）</td></tr>
<tr><td>週六</td><td><strong>次次週日</strong>（等於 15 天後）</td></tr>
</table>
<div class="tip"><strong>網路訂票時間是 06:00–24:00。</strong>凌晨 0 點到 6 點系統是關的 —— 想搶熱門日期，是<strong>當天早上 6 點</strong>開賣，不是半夜 12 點。</div>
<h3>還有兩個分階段開放的規則</h3>
<ul>
<li>乘車日前 14 天：<strong>優先開放嘉義、北門 → 阿里山</strong></li>
<li>乘車日前 <strong>3 天</strong>起：若仍有剩餘座位，才開放<strong>嘉義 → 奮起湖</strong></li>
</ul>
<p>所以如果你想訂嘉義到奮起湖，太早去反而訂不到，要等到乘車日前 3 天。</p>
<div class="note"><strong>祝山線特別規定：</strong>要訂隔天的祝山線（看日出），最晚只能在乘車前一日<strong>中午 12 點</strong>之前訂。</div>
</section>

<section id="package">
<h2>二、遊樂區套票 —— 最容易填錯的地方</h2>
<p>如果你的<strong>到達站在遊樂區內</strong>（阿里山、二萬平），系統會強制你同時購買<strong>阿里山國家森林遊樂區門票</strong>，這叫「遊樂區套票」。</p>
<div class="note"><strong>關鍵規則：每一類「車票」的張數，必須等於該類「門票」的張數。</strong>對不上就送不出去。這是最多人卡關的原因。</div>
<h3>舉個例子</h3>
<p>你訂 2 張全票 + 1 張孩童票，那門票也要剛好 2 張（對應全票）+ 1 張（對應孩童票）。而每一張門票還要各自選一個「身分」：</p>
<table>
<tr><th>門票身分</th><th>價格</th><th>誰符合</th></tr>
<tr><td>全票</td><td>150 元</td><td>搭乘大眾運輸工具、持有票根者</td></tr>
<tr><td>半票</td><td>100 元</td><td>軍警學生、因公撫恤遺族、設籍嘉義縣市、7–12 歲兒童</td></tr>
<tr><td>優待票</td><td>10 元</td><td>3–6 歲幼兒、65 歲以上長者、持證導遊</td></tr>
<tr><td>免票</td><td>0 元</td><td>0–2 歲幼兒、身心障礙者及必要陪伴者 1 人、志工、區內居民、設籍阿里山鄉</td></tr>
</table>
<div class="tip">多數人是<strong>全票 150 元</strong> —— 只要你是搭大眾運輸來的、有票根就符合。設籍嘉義縣市的人記得選半票，一個人差 50 元。</div>
<h3>套票的其他限制</h3>
<ul>
<li>套票<strong>不拆賣</strong>，退票或換票時要成套處理</li>
<li>車票為<strong>免票</strong>者，系統<strong>不提供座位</strong></li>
<li>車票和門票<strong>皆為免票</strong>者，不提供座位及票券</li>
</ul>
</section>

<section id="tickets">
<h2>三、車票身分怎麼選</h2>
<table>
<tr><th>身分</th><th>資格</th></tr>
<tr><td>全票</td><td>一般成人</td></tr>
<tr><td>孩童票</td><td>乘車當日滿 6 歲未滿 12 歲，或滿 115 公分不滿 150 公分</td></tr>
<tr><td>敬老票</td><td>乘車當日年滿 65 歲以上之中華民國國民</td></tr>
<tr><td>愛心票</td><td>持身心障礙證明者（證明背面註記「國內大眾運輸工具」者可帶必要陪伴者 1 人）</td></tr>
<tr><td>免票</td><td>未滿 6 歲或未滿 115 公分之兒童（不佔位，需成人陪同，每人限帶 2 名）；持證導遊不佔位</td></tr>
</table>
<div class="note"><strong>乘車時一定要帶符合票種的證件正本。</strong>查驗時拿不出來，會被視為無票乘車並依規補票。</div>
<p>每一身分證字號（或護照號碼），<strong>同一線別、每乘車日最多 6 張</strong>；同時訂去回程則各最多 6 張。</p>
</section>

<section id="pay">
<h2>四、付款與取票</h2>
<ul>
<li><strong>線上刷卡</strong>：確認車次後直接付款</li>
<li><strong>統一超商</strong>：憑預約號至門市多媒體機台付款取票，24 小時服務，<strong>每張車票收 10 元手續費</strong>（去回票以 2 張計）</li>
<li><strong>林鐵車站</strong>：留意各站售票時間</li>
</ul>
<div class="note"><strong>逾期未付款會自動取消訂位。</strong>若一個月內累積 3 次逾期未付款紀錄，將<strong>停權 6 個月</strong>。</div>
<p>超商取票每筆預約號最多取 6 張，超過要到林鐵售票站辦理。本線部分車站提供電子車票。</p>
</section>

<section id="faq">
<h2>五、常見問題</h2>
<div class="card">
<div class="faq"><b>顯示「查無可售車次或選購的車票已售完」怎麼辦？</b>
<span>先試前一天或後一天 —— 熱門日期常常只差一天就有位。如果乘車日在 3 天內，也可以改查「嘉義 → 奮起湖」，那個區間較晚開放、通常剩位較多。再不行就減少張數試試。</span></div>
<div class="faq"><b>為什麼我想訂的日期選不到？</b>
<span>超過開放範圍了。看上面第一段的表格算一下最遠可訂到哪天，或用擴充的日曆 —— 不能選的日子會直接灰掉，並告訴你那天什麼時候開賣。</span></div>
<div class="faq"><b>可以同時開很多分頁一起搶嗎？</b>
<span>不行。系統會偵測多開視窗並跳出提醒。只能一個分頁操作。</span></div>
<div class="faq"><b>座位可以自己選嗎？</b>
<span>不行，由系統自動配置。有空位時會優先配最近的連續座位。</span></div>
<div class="faq"><b>訂錯了可以改嗎？</b>
<span>付款前後、取票前都可以透過網路訂票系統辦理「搭乘日期、班次」變更。已付款者第 1 次變更免手續費，第 2 次起收票價 10%。對號車最遲須於原訂車次開車前 60 分鐘辦理。</span></div>
</div>
</section>

<section id="ext">
<h2>六、這個擴充幫你做什麼</h2>
<p>上面這些規則我都寫進擴充裡了。安裝後開啟訂票頁，它會自動幫你：</p>
<ul>
<li><strong>代填查詢條件</strong> —— 路線、日期、起迄站、票數一次填好</li>
<li><strong>遊樂區套票逐張選</strong> —— 每張票各自選門票身分，張數自動對齊，不會再送出被退</li>
<li><strong>日曆只顯示可訂的日子</strong> —— 還沒開放的日期會告訴你哪天 06:00 開賣</li>
<li><strong>放大驗證碼</strong> —— 官方的圖只有 80×30，放大 3 倍好認很多</li>
<li><strong>偵測官方開賣倒數</strong> —— 倒數期間先把條件填好，時間一到自動聚焦驗證碼欄位</li>
<li><strong>售完時的快捷調整</strong> —— 一鍵換日期、換區間、減票數</li>
<li><strong>餘票掃描</strong> —— 逐日查哪幾天有票，並讀出各車次還剩幾位</li>
</ul>
<div class="note"><strong>它不會、也不能幫你辨識驗證碼。</strong>驗證碼一律由你本人輸入 —— 那是官方防止程式大量搶票的機制，我們不會去繞過它。擴充能做的是把「填表」這件重複的事變快，讓你把注意力放在真正需要人的那 4 個字上。</div>
<p style="margin-top:16px"><a class="cta" href="{STORE}" target="_blank" rel="noopener noreferrer">安裝免費擴充</a></p>
</section>

<section id="more">
<h2>七、順便安排行程</h2>
<div class="disclose">以下為<strong>合作連結</strong>：透過這些連結完成預訂，本站可能獲得少量分潤，對你的價格沒有影響。你也可以直接搜尋這些平台。</div>
<div class="links">
  <a href="{AFF_STAY1}" target="_blank" rel="noopener noreferrer"><b>阿里山神木賓館</b><span>距阿里山車站約 400 公尺，下車就到</span></a>
  <a href="{AFF_STAY2}" target="_blank" rel="noopener noreferrer"><b>禾楓別墅</b><span>同在阿里山園區內，查看當晚空房與房價</span></a>
  <a href="{AFF_TOUR}" target="_blank" rel="noopener noreferrer"><b>阿里山一日遊 · 當地體驗</b><span>日出、神木、步道行程</span></a>
</div>
<h3 style="margin-top:26px">覺得有幫助嗎？</h3>
<div class="links">
  <a href="{FEEDBK}" target="_blank" rel="noopener noreferrer"><b>回報問題 / 給建議</b><span>官網改版時，你的回報特別重要</span></a>
  <a href="{DONATE}" target="_blank" rel="noopener noreferrer"><b>請我喝杯咖啡</b><span>擴充完全免費，贊助隨意</span></a>
</div>
</section>

</div></main>
"""

PRIVACY = """
<main><div class="wrap">
<section>
<h2>隱私權政策</h2>
<p style="color:var(--muted);font-size:14px">最後更新：2026 年 7 月</p>

<div class="tip"><strong>核心原則：本擴充不會上傳你的任何個人資料、不追蹤、不含分析或廣告。你輸入的資料只存在你自己的瀏覽器。</strong></div>

<h3>個人資料（乘客資料）</h3>
<p>為了自動代填官方訂票的乘客欄位，本擴充提供「乘客資料」功能（身分證／護照號碼、電話、Email）。此為<strong>選填</strong>，且採安全優先設計：</p>
<ul>
<li><strong>預設「本次使用」</strong>：只存在瀏覽器記憶體（<code>chrome.storage.session</code>），<strong>不寫入硬碟、關閉瀏覽器即清除</strong>。</li>
<li><strong>選用「加密記住」</strong>：以你設定的密碼經 PBKDF2-SHA256 ＋ AES-GCM 加密後，以<strong>密文</strong>存於本機；明文與密碼皆不儲存，每次開瀏覽器需輸入密碼解鎖。</li>
<li>已儲存的乘客資料<strong>不會回填顯示</strong>於設定畫面，只能重新輸入或刪除。</li>
<li>上述資料<strong>一律不上傳</strong>，僅用於在官方訂票頁自動填入你本人的欄位。</li>
</ul>

<h3>其他設定</h3>
<p>訂票偏好（路線、日期、票數、介面語言、提醒等）只存在<strong>你自己電腦的瀏覽器儲存區</strong>（<code>chrome.storage.local</code>），不會離開你的裝置，移除擴充時一併刪除。</p>

<h3>權限說明</h3>
<table>
<tr><th>權限</th><th>用途</th></tr>
<tr><td>storage</td><td>把你的訂票偏好與乘客資料存在本機（不外傳）</td></tr>
<tr><td>alarms、notifications</td><td>開賣／付款期限提醒的本機鬧鐘與通知，不經任何伺服器</td></tr>
<tr><td>afrts.forest.gov.tw</td><td>只在官方訂票頁執行代填；並在「開啟訂票頁面」時切換到已開啟的分頁</td></tr>
</table>
<p>擴充<strong>只在 <code>afrts.forest.gov.tw</code> 的訂票頁面上運作</strong>，不會在其他任何網站上執行。</p>

<h3>驗證碼</h3>
<p>本擴充<strong>不包含任何自動辨識或破解驗證碼的功能</strong>。驗證碼一律由使用者本人輸入。擴充只做「放大圖片」和「把游標移到輸入框」這類便利功能。</p>

<h3>合作連結與完成頁促銷</h3>
<p>訂票完成頁會顯示旅遊服務的<strong>合作連結</strong>（住宿、行程），明確標示、僅在你<strong>主動點擊</strong>時才前往外部網站，不自動導轉、不覆蓋任何既有聯盟參數。透過連結完成預訂本站可能獲少量分潤，<strong>對你的價格沒有影響</strong>。你可隨時關閉該面板或用總開關停用整個擴充。</p>
<p>完成頁的推薦內容可由<strong>本站自有網站</strong>提供（單向下載要顯示的文字與圖片），<strong>不會傳送你的任何資料、也不連任何第三方</strong>；未啟用時完成頁使用內建內容、完全不對外連線。</p>

<h3>資料分享</h3>
<p>本擴充不會上傳你的任何個人資料，技術上不具備將你的資料傳出的能力，<strong>沒有任何個人資料可以分享、出售或轉移</strong>給第三方。</p>

<h3>變更</h3>
<p>若本政策有變更，會更新本頁的日期。</p>

<h3>聯絡</h3>
<p>有任何疑問，請透過頁尾的「意見回饋」連結與我聯絡。</p>
</section>
</div></main>
"""
