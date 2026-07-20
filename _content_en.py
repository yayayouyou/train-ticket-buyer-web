# -*- coding: utf-8 -*-
from _build import STORE, FEEDBK, DONATE, aff_links
_A = aff_links("en")
AFF_TOUR, AFF_STAY1, AFF_STAY2 = _A["tour"], _A["stay1"], _A["stay2"]

HERO = f"""
<div class="hero"><div class="wrap">
  <h1>Booking the Alishan Forest Railway<br>follows rules most people miss</h1>
  <p>When tickets open, why you are forced to buy a park admission ticket, and how to match ticket types so your booking is not rejected. This page collects the official rules scattered across the operator's site — plus a free Chrome extension that fills the form for you.</p>
  <a class="cta" href="{STORE}" target="_blank" rel="noopener noreferrer">Install the free extension</a>
  <p class="cta-note">Free · Collects no personal data · Contacts no external server · Never solves captchas</p>
</div></div>
"""

BODY = f"""
<main><div class="wrap">

<section id="when">
<h2>1. When do tickets go on sale?</h2>
<p>This is where most people get stuck. The rule is <strong>1 to 14 days before your travel date</strong> — with a weekend exception.</p>
<table>
<tr><th>Day you book</th><th>Furthest date available</th></tr>
<tr><td>Mon – Thu</td><td>14 days ahead</td></tr>
<tr><td>Friday</td><td><strong>The Sunday after next</strong> (16 days)</td></tr>
<tr><td>Saturday</td><td><strong>The Sunday after next</strong> (15 days)</td></tr>
</table>
<div class="tip"><strong>Online booking runs 06:00–24:00.</strong> The system is closed between midnight and 6 am — so for a popular date, tickets open at <strong>6 am that morning</strong>, not at midnight.</div>
<h3>Two staged-release rules</h3>
<ul>
<li>From 14 days out: <strong>Chiayi / Beimen → Alishan</strong> is released first</li>
<li>From <strong>3 days</strong> out: <strong>Chiayi → Fenqihu</strong> opens, if seats remain</li>
</ul>
<div class="note"><strong>Zhushan Line (sunrise trains):</strong> next-day tickets must be booked before <strong>12:00 noon</strong> the day before.</div>
</section>

<section id="package">
<h2>2. The recreation area package — the easiest thing to get wrong</h2>
<p>If your <strong>destination is inside the recreation area</strong> (Alishan, Erwanping), the system forces you to buy an <strong>Alishan National Forest Recreation Area admission ticket</strong> together with the train ticket.</p>
<div class="note"><strong>The key rule: for each ticket category, the number of train tickets must equal the number of admission tickets.</strong> If they do not match, the form will not submit. This is the single most common reason bookings fail.</div>
<h3>Admission ticket types</h3>
<table>
<tr><th>Type</th><th>Price</th><th>Who qualifies</th></tr>
<tr><td>Full</td><td>NT$150</td><td>Arriving by public transport (keep your ticket stub)</td></tr>
<tr><td>Half</td><td>NT$100</td><td>Military, police, students, Chiayi county/city residents, ages 7–12</td></tr>
<tr><td>Concession</td><td>NT$10</td><td>Ages 3–6, aged 65+, licensed tour guides</td></tr>
<tr><td>Exempt</td><td>NT$0</td><td>Ages 0–2, disabled visitors plus one companion, volunteers, local residents</td></tr>
</table>
<div class="tip">Most visitors take the <strong>NT$150 full ticket</strong> — if you arrived by public transport with a ticket stub, you qualify.</div>
<h3>Other package restrictions</h3>
<ul>
<li>The package <strong>cannot be split</strong> — refunds and changes apply to the whole set</li>
<li>If the train ticket is <strong>exempt</strong>, <strong>no seat is assigned</strong></li>
<li>If both train ticket and admission are exempt, no seat and no ticket is issued</li>
</ul>
</section>

<section id="tickets">
<h2>3. Train ticket categories</h2>
<table>
<tr><th>Category</th><th>Who qualifies</th></tr>
<tr><td>Adult</td><td>General adult</td></tr>
<tr><td>Child</td><td>Aged 6–11 on the travel date, or 115–150 cm tall</td></tr>
<tr><td>Senior</td><td>Aged 65+ (ROC nationals)</td></tr>
<tr><td>Disabled</td><td>Holders of a disability certificate (plus one companion if endorsed)</td></tr>
<tr><td>Free</td><td>Under 6 or under 115 cm, not occupying a seat, accompanied by an adult (max 2 per passenger); licensed guides not occupying a seat</td></tr>
</table>
<div class="note"><strong>Bring original documents matching your ticket type.</strong> If you cannot show them during inspection, you are treated as travelling without a ticket and must pay the fare again.</div>
<p>Each ID or passport number may book <strong>up to 6 tickets per line, per travel date</strong>; up to 6 each way for return trips.</p>
</section>

<section id="pay">
<h2>4. Payment and ticket collection</h2>
<ul>
<li><strong>Online card payment</strong> — pay immediately after confirming your train</li>
<li><strong>7-Eleven</strong> — pay and collect at a store kiosk with your booking number, 24 hours, <strong>NT$10 service fee per ticket</strong></li>
<li><strong>Railway stations</strong> — check each station's opening hours</li>
</ul>
<div class="note"><strong>Unpaid bookings are cancelled automatically.</strong> Three late payments within one month results in a <strong>6-month suspension</strong>.</div>
</section>

<section id="faq">
<h2>5. Common questions</h2>
<div class="card">
<div class="faq"><b>It says the trains are sold out. What now?</b>
<span>Try one day earlier or later first — popular dates are often available just a day apart. If your travel date is within 3 days, also try Chiayi → Fenqihu, which opens later and usually has more seats. Reducing the number of tickets can also help.</span></div>
<div class="faq"><b>Why can I not select the date I want?</b>
<span>It is outside the release window. Check the table in section 1, or use the extension's calendar — unavailable dates are greyed out and it tells you exactly when each one opens.</span></div>
<div class="faq"><b>Can I open several tabs to book faster?</b>
<span>No. The site detects multiple windows and warns you. Use one tab.</span></div>
<div class="faq"><b>Can I choose my seat?</b>
<span>No. Seats are assigned automatically, with consecutive seats given priority when available.</span></div>
</div>
</section>

<section id="ext">
<h2>6. What the extension does</h2>
<p>Every rule above is built into the extension. Open the booking page and it will:</p>
<ul>
<li><strong>Fill in your search criteria</strong> — line, date, stations and ticket counts in one go</li>
<li><strong>Handle the package matrix</strong> — pick an admission type per ticket; counts always match</li>
<li><strong>Show only bookable dates</strong> — and tell you when the others open</li>
<li><strong>Enlarge the captcha</strong> — the original is only 80×30 pixels; 3× is far easier to read</li>
<li><strong>Detect the official countdown</strong> — everything is pre-filled, then your cursor lands in the captcha box</li>
<li><strong>Offer shortcuts when sold out</strong> — change day, route or ticket count in one click</li>
<li><strong>Scan for seats</strong> — check day by day and read how many seats remain per train</li>
</ul>
<div class="note"><strong>It does not and cannot solve captchas.</strong> You always type them yourself — that is the operator's safeguard against bulk automated booking, and we do not work around it. The extension makes the repetitive form-filling fast so you can focus on those four characters.</div>
<p style="margin-top:16px"><a class="cta" href="{STORE}" target="_blank" rel="noopener noreferrer">Install the free extension</a></p>
</section>

<section id="more">
<h2>7. Planning the rest of your trip</h2>
<div class="disclose">The links below are <strong>partner links</strong>. If you book through them this site may earn a small commission, at no extra cost to you. You are equally welcome to search these platforms directly.</div>
<div class="links">
  <a href="{AFF_STAY1}" target="_blank" rel="noopener noreferrer"><b>Alishan Shermuh Hotel</b><span>About 400 m from Alishan Station</span></a>
  <a href="{AFF_STAY2}" target="_blank" rel="noopener noreferrer"><b>Ho Fong Villa Hotel</b><span>Also inside the Alishan area — check rooms and rates</span></a>
  <a href="{AFF_TOUR}" target="_blank" rel="noopener noreferrer"><b>Alishan day tours</b><span>Sunrise, sacred trees, hiking trails</span></a>
</div>
<h3 style="margin-top:26px">Was this useful?</h3>
<div class="links">
  <a href="{FEEDBK}" target="_blank" rel="noopener noreferrer"><b>Report a problem / suggest</b><span>Especially valuable when the official site changes</span></a>
  <a href="{DONATE}" target="_blank" rel="noopener noreferrer"><b>Buy me a coffee</b><span>The extension is free — tips are optional</span></a>
</div>
</section>

</div></main>
"""

