---
layout: default
title: Most Popular Open Source OS & Desktop Environments (30 Days and 3 Months)
description: Ranking of Linux, BSD, and open source operating systems plus desktop environments using OpenSourceFeed page views for the last 30 days and last 3 months.
image: "/assets/images/meta/logo-collage.png"
seo:
  type: CollectionPage
  name: Popular Open Source OS and Desktop Ranking
---
<style>
.rank-page {
  --rk-accent: #046cdc;
  --rk-accent-strong: #0357b0;
  --rk-accent-soft: #eaf2fc;
  --rk-accent-2: #5aa2ee;
  --rk-text: #1d2733;
  --rk-muted: #5f6b7a;
  --rk-border: #e3ecf7;
  --rk-surface: #ffffff;
  --rk-surface-alt: #f6f9fd;
  --rk-up: #157a3c;
  --rk-up-soft: #e3f6ea;
  --rk-down: #b42323;
  --rk-down-soft: #fde8e8;
  --rk-gold: #d4a017;
  --rk-silver: #8e9aa8;
  --rk-bronze: #b36b32;
  --rk-radius: 1rem;
  --rk-shadow: 0 1px 2px rgba(16, 40, 80, 0.06), 0 6px 20px rgba(16, 40, 80, 0.06);

  max-width: 1080px;
  margin: 0 auto;
  padding: 1rem 0 2rem;
  color: var(--rk-text);
  line-height: 1.5;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.rank-page a { color: var(--rk-accent); text-decoration: none; }
.rank-page a:hover, .rank-page a:focus { color: var(--rk-accent-strong); text-decoration: underline; }
.rank-page [hidden] { display: none !important; }

/* ---------- Hero ---------- */
.rank-hero {
  padding: 2rem 1.5rem 1.5rem;
  margin-bottom: 1.5rem;
  border: 1px solid var(--rk-border);
  border-radius: calc(var(--rk-radius) * 1.25);
  background:
    radial-gradient(120% 140% at 100% 0%, rgba(90, 162, 238, 0.18) 0%, transparent 55%),
    linear-gradient(180deg, var(--rk-surface-alt), var(--rk-surface));
  text-align: center;
}
.rank-eyebrow {
  display: inline-block;
  margin-bottom: 0.6rem;
  padding: 0.2rem 0.7rem;
  border-radius: 999px;
  background: var(--rk-accent-soft);
  color: var(--rk-accent);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.rank-hero h1 {
  font-weight: 800;
  letter-spacing: -0.025em;
  margin-bottom: 0.6rem;
}
.rank-hero .lead-text {
  max-width: 46rem;
  line-height: 1.6;
  margin: 0 auto 0.5rem;
  color: var(--rk-muted);
}
.rank-updated { color: var(--rk-muted); font-size: 0.875rem; margin-bottom: 1.25rem; }

/* ---------- Controls ---------- */
.rank-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  justify-content: center;
}
.segmented {
  display: inline-flex;
  padding: 0.25rem;
  border: 1px solid var(--rk-border);
  border-radius: 999px;
  background: var(--rk-surface);
}
.rank-page .segmented a {
  padding: 0.4rem 1rem;
  border-radius: 999px;
  color: var(--rk-muted);
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.2;
  white-space: nowrap;
  text-decoration: none;
}
.rank-page .segmented a:hover { color: var(--rk-accent); }
.lbl-short { display: none; }
.rank-page .segmented a.is-active {
  background: var(--rk-accent);
  color: #fff;
  box-shadow: 0 2px 6px rgba(4, 108, 220, 0.3);
}

.rank-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem 1rem;
  align-items: center;
  margin: 0 0 1.25rem;
  padding: 0.85rem 1rem;
  border: 1px solid var(--rk-border);
  border-radius: var(--rk-radius);
  background: var(--rk-surface-alt);
}
.rank-filters .filter-label { font-size: 0.85rem; font-weight: 700; color: var(--rk-muted); margin-right: 0.15rem; }
.filter-chips { display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: center; }
.filter-chip {
  appearance: none;
  padding: 0.3rem 0.75rem;
  border: 1px solid var(--rk-border);
  border-radius: 999px;
  background: var(--rk-surface);
  color: var(--rk-text);
  font-size: 0.85rem;
  font-weight: 600;
  line-height: 1.2;
  cursor: pointer;
}
.filter-chip:hover { border-color: var(--rk-accent-2); color: var(--rk-accent); }
.filter-chip.is-active { background: var(--rk-accent); border-color: var(--rk-accent); color: #fff; }
.filter-de { display: flex; align-items: center; gap: 0.5rem; }
.filter-de select {
  padding: 0.3rem 2rem 0.3rem 0.75rem;
  border: 1px solid var(--rk-border);
  border-radius: 999px;
  background-color: var(--rk-surface);
  color: var(--rk-text);
  font-size: 0.85rem;
  font-weight: 600;
}
.filter-status { margin: -0.6rem 0 1.25rem; font-size: 0.85rem; color: var(--rk-muted); }
.filters-toggle {
  display: none;
  align-items: center;
  gap: 0.45rem;
  margin-bottom: 1rem;
  padding: 0.45rem 0.95rem;
  border: 1px solid var(--rk-border);
  border-radius: 999px;
  background: var(--rk-surface);
  color: var(--rk-text);
  font-size: 0.9rem;
  font-weight: 600;
}
.filters-toggle[aria-expanded="true"] { border-color: var(--rk-accent); color: var(--rk-accent); }
.filters-count {
  min-width: 1.3rem;
  padding: 0 0.35rem;
  border-radius: 999px;
  background: var(--rk-accent);
  color: #fff;
  font-size: 0.75rem;
  line-height: 1.3rem;
  text-align: center;
}
.filter-reset {
  border: 0;
  background: none;
  padding: 0;
  margin-left: 0.4rem;
  color: var(--rk-accent);
  font-weight: 600;
  cursor: pointer;
}

/* ---------- Section ---------- */
.period-block { margin-top: 0.5rem; }
.period-title { font-size: 1.15rem; font-weight: 700; margin: 0 0 0.25rem; scroll-margin-top: 6rem; }
.period-range { color: var(--rk-muted); font-size: 0.85rem; margin-bottom: 1rem; }
.rank-section > h3 {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 1rem;
}

/* ---------- Podium ---------- */
.rank-podium {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  align-items: end;
  gap: 1rem;
  margin-bottom: 1.25rem;
}
.podium-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.35rem;
  padding: 2rem 1rem 1.1rem;
  border: 1px solid var(--rk-border);
  border-top: 4px solid var(--medal);
  border-radius: var(--rk-radius);
  background: var(--rk-surface);
  box-shadow: var(--rk-shadow);
  text-align: center;
  min-width: 0;
}
.podium-card.place-1 { --medal: var(--rk-gold); order: 2; padding-top: 2.6rem; padding-bottom: 1.6rem;
  background: linear-gradient(180deg, rgba(212, 160, 23, 0.08), var(--rk-surface) 45%); }
