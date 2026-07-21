# -*- coding: utf-8 -*-
from _build import STORE, FEEDBK, DONATE, aff_links
_A = aff_links("ja")
AFF_TOUR, AFF_STAY1, AFF_STAY2 = _A["tour"], _A["stay1"], _A["stay2"]

HERO = f"""
<div class="hero"><div class="wrap">
  <h1>阿里山森林鉄道の予約には、<br>知られていないルールがあります</h1>
  <p>いつ発売されるのか、なぜ遊楽区の入場券が必須なのか、券種をどう組み合わせれば弾かれないのか。公式サイトに散らばったルールをまとめ、フォームを自動入力する無料の Chrome 拡張機能もご用意しました。</p>
  <a class="cta" href="{STORE}" target="_blank" rel="noopener noreferrer">無料の拡張機能をインストール</a>
  <p class="cta-note">無料 · 個人情報を収集しません · 外部サーバーに接続しません · 認証コードは解読しません</p>
</div></div>
"""

BODY = f"""
<main><div class="wrap">

<section id="when">
<h2>1. いつ予約できるのか</h2>
<p>最もつまずきやすい点です。基本ルールは<strong>乗車日の1日前から14日前まで</strong>。ただし週末に例外があります。</p>
<table>
<tr><th>予約する曜日</th><th>予約できる最も先の日</th></tr>
<tr><td>月〜木</td><td>14日後まで</td></tr>
<tr><td>金曜日</td><td><strong>再来週の日曜日</strong>（16日後）</td></tr>
<tr><td>土曜日</td><td><strong>再来週の日曜日</strong>（15日後）</td></tr>
</table>
<div class="tip"><strong>ネット予約の受付時間は 06:00〜24:00 です。</strong>深夜0時から朝6時まではシステムが停止しています。人気の日は<strong>当日の朝6時</strong>が発売開始で、深夜0時ではありません。</div>
<h3>段階的に開放される区間</h3>
<ul>
<li>乗車日の14日前から：<strong>嘉義・北門 → 阿里山</strong>を優先的に発売</li>
<li>乗車日の<strong>3日前</strong>から：空席があれば<strong>嘉義 → 奮起湖</strong>も発売</li>
</ul>
<div class="note"><strong>祝山線（日の出）の特別ルール：</strong>翌日のチケットは、乗車前日の<strong>正午12時</strong>までに予約する必要があります。</div>
</section>

<section id="package">
<h2>2. 遊園地パッケージ — 最も間違えやすい部分</h2>
<p><strong>降車駅が遊楽区内</strong>（阿里山、二万坪）の場合、<strong>阿里山国家森林遊楽区の入場券</strong>を列車チケットと同時に購入する必要があります。</p>
<div class="note"><strong>重要なルール：券種ごとに「列車チケット」と「入場券」の枚数を一致させる必要があります。</strong>一致しないと送信できません。予約が通らない最大の原因です。</div>
<h3>入場券の種別</h3>
<table>
<tr><th>種別</th><th>料金</th><th>対象</th></tr>
<tr><td>おとな</td><td>150元</td><td>公共交通機関を利用し、乗車券の半券をお持ちの方</td></tr>
<tr><td>半額</td><td>100元</td><td>軍人・警察・学生、嘉義県市にお住まいの方、7〜12歳</td></tr>
<tr><td>優待割引</td><td>10元</td><td>3〜6歳、65歳以上、公認ガイド</td></tr>
<tr><td>無料</td><td>0元</td><td>0〜2歳、障害のある方と介助者1名、ボランティア、区内住民</td></tr>
</table>
<div class="tip">多くの方は<strong>おとな150元</strong>に該当します。公共交通機関で来て半券をお持ちであれば対象です。</div>
<h3>その他の制限</h3>
<ul>
<li>パッケージは<strong>分割販売されません</strong>。払い戻し・変更はセット単位です</li>
<li>列車チケットが<strong>無料</strong>の場合、<strong>座席は提供されません</strong></li>
<li>列車チケットと入場券がどちらも無料の場合、座席も乗車券も発行されません</li>
</ul>
</section>

<section id="tickets">
<h2>3. 列車チケットの券種</h2>
<table>
<tr><th>券種</th><th>対象</th></tr>
<tr><td>おとな</td><td>一般の成人</td></tr>
<tr><td>こども</td><td>乗車日に6歳以上12歳未満、または身長115〜150cm</td></tr>
<tr><td>シニア</td><td>乗車日に65歳以上の中華民国国民</td></tr>
<tr><td>身体障害者</td><td>障害者手帳をお持ちの方（記載があれば介助者1名も対象）</td></tr>
<tr><td>無料</td><td>6歳未満または115cm未満で座席を使わないお子様（大人の同伴が必要、1名につき2名まで）</td></tr>
</table>
<div class="note"><strong>乗車時は券種に対応する証明書の原本をご持参ください。</strong>提示できない場合、無券乗車として運賃を再度お支払いいただきます。</div>
<p>1つのID番号（またはパスポート番号）につき、<strong>同一路線・1乗車日あたり最大6枚</strong>。往復の場合は各6枚までです。</p>
</section>

<section id="pay">
<h2>4. お支払いと受け取り</h2>
<ul>
<li><strong>オンラインカード決済</strong> — 列車の確認後、すぐにお支払い</li>
<li><strong>セブン-イレブン</strong> — 予約番号で店内端末から支払い・発券、24時間対応、<strong>1枚につき10元の手数料</strong></li>
<li><strong>林鉄の駅窓口</strong> — 各駅の営業時間をご確認ください</li>
</ul>
<div class="note"><strong>未払いの予約は自動的にキャンセルされます。</strong>1か月に3回の支払い遅延で<strong>6か月の利用停止</strong>となります。</div>
</section>

<section id="faq">
<h2>5. よくある質問</h2>
<div class="card">
<div class="faq"><b>「満席」と表示されました。どうすれば？</b>
<span>まず前日か翌日を試してください。人気の日でも1日ずらすと空いていることがよくあります。乗車日が3日以内なら「嘉義 → 奮起湖」も試す価値があります。枚数を減らすのも有効です。</span></div>
<div class="faq"><b>希望の日付が選べません</b>
<span>発売期間外です。上の表で確認するか、拡張機能のカレンダーをご利用ください。選べない日はグレー表示になり、いつ発売されるかが表示されます。</span></div>
<div class="faq"><b>複数のタブで同時に予約できますか？</b>
<span>できません。複数ウィンドウは検知され、警告が表示されます。1つのタブでご利用ください。</span></div>
<div class="faq"><b>座席は選べますか？</b>
<span>選べません。システムが自動で割り当てます。空席がある場合は連続した席が優先されます。</span></div>
</div>
</section>

<section id="ext">
<h2>6. 拡張機能でできること</h2>
<p>上記のルールはすべて拡張機能に組み込まれています。予約ページを開くと：</p>
<ul>
<li><strong>検索条件を自動入力</strong> — 路線・日付・駅・枚数をまとめて</li>
<li><strong>パッケージの枚数合わせ</strong> — 1枚ごとに入場券の種別を選択、枚数は常に一致</li>
<li><strong>予約可能な日だけ表示</strong> — それ以外は発売日をお知らせ</li>
<li><strong>認証コードを拡大</strong> — 元画像は80×30ピクセル。3倍で格段に見やすく</li>
<li><strong>公式カウントダウンを検知</strong> — 事前に入力を済ませ、発売と同時にカーソルを移動</li>
<li><strong>満席時のショートカット</strong> — 日付・区間・枚数をワンクリックで変更</li>
<li><strong>空席スキャン</strong> — 日ごとに確認し、列車ごとの残席数も表示</li>
</ul>
<div class="note"><strong>認証コードの解読は行いません。できません。</strong>認証コードは必ずご自身で入力していただきます。これは大量の自動予約を防ぐための公式の仕組みであり、回避することはしません。拡張機能は繰り返しの入力作業を速くし、その4文字に集中できるようにするためのものです。</div>
<p style="margin-top:16px"><a class="cta" href="{STORE}" target="_blank" rel="noopener noreferrer">無料の拡張機能をインストール</a></p>
</section>

<section id="more">
<h2>7. 旅の準備</h2>
<div class="disclose">以下は<strong>提携リンク</strong>です。ご予約いただくと当サイトに少額の紹介料が入る場合がありますが、お客様の料金は変わりません。各サイトで直接検索していただいても構いません。</div>
<div class="links">
  <a href="{AFF_STAY1}" target="_blank" rel="noopener noreferrer"><b>阿里山神木賓館</b><span>阿里山駅から約 400 m、降りてすぐ</span></a>
  <a href="{AFF_STAY2}" target="_blank" rel="noopener noreferrer"><b>禾楓別墅（Ho Fong Villa Hotel）</b><span>同じく阿里山エリア内。空室と料金を確認できます</span></a>
  <a href="{AFF_TOUR}" target="_blank" rel="noopener noreferrer"><b>阿里山 日帰りツアー・現地体験</b><span>日の出、神木、トレイル</span></a>
</div>
<h3 style="margin-top:26px">お役に立ちましたか？</h3>
<div class="links">
  <a href="{FEEDBK}" target="_blank" rel="noopener noreferrer"><b>不具合の報告・ご意見</b><span>公式サイト変更時のご報告が特に助かります</span></a>
  <a href="{DONATE}" target="_blank" rel="noopener noreferrer"><b>コーヒーをおごる</b><span>拡張機能は無料です。支援は任意です</span></a>
</div>
</section>

</div></main>
"""

