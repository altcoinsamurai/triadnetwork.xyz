import re

# ---------- 1. Build the new article from the originality shell ----------
shell = open('articles/originality-above-everything.html').read()

head_end = shell.index('<article class="research">')
head = shell[:head_end]
foot = shell[shell.index('<div class="sf-footer"'):]

head = re.sub(r'<title>[^<]*</title>', '<title>Customer Acquisition at Birth · Triad Research</title>', head)
head = re.sub(r'(property="og:title" content=")[^"]*(")', r'\1Customer Acquisition at Birth\2', head)
head = re.sub(r'(property="og:description" content=")[^"]*(")', r'\1Robinhood is now sole initial trustee of a federal program that opens an investment account for every American newborn. The distribution read.\2', head)
head = re.sub(r'(property="og:image" content=")[^"]*(")', r'\1https://triadnetwork.xyz/assets/tenev-stanford.jpg\2', head)

BODY = '''<article class="research">
  <div class="research-eyebrow">Triad Research · Memo 04 · Distribution</div>
  <h1 class="research-title">Customer Acquisition <em>at Birth</em></h1>
  <p class="research-deck">Robinhood is now the sole initial trustee of a federal program that opens an investment account for every eligible American newborn. Set the politics aside. Read it as distribution.</p>

  <div class="research-meta">
    <span><strong>Author</strong> &nbsp; <a href="https://x.com/Altcoinsamurai" target="_blank" style="color:var(--teal);text-decoration:none;font-weight:600">@Altcoinsamurai</a></span>
    <span class="research-meta-divider">·</span>
    <span><strong>Published</strong> &nbsp; July 2026</span>
    <span class="research-meta-divider">·</span>
    <span><strong>Read</strong> &nbsp; 7 min</span>
    <span class="research-meta-divider">·</span>
    <span><strong>Sources</strong> &nbsp; 10 citations</span>
  </div>

  <figure style="margin:0 0 34px">
    <img src="/assets/tenev-stanford.jpg" alt="Vlad Tenev speaking at Stanford Directors' College" style="width:100%;border-radius:6px;display:block">
    <figcaption style="font-family:var(--mono);font-size:11px;color:var(--ink-mute);margin-top:10px;letter-spacing:.04em">Robinhood CEO Vlad Tenev at Stanford Directors' College, 2026. Photo via Stanford Rock Center on X.</figcaption>
  </figure>

  <div class="disclaimer-research">
    <strong>On the numbers</strong>
    Every figure links to a public source at the end of the page: Treasury and Robinhood announcements, and reporting from CNBC, Forbes, CNN and The 19th. This memo is distribution analysis, not political commentary, and not financial advice.
  </div>

  <h2><span class="section-num">§ 01</span>What happened</h2>

  <p>On July 4, the country's 250th birthday, the US Treasury launched Trump Accounts: tax-advantaged investment accounts for American children, with a $1,000 federal contribution for every eligible child born between 2025 and 2028<a href="#ref-1" class="cite">[1]</a>. Two days later the President rang the NYSE opening bell from the Oval Office as the first deposits landed<a href="#ref-8" class="cite">[8]</a>.</p>

  <p>The branding is loud and the politics are not our subject. Our subject is one line in the program structure: <strong>Robinhood Securities serves as broker and sole initial trustee</strong>, with BNY as the Treasury's financial agent<a href="#ref-1" class="cite">[1]</a><a href="#ref-2" class="cite">[2]</a>. Selected in April, live in July<a href="#ref-9" class="cite">[9]</a>. Vlad Tenev spent launch week on CNBC, Bloomberg and Fox describing his company's new role as, in his words, a government subcontractor<a href="#ref-10" class="cite">[10]</a>.</p>

  <p>Strip everything else away and look at what the company actually acquired. We think it is the largest customer-acquisition event in fintech history.</p>

  <h2><span class="section-num">§ 02</span>The arithmetic of default</h2>

  <p>Roughly 14.3 million babies are expected to be born in the US between 2025 and 2028, which puts the federal seed program at about $14.3 billion<a href="#ref-4" class="cite">[4]</a>. Before launch day, more than 6 million accounts had already been opened, around 1.4 million of them eligible for the $1,000 seed, and 86% of applicant families earn under $200,000<a href="#ref-5" class="cite">[5]</a><a href="#ref-6" class="cite">[6]</a>. This is not a product for the top decile. It is a default for everyone.</p>

  <p>Then look at who is stacking money on top. The Dell Foundation pledged $6.25 billion to add $250 for an estimated 25 million children<a href="#ref-4" class="cite">[4]</a>. Ray Dalio is funding top-ups in Connecticut<a href="#ref-4" class="cite">[4]</a>. SpaceX's president announced share donations into more than 2 million accounts<a href="#ref-5" class="cite">[5]</a>. Over 50 companies, from Micron to Schwab, are matching the federal $1,000 for employees' children<a href="#ref-4" class="cite">[4]</a>. Families, friends and employers can add up to $5,000 a year on top of all of it<a href="#ref-7" class="cite">[7]</a>.</p>

  <p>Now follow who pays and who collects. The Treasury funds the deposits. Dell and Dalio fund the top-ups. Employers fund the matches. And Robinhood, the trustee, collects the customer relationship. Its acquisition cost per funded account rounds to zero.</p>

  <h2><span class="section-num">§ 03</span>The state as a channel</h2>

  <p>The distribution mechanics are the part worth studying. The Social Security Administration now lets parents open a Trump Account at the hospital, in the same flow as registering the newborn's Social Security number<a href="#ref-6" class="cite">[6]</a>. State child-welfare agencies can open accounts for foster children, with about half of states signed up<a href="#ref-6" class="cite">[6]</a>. Enrollment otherwise runs through an IRS form and an app that families download to activate and track the account, an app built in partnership with Robinhood<a href="#ref-3" class="cite">[3]</a>.</p>

  <p>Every fintech on earth pays real money for a funded account. Hundreds of dollars per user is normal, and the deposit bonuses come out of the company's own pocket. Here, sign-up is embedded in the paperwork of being born, the deposit comes from the government, and the app on the family's phone belongs to the trustee.</p>

  <p>A channel is any surface where your customer already has to be. There is no surface more universal than a birth certificate.</p>

  <h2><span class="section-num">§ 04</span>The 2043 cohort</h2>

  <p>The accounts are built for lock-in by law, not by product design. Funds sit in low-cost US equity index funds and generally cannot be touched before the child turns 18<a href="#ref-7" class="cite">[7]</a>. At 18, the account converts into a traditional IRA and the child takes control<a href="#ref-5" class="cite">[5]</a>.</p>

  <p>Run the dates. A child born this year takes control in 2044. Robinhood has, in one program, signed a cohort of customers who structurally cannot churn for eighteen years, and who will each be handed a funded retirement account at the exact moment they become adult investors, inside an app their family has been checking since the week they were born.</p>

  <p>Nobody has ever bought loyalty that early or held it that long. The program does not guarantee those 18-year-olds stay. It guarantees Robinhood is the incumbent when the decision gets made, 14 million times, on a schedule that runs into the 2040s.</p>

  <h2><span class="section-num">§ 05</span>The pattern, and the caveats</h2>

  <p>There is a bigger arc here. Robinhood has spent this cycle becoming the rail other businesses run on: Kalshi, the fastest-scaling app of 2026, routes more than half of its trading volume through its Robinhood integration<a href="#ref-11" class="cite">[11]</a>. Now the US Treasury runs a national savings program on Robinhood's trusteeship. The company everyone borrows rails from just borrowed the biggest rail in existence: the state itself.</p>

  <p>For anyone building distribution, the lesson repeats. Audiences are rented. Channels are borrowed. The durable position is being the infrastructure that other people's programs get built on, and the second-best position is borrowing a channel your customers already cannot avoid.</p>

  <p>The caveats, stated plainly. This is a politically branded program, and political programs carry regime risk: Robinhood is the initial trustee, not a permanent one, and a future administration can restructure or re-tender the mandate. Researchers already flag that unequal family contributions could compound wealth gaps rather than close them<a href="#ref-4" class="cite">[4]</a>. And a single broker as sole initial trustee of a national program is a concentration the next Treasury may well revisit.</p>

  <p>None of that changes the distribution fact. As of July 4, 2026, being born in America comes with a brokerage account, and one company is the counterparty. Customer acquisition has a new ceiling.</p>

  <div class="research-end">
    Triad Research · Memo 04 · <strong>Distribution Series</strong>
  </div>

  <!-- ═══════════ REFERENCES ═══════════ -->
  <div class="references">
    <h2>Sources &amp; References</h2>
    <ul class="ref-list">
      <li class="ref-item" id="ref-1">"Trump Accounts Officially Launch." Robinhood Newsroom, July 6, 2026. Trustee and broker role, launch mechanics, Tenev statement. <a href="https://robinhood.com/us/en/newsroom/trump-accounts-officially-launch/" target="_blank">robinhood.com/us/en/newsroom/trump-accounts-officially-launch</a></li>
      <li class="ref-item" id="ref-2">"Trump Accounts Launch to All Eligible American Families." BNY press release, July 6, 2026. BNY as financial agent; program infrastructure. <a href="https://www.bny.com/corporate/global/en/about-us/newsroom/press-release/trump-accounts-launch-eligible-american-families.html" target="_blank">bny.com/corporate/newsroom</a></li>
      <li class="ref-item" id="ref-3">"Trump Accounts for kids launched July 4: What parents need to know." CNBC, July 1, 2026. Account mechanics, app partnership, enrollment. <a href="https://www.cnbc.com/2026/07/01/trump-accounts-launch-july-4.html" target="_blank">cnbc.com/2026/07/01/trump-accounts-launch-july-4</a></li>
      <li class="ref-item" id="ref-4">"Trump's Investment Accounts For Kids Launch Tomorrow." Forbes, July 3, 2026. 14.3M projected births, $14.3B cost, employer matches, Dell $6.25B pledge, contribution-inequality research. <a href="https://www.forbes.com/sites/maryroeloffs/2026/07/03/trumps-investment-accounts-for-kids-launch-tomorrow-how-to-register/" target="_blank">forbes.com</a></li>
      <li class="ref-item" id="ref-5">"Trump Accounts are now live. Here's what you need to know." CNN Business, July 4, 2026. 6M+ accounts, 1.4M seed-eligible, SpaceX share donations, IRA conversion at 18. <a href="https://www.cnn.com/2026/07/04/business/trump-accounts-faq" target="_blank">cnn.com/2026/07/04/business/trump-accounts-faq</a></li>
      <li class="ref-item" id="ref-6">"What are Trump Accounts for kids?" The 19th, July 6, 2026. SSA hospital enrollment, Fostering the Future, applicant income distribution. <a href="https://19thnews.org/2026/07/trump-accounts-children-savings-eligibility/" target="_blank">19thnews.org</a></li>
      <li class="ref-item" id="ref-7">"Trump Accounts: Long-Term Investing for the Next Generation." Robinhood Learn, 2026. Contribution limits, index-fund restriction, age-18 rules. <a href="https://learn.robinhood.com/articles/trump-accounts/" target="_blank">learn.robinhood.com/articles/trump-accounts</a></li>
      <li class="ref-item" id="ref-8">"Robinhood CEO Vlad Tenev breaks down how Trump Accounts work." CBS News via Social News XYZ, July 6, 2026. Oval Office NYSE bell. <a href="https://www.socialnews.xyz/2026/07/06/robinhood-ceo-vlad-tenev-breaks-down-how-trump-accounts-work-video/" target="_blank">socialnews.xyz</a></li>
      <li class="ref-item" id="ref-9">"Robinhood Launches Trump Accounts App Ahead Of July 4 Rollout." Benzinga via Yahoo Finance, July 2026. April selection of Robinhood and BNY by Treasury. <a href="https://finance.yahoo.com/markets/stocks/articles/robinhood-launches-trump-accounts-app-180107673.html" target="_blank">finance.yahoo.com</a></li>
      <li class="ref-item" id="ref-10">"Watch CNBC's full interview with Robinhood CEO Vlad Tenev." CNBC, July 6, 2026. Government-subcontractor framing. <a href="https://www.cnbc.com/video/2026/07/06/watch-cnbcas-full-interview-with-robinhood-ceo-vlad-tenev.html" target="_blank">cnbc.com</a></li>
      <li class="ref-item" id="ref-11">"Kalshi." TSG Invest analysis, April 2026. Robinhood integration share of Kalshi volume. <a href="https://tsginvest.com/kalshi/" target="_blank">tsginvest.com/kalshi</a></li>
    </ul>
  </div>

'''