.podium-card.place-2 { --medal: var(--rk-silver); order: 1; }
.podium-card.place-3 { --medal: var(--rk-bronze); order: 3; }
.podium-medal {
  position: absolute;
  top: -1rem;
  left: 50%;
  transform: translateX(-50%);
  display: grid;
  place-items: center;
  width: 2.1rem;
  height: 2.1rem;
  border-radius: 50%;
  background: var(--medal);
  color: #fff;
  font-weight: 800;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.18);
}
.podium-logo {
  display: grid;
  place-items: center;
  width: 4.5rem;
  height: 4.5rem;
  margin-bottom: 0.25rem;
}
.place-1 .podium-logo { width: 5.5rem; height: 5.5rem; }
.podium-logo img { max-width: 100%; max-height: 100%; object-fit: contain; }
.podium-info { display: contents; }
.rank-list-wrap { container-type: inline-size; }
.podium-name { font-size: 1.05rem; font-weight: 700; margin: 0; overflow-wrap: anywhere; }
.place-1 .podium-name { font-size: 1.2rem; }
.rank-page .podium-name a { color: var(--rk-text); }
.podium-sub { color: var(--rk-muted); font-size: 0.85rem; }
.rank-page .podium-release { font-size: 0.8rem; font-weight: 600; }
.podium-stats { display: flex; align-items: center; gap: 0.6rem; margin-top: 0.35rem; }
.podium-score strong { font-size: 1.15rem; font-variant-numeric: tabular-nums; }
.podium-score small { color: var(--rk-muted); }

