# -*- coding: utf-8 -*-
"""Tools: index + Private Practice Revenue Estimator."""
import engine as S

PAGES = []

# -------- Tools index --------
def _tool_cards():
    cards = [
        S.card("Private practice revenue estimator", "See how visit volume, pricing, payer mix, and overhead shape what an independent psychiatry practice actually nets. Educational, not financial advice.", "/tools/private-practice-revenue-estimator/", tag="Live tool", tagclass="tag--blue", more="Open tool"),
        S.card("Residency program explorer", "Filter and compare psychiatry residency programs. In development.", "/contact/", tag="Planned", tagclass="tag--olive", more="Suggest a feature"),
        S.card("Psychiatry workforce map", "Mental health shortage areas by state, built from HRSA data. In development.", "/contact/", tag="Planned", tagclass="tag--olive", more="Suggest a feature"),
        S.card("Salary explorer", "Compensation by practice type, setting, and experience. In development.", "/contact/", tag="Planned", tagclass="tag--olive", more="Suggest a feature"),
    ]
    return S.card_grid(cards, 2)

PAGES.append({
    "slug": "tools", "active": "/tools/",
    "title": "Tools | shrinkiatry",
    "desc": "Educational tools for understanding the profession of psychiatry: a private-practice revenue estimator, with a workforce map, residency explorer, and salary explorer in development.",
    "breadcrumbs": [("Home", "/"), ("Tools", None)],
    "body": (
        f"""<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">Tools</span></nav>
<span class="eyebrow">Tools</span><h1 class="mt-1">Tools for understanding the profession</h1>
<p class="hero__sub mt-2" style="max-width:54ch">Useful, educational tools rather than gimmicks. Built to be bookmarked, sourced where they use data, and clear about what they are and aren't.</p>
</div></section>
<section class="section section--surface"><div class="wrap"><div class="maxread flow">
<p>shrinkiatry's tools are meant to make the structure of the profession legible: what a practice earns, where the workforce is thin, how programs compare. They're educational. None of them is medical, legal, or financial advice, and none of them replaces a professional who knows your specific situation.</p>
</div><div class="mt-4">{_tool_cards()}</div></div></section>
<section class="section section--tint"><div class="wrap"><div class="maxread">{S.network_continue(["shrinkmd","anxietyresearch","shrinknetwork"])}</div></div></section>"""
    ),
})

# -------- Revenue estimator (interactive) --------
TOOL_SCHEMA = {
    "@type": "SoftwareApplication",
    "name": "Private Practice Revenue Estimator",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "Web",
    "url": "https://shrinkiatry.com/tools/private-practice-revenue-estimator/",
    "description": "An educational calculator that estimates gross and net annual revenue for an independent psychiatry practice from visit volume, pricing, payer mix, and overhead.",
    "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    "isAccessibleForFree": True,
    "publisher": {"@id": "https://shrinkiatry.com/#org"},
}