new_article = head + BODY + foot
open('articles/customer-acquisition-at-birth.html', 'w').write(new_article)
print('article written:', len(new_article), 'bytes')

# dash check on body
b = BODY
print('em/en dashes in new body:', b.count('\u2014') + b.count('\u2013'))

# ---------- 2. Homepage swaps ----------
h = open('home.html').read()

old_featured_href = '<a href="/articles/originality-above-everything.html" class="click-card reveal" style="grid-row:1/3'
assert old_featured_href in h

# featured -> new article
h = h.replace("url('/assets/originality-card.png')", "url('/assets/tenev-stanford.jpg')")
h = h.replace('<a href="/articles/originality-above-everything.html" class="click-card reveal" style="grid-row:1/3',
              '<a href="/articles/customer-acquisition-at-birth.html" class="click-card reveal" style="grid-row:1/3')
h = h.replace('>Manifesto · Founder Note</span>', '>Research · Distribution</span>', 1)
h = h.replace('<h3 style="font-size:22px;margin-bottom:8px;line-height:1.3;color:#fff">Originality, Above Everything</h3>',
              '<h3 style="font-size:22px;margin-bottom:8px;line-height:1.3;color:#fff">Customer Acquisition at Birth</h3>')
h = h.replace("<p style=\"font-size:13px;color:rgba(255,255,255,.78);margin-bottom:12px;line-height:1.5\">A founder note on what crypto creator agencies select for, and why Triad's bar is structurally different. The case for the only filter that compounds.</p>",
              "<p style=\"font-size:13px;color:rgba(255,255,255,.78);margin-bottom:12px;line-height:1.5\">Robinhood is now sole initial trustee of a federal program seeding every American newborn with $1,000. The distribution read on the largest customer-acquisition event in fintech history.</p>")