/* ---------- Movers ---------- */
.rank-movers {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin-bottom: 1.25rem;
}
.movers-group {
  padding: 0.9rem 1rem;
  border: 1px solid var(--rk-border);
  border-radius: var(--rk-radius);
  background: var(--rk-surface-alt);
}
.movers-title { font-size: 0.8rem; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 0.5rem; }
.movers-title.is-up { color: var(--rk-up); }
.movers-title.is-down { color: var(--rk-down); }
.movers-list { list-style: none; margin: 0; padding: 0; }
.movers-list li {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  gap: 0.25rem 0.5rem;
  padding: 0.3rem 0;
  font-size: 0.92rem;
}
.movers-list li + li { border-top: 1px dashed var(--rk-border); }
.movers-list a { font-weight: 600; }
.movers-meta { color: var(--rk-muted); font-size: 0.8rem; font-variant-numeric: tabular-nums; flex: 0 0 auto; }
.rank-page .movers-list a { flex: 1 1 auto; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.movers-list .rank-change { flex: 0 0 auto; }

/* ---------- List ---------- */
.rank-list-head,
.rank-row {
  display: grid;
  grid-template-columns: 2.5rem 2.75rem minmax(0, 1fr) 4.25rem minmax(8rem, 26%);
  align-items: center;
  gap: 0.75rem;
}
.rank-list-head {
  padding: 0 1rem 0.4rem;
  color: var(--rk-muted);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.rank-list-head span:nth-child(2) { grid-column: 2 / 4; }
.rank-list {
  list-style: none;
  margin: 0;
  padding: 0;
  border: 1px solid var(--rk-border);
  border-radius: var(--rk-radius);
  background: var(--rk-surface);
  box-shadow: var(--rk-shadow);
  overflow: hidden;
}
.rank-row { padding: 0.6rem 1rem; }
.rank-row + .rank-row { border-top: 1px solid var(--rk-border); }
.rank-row:hover { background: var(--rk-surface-alt); }
.rank-list:not(.is-filtered) .rank-row.is-podium { display: none; }
.row-rank { font-weight: 800; font-size: 1.05rem; color: var(--rk-muted); font-variant-numeric: tabular-nums; text-align: center; }
.row-logo { display: grid; place-items: center; width: 2.25rem; height: 2.25rem; }
.row-logo img { max-width: 100%; max-height: 100%; object-fit: contain; }
.row-main { display: flex; flex-direction: column; gap: 0.2rem; min-width: 0; }
.rank-page .row-name { color: var(--rk-text); font-weight: 650; overflow-wrap: anywhere; }
.row-chips { display: flex; flex-wrap: wrap; gap: 0.3rem; }
.chip {
  padding: 0.05rem 0.5rem;
  border-radius: 999px;
  background: var(--rk-surface-alt);
  border: 1px solid var(--rk-border);
  color: var(--rk-muted);
  font-size: 0.72rem;
  font-weight: 600;
  line-height: 1.5;
  white-space: nowrap;
}
.chip-base { background: var(--rk-accent-soft); border-color: transparent; color: var(--rk-accent); }
.row-change { text-align: center; }
.row-score { display: flex; align-items: center; gap: 0.6rem; }
.score-bar { flex: 1; height: 0.5rem; border-radius: 999px; background: var(--rk-accent-soft); overflow: hidden; }
.score-bar span { display: block; height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--rk-accent-2), var(--rk-accent)); }
.score-value { min-width: 1.9rem; text-align: right; font-weight: 700; font-variant-numeric: tabular-nums; }
.rank-empty { padding: 1.5rem; text-align: center; color: var(--rk-muted); }