ESTIMATOR_BODY = """
<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <a href="/tools/" style="color:#cdd6dd">Tools</a> <span aria-hidden="true">/</span> <span aria-current="page">Revenue estimator</span></nav>
<span class="eyebrow">Live tool</span>
<h1 class="mt-1">Private practice revenue estimator</h1>
<p class="hero__sub mt-2" style="max-width:58ch">Adjust the inputs to see how visit volume, pricing, payer mix, and overhead shape what an independent psychiatry practice actually nets. Everything runs in your browser; nothing is sent anywhere.</p>
</div></section>

<section class="section section--surface"><div class="wrap">
<div class="tool">
<form class="tool__panel" id="rev-form" aria-label="Revenue inputs">
<div class="field">
<label for="visits">Patient visits per week: <span class="field__val" id="visits-val">30</span></label>
<input type="range" id="visits" min="5" max="60" step="1" value="30">
</div>
<div class="field">
<label for="weeks">Weeks worked per year: <span class="field__val" id="weeks-val">46</span></label>
<input type="range" id="weeks" min="40" max="50" step="1" value="46">
</div>
<div class="field">
<label for="cashshare">Cash-pay share of visits: <span class="field__val" id="cashshare-val">60%</span></label>
<input type="range" id="cashshare" min="0" max="100" step="5" value="60">
</div>
<div class="field">
<label for="cashrate">Average cash rate per visit ($)</label>
<input type="number" id="cashrate" min="50" max="600" step="5" value="225" inputmode="numeric">
</div>
<div class="field">
<label for="insrate">Average insurance reimbursement per visit ($)</label>
<input type="number" id="insrate" min="40" max="400" step="5" value="130" inputmode="numeric">
</div>
<div class="field">
<label for="noshow">No-show and cancellation rate: <span class="field__val" id="noshow-val">10%</span></label>
<input type="range" id="noshow" min="0" max="30" step="1" value="10">
</div>
<div class="field">
<label for="overhead">Overhead as a share of collections: <span class="field__val" id="overhead-val">35%</span></label>
<input type="range" id="overhead" min="10" max="70" step="1" value="35">
</div>
</form>

<div class="tool__out" aria-live="polite">
<div class="stat"><div class="stat__num" id="out-net">$0</div><div class="stat__label">Estimated net annual revenue, before income tax</div></div>
<div class="grid grid-2">
<div class="stat"><div class="stat__num" id="out-gross">$0</div><div class="stat__label">Gross collections per year</div></div>
<div class="stat"><div class="stat__num" id="out-monthly">$0</div><div class="stat__label">Net per month</div></div>
</div>
<div class="stat">
<div class="stat__label" style="margin-bottom:.5rem">Where the gross goes</div>
<div class="databar"><span id="bar-net" style="width:65%"></span></div>
<p class="small muted" style="margin-top:.5rem"><span id="out-blended">$0</span> blended revenue per completed visit &middot; <span id="out-visits">0</span> completed visits per year &middot; <span id="out-overheadpct">35%</span> overhead</p>
</div>
<div class="callout"><strong class="callout__label">What this is</strong>An educational model, not a forecast. It ignores taxes, benefits, startup costs, bad debt, and the time it takes to fill a schedule. Real numbers vary widely by state, specialty, and payer contracts. Treat the output as a way to see how the levers interact, not as a projection for any specific practice. This is not financial advice.</div>
</div>
</div>
</div></section>

<section class="section section--tint"><div class="wrap"><div class="maxread">
<h2>How the math works</h2>
<p class="mt-2">The estimator multiplies your visits per week by the weeks you work to get annual visit slots, then removes the no-show and cancellation share to get completed visits. It blends your cash and insurance rates by the payer mix you set, multiplies that blended rate by completed visits to get gross collections, and subtracts overhead to get net revenue before income tax.</p>
<p class="mt-2">The point isn't the exact number. It's what happens when you move a slider. Watch how much a small change in no-show rate or payer mix moves the net, and you'll understand why independent psychiatrists pay so much attention to both. For the reimbursement story behind these inputs, read <a href="/business/cash-pay-vs-insurance/">cash-pay vs insurance</a>.</p>
</div></div></section>

<section class="section section--surface"><div class="wrap"><div class="maxread">
""" + S.network_continue(["shrinkmd","shariqrefai","shrinknetwork"]) + """
</div></div></section>

<script>
(function(){
  var ids = ["visits","weeks","cashshare","cashrate","insrate","noshow","overhead"];
  var el = {}; ids.forEach(function(i){ el[i] = document.getElementById(i); });
  function money(n){ return "$" + Math.round(n).toLocaleString("en-US"); }
  function compute(){
    var visits = +el.visits.value, weeks = +el.weeks.value;
    var cashShare = +el.cashshare.value/100, cashRate = +el.cashrate.value, insRate = +el.insrate.value;
    var noShow = +el.noshow.value/100, overhead = +el.overhead.value/100;
    var slots = visits*weeks;
    var completed = slots*(1-noShow);
    var blended = cashShare*cashRate + (1-cashShare)*insRate;
    var gross = completed*blended;
    var net = gross*(1-overhead);
    document.getElementById("visits-val").textContent = visits;
    document.getElementById("weeks-val").textContent = weeks;
    document.getElementById("cashshare-val").textContent = Math.round(cashShare*100)+"%";
    document.getElementById("noshow-val").textContent = Math.round(noShow*100)+"%";
    document.getElementById("overhead-val").textContent = Math.round(overhead*100)+"%";
    document.getElementById("out-net").textContent = money(net);
    document.getElementById("out-gross").textContent = money(gross);
    document.getElementById("out-monthly").textContent = money(net/12);
    document.getElementById("out-blended").textContent = money(blended);
    document.getElementById("out-visits").textContent = Math.round(completed).toLocaleString("en-US");
    document.getElementById("out-overheadpct").textContent = Math.round(overhead*100)+"%";
    document.getElementById("bar-net").style.width = Math.max(4, Math.round((1-overhead)*100)) + "%";
  }
  ids.forEach(function(i){ el[i].addEventListener("input", compute); });
  compute();
})();
</script>
"""

PAGES.append({
    "slug": "tools/private-practice-revenue-estimator",
    "active": "/tools/",
    "title": "Private Practice Revenue Estimator | shrinkiatry",
    "desc": "A free, educational calculator that estimates net and gross annual revenue for an independent psychiatry practice from visit volume, pricing, payer mix, and overhead.",
    "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Revenue estimator", None)],
    "schema": [TOOL_SCHEMA],
    "body": ESTIMATOR_BODY,
})
