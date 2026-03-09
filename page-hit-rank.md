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
  font-weight: 600;
  margin-bottom: 0.8rem;
}
.distribution p {
  color: #555;
}
.rank-page {
  max-width: 1080px;
  margin: 0 auto;
  padding: 1rem 0 2rem;
}
.rank-page .table {
  margin-bottom: 0;
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
.rank-page .views-col,
.rank-page .status-indicator {
  white-space: nowrap;
}
.rank-page .status-indicator {
  font-weight: 600;
}
.rank-page .status-indicator span {
  display: inline-block;
  min-width: 1.25rem;
  text-align: center;
}
.rank-page details > summary {
  cursor: pointer;
  font-weight: 600;
  color: #173f4f;
}
.rank-page .period-block {
  margin-top: 1.5rem;
}
.rank-page .period-title {
  scroll-margin-top: 6rem;
}
.rank-page .quick-links a {
  margin-right: 0.75rem;
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

<div class="distribution">
  <div class="rank-page">
    <h1>Open Source Popularity Ranking</h1>
    <hr>
    <p>This page shows popularity rankings of open source operating systems and desktop environments based on OpenSourceFeed page hits.</p>
    <p>Both short-term (last 30 days) and medium-term (last 3 months) trends are shown to make comparisons easier.</p>

    {% assign last_updated = site.data.rank.meta.currentDate | default: site.data.rank.meta.current_date %}
    {% if last_updated %}
    <p class="text-muted small mb-3">Last updated:
      <time datetime="{{ last_updated | date_to_xmlschema }}" itemprop="dateModified">{{ last_updated | date: "%B %-d, %Y" }}</time>
    </p>
    {% endif %}

    <p class="small text-muted">Sorted by page views for each time range.</p>
    <p class="small quick-links">
      View:
      <a href="?period=30d">30 Days (All)</a>
      <a href="?period=3m">3 Months (All)</a>
      <a href="?period=30d&type=os">30 Days: OS Only</a>
      <a href="?period=30d&type=desktop">30 Days: Desktop Only</a>
      <a href="?period=3m&type=os">3 Months: OS Only</a>
      <a href="?period=3m&type=desktop">3 Months: Desktop Only</a>
    </p>

    <p class="small text-muted d-md-none swipe-hint">Swipe the table horizontally to view all columns.</p>

    <section class="period-block" data-period="30d" aria-labelledby="last-30-days">
      <h2 id="last-30-days" class="period-title">Last 30 Days</h2>
      <div class="row g-4">
        <div class="col-12 col-lg-6 rank-section" data-period="30d" data-type="os" id="last-30-days-os">
          <h3>Operating Systems</h3>
          <div class="table-responsive-md">
            <table class="table table-sm table-striped table-hover align-middle rank-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th class="name-col">OS</th>
                  <th>Status</th>
                  <th class="text-end views-col">Page Views</th>
                </tr>
              </thead>
              <tbody>
                {% for distribution in d30_distributions %}
                  {% assign match = nil %}
                  {% for page in site.pages %}
                    {% if page.url == distribution.url %}
                      {% assign match = page %}
                      {% break %}
                    {% endif %}
                  {% endfor %}

                  {% if match and distribution.current %}
                  <tr>
                    <td>{{ distribution.current.rank }}</td>
                    <td class="name-col"><a href="{{ match.url }}">{{ match.title }}</a></td>
                    <td class="status-indicator">
                      {% if distribution.previous and distribution.previous.rank %}
                        {% if distribution.current.rank < distribution.previous.rank %}
                          <span title="Moved up from {{ distribution.previous.rank }}" class="text-success" aria-label="Moved up from previous rank {{ distribution.previous.rank }}">&uarr;<span class="visually-hidden">Moved up from previous rank {{ distribution.previous.rank }}</span></span>
                        {% elsif distribution.previous.rank < distribution.current.rank %}
                          <span title="Moved down from {{ distribution.previous.rank }}" class="text-danger" aria-label="Moved down from previous rank {{ distribution.previous.rank }}">&darr;<span class="visually-hidden">Moved down from previous rank {{ distribution.previous.rank }}</span></span>
                        {% else %}
                          <span title="No change from {{ distribution.previous.rank }}" class="text-muted" aria-label="No change from previous rank {{ distribution.previous.rank }}">&rarr;<span class="visually-hidden">No change from previous rank {{ distribution.previous.rank }}</span></span>
                        {% endif %}
                      {% else %}
                        <span title="New in ranking" class="text-muted" aria-label="New in ranking">&bull;<span class="visually-hidden">New in ranking</span></span>
                      {% endif %}
                    </td>
                    <td class="text-end views-col">{{ distribution.current.count }}</td>
                  </tr>
                  {% endif %}
                {% endfor %}
              </tbody>
            </table>
          </div>
        </div>

        <div class="col-12 col-lg-6 rank-section" data-period="30d" data-type="desktop" id="last-30-days-desktop">
          <h3>Desktop Environments</h3>
          <div class="table-responsive-md">
            <table class="table table-sm table-striped table-hover align-middle rank-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th class="name-col">Desktop / WM</th>
                  <th>Status</th>
                  <th class="text-end views-col">Page Views</th>
                </tr>
              </thead>
              <tbody>
                {% for desktop in d30_desktops %}
                  {% assign match = nil %}
                  {% for page in site.pages %}
                    {% if page.url == desktop.url %}
                      {% assign match = page %}
                      {% break %}
                    {% endif %}
                  {% endfor %}

                  {% if match and desktop.current %}
                  <tr>
                    <td>{{ desktop.current.rank }}</td>
                    <td class="name-col"><a href="{{ match.url }}">{{ match.title }}</a></td>
                    <td class="status-indicator">
                      {% if desktop.previous and desktop.previous.rank %}
                        {% if desktop.current.rank < desktop.previous.rank %}
                          <span title="Moved up from {{ desktop.previous.rank }}" class="text-success" aria-label="Moved up from previous rank {{ desktop.previous.rank }}">&uarr;<span class="visually-hidden">Moved up from previous rank {{ desktop.previous.rank }}</span></span>
                        {% elsif desktop.previous.rank < desktop.current.rank %}
                          <span title="Moved down from {{ desktop.previous.rank }}" class="text-danger" aria-label="Moved down from previous rank {{ desktop.previous.rank }}">&darr;<span class="visually-hidden">Moved down from previous rank {{ desktop.previous.rank }}</span></span>
                        {% else %}
                          <span title="No change from {{ desktop.previous.rank }}" class="text-muted" aria-label="No change from previous rank {{ desktop.previous.rank }}">&rarr;<span class="visually-hidden">No change from previous rank {{ desktop.previous.rank }}</span></span>
                        {% endif %}
                      {% else %}
                        <span title="New in ranking" class="text-muted" aria-label="New in ranking">&bull;<span class="visually-hidden">New in ranking</span></span>
                      {% endif %}
                    </td>
                    <td class="text-end views-col">{{ desktop.current.count }}</td>
                  </tr>
                  {% endif %}
                {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <section class="period-block" data-period="3m" aria-labelledby="last-3-months">
      <h2 id="last-3-months" class="period-title">Last 3 Months</h2>
      <div class="row g-4">
        <div class="col-12 col-lg-6 rank-section" data-period="3m" data-type="os" id="last-3-months-os">
          <h3>Operating Systems</h3>
          <div class="table-responsive-md">
            <table class="table table-sm table-striped table-hover align-middle rank-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th class="name-col">OS</th>
                  <th>Status</th>
                  <th class="text-end views-col">Page Views</th>
                </tr>
              </thead>
              <tbody>
                {% for distribution in m3_distributions %}
                  {% assign match = nil %}
                  {% for page in site.pages %}
                    {% if page.url == distribution.url %}
                      {% assign match = page %}
                      {% break %}
                    {% endif %}
                  {% endfor %}

                  {% if match and distribution.current %}
                  <tr>
                    <td>{{ distribution.current.rank }}</td>
                    <td class="name-col"><a href="{{ match.url }}">{{ match.title }}</a></td>
                    <td class="status-indicator">
                      {% if distribution.previous and distribution.previous.rank %}
                        {% if distribution.current.rank < distribution.previous.rank %}
                          <span title="Moved up from {{ distribution.previous.rank }}" class="text-success" aria-label="Moved up from previous rank {{ distribution.previous.rank }}">&uarr;<span class="visually-hidden">Moved up from previous rank {{ distribution.previous.rank }}</span></span>
                        {% elsif distribution.previous.rank < distribution.current.rank %}
                          <span title="Moved down from {{ distribution.previous.rank }}" class="text-danger" aria-label="Moved down from previous rank {{ distribution.previous.rank }}">&darr;<span class="visually-hidden">Moved down from previous rank {{ distribution.previous.rank }}</span></span>
                        {% else %}
                          <span title="No change from {{ distribution.previous.rank }}" class="text-muted" aria-label="No change from previous rank {{ distribution.previous.rank }}">&rarr;<span class="visually-hidden">No change from previous rank {{ distribution.previous.rank }}</span></span>
                        {% endif %}
                      {% else %}
                        <span title="New in ranking" class="text-muted" aria-label="New in ranking">&bull;<span class="visually-hidden">New in ranking</span></span>
                      {% endif %}
                    </td>
                    <td class="text-end views-col">{{ distribution.current.count }}</td>
                  </tr>
                  {% endif %}
                {% endfor %}
              </tbody>
            </table>
          </div>
        </div>

        <div class="col-12 col-lg-6 rank-section" data-period="3m" data-type="desktop" id="last-3-months-desktop">
          <h3>Desktop Environments</h3>
          <div class="table-responsive-md">
            <table class="table table-sm table-striped table-hover align-middle rank-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th class="name-col">Desktop / WM</th>
                  <th>Status</th>
                  <th class="text-end views-col">Page Views</th>
                </tr>
              </thead>
              <tbody>
                {% for desktop in m3_desktops %}
                  {% assign match = nil %}
                  {% for page in site.pages %}
                    {% if page.url == desktop.url %}
                      {% assign match = page %}
                      {% break %}
                    {% endif %}
                  {% endfor %}

                  {% if match and desktop.current %}
                  <tr>
                    <td>{{ desktop.current.rank }}</td>
                    <td class="name-col"><a href="{{ match.url }}">{{ match.title }}</a></td>
                    <td class="status-indicator">
                      {% if desktop.previous and desktop.previous.rank %}
                        {% if desktop.current.rank < desktop.previous.rank %}
                          <span title="Moved up from {{ desktop.previous.rank }}" class="text-success" aria-label="Moved up from previous rank {{ desktop.previous.rank }}">&uarr;<span class="visually-hidden">Moved up from previous rank {{ desktop.previous.rank }}</span></span>
                        {% elsif desktop.previous.rank < desktop.current.rank %}
                          <span title="Moved down from {{ desktop.previous.rank }}" class="text-danger" aria-label="Moved down from previous rank {{ desktop.previous.rank }}">&darr;<span class="visually-hidden">Moved down from previous rank {{ desktop.previous.rank }}</span></span>
                        {% else %}
                          <span title="No change from {{ desktop.previous.rank }}" class="text-muted" aria-label="No change from previous rank {{ desktop.previous.rank }}">&rarr;<span class="visually-hidden">No change from previous rank {{ desktop.previous.rank }}</span></span>
                        {% endif %}
                      {% else %}
                        <span title="New in ranking" class="text-muted" aria-label="New in ranking">&bull;<span class="visually-hidden">New in ranking</span></span>
                      {% endif %}
                    </td>
                    <td class="text-end views-col">{{ desktop.current.count }}</td>
                  </tr>
                  {% endif %}
                {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <script>
      (function () {
        var sections = document.querySelectorAll('.rank-section');
        var periodBlocks = document.querySelectorAll('.period-block');

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

        applyFilters(period, type);
        if (isValidPeriod(period)) {
          syncUrl(period, type, true);
        }

        var targetId = stateToTargetId(period, type);
        if (targetId) {
          setTimeout(function () { scrollToTarget(targetId); }, 0);
        }

        document.querySelectorAll('.quick-links a[href*="?period="]').forEach(function (link) {
          link.addEventListener('click', function (e) {
            var href = link.getAttribute('href');
            if (!href) return;
            var linkUrl = new URL(href, window.location.href);
            var nextPeriod = linkUrl.searchParams.get('period');
            var nextType = linkUrl.searchParams.get('type');
            if (!isValidPeriod(nextPeriod)) return;

            e.preventDefault();
            applyFilters(nextPeriod, nextType);
            syncUrl(nextPeriod, nextType, false);
            scrollToTarget(stateToTargetId(nextPeriod, nextType));
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
      <summary>Disclaimer - Page Hit Count Information</summary>
      <div class="mt-2">
        <p><strong>Data Source:</strong> The page hit count displayed on this website is sourced from the <a href="https://developers.google.com/analytics/">Google Analytics API</a>. It serves as a general indicator of user interest and engagement with our content.</p>
        <p><strong>Data Precision:</strong> The hit count provides a directional view and may not precisely reflect quality or efficiency of a distribution or desktop environment.</p>
        <p><strong>Data Update Frequency:</strong> The displayed data is not real-time and may take several days to fully reflect traffic changes.</p>
      </div>
    </details>

    <h2>Express your views on distributions and desktop environments.</h2>
    <div id="disqus_thread"></div>
    <script>
      (function() {
        var d = document, s = d.createElement('script');
        s.src = 'https://theopensourcefeed.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
      })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  </div>
</div>