.logo-fallback {
  display: grid;
  place-items: center;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: var(--rk-accent-soft);
  color: var(--rk-accent);
  font-weight: 800;
}

.rank-change {
  display: inline-block;
  min-width: 2.6rem;
  padding: 0.1rem 0.45rem;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 700;
  text-align: center;
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}
.rank-change.is-up { background: var(--rk-up-soft); color: var(--rk-up); }
.rank-change.is-down { background: var(--rk-down-soft); color: var(--rk-down); }
.rank-change.is-same { background: var(--rk-surface-alt); color: var(--rk-muted); }
.rank-change.is-new { background: var(--rk-accent-soft); color: var(--rk-accent); letter-spacing: 0.03em; }

/* ---------- Methodology ---------- */
.rank-method {
  margin-top: 2rem;
  padding: 1.25rem 1.5rem;
  border: 1px solid var(--rk-border);
  border-radius: var(--rk-radius);
  background: var(--rk-surface-alt);
}
.rank-method h2 { font-size: 1.25rem; font-weight: 700; margin-bottom: 0.75rem; }
.rank-method dl { display: grid; grid-template-columns: minmax(8rem, 12rem) 1fr; gap: 0.5rem 1.25rem; margin: 0; }
.rank-method dt { font-weight: 700; }
.rank-method dd { margin: 0; color: var(--rk-muted); }
.rank-ad { margin: 2rem 0; }

