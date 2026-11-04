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
    color:#555;
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
    border-left:4px solid #007acc;
    padding-left:10px;
}

.distribution-count{
    color:#6b7280;
    font-size:0.95rem;
}

.distribution-grid{
    display:grid;
    grid-template-columns:repeat(auto-fill, minmax(210px, 1fr));
    gap:12px;
}

.distribution-card{
    display:flex;
    align-items:center;
    gap:12px;
    min-height:78px;
    padding:12px 14px;
    border:1px solid #e7e7e7;
    border-radius:12px;
    background:#fff;
    color:inherit;
    text-decoration:none;
    transition:transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.distribution-card:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    border-color:#d9e9f8;
}

.distribution-card:focus-visible{
    outline:3px solid rgba(0, 122, 204, 0.25);
    outline-offset:2px;
}

.distribution-card-media{
    width:52px;
    height:52px;
    flex:0 0 52px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:12px;
    background:#f7f9fb;
}

.distribution-card-media img{
    max-width:40px;
    max-height:40px;
    object-fit:contain;
}

.distribution-card-fallback{
    color:#6b7280;
    font-size:0.78rem;
    font-weight:700;
    letter-spacing:0.04em;
}

.distribution-card-title{
    font-weight:600;
    line-height:1.3;
    color:#222;
}

.distribution-card:hover .distribution-card-title,
.distribution-card:focus-visible .distribution-card-title{
    color:#007acc;
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
    border-left:4px solid #007acc;
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
    color:#9aa3af;
    pointer-events:none;
}

.distribution-search-input{
    width:100%;
    padding:12px 44px 12px 44px;
    font-size:1rem;
    line-height:1.4;
    color:#222;
    background:#fff;
    border:1px solid #d9dde3;
    border-radius:999px;
    box-shadow:0 1px 2px rgba(0,0,0,0.04);
    transition:border-color 0.2s ease, box-shadow 0.2s ease;
    -webkit-appearance:none;
    appearance:none;
}

.distribution-search-input::placeholder{
    color:#9aa3af;
}

.distribution-search-input:focus{
    outline:none;
    border-color:#007acc;
    box-shadow:0 0 0 3px rgba(0, 122, 204, 0.18);
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
    color:#6b7280;
    font-size:1.25rem;
    line-height:1;
    cursor:pointer;
    transition:background 0.2s ease, color 0.2s ease;
}

.distribution-search-clear:hover{
    background:#f1f3f5;
    color:#222;
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
    color:#6b7280;
}

.distribution-empty strong{
    color:#222;
}


.distribution-card{ position:relative; }
.distribution-card-body{ display:flex; flex-direction:column; gap:2px; min-width:0; padding-right:2.4rem; }
.distribution-card-meta{ color:#6b7280; font-size:0.78rem; }
.distribution-card-rank{
    position:absolute;
    top:8px;
    right:10px;
    padding:1px 7px;
    border-radius:999px;
    background:#eaf2fc;
    color:#046cdc;
    font-size:0.72rem;
    font-weight:700;
    font-variant-numeric:tabular-nums;
}

.distribution-filters{
    display:flex;
    flex-direction:column;
    gap:0.6rem;
    max-width:960px;
    margin:0 auto 1.75rem auto;
    padding:0.85rem 1rem;
    border:1px solid #e3ecf7;
    border-radius:14px;
    background:#f6f9fd;
}
.distribution-filter-chips,
.distribution-filter-row,
.distribution-sort{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:0.4rem;
}
.distribution-filter-row{ gap:0.6rem 1.25rem; }
.distribution-filter-label{ font-size:0.85rem; font-weight:700; color:#6b7280; margin-right:0.15rem; }
.distribution-chip{
    appearance:none;
    padding:0.3rem 0.75rem;
    border:1px solid #e3ecf7;
    border-radius:999px;
    background:#fff;
    color:#222;
    font-size:0.85rem;
    font-weight:600;
    line-height:1.2;
    cursor:pointer;
}
.distribution-chip:hover{ border-color:#5aa2ee; color:#046cdc; }
.distribution-chip.is-active{ background:#046cdc; border-color:#046cdc; color:#fff; }
.distribution-filter-select{ display:flex; align-items:center; gap:0.5rem; margin:0; }
.distribution-filter-select select{
    padding:0.3rem 2rem 0.3rem 0.75rem;
    border:1px solid #e3ecf7;
    border-radius:999px;
    background-color:#fff;
    color:#222;
    font-size:0.85rem;
    font-weight:600;
}
.distribution-rank-link{ margin-left:auto; font-size:0.85rem; font-weight:600; }
@media (max-width:575px){
    .distribution-rank-link{ margin-left:0; }
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
        Browse the collection to compare distributions, discover alternatives, and jump into detailed pages.
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
        <div class="distribution-filter-row">
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
            <div class="distribution-sort" role="group" aria-label="Sort distributions">
                <span class="distribution-filter-label">Sort</span>
                <button type="button" class="distribution-chip" data-sort="az">A&ndash;Z</button>
                <button type="button" class="distribution-chip" data-sort="popular">Most popular</button>
            </div>
            <a class="distribution-rank-link" href="/page-hit-rank/">Full popularity ranking &rarr;</a>
        </div>
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
                    {% if re_base_label %}<div class="distribution-card-meta">{{ re_base_label }}</div>{% endif %}
                </div>
                {% if card_rank.current %}<span class="distribution-card-rank" title="#{{ card_rank.current.rank }} in the last 30 days on the popularity ranking">#{{ card_rank.current.rank }}</span>{% endif %}
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
                    {% if re_base_label %}<div class="distribution-card-meta">{{ re_base_label }}</div>{% endif %}
                </div>
                {% if card_rank.current %}<span class="distribution-card-rank" title="#{{ card_rank.current.rank }} in the last 30 days on the popularity ranking">#{{ card_rank.current.rank }}</span>{% endif %}
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
                    {% if re_base_label %}<div class="distribution-card-meta">{{ re_base_label }}</div>{% endif %}
                </div>
                {% if card_rank.current %}<span class="distribution-card-rank" title="#{{ card_rank.current.rank }} in the last 30 days on the popularity ranking">#{{ card_rank.current.rank }}</span>{% endif %}
            </a>
            {% endfor %}
        </div>
    </section>

    <p class="distribution-empty" id="distribution-empty" role="status">
        No distributions match <strong id="distribution-empty-term"></strong>. Try a different name or clear the filters.
    </p>

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
    var filterBar = document.getElementById('distribution-filters');
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
    deSelect.addEventListener('change', function () {
        state.de = deSelect.value;
        render();
    });

    render();
})();
</script>
