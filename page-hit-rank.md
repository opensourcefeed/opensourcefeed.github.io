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
.distribution h1 {
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.8rem;
}
.distribution p {
  color: #555;
}
.rank-page {
  max-width: 1080px;
  margin: 0 auto;
  padding: 1rem 0 2rem;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.rank-page .row {
  --bs-gutter-x: 0;
}
.rank-page .table {
  margin-bottom: 0;
  width: 100%;
}
.rank-page .table thead th {
  white-space: nowrap;
}
.rank-page .rank-table td + td {
  word-break: normal;
  overflow-wrap: normal;
}
.rank-page .swipe-hint {
  margin-top: -0.25rem;
  margin-bottom: 0.75rem;
}
.rank-page .name-col a {
  white-space: normal;
}
.rank-page .rank-col,
.rank-page .change-col {
  white-space: nowrap;
  width: 1%;
}
.rank-page .rank-col {
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}
.rank-page .score-col {
  width: 38%;
  min-width: 9rem;
}
.rank-page .score-wrap {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.rank-page .score-bar {
  flex: 1;
  height: 0.5rem;
  border-radius: 999px;
  background: #e8f0fb;
  overflow: hidden;
}
.rank-page .score-bar span {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #5aa2ee, #046cdc);
}
.rank-page .score-value {
  min-width: 2rem;
  text-align: right;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}
.rank-page .rank-change {
  display: inline-block;
  min-width: 2.6rem;
  padding: 0.1rem 0.45rem;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 700;
  text-align: center;
  font-variant-numeric: tabular-nums;
}
.rank-page .rank-change.is-up { background: #e3f6ea; color: #157a3c; }
.rank-page .rank-change.is-down { background: #fde8e8; color: #b42323; }
.rank-page .rank-change.is-same { background: #f1f3f5; color: #6c757d; }
.rank-page .rank-change.is-new { background: #eaf2fc; color: #046cdc; letter-spacing: 0.03em; }
.rank-page .period-range {
  margin-top: -0.4rem;
}
.rank-page details > summary {
  cursor: pointer;
  font-weight: 600;
  color: #046cdc;
}
.rank-page .period-block {
  margin-top: 1.5rem;
}
.rank-page .period-title {
  scroll-margin-top: 6rem;
}
.rank-page .rank-summary {
  margin-bottom: 0.75rem;
}
.rank-page .quick-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1rem;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}
.rank-page .quick-link-label {
  color: #555;
  font-weight: 600;
  margin-right: 0.15rem;
}
.rank-page .quick-link-group,
.rank-page .category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  justify-content: center;
}
.rank-page .quick-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2rem;
  padding: 0.35rem 0.75rem;
  border: 1px solid #d3e3f5;
  border-radius: 999px;
  background: #fff;
  color: #046cdc;
  line-height: 1.2;
  text-decoration: none;
  transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
}
.rank-page .quick-link:hover,
.rank-page .quick-link:focus {
  background: #eaf2fc;
  border-color: #a8c9f0;
  color: #0357b0;
}
.rank-page .quick-link.is-active {
  background: #046cdc;
  border-color: #046cdc;
  color: #fff;
}
.rank-page .quick-link.is-active:hover,
.rank-page .quick-link.is-active:focus {
  background: #0357b0;
  border-color: #0357b0;
  color: #fff;
}
.rank-page .status-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 0.9rem;
  align-items: center;
  margin-bottom: 1rem;
  padding: 0.75rem 0.9rem;
  border: 1px solid #dce7f7;
  border-radius: 0.75rem;
  background: #f5f9fe;
}
.rank-page .status-legend-label {
  font-weight: 600;
  color: #046cdc;
}
.rank-page .status-legend-item {
  white-space: nowrap;
}
.rank-page .category-tabs {
  gap: 0.5rem;
  margin-bottom: 0.85rem;
  justify-content: center;
}
.rank-page .category-tab {
  appearance: none;
  border: 1px solid #d3e3f5;
  border-radius: 999px;
  background: #fff;
  color: #046cdc;
  padding: 0.4rem 0.9rem;
  font-size: 0.95rem;
  line-height: 1.2;
  font-weight: 600;
  text-decoration: none;
}
.rank-page .category-tab.is-active {
  background: #046cdc;
  border-color: #046cdc;
  color: #fff;
}
.rank-page .rank-section {
  padding: 1rem;
  border: 1px solid #e3ecf7;
  border-radius: 0.9rem;
  background: #fff;
  box-shadow: 0 1px 3px rgba(4, 108, 220, 0.08);
}
.rank-page .rank-section h3 {
  margin-bottom: 0.85rem;
}
@media (max-width: 575.98px) {
  .rank-page .quick-links {
    flex-direction: column;
    gap: 0.75rem;
  }
  .rank-page .quick-link-group,
  .rank-page .category-tabs {
    gap: 0.45rem;
  }
  .rank-page .quick-link-label {
    width: 100%;
    margin-right: 0;
    margin-bottom: 0.1rem;
  }
  .rank-page .status-legend {
    padding: 0.65rem 0.75rem;
    gap: 0.35rem 0.75rem;
  }
  .rank-page .rank-section {
    padding: 0.85rem;
  }
  .rank-page .rank-table {
    font-size: 0.95rem;
  }
  .rank-page .rank-table th,
  .rank-page .rank-table td {
    padding: 0.45rem;
  }
}
.rank-page .rank-section[hidden],
.rank-page .period-block[hidden] {
  display: none !important;
}
</style>

{% assign rankings = site.data.rank.rankings %}
{% assign d30_distributions = rankings.d30.distributions | default: site.data.rank.distributions %}
{% assign d30_desktops = rankings.d30.desktops | default: site.data.rank.desktops %}
{% assign m3_distributions = rankings.m3.distributions | default: site.data.rank.distributions %}
{% assign m3_desktops = rankings.m3.desktops | default: site.data.rank.desktops %}
{% assign periods = site.data.rank.meta.periods %}

<div class="distribution">
  <div class="rank-page">
    <h1>Open Source Popularity Ranking</h1>
    <hr>
    <p>This page shows popularity rankings of open source operating systems and desktop environments based on OpenSourceFeed page hits.</p>
    <p>Rankings are shown for the last 30 days and the last 3 months. <strong>Change</strong> compares each rank with the equivalent preceding period, and <strong>Popularity</strong> is relative to the #1 entry (100).</p>

    {% assign last_updated = site.data.rank.meta.currentDate | default: site.data.rank.meta.current_date %}
    {% if last_updated %}
    <p class="text-muted small mb-3">Last updated:
      <time datetime="{{ last_updated | date_to_xmlschema }}" itemprop="dateModified">{{ last_updated | date: "%B %-d, %Y" }}</time>
    </p>
    {% endif %}
    <div class="small quick-links" aria-label="Ranking filters">
      <div class="quick-link-group" role="group" aria-label="Select time range">
        <a class="quick-link" data-filter-period="30d" href="?period=30d&type=os">30 Days</a>
        <a class="quick-link" data-filter-period="3m" href="?period=3m&type=os">3 Months</a>
      </div>
    </div>
    <div class="category-tabs" role="tablist" aria-label="Ranking category">
      <a class="category-tab" data-filter-type="os" href="?period=30d&type=os" role="tab" aria-controls="rank-results">Operating Systems</a>
      <a class="category-tab" data-filter-type="desktop" href="?period=30d&type=desktop" role="tab" aria-controls="rank-results">Desktop Environments</a>
    </div>

    <p class="small text-muted d-md-none swipe-hint">Swipe the table horizontally to view all columns.</p>

    <section class="period-block" data-period="30d" aria-labelledby="last-30-days">
      <h2 id="last-30-days" class="period-title">Last 30 Days</h2>
      {% if periods.d30.current %}<p class="small text-muted period-range">{{ periods.d30.current.start | date: "%b %-d" }} &ndash; {{ periods.d30.current.end | date: "%b %-d, %Y" }}, compared with {{ periods.d30.previous.start | date: "%b %-d" }} &ndash; {{ periods.d30.previous.end | date: "%b %-d" }}</p>{% endif %}
      <div id="rank-results" class="row g-4">
        <div class="col-12 rank-section" data-period="30d" data-type="os" id="last-30-days-os">
          <h3>Operating Systems</h3>
          {% include rank-table.html entries=d30_distributions name_label="OS" compare="previous 30 days" %}
        </div>

        <div class="col-12 rank-section" data-period="30d" data-type="desktop" id="last-30-days-desktop">
          <h3>Desktop Environments</h3>
          {% include rank-table.html entries=d30_desktops name_label="Desktop / WM" compare="previous 30 days" %}
        </div>
      </div>
    </section>

    <section class="period-block" data-period="3m" aria-labelledby="last-3-months">
      <h2 id="last-3-months" class="period-title">Last 3 Months</h2>
      {% if periods.m3.current %}<p class="small text-muted period-range">{{ periods.m3.current.start | date: "%b %-d" }} &ndash; {{ periods.m3.current.end | date: "%b %-d, %Y" }}, compared with {{ periods.m3.previous.start | date: "%b %-d" }} &ndash; {{ periods.m3.previous.end | date: "%b %-d" }}</p>{% endif %}
      <div class="row g-4">
        <div class="col-12 rank-section" data-period="3m" data-type="os" id="last-3-months-os">
          <h3>Operating Systems</h3>
          {% include rank-table.html entries=m3_distributions name_label="OS" compare="previous 3 months" %}
        </div>

        <div class="col-12 rank-section" data-period="3m" data-type="desktop" id="last-3-months-desktop">
          <h3>Desktop Environments</h3>
          {% include rank-table.html entries=m3_desktops name_label="Desktop / WM" compare="previous 3 months" %}
        </div>
      </div>
    </section>

    <script>
      (function () {
        var sections = document.querySelectorAll('.rank-section');
        var periodBlocks = document.querySelectorAll('.period-block');
        var categoryTabs = document.querySelectorAll('.category-tab');

        function isValidPeriod(period) {
          return period === '30d' || period === '3m';
        }

        function isValidType(type) {
          return type === 'os' || type === 'desktop';
        }

        function stateToTargetId(period, type) {
          if (!isValidPeriod(period)) return '';
          if (period === '30d') return 'last-30-days';
          if (period === '3m') return 'last-3-months';
          return '';
        }

        function hashToLegacyState(hash) {
          if (!hash) return {};
          if (hash === '#last-30-days') return { period: '30d', type: null };
          if (hash === '#last-30-days-os') return { period: '30d', type: 'os' };
          if (hash === '#last-30-days-desktop') return { period: '30d', type: 'desktop' };
          if (hash === '#last-3-months') return { period: '3m', type: null };
          if (hash === '#last-3-months-os') return { period: '3m', type: 'os' };
          if (hash === '#last-3-months-desktop') return { period: '3m', type: 'desktop' };
          return {};
        }

        function syncUrl(period, type, replaceState) {
          var url = new URL(window.location.href);

          url.searchParams.delete('period');
          url.searchParams.delete('type');

          if (isValidPeriod(period)) {
            url.searchParams.set('period', period);
          }
          if (isValidPeriod(period) && isValidType(type)) {
            url.searchParams.set('type', type);
          }

          url.hash = '';

          var next = url.pathname + url.search;
          if (replaceState) {
            history.replaceState(null, '', next);
          } else {
            history.pushState(null, '', next);
          }
        }

        function applyFilters(period, type) {
          var hasPeriod = isValidPeriod(period);
          var hasType = isValidType(type);

          sections.forEach(function (section) {
            var periodMatch = !hasPeriod || section.dataset.period === period;
            var typeMatch = !hasType || section.dataset.type === type;
            section.hidden = !(periodMatch && typeMatch);
          });

          periodBlocks.forEach(function (block) {
            if (!hasPeriod) {
              block.hidden = false;
              return;
            }
            block.hidden = block.dataset.period !== period;
          });
        }

        function updateQuickLinks(period, type) {
          var normalizedPeriod = isValidPeriod(period) ? period : '30d';
          var normalizedType = isValidType(type) ? type : 'os';

          document.querySelectorAll('.quick-link').forEach(function (link) {
            var linkPeriod = link.dataset.filterPeriod;
            var matchesPeriod = false;
            var href = new URL(link.getAttribute('href'), window.location.href);

            if (linkPeriod) {
              matchesPeriod = linkPeriod === normalizedPeriod;
              href.searchParams.set('period', linkPeriod);
              href.searchParams.set('type', normalizedType);
            }

            link.classList.toggle('is-active', matchesPeriod);

            if (link.classList.contains('is-active')) {
              link.setAttribute('aria-current', 'page');
            } else {
              link.removeAttribute('aria-current');
            }

            link.setAttribute('href', href.pathname + href.search);
          });
        }

        function updateCategoryTabs(period, type) {
          var normalizedPeriod = isValidPeriod(period) ? period : '30d';
          var normalizedType = isValidType(type) ? type : 'os';

          categoryTabs.forEach(function (tab) {
            var tabType = tab.dataset.filterType;
            var href = new URL(tab.getAttribute('href'), window.location.href);
            var isActive = tabType === normalizedType;

            href.searchParams.set('period', normalizedPeriod);
            href.searchParams.set('type', tabType);

            tab.classList.toggle('is-active', isActive);
            tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
            tab.setAttribute('tabindex', isActive ? '0' : '-1');
            tab.setAttribute('href', href.pathname + href.search);
          });
        }

        function getHeaderOffset() {
          var navbar = document.querySelector('.navbar');
          if (!navbar) return 12;

          var style = window.getComputedStyle(navbar);
          var isPinned = style.position === 'fixed' || style.position === 'sticky';
          if (!isPinned) return 12;

          return navbar.offsetHeight + 12;
        }

        function scrollToTarget(targetId) {
          if (!targetId) return;
          var target = document.getElementById(targetId);
          if (!target) return;

          var top = target.getBoundingClientRect().top + window.pageYOffset - getHeaderOffset();
          window.scrollTo({ top: top, behavior: 'smooth' });
        }

        var params = new URLSearchParams(window.location.search);
        var paramPeriod = params.get('period');
        var paramType = params.get('type');
        var hashState = hashToLegacyState(window.location.hash);

        var period = null;
        var type = null;

        if (isValidPeriod(hashState.period)) {
          period = hashState.period;
          if (isValidType(hashState.type)) {
            type = hashState.type;
          }
        } else if (isValidPeriod(paramPeriod)) {
          period = paramPeriod;
          if (isValidType(paramType)) {
            type = paramType;
          }
        }

        if (!isValidPeriod(period)) period = '30d';
        if (!isValidType(type)) type = 'os';

        applyFilters(period, type);
        updateQuickLinks(period, type);
        updateCategoryTabs(period, type);
        syncUrl(period, type, true);

        document.querySelectorAll('.quick-links a[href*="?period="]').forEach(function (link) {
          link.addEventListener('click', function (e) {
            var href = link.getAttribute('href');
            if (!href) return;
            var linkUrl = new URL(href, window.location.href);
            var nextPeriod = linkUrl.searchParams.get('period');
            var nextType = linkUrl.searchParams.get('type');
            if (!isValidPeriod(nextPeriod)) return;

            e.preventDefault();
            period = nextPeriod;
            type = isValidType(nextType) ? nextType : 'os';
            applyFilters(nextPeriod, nextType);
            updateQuickLinks(nextPeriod, nextType);
            updateCategoryTabs(nextPeriod, nextType);
            syncUrl(nextPeriod, nextType, false);
          });
        });

        categoryTabs.forEach(function (tab) {
          tab.addEventListener('click', function (e) {
            var tabType = tab.dataset.filterType;
            if (!isValidType(tabType)) return;

            e.preventDefault();
            type = tabType;
            applyFilters(period, type);
            updateQuickLinks(period, type);
            updateCategoryTabs(period, type);
            syncUrl(period, type, false);
          });
        });
      })();
    </script>

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

    <details class="alert alert-info mt-3">
      <summary>Methodology &amp; Disclaimer</summary>
      <div class="mt-2">
        <p><strong>Data Source:</strong> The page hit count displayed on this website is sourced from the <a href="https://developers.google.com/analytics/">Google Analytics API</a>. It serves as a general indicator of user interest and engagement with our content.</p>
        <p><strong>Popularity score:</strong> Each entry's page views divided by the page views of the #1 entry in the same list, scaled to 100. Hits on old or alias URLs are merged into the main page.</p>
        <p><strong>Rank change:</strong> Compares the current rank with the rank in the preceding period of the same length (for example, the last 30 days against the 30 days before them). &ldquo;NEW&rdquo; means the entry was not ranked in the preceding period.</p>
        <p><strong>Data Precision:</strong> The ranking is a directional indicator of reader interest and does not reflect the quality or efficiency of a distribution or desktop environment.</p>
        <p><strong>Data Update Frequency:</strong> The displayed data is not real-time and may take several days to fully reflect traffic changes.</p>
      </div>
    </details>

    <h2>Express your views on distributions and desktop environments.</h2>
    {% include echothread.html %}
  </div>
</div>