/* ---------- Responsive ---------- */
/* List adapts to its own width (the site column is narrow on tablets/small laptops) */
@container (max-width: 720px) {
  .rank-list-head { display: none; }
  .rank-row {
    grid-template-columns: 2rem 2.25rem minmax(0, 1fr) auto;
    grid-template-areas: "rank logo main change" "rank logo score score";
    row-gap: 0.4rem;
    padding: 0.7rem 0.85rem;
  }
  .row-rank { grid-area: rank; }
  .row-logo { grid-area: logo; width: 2rem; height: 2rem; }
  .row-main { grid-area: main; }
  .row-change { grid-area: change; }
  .row-score { grid-area: score; }
}
@media (min-width: 768px) and (max-width: 1199.98px) {
  .rank-movers .movers-meta { display: none; }
}
@media (max-width: 767.98px) {
  .rank-hero { padding: 1rem 0.85rem; margin-bottom: 1rem; }
  .rank-eyebrow { display: none; }
  .rank-hero h1 { font-size: 1.5rem; margin-bottom: 0.35rem; }
  .rank-hero .lead-text { font-size: 0.92rem; margin-bottom: 0.25rem; }
  .rank-updated { font-size: 0.8rem; margin-bottom: 0.85rem; }
  .rank-controls { gap: 0.4rem; }
  .filters-toggle { display: inline-flex; }
  .rank-filters { display: none; margin-bottom: 1rem; padding: 0.75rem; }
  .rank-filters.is-open { display: flex; }
  .filter-chips { flex-wrap: nowrap; overflow-x: auto; margin: 0 -0.75rem; padding: 0 0.75rem 0.25rem; scrollbar-width: none; }
  .filter-chips::-webkit-scrollbar { display: none; }
  .filter-chip, .filter-chips .filter-label { flex: 0 0 auto; }
  .filter-status { margin-top: -0.5rem; }
  .period-title { font-size: 1rem; }
  .period-range { font-size: 0.8rem; margin-bottom: 0.75rem; }
  .rank-section > h3 { font-size: 1.3rem; margin-bottom: 1.4rem; }
  .rank-controls { flex-wrap: nowrap; }
  .segmented { display: flex; flex: 1 1 auto; min-width: 0; }
  .segmented:first-child { flex: 0 0 auto; }
  .lbl-long { display: none; }
  .lbl-short { display: inline; }
  .period-title { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
  .rank-page .segmented a { flex: 1; display: flex; align-items: center; justify-content: center; padding: 0.45rem 0.5rem; font-size: 0.9rem; text-align: center; white-space: normal; }
  .rank-podium { grid-template-columns: 1fr; gap: 1.4rem; margin-top: 1rem; }
  .podium-card, .podium-card.place-1 { order: 0; padding: 1.6rem 1rem 1rem; }
}
@media (max-width: 575.98px) {
  .rank-podium { gap: 0.6rem; margin-top: 0; }
  .podium-card, .podium-card.place-1 {
    flex-direction: row;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 0.85rem;
    border-top-width: 1px;
    border-left: 4px solid var(--medal);
    text-align: left;
  }
  .podium-medal { position: static; transform: none; flex: 0 0 auto; width: 1.75rem; height: 1.75rem; font-size: 0.9rem; }
  .podium-logo, .place-1 .podium-logo { flex: 0 0 auto; width: 2.75rem; height: 2.75rem; margin: 0; }
  .podium-info { display: flex; flex-direction: column; gap: 0.1rem; flex: 1 1 auto; min-width: 0; }
  .podium-name, .place-1 .podium-name { font-size: 1rem; }
  .podium-sub, .rank-page .podium-release { font-size: 0.78rem; }
  .podium-stats { flex-direction: column; align-items: flex-end; gap: 0.25rem; margin: 0; flex: 0 0 auto; }
  .podium-score strong { font-size: 1rem; }
  .rank-movers { grid-template-columns: 1fr; }
  .filter-de { margin-left: 0; }
  .rank-method dl { grid-template-columns: 1fr; }
  .rank-method dd { margin-bottom: 0.5rem; }
}
</style>

{% assign rankings = site.data.rank.rankings %}
{% assign d30_distributions = rankings.d30.distributions | default: site.data.rank.distributions %}
{% assign d30_desktops = rankings.d30.desktops | default: site.data.rank.desktops %}
{% assign m3_distributions = rankings.m3.distributions | default: site.data.rank.distributions %}
{% assign m3_desktops = rankings.m3.desktops | default: site.data.rank.desktops %}
{% assign periods = site.data.rank.meta.periods %}
{% assign last_updated = site.data.rank.meta.current_date %}

<div class="distribution">
  <div class="rank-page">

    <header class="rank-hero">
      <span class="rank-eyebrow">Popularity Index</span>
      <h1>Open Source Popularity Ranking</h1>
      <p class="lead-text">The most-viewed Linux distributions, BSDs and desktops on OpenSourceFeed, compared with the previous period.</p>
      {% if last_updated %}
      <p class="rank-updated">Updated <time datetime="{{ last_updated | date_to_xmlschema }}" itemprop="dateModified">{{ last_updated | date: "%B %-d, %Y" }}</time></p>
      {% endif %}
      <div class="rank-controls">
        <nav class="segmented" aria-label="Time range">
          <a data-filter-period="30d" href="?period=30d&type=os"><span class="lbl-long">30 Days</span><span class="lbl-short">30D</span></a>
          <a data-filter-period="3m" href="?period=3m&type=os"><span class="lbl-long">3 Months</span><span class="lbl-short">3M</span></a>
        </nav>
        <nav class="segmented" aria-label="Category">
          <a data-filter-type="os" href="?period=30d&type=os"><span class="lbl-long">Operating Systems</span><span class="lbl-short">OS</span></a>
          <a data-filter-type="desktop" href="?period=30d&type=desktop"><span class="lbl-long">Desktop Environments</span><span class="lbl-short">Desktops</span></a>
        </nav>
      </div>
    </header>

    <div class="rank-filter-wrap" id="rank-filter-wrap">
    <button type="button" class="filters-toggle" id="rank-filters-toggle" aria-expanded="false" aria-controls="rank-filters">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M7 12h10M10 18h4"/></svg>
      Filters <span class="filters-count" hidden></span>
    </button>
    <div class="rank-filters" id="rank-filters" aria-label="Filter operating systems">
      <div class="filter-chips" role="group" aria-label="Filter by base">
        <span class="filter-label">Base</span>
        <button type="button" class="filter-chip" data-base="">All</button>
        <button type="button" class="filter-chip" data-base="debian">Debian</button>
        <button type="button" class="filter-chip" data-base="ubuntu">Ubuntu</button>
        <button type="button" class="filter-chip" data-base="arch">Arch</button>
        <button type="button" class="filter-chip" data-base="fedora">Fedora / RHEL</button>
        <button type="button" class="filter-chip" data-base="gentoo">Gentoo</button>
        <button type="button" class="filter-chip" data-base="slackware">Slackware</button>
        <button type="button" class="filter-chip" data-base="bsd">BSD</button>
        <button type="button" class="filter-chip" data-base="independent">Independent</button>
      </div>
      <label class="filter-de">
        <span class="filter-label">Desktop</span>
        <select id="filter-de">
          <option value="">Any desktop</option>
          <option value="gnome">GNOME</option>
          <option value="plasma">KDE Plasma</option>
          <option value="xfce">Xfce</option>
          <option value="mate">MATE</option>
          <option value="cinnamon">Cinnamon</option>
          <option value="lxqt">LXQt</option>
          <option value="lxde">LXDE</option>
          <option value="budgie">Budgie</option>
          <option value="openbox">Openbox</option>
          <option value="i3">i3</option>
        </select>
      </label>
    </div>
    <p class="filter-status" aria-live="polite" hidden></p>
    </div>

    <section class="period-block" data-period="30d" aria-labelledby="last-30-days">
      <h2 id="last-30-days" class="period-title">Last 30 Days</h2>
      {% if periods.d30.current %}<p class="period-range">{{ periods.d30.current.start | date: "%b %-d" }} &ndash; {{ periods.d30.current.end | date: "%b %-d, %Y" }} &middot; compared with {{ periods.d30.previous.start | date: "%b %-d" }} &ndash; {{ periods.d30.previous.end | date: "%b %-d" }}</p>{% endif %}
      <div class="rank-section" data-period="30d" data-type="os" id="last-30-days-os">
        <h3>Operating Systems</h3>
        {% include rank-board.html entries=d30_distributions kind="os" compare="previous 30 days" label="operating system" %}
      </div>
      <div class="rank-section" data-period="30d" data-type="desktop" id="last-30-days-desktop">
        <h3>Desktop Environments</h3>
        {% include rank-board.html entries=d30_desktops kind="desktop" compare="previous 30 days" label="desktop environment" %}
      </div>
    </section>

    <section class="period-block" data-period="3m" aria-labelledby="last-3-months">
      <h2 id="last-3-months" class="period-title">Last 3 Months</h2>
      {% if periods.m3.current %}<p class="period-range">{{ periods.m3.current.start | date: "%b %-d" }} &ndash; {{ periods.m3.current.end | date: "%b %-d, %Y" }} &middot; compared with {{ periods.m3.previous.start | date: "%b %-d" }} &ndash; {{ periods.m3.previous.end | date: "%b %-d" }}</p>{% endif %}
      <div class="rank-section" data-period="3m" data-type="os" id="last-3-months-os">
        <h3>Operating Systems</h3>
        {% include rank-board.html entries=m3_distributions kind="os" compare="previous 3 months" label="operating system" %}
      </div>
      <div class="rank-section" data-period="3m" data-type="desktop" id="last-3-months-desktop">
        <h3>Desktop Environments</h3>
        {% include rank-board.html entries=m3_desktops kind="desktop" compare="previous 3 months" label="desktop environment" %}
      </div>
    </section>

    <section class="rank-method" aria-labelledby="methodology">
      <h2 id="methodology">Methodology</h2>
      <dl>
        <dt>Data source</dt>
        <dd>Page views of each distribution and desktop page on OpenSourceFeed, from the <a href="https://developers.google.com/analytics/">Google Analytics</a> Data API. Hits on old or alias URLs are merged into the main page.</dd>
        <dt>Popularity score</dt>
        <dd>Each entry's page views divided by those of the #1 entry in the same list, scaled to 100.</dd>
        <dt>Rank change</dt>
        <dd>The current rank compared with the rank in the preceding period of the same length, for example the last 30 days against the 30 days before them. &ldquo;NEW&rdquo; means the entry was not ranked in the preceding period.</dd>
        <dt>Biggest movers</dt>
        <dd>The largest rank changes among entries currently in the top 50.</dd>
        <dt>Limitations</dt>
        <dd>The ranking reflects reader interest on this site only. It does not measure install base, quality or efficiency, and it is not real-time.</dd>
      </dl>
    </section>

    <div class="rank-ad">
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
      <ins class="adsbygoogle"
           style="display:block"
           data-ad-client="ca-pub-6380671811722843"
           data-ad-slot="9117305104"
           data-ad-format="auto"
           data-full-width-responsive="true"></ins>
      <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
      </script>
    </div>

    <h2>Express your views on distributions and desktop environments.</h2>
    {% include echothread.html %}

    <script>
      (function () {
        var PERIODS = ['30d', '3m'];
        var TYPES = ['os', 'desktop'];
        var LEGACY_HASHES = {
          '#last-30-days': ['30d', 'os'], '#last-30-days-os': ['30d', 'os'], '#last-30-days-desktop': ['30d', 'desktop'],
          '#last-3-months': ['3m', 'os'], '#last-3-months-os': ['3m', 'os'], '#last-3-months-desktop': ['3m', 'desktop']
        };

        var sections = document.querySelectorAll('.rank-section');
        var periodBlocks = document.querySelectorAll('.period-block');
        var periodLinks = document.querySelectorAll('[data-filter-period]');
        var typeLinks = document.querySelectorAll('[data-filter-type]');
        var filterBar = document.getElementById('rank-filters');
        var filterWrap = document.getElementById('rank-filter-wrap');
        var filterToggle = document.getElementById('rank-filters-toggle');
        var filterCount = filterToggle.querySelector('.filters-count');
        var baseChips = filterBar.querySelectorAll('[data-base]');
        var deSelect = document.getElementById('filter-de');
        var status = filterWrap.querySelector('.filter-status');

        var params = new URLSearchParams(window.location.search);
        var legacy = LEGACY_HASHES[window.location.hash] || [];
        var state = {
          period: legacy[0] || params.get('period'),
          type: legacy[1] || params.get('type'),
          base: params.get('base') || '',
          de: params.get('de') || ''
        };
        if (PERIODS.indexOf(state.period) < 0) state.period = '30d';
        if (TYPES.indexOf(state.type) < 0) state.type = 'os';
        if (!filterBar.querySelector('[data-base="' + state.base + '"]')) state.base = '';
        if (!deSelect.querySelector('option[value="' + state.de + '"]')) state.de = '';

        function buildQuery(s) {
          var q = new URLSearchParams();
          q.set('period', s.period);
          q.set('type', s.type);
          if (s.type === 'os' && s.base) q.set('base', s.base);
          if (s.type === 'os' && s.de) q.set('de', s.de);
          return '?' + q.toString();
        }

        function hasToken(list, token) {
          return (' ' + (list || '') + ' ').indexOf(' ' + token + ' ') >= 0;
        }

        function applyRowFilters(section) {
          var list = section.querySelector('.rank-list');
          var empty = section.querySelector('.rank-empty');
          if (!list) return;
          var rows = list.querySelectorAll('.rank-row');
          var filtering = section.dataset.type === 'os' && (state.base || state.de);
          var shown = 0;

          rows.forEach(function (row) {
            var ok = !filtering ||
              ((!state.base || hasToken(row.dataset.bases, state.base)) &&
               (!state.de || hasToken(row.dataset.des, state.de)));
            row.hidden = !ok;
            if (ok) shown++;
          });

          list.classList.toggle('is-filtered', !!filtering);
          section.querySelectorAll('.rank-podium, .rank-movers').forEach(function (el) { el.hidden = !!filtering; });
          if (empty) empty.hidden = !(filtering && shown === 0);

          if (section.dataset.period === state.period && section.dataset.type === state.type) {
            status.hidden = !filtering;
            if (filtering) {
              status.innerHTML = 'Showing ' + shown + ' of ' + rows.length + ' operating systems. ' +
                '<button type="button" class="filter-reset">Clear filters</button>';
            }
          }
        }

        function render(push) {
          sections.forEach(function (section) {
            section.hidden = !(section.dataset.period === state.period && section.dataset.type === state.type);
            applyRowFilters(section);
          });
          periodBlocks.forEach(function (block) { block.hidden = block.dataset.period !== state.period; });

          periodLinks.forEach(function (link) {
            var on = link.dataset.filterPeriod === state.period;
            link.classList.toggle('is-active', on);
            if (on) link.setAttribute('aria-current', 'true'); else link.removeAttribute('aria-current');
            link.setAttribute('href', buildQuery({ period: link.dataset.filterPeriod, type: state.type, base: state.base, de: state.de }));
          });
          typeLinks.forEach(function (link) {
            var on = link.dataset.filterType === state.type;
            link.classList.toggle('is-active', on);
            if (on) link.setAttribute('aria-current', 'true'); else link.removeAttribute('aria-current');
            link.setAttribute('href', buildQuery({ period: state.period, type: link.dataset.filterType, base: state.base, de: state.de }));
          });

          filterWrap.hidden = state.type !== 'os';
          var active = (state.base ? 1 : 0) + (state.de ? 1 : 0);
          filterCount.hidden = active === 0;
          filterCount.textContent = active;
          baseChips.forEach(function (chip) {
            var on = chip.dataset.base === state.base;
            chip.classList.toggle('is-active', on);
            chip.setAttribute('aria-pressed', on ? 'true' : 'false');
          });
          deSelect.value = state.de;

          var next = window.location.pathname + buildQuery(state);
          if (push) history.pushState(null, '', next); else history.replaceState(null, '', next);
        }

        periodLinks.forEach(function (link) {
          link.addEventListener('click', function (e) {
            e.preventDefault();
            state.period = link.dataset.filterPeriod;
            render(true);
          });
        });
        typeLinks.forEach(function (link) {
          link.addEventListener('click', function (e) {
            e.preventDefault();
            state.type = link.dataset.filterType;
            render(true);
          });
        });
        baseChips.forEach(function (chip) {
          chip.addEventListener('click', function () {
            state.base = chip.dataset.base;
            render(false);
          });
        });
        deSelect.addEventListener('change', function () {
          state.de = deSelect.value;
          render(false);
        });
        filterToggle.addEventListener('click', function () {
          var open = !filterBar.classList.contains('is-open');
          filterBar.classList.toggle('is-open', open);
          filterToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        status.addEventListener('click', function (e) {
          if (!e.target.classList.contains('filter-reset')) return;
          state.base = '';
          state.de = '';
          render(false);
        });

        render(false);
      })();
    </script>
  </div>
</div>
