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

    <div id="distribution-results">

    {% assign linux_distributions = site.pages | where: "Category", "Distribution" | where_exp: "item", "item.type != 'BSD'" | where_exp: "item", "item.type != 'Other'" | sort: "title" %}
    {% assign bsd_distributions = site.pages | where: "Category", "Distribution" | where: "type", "BSD" | sort: "title" %}
    {% assign other_distributions = site.pages | where: "Category", "Distribution" | where: "type", "Other" | sort: "title" %}

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>GNU/Linux</h2>
            <span class="distribution-count" data-distribution-count>{{ linux_distributions | size }} distributions</span>
        </div>
        <div class="distribution-grid">
            {% for page in linux_distributions %}
            <a href="{{ page.url }}" class="distribution-card" data-name="{{ page.title | downcase }} {{ page.url | split: '/' | last | downcase }}">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                    <div class="distribution-card-fallback" aria-hidden="true" style="display:none">OS</div>
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">OS</div>
                    {% endif %}
                </div>
                <div class="distribution-card-title">{{ page.title }}</div>
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
            <a href="{{ page.url }}" class="distribution-card" data-name="{{ page.title | downcase }} {{ page.url | split: '/' | last | downcase }}">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                    <div class="distribution-card-fallback" aria-hidden="true" style="display:none">BSD</div>
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">BSD</div>
                    {% endif %}
                </div>
                <div class="distribution-card-title">{{ page.title }}</div>
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
            <a href="{{ page.url }}" class="distribution-card" data-name="{{ page.title | downcase }} {{ page.url | split: '/' | last | downcase }}">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                    <div class="distribution-card-fallback" aria-hidden="true" style="display:none">OS</div>
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">OS</div>
                    {% endif %}
                </div>
                <div class="distribution-card-title">{{ page.title }}</div>
            </a>
            {% endfor %}
        </div>
    </section>

    <p class="distribution-empty" id="distribution-empty" role="status">
        No distributions match <strong id="distribution-empty-term"></strong>. Try a different name.
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
    var sections = Array.prototype.slice.call(document.querySelectorAll('.distribution-section'));

    sections.forEach(function (section) {
        section._cards = Array.prototype.slice.call(section.querySelectorAll('.distribution-card'));
        section._countEl = section.querySelector('[data-distribution-count]');
    });

    function label(n) {
        return n + (n === 1 ? ' distribution' : ' distributions');
    }

    function applyFilter() {
        var query = input.value.trim().toLowerCase();
        var total = 0;

        sections.forEach(function (section) {
            var visible = 0;
            section._cards.forEach(function (card) {
                var match = !query || (card.getAttribute('data-name') || '').indexOf(query) !== -1;
                card.hidden = !match;
                if (match) visible++;
            });
            if (section._countEl) section._countEl.textContent = label(visible);
            section.hidden = visible === 0;
            total += visible;
        });

        var hasQuery = query.length > 0;
        clearBtn.classList.toggle('is-visible', hasQuery);

        if (hasQuery && total === 0) {
            emptyTerm.textContent = '"' + input.value.trim() + '"';
            empty.style.display = 'block';
        } else {
            empty.style.display = 'none';
        }

        if (hasQuery) {
            status.textContent = total + ' ' + (total === 1 ? 'result' : 'results') + ' found';
        } else {
            status.textContent = '';
        }
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

    applyFilter();
})();
</script>