h = h.replace('<span style="font-family:var(--mono);font-size:10px;color:rgba(255,255,255,.55)">May 2026 &middot; 11 min read</span>',
              '<span style="font-family:var(--mono);font-size:10px;color:rgba(255,255,255,.55)">July 2026 &middot; 7 min read</span>')

# Taisys small card -> Originality
old_card = '''<a href="/articles/nero-taisys-mwc.html" class="click-card reveal">
      <span style="font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-weight:500;display:inline-block;padding:3px 10px;background:rgba(0,191,166,.12);border-radius:100px;margin-bottom:12px">Partnership</span>
      <h3 style="font-size:17px;margin-bottom:6px;line-height:1.3">NERO Chain x Taisys: Wallet Auth at MWC Barcelona</h3>
      <p style="font-size:12px;color:var(--text2);margin-bottom:8px">Web2-grade mobile security meets Web3 infrastructure. Signed on-site at MWC.</p>
      <span style="font-family:var(--mono);font-size:10px;color:var(--text3)">April 2026 &middot; 5 min read</span>
    </a>'''
new_card = '''<a href="/articles/originality-above-everything.html" class="click-card reveal">
      <span style="font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-weight:500;display:inline-block;padding:3px 10px;background:rgba(0,191,166,.12);border-radius:100px;margin-bottom:12px">Manifesto &middot; Founder Note</span>
      <h3 style="font-size:17px;margin-bottom:6px;line-height:1.3">Originality, Above Everything</h3>
      <p style="font-size:12px;color:var(--text2);margin-bottom:8px">A founder note on what crypto creator agencies select for. The case for the only filter that compounds.</p>
      <span style="font-family:var(--mono);font-size:10px;color:var(--text3)">May 2026 &middot; 8 min read</span>
    </a>'''
assert old_card in h
h = h.replace(old_card, new_card)

open('home.html', 'w').write(h)
print('home.html swapped')
