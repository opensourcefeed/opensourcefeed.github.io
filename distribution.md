---
layout: wide
title: Collection of Free and Open Source operating systems
description: Collection of Free and Open Source operating systems including GNU/Linux and BSD distributions.
seo:
  type: ItemList
---

<style>
.distribution h1{
    text-align:center;
    margin-bottom:10px;
    font-weight:600;
}

.distribution-intro{
    text-align:center;
    max-width:840px;
    margin:0 auto 20px auto;
    color:var(--osf-color-text-secondary);
}

.distribution-section{
    margin-bottom:2rem;
}

.distribution-section-header{
    display:flex;
    align-items:baseline;
    gap:0.75rem;
    margin:0 0 0.9rem 0;
}

.distribution-section-header h2{
    margin:0;
    font-weight:600;
    border-left:3px solid var(--osf-color-primary);
    padding-left:10px;
}

.distribution-count{
    color:var(--osf-color-text-muted);
    font-size:0.95rem;
}

.distribution-grid{
    display:grid;
    grid-template-columns:repeat(auto-fill, minmax(230px, 1fr));
    gap:12px;
}

.distribution-card{
    display:flex;
    align-items:center;
    gap:12px;
    min-height:78px;
    padding:12px 14px;
    border:0;
    border-radius:var(--osf-radius-lg);
    background:var(--osf-color-surface);
    box-shadow:var(--osf-shadow-sm);
    color:inherit;
    text-decoration:none;
    transition:transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.distribution-card:hover{
    transform:translateY(-2px);
    box-shadow:var(--osf-shadow-md);
}

.distribution-card:focus-visible{
    outline:none;
    box-shadow:var(--osf-shadow-focus), var(--osf-shadow-sm);
}

.distribution-card-media{
    width:52px;
    height:52px;
    flex:0 0 52px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:var(--osf-radius-md);
    background:var(--osf-color-surface-sunk);
}

.distribution-card-media img{
    max-width:40px;
    max-height:40px;
    object-fit:contain;
}

.distribution-card-fallback{
    color:var(--osf-color-text-muted);
    font-size:0.78rem;
    font-weight:700;
    letter-spacing:0.04em;
}

.distribution-card-title{
    font-weight:600;
    line-height:1.3;
    color:var(--osf-color-heading);
}

.distribution-card:hover .distribution-card-title,
.distribution-card:focus-visible .distribution-card-title{
    color:var(--osf-color-primary);
}

.distribution-ad{
    margin:2rem 0;
}

.distribution-comments{
    margin-top:2rem;
}

.distribution-comments h2{
    margin:0 0 0.5rem 0;
    font-weight:600;
    border-left:3px solid var(--osf-color-primary);
    padding-left:10px;
}

.distribution-comments .btn{
    margin-top:0.5rem;
    margin-bottom:1rem;
}

.distribution-search{
    max-width:560px;
    margin:0 auto 1.75rem auto;
}

.distribution-search-field{
    position:relative;
    display:flex;
    align-items:center;
}

.distribution-search-field svg{
    position:absolute;
    left:16px;
    width:18px;
    height:18px;
    color:var(--osf-color-text-faint);
    pointer-events:none;
}

.distribution-search-input{
    width:100%;
    padding:12px 44px 12px 44px;
    font-size:1rem;
    line-height:1.4;
    color:var(--osf-color-text);
    background:var(--osf-color-surface);
    border:1px solid var(--osf-color-line-strong);
    border-radius:var(--osf-radius-md);
    box-shadow:var(--osf-shadow-xs);
    transition:border-color 0.2s ease, box-shadow 0.2s ease;
    -webkit-appearance:none;
    appearance:none;
}

.distribution-search-input::placeholder{
    color:var(--osf-color-text-muted);
}

.distribution-search-input:focus{
    outline:none;
    border-color:var(--osf-color-primary);
    box-shadow:var(--osf-shadow-focus);
}

.distribution-search-input::-webkit-search-cancel-button{
    -webkit-appearance:none;
    appearance:none;
}

.distribution-search-clear{
    position:absolute;
    right:10px;
    display:none;
    align-items:center;
    justify-content:center;
    width:28px;
    height:28px;
    padding:0;
    border:none;
    border-radius:50%;
    background:transparent;
    color:var(--osf-color-text-muted);
    font-size:1.25rem;
    line-height:1;
    cursor:pointer;
    transition:background 0.2s ease, color 0.2s ease;
}

.distribution-search-clear:hover{
    background:var(--osf-color-surface-strong);
    color:var(--osf-color-text);
}

.distribution-search-clear.is-visible{
    display:flex;
}

.distribution-search-status{
    position:absolute;
    width:1px;
    height:1px;
    padding:0;
    margin:-1px;
    overflow:hidden;
    clip:rect(0,0,0,0);
    white-space:nowrap;
    border:0;
}

.distribution-empty{
    display:none;
    text-align:center;
    padding:2.5rem 1rem;
    color:var(--osf-color-text-muted);
}

.distribution-empty strong{
    color:var(--osf-color-text);
}


.distribution-card,
.distribution-controls{ line-height:1.5; }
.distribution-card-body{ display:flex; flex-direction:column; gap:4px; min-width:0; }
.distribution-card-meta{ display:flex; flex-wrap:wrap; align-items:center; gap:4px 8px; color:var(--osf-color-text-muted); font-size:0.78rem; }
.lbl-short{ display:none; }
.distribution-card-rank{
    padding:1px 7px;
    border-radius:var(--osf-radius-pill);
    background:var(--osf-color-primary-tint);
    color:var(--osf-color-primary);
    font-size:0.72rem;
    font-weight:700;
    font-variant-numeric:tabular-nums;
}

.distribution-controls{
    margin:0 0 1.75rem 0;
    padding:0.85rem 1rem;
    border:1px solid var(--osf-color-line);
    border-radius:var(--osf-radius-lg);
    background:var(--osf-color-surface-sunk);
}
.distribution-toolbar{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:0.6rem;
    margin-bottom:0.6rem;
}
.distribution-filters{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:0.6rem 1.25rem;
}
.distribution-filter-chips,
.distribution-sort{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:0.4rem;
}
.distribution-filter-label{ font-size:0.85rem; font-weight:700; color:var(--osf-color-text-muted); margin-right:0.15rem; }
.distribution-chip{
    appearance:none;
    padding:0.3rem 0.75rem;
    border:1px solid var(--osf-color-line-strong);
    border-radius:var(--osf-radius-pill);
    background:var(--osf-color-surface);
    color:var(--osf-color-text);
    font-size:0.85rem;
    font-weight:600;
    line-height:1.2;
    cursor:pointer;
}
.distribution-chip:hover{ border-color:var(--osf-color-primary-soft); color:var(--osf-color-primary); }
.distribution-chip.is-active{ background:var(--osf-color-primary); border-color:var(--osf-color-primary); color:#fff; }
.distribution-filter-select{ display:flex; align-items:center; gap:0.5rem; margin:0; }
.distribution-filter-select select{
    padding:0.3rem 2rem 0.3rem 0.75rem;
    border:1px solid var(--osf-color-line-strong);
    border-radius:var(--osf-radius-pill);
    background-color:var(--osf-color-surface);
    color:var(--osf-color-text);
    font-size:0.85rem;
    font-weight:600;
}
.distribution-filters-toggle{
    display:none;
    align-items:center;
    gap:0.45rem;
    padding:0.35rem 0.9rem;
    border:1px solid var(--osf-color-line-strong);
    border-radius:var(--osf-radius-pill);
    background:var(--osf-color-surface);
    color:var(--osf-color-text);
    font-size:0.9rem;
    font-weight:600;
}
.distribution-filters-toggle[aria-expanded="true"]{ border-color:var(--osf-color-primary); color:var(--osf-color-primary); }
.distribution-filters-count{
    min-width:1.3rem;
    padding:0 0.35rem;
    border-radius:var(--osf-radius-pill);
    background:var(--osf-color-primary);
    color:#fff;
    font-size:0.75rem;
    line-height:1.3rem;
    text-align:center;
}
.distribution-filter-status{ margin:0.6rem 0 0; font-size:0.85rem; color:var(--osf-color-text-muted); }
.distribution-filter-reset{
    border:0;
    background:none;
    padding:0;
    margin-left:0.4rem;
    color:var(--osf-color-primary);
    font-weight:600;
    cursor:pointer;
}
.distribution-rank-link{ margin-left:auto; font-size:0.85rem; font-weight:600; white-space:nowrap; }
.distribution-filters[hidden], .distribution-filter-status[hidden]{ display:none !important; }

@media (max-width:767.98px){
    .distribution h1{ font-size:1.5rem; }
    .distribution-intro{ font-size:0.92rem; margin-bottom:0.75rem; }
    .distribution > hr{ display:none; }
    .distribution-search{ margin-bottom:0.6rem; }
    .distribution-controls{ margin-bottom:1.25rem; padding:0; border:0; background:none; }
    .distribution-toolbar{ justify-content:space-between; margin-bottom:0; }
    .distribution-filters-toggle{ display:inline-flex; }
    .distribution-filters{ display:none; margin-top:0.6rem; padding:0.75rem; border:1px solid var(--osf-color-line); border-radius:var(--osf-radius-lg); background:var(--osf-color-surface-sunk); }
    .distribution-filters.is-open{ display:flex; }
    .distribution-filter-chips{
        flex-wrap:nowrap;
        overflow-x:auto;
        width:calc(100% + 1.5rem);
        margin:0 -0.75rem;
        padding:0 0.75rem 0.25rem;
        scrollbar-width:none;
    }
    .distribution-filter-chips::-webkit-scrollbar{ display:none; }
    .distribution-filter-chips > *{ flex:0 0 auto; }
    .distribution-section-header{ flex-wrap:wrap; }
}
@media (max-width:575.98px){
    .distribution-grid{ grid-template-columns:repeat(2, minmax(0, 1fr)); gap:10px; }
    .distribution-card{
        flex-direction:column;
        align-items:center;
        justify-content:flex-start;
        gap:8px;
        min-height:0;
        padding:14px 10px 12px;
        text-align:center;
    }
    .distribution-card:hover{ transform:none; }
    .distribution-card-media{ width:48px; height:48px; flex:0 0 48px; }
    .distribution-card-media img{ max-width:36px; max-height:36px; }
    .distribution-card-body{ align-items:center; }
    .distribution-card-title{ font-size:0.92rem; }
    .distribution-card-meta{ justify-content:center; font-size:0.72rem; }
    .distribution-section-header h2{ font-size:1.4rem; }
}
@media (max-width:379.98px){
    .distribution-sort-label{ display:none; }
    .distribution-sort .lbl-long{ display:none; }
    .distribution-sort .lbl-short{ display:inline; }
}

.distribution-section[hidden],
.distribution-card[hidden]{
    display:none !important;
}

@media (max-width:575px){
    .distribution-search{
        margin-bottom:1.25rem;
    }
    .distribution-search-input{
        font-size:16px; /* prevents iOS zoom-on-focus */
    }
}
</style>

<div class="distribution">
    <h1>Open Source Operating Systems</h1>
    <p class="distribution-intro">
        Explore free and open source operating systems across GNU/Linux, BSD, and other independent projects.
        <span class="d-none d-md-inline">Browse the collection to compare distributions, discover alternatives, and jump into detailed pages.</span>
    </p>

    <hr>

    <div class="distribution-search">
        <label for="distribution-search-input" class="visually-hidden">Search distributions</label>
        <div class="distribution-search-field">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <circle cx="11" cy="11" r="7"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="search" id="distribution-search-input" class="distribution-search-input"
                   placeholder="Search distributions by name…" autocomplete="off"
                   aria-controls="distribution-results" aria-describedby="distribution-search-status">
            <button type="button" class="distribution-search-clear" id="distribution-search-clear" aria-label="Clear search">&times;</button>
        </div>
        <div class="distribution-search-status" id="distribution-search-status" role="status" aria-live="polite"></div>
    </div>

    <div class="distribution-controls" id="distribution-controls">
        <div class="distribution-toolbar">
            <button type="button" class="distribution-filters-toggle" id="distribution-filters-toggle" aria-expanded="false" aria-controls="distribution-filters">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M7 12h10M10 18h4"/></svg>
                Filters <span class="distribution-filters-count" hidden></span>
            </button>
            <div class="distribution-sort" role="group" aria-label="Sort distributions">
                <span class="distribution-filter-label distribution-sort-label">Sort</span>
                <button type="button" class="distribution-chip" data-sort="az">A&ndash;Z</button>
                <button type="button" class="distribution-chip" data-sort="popular"><span class="lbl-long">Most popular</span><span class="lbl-short">Popular</span></button>
            </div>
        </div>
        <div class="distribution-filters" id="distribution-filters">
            <div class="distribution-filter-chips" role="group" aria-label="Filter by base">
                <span class="distribution-filter-label">Base</span>
                <button type="button" class="distribution-chip" data-base="">All</button>
                <button type="button" class="distribution-chip" data-base="debian">Debian</button>
                <button type="button" class="distribution-chip" data-base="ubuntu">Ubuntu</button>
                <button type="button" class="distribution-chip" data-base="arch">Arch</button>
                <button type="button" class="distribution-chip" data-base="fedora">Fedora / RHEL</button>
                <button type="button" class="distribution-chip" data-base="gentoo">Gentoo</button>
                <button type="button" class="distribution-chip" data-base="slackware">Slackware</button>
                <button type="button" class="distribution-chip" data-base="bsd">BSD</button>
                <button type="button" class="distribution-chip" data-base="independent">Independent</button>
            </div>
            <label class="distribution-filter-select">
                <span class="distribution-filter-label">Desktop</span>
                <select id="distribution-filter-de">
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
        <p class="distribution-filter-status" id="distribution-filter-status" hidden></p>
    </div>

    <div id="distribution-results">

    {% assign linux_distributions = site.pages | where: "Category", "Distribution" | where_exp: "item", "item.type != 'BSD'" | where_exp: "item", "item.type != 'Other'" | sort: "title" %}
    {% assign bsd_distributions = site.pages | where: "Category", "Distribution" | where: "type", "BSD" | sort: "title" %}
    {% assign rank_list = site.data.rank.rankings.d30.distributions | default: site.data.rank.distributions %}
    {% assign other_distributions = site.pages | where: "Category", "Distribution" | where: "type", "Other" | sort: "title" %}

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>GNU/Linux</h2>
            <span class="distribution-count" data-distribution-count>{{ linux_distributions | size }} distributions</span>
            <a class="distribution-rank-link" href="/page-hit-rank/">Popularity ranking &rarr;</a>
        </div>
        <div class="distribution-grid">
            {% for page in linux_distributions %}
            {% include os-meta.html page=page %}
            {% assign card_rank = rank_list | where: "url", page.url | first %}
            <a href="{{ page.url }}" class="distribution-card" data-name="{{ page.title | downcase }} {{ page.url | split: '/' | last | downcase }}" data-bases="{{ re_base_keys }}" data-des="{{ re_de_keys }}" data-rank="{% if card_rank.current %}{{ card_rank.current.rank }}{% endif %}">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                    <div class="distribution-card-fallback" aria-hidden="true" style="display:none">OS</div>
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">OS</div>
                    {% endif %}
                </div>
                <div class="distribution-card-body">
                    <div class="distribution-card-title">{{ page.title }}</div>
                    {% if re_base_label or card_rank.current %}<div class="distribution-card-meta">
                        {% if re_base_label %}<span>{{ re_base_label }}</span>{% endif %}
                        {% if card_rank.current %}<span class="distribution-card-rank" title="#{{ card_rank.current.rank }} in the last 30 days on the popularity ranking">#{{ card_rank.current.rank }}</span>{% endif %}
                    </div>{% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
    </section>

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>BSD</h2>
            <span class="distribution-count" data-distribution-count>{{ bsd_distributions | size }} distributions</span>
        </div>
        <div class="distribution-grid">
            {% for page in bsd_distributions %}
            {% include os-meta.html page=page %}
            {% assign card_rank = rank_list | where: "url", page.url | first %}
            <a href="{{ page.url }}" class="distribution-card" data-name="{{ page.title | downcase }} {{ page.url | split: '/' | last | downcase }}" data-bases="{{ re_base_keys }}" data-des="{{ re_de_keys }}" data-rank="{% if card_rank.current %}{{ card_rank.current.rank }}{% endif %}">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                    <div class="distribution-card-fallback" aria-hidden="true" style="display:none">BSD</div>
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">BSD</div>
                    {% endif %}
                </div>
                <div class="distribution-card-body">
                    <div class="distribution-card-title">{{ page.title }}</div>
                    {% if re_base_label or card_rank.current %}<div class="distribution-card-meta">
                        {% if re_base_label %}<span>{{ re_base_label }}</span>{% endif %}
                        {% if card_rank.current %}<span class="distribution-card-rank" title="#{{ card_rank.current.rank }} in the last 30 days on the popularity ranking">#{{ card_rank.current.rank }}</span>{% endif %}
                    </div>{% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
    </section>

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>Others</h2>
            <span class="distribution-count" data-distribution-count>{{ other_distributions | size }} distributions</span>
        </div>
        <div class="distribution-grid">
            {% for page in other_distributions %}
            {% include os-meta.html page=page %}
            {% assign card_rank = rank_list | where: "url", page.url | first %}
            <a href="{{ page.url }}" class="distribution-card" data-name="{{ page.title | downcase }} {{ page.url | split: '/' | last | downcase }}" data-bases="{{ re_base_keys }}" data-des="{{ re_de_keys }}" data-rank="{% if card_rank.current %}{{ card_rank.current.rank }}{% endif %}">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                    <div class="distribution-card-fallback" aria-hidden="true" style="display:none">OS</div>
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">OS</div>
                    {% endif %}
                </div>
                <div class="distribution-card-body">
                    <div class="distribution-card-title">{{ page.title }}</div>
                    {% if re_base_label or card_rank.current %}<div class="distribution-card-meta">
                        {% if re_base_label %}<span>{{ re_base_label }}</span>{% endif %}
                        {% if card_rank.current %}<span class="distribution-card-rank" title="#{{ card_rank.current.rank }} in the last 30 days on the popularity ranking">#{{ card_rank.current.rank }}</span>{% endif %}
                    </div>{% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
    </section>

    <p class="distribution-empty" id="distribution-empty" role="status">
        No distributions match <strong id="distribution-empty-term"></strong>. Try a different name or clear the filters.
    </p>

    {% include distro-group-links.html %}

    </div><!-- /#distribution-results -->

    <div class="distribution-ad">
        <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <div class="ad">
            <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6380671811722843" data-ad-slot="8487642304" data-ad-format="auto"></ins>
        </div>
        <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>

    <div class="distribution-comments">
        <h2>Propose a Distribution</h2>
        <p>If you are not able to see a distribution of your interest, comment below and we'll review and add it.</p>
        {% include echothread.html %}
    </div>
</div>

<script>
(function () {
    var input = document.getElementById('distribution-search-input');
    if (!input) return;

    var clearBtn = document.getElementById('distribution-search-clear');
    var status = document.getElementById('distribution-search-status');
    var empty = document.getElementById('distribution-empty');
    var emptyTerm = document.getElementById('distribution-empty-term');
    var filterBar = document.getElementById('distribution-controls');
    var filterPanel = document.getElementById('distribution-filters');
    var filterToggle = document.getElementById('distribution-filters-toggle');
    var filterCount = filterToggle.querySelector('.distribution-filters-count');
    var filterStatus = document.getElementById('distribution-filter-status');
    var baseChips = filterBar.querySelectorAll('[data-base]');
    var sortChips = filterBar.querySelectorAll('[data-sort]');
    var deSelect = document.getElementById('distribution-filter-de');
    var sections = Array.prototype.slice.call(document.querySelectorAll('.distribution-section'));

    sections.forEach(function (section) {
        section._grid = section.querySelector('.distribution-grid');
        section._cards = Array.prototype.slice.call(section.querySelectorAll('.distribution-card'));
        section._cards.forEach(function (card, i) { card._order = i; });
        section._countEl = section.querySelector('[data-distribution-count]');
    });

    var params = new URLSearchParams(window.location.search);
    var state = {
        base: params.get('base') || '',
        de: params.get('de') || '',
        sort: params.get('sort') === 'popular' ? 'popular' : 'az'
    };
    if (!filterBar.querySelector('[data-base="' + state.base + '"]')) state.base = '';
    if (!deSelect.querySelector('option[value="' + state.de + '"]')) state.de = '';

    function label(n) {
        return n + (n === 1 ? ' distribution' : ' distributions');
    }

    function hasToken(list, token) {
        return (' ' + (list || '') + ' ').indexOf(' ' + token + ' ') >= 0;
    }

    function rankOf(card) {
        var r = parseInt(card.getAttribute('data-rank'), 10);
        return isNaN(r) ? Infinity : r;
    }

    function applySort() {
        sections.forEach(function (section) {
            var cards = section._cards.slice();
            if (state.sort === 'popular') {
                cards.sort(function (a, b) {
                    var ra = rankOf(a), rb = rankOf(b);
                    if (ra !== rb) return ra < rb ? -1 : 1;
                    return a._order - b._order;
                });
            } else {
                cards.sort(function (a, b) { return a._order - b._order; });
            }
            cards.forEach(function (card) { section._grid.appendChild(card); });
        });
    }

    function syncUrl() {
        var q = new URLSearchParams(window.location.search);
        ['base', 'de', 'sort'].forEach(function (k) { q.delete(k); });
        if (state.base) q.set('base', state.base);
        if (state.de) q.set('de', state.de);
        if (state.sort === 'popular') q.set('sort', 'popular');
        var qs = q.toString();
        history.replaceState(null, '', window.location.pathname + (qs ? '?' + qs : '') + window.location.hash);
    }

    function applyFilter() {
        var query = input.value.trim().toLowerCase();
        var total = 0;

        sections.forEach(function (section) {
            var visible = 0;
            section._cards.forEach(function (card) {
                var match = (!query || (card.getAttribute('data-name') || '').indexOf(query) !== -1) &&
                    (!state.base || hasToken(card.getAttribute('data-bases'), state.base)) &&
                    (!state.de || hasToken(card.getAttribute('data-des'), state.de));
                card.hidden = !match;
                if (match) visible++;
            });
            if (section._countEl) section._countEl.textContent = label(visible);
            section.hidden = visible === 0;
            total += visible;
        });

        var hasQuery = query.length > 0;
        var hasFilters = !!(state.base || state.de);
        clearBtn.classList.toggle('is-visible', hasQuery);

        if ((hasQuery || hasFilters) && total === 0) {
            emptyTerm.textContent = hasQuery ? '"' + input.value.trim() + '"' : 'these filters';
            empty.style.display = 'block';
        } else {
            empty.style.display = 'none';
        }

        status.textContent = (hasQuery || hasFilters) ? total + ' ' + (total === 1 ? 'result' : 'results') + ' found' : '';

        var active = (state.base ? 1 : 0) + (state.de ? 1 : 0);
        filterCount.hidden = active === 0;
        filterCount.textContent = active;
        filterStatus.hidden = !hasFilters;
        if (hasFilters) {
            filterStatus.innerHTML = 'Showing ' + label(total) + '. ' +
                '<button type="button" class="distribution-filter-reset">Clear filters</button>';
        }
    }

    function render() {
        baseChips.forEach(function (chip) {
            var on = chip.getAttribute('data-base') === state.base;
            chip.classList.toggle('is-active', on);
            chip.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        sortChips.forEach(function (chip) {
            var on = chip.getAttribute('data-sort') === state.sort;
            chip.classList.toggle('is-active', on);
            chip.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        deSelect.value = state.de;
        applySort();
        applyFilter();
        syncUrl();
    }

    input.addEventListener('input', applyFilter);

    input.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && input.value) {
            input.value = '';
            applyFilter();
        }
    });

    clearBtn.addEventListener('click', function () {
        input.value = '';
        applyFilter();
        input.focus();
    });

    baseChips.forEach(function (chip) {
        chip.addEventListener('click', function () {
            state.base = chip.getAttribute('data-base');
            render();
        });
    });
    sortChips.forEach(function (chip) {
        chip.addEventListener('click', function () {
            state.sort = chip.getAttribute('data-sort');
            render();
        });
    });
    filterToggle.addEventListener('click', function () {
        var open = !filterPanel.classList.contains('is-open');
        filterPanel.classList.toggle('is-open', open);
        filterToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    filterStatus.addEventListener('click', function (e) {
        if (!e.target.classList.contains('distribution-filter-reset')) return;
        state.base = '';
        state.de = '';
        render();
    });
    deSelect.addEventListener('change', function () {
        state.de = deSelect.value;
        render();
    });

    render();
})();
</script>
