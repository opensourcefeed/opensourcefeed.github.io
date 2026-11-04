---
layout: default
title: Most Popular Open Source OS & Desktop Environments (30 Days and 3 Months)
description: Ranking of Linux, BSD, and open source operating systems plus desktop environments using OpenSourceFeed page views for the last 30 days and last 3 months.
image: "/assets/images/meta/logo-collage.png"
seo:
  type: CollectionPage
  name: Popular Open Source OS and Desktop Ranking
---
{% include rank-styles.html %}

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
        {% include rank-board.html entries=d30_distributions kind="os" compare="previous 30 days" label="operating system" trend_months=site.data.rank.meta.trend_months %}
      </div>
      <div class="rank-section" data-period="30d" data-type="desktop" id="last-30-days-desktop">
        <h3>Desktop Environments</h3>
        {% include rank-board.html entries=d30_desktops kind="desktop" compare="previous 30 days" label="desktop environment" trend_months=site.data.rank.meta.trend_months %}
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

    {% include rank-archive-list.html %}

    <section class="rank-method" aria-labelledby="methodology">
      <h2 id="methodology">Methodology</h2>
      <dl>
        <dt>Data source</dt>
        <dd>Page views of each distribution and desktop page on OpenSourceFeed, from the <a href="https://developers.google.com/analytics/">Google Analytics</a> Data API. Hits on old or alias URLs are merged into the main page.</dd>
        <dt>Popularity score</dt>
        <dd>Each entry's page views divided by those of the #1 entry in the same list, scaled to 100.</dd>
        <dt>Rank change</dt>
        <dd>The current rank compared with the rank in the preceding period of the same length, for example the last 30 days against the 30 days before them. &ldquo;NEW&rdquo; means the entry was not ranked in the preceding period.</dd>
        <dt>12-month trend</dt>
        <dd>Each entry's rank in every complete calendar month of the last year, then its current 30-day rank. Monthly and yearly rankings are frozen in the archive and never change afterwards.</dd>
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