PRIVACY = """
<main><div class="wrap">
<section>
<h2>Privacy policy</h2>
<p style="color:var(--muted);font-size:14px">Last updated: July 2026</p>

<div class="tip"><strong>Short version: this extension collects none of your data and sends nothing to any external server.</strong></div>

<h3>What we collect</h3>
<p><strong>Nothing.</strong> The extension collects, stores and transmits no personal data.</p>
<ul>
<li>It never asks for or stores ID numbers, passport numbers, phone numbers or email addresses</li>
<li>It does not track your browsing</li>
<li>It uses no analytics or tracking services</li>
<li>It loads no external images, fonts or scripts</li>
</ul>

<h3>Where your settings live</h3>
<p>Your booking preferences (line, date, ticket counts, interface language and so on) are stored only in <strong>your own browser's local storage</strong> (<code>chrome.storage.local</code>). This data never leaves your device and is deleted when you remove the extension.</p>

<h3>Permissions</h3>
<table>
<tr><th>Permission</th><th>Why</th></tr>
<tr><td>storage</td><td>Save your booking preferences locally</td></tr>
<tr><td>tabs</td><td>The "open booking site" button; switches to an existing tab instead of opening a duplicate</td></tr>
<tr><td>alarms</td><td>Local reminders for when tickets go on sale</td></tr>
<tr><td>notifications</td><td>Show the reminder when it fires</td></tr>
<tr><td>afrts.forest.gov.tw</td><td>Run form-filling only on the official booking site</td></tr>
</table>
<p>The extension runs <strong>only on <code>afrts.forest.gov.tw</code></strong> booking pages, never on any other website.</p>

<h3>Captchas</h3>
<p>This extension contains <strong>no captcha recognition or bypass code whatsoever</strong>. Captchas are always typed by you. The extension only enlarges the image and moves your cursor to the input box.</p>

<h3>External links</h3>
<p>After a successful booking the extension shows travel <strong>partner links</strong> (accommodation, tours), clearly labelled as such. These links:</p>
<ul>
<li>are followed only when <strong>you click them</strong></li>
<li>never redirect automatically or send background requests</li>
<li>never overwrite or modify any existing affiliate parameters</li>
<li>can be dismissed, or disabled entirely with the master switch</li>
</ul>
<p>Clicking takes you to a third-party site with its own privacy policy. If you book through these links this site may earn a small commission, at no extra cost to you.</p>

<h3>Data sharing</h3>
<p>Since we collect no data, there is <strong>no data to share, sell or transfer</strong> to anyone.</p>

<h3>Changes</h3>
<p>If this policy changes, the date above will be updated. If any future feature requires a network connection, it will be described here before that update ships.</p>

<h3>Contact</h3>
<p>Questions? Use the feedback link in the footer.</p>
</section>
</div></main>
"""