PRIVACY = """
<main><div class="wrap">
<section>
<h2>プライバシーポリシー</h2>
<p style="color:var(--muted);font-size:14px">最終更新：2026年7月</p>

<div class="tip"><strong>基本方針：本拡張機能はお客様の個人情報を一切アップロードせず、追跡もせず、アナリティクスや広告も含みません。入力した情報はご自身のブラウザ内にとどまります。</strong></div>

<h3>個人情報（搭乗者情報）</h3>
<p>公式予約サイトの搭乗者欄を自動入力するため、本拡張機能は「搭乗者情報」機能（ID／パスポート番号・電話・メール）を提供します。これは<strong>任意</strong>で、セキュリティ優先で設計されています：</p>
<ul>
<li><strong>既定は「今回のみ」</strong>：ブラウザのメモリ（<code>chrome.storage.session</code>）にのみ保持し、<strong>ディスクには書き込まず、ブラウザを閉じると消去</strong>されます。</li>
<li><strong>任意の「暗号化して記憶」</strong>：お客様が設定したパスワードで PBKDF2-SHA256 ＋ AES-GCM により暗号化し、<strong>暗号文のみ</strong>をローカル保存します。平文もパスワードも保存せず、ブラウザを開くたびにパスワードで解錠します。</li>
<li>保存済みの搭乗者情報は設定画面に<strong>再表示されません</strong>。再入力または削除のみ可能です。</li>
<li>これらの情報は<strong>一切アップロードされず</strong>、公式予約ページでご自身の欄を埋めるためだけに使われます。</li>
</ul>

<h3>設定の保存場所</h3>
<p>予約の設定（路線・日付・枚数・表示言語・リマインダーなど）は<strong>お使いのブラウザのローカルストレージ</strong>（<code>chrome.storage.local</code>）にのみ保存されます。デバイスの外に出ることはなく、拡張機能を削除すると一緒に削除されます。</p>

<h3>権限について</h3>
<table>
<tr><th>権限</th><th>用途</th></tr>
<tr><td>storage</td><td>予約設定と搭乗者情報をローカルに保存（外部送信なし）</td></tr>
<tr><td>alarms、notifications</td><td>発売・支払期限のリマインダー用のローカルアラームと通知。サーバーは介在しません</td></tr>
<tr><td>afrts.forest.gov.tw</td><td>公式予約サイトでのみ自動入力を実行。既に開いている予約タブへの切り替えにも使用</td></tr>
</table>
<p>本拡張機能は<strong><code>afrts.forest.gov.tw</code> の予約ページでのみ動作</strong>し、他のサイトでは一切動作しません。</p>

<h3>認証コードについて</h3>
<p>本拡張機能には<strong>認証コードの解読・回避を行うコードは一切含まれていません</strong>。認証コードは必ずご自身で入力していただきます。拡張機能が行うのは画像の拡大とカーソル移動のみです。</p>

<h3>提携リンクと完了ページのおすすめ</h3>
<p>予約完了後、旅行サービスの<strong>提携リンク</strong>（宿泊・ツアー）を明示して表示します。<strong>お客様がクリックした場合のみ</strong>外部サイトへ移動し、自動転送はせず、既存のアフィリエイトパラメータも上書きしません。ご予約いただくと当サイトに少額の紹介料が入る場合がありますが、<strong>料金は変わりません</strong>。パネルは閉じられ、マスタースイッチで拡張機能全体を無効にもできます。</p>
<p>完了ページのおすすめ内容は<strong>当サイト自身のウェブサイト</strong>から提供される場合があります（表示するテキストと画像を一方向でダウンロード）。これは<strong>お客様のデータを一切送信せず、第三者にも接続しません</strong>。無効の場合、完了ページは組み込みの内容を使い、外部接続を一切行いません。</p>

<h3>データの共有</h3>
<p>本拡張機能はお客様の個人情報を一切アップロードせず、技術的に外部へ送信する能力を持たないため、<strong>共有・販売・移転する個人情報は存在しません</strong>。</p>

<h3>変更について</h3>
<p>本ポリシーを変更した場合は上記の日付を更新します。</p>

<h3>お問い合わせ</h3>
<p>ご質問はフッターの「ご意見」リンクからお願いします。</p>
</section>
</div></main>
"""
