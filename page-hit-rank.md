--- 
layout: default
title: Most Popular Open Source OS & Desktop Environments (Monthly Ranking)
description: Monthly ranking of Linux, BSD, and open source operating systems plus desktop environments based on page views from OpenSourceFeed.
image: "/assets/images/meta/logo-collage.png"
seo:
  type: ItemList
  name: Popular Open Source OS Ranking
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
.rank-page .top-rank {
  font-weight: 600;
}
.rank-page details > summary {
  cursor: pointer;
  font-weight: 600;
  color: #173f4f;
}
.rank-page .info-note {
  margin-top: 0.75rem;
}
</style>
<div class="distribution">
  <div class="rank-page">
    <h1>Monthly Popularity Ranking</h1>
    <hr>
    <p>This page shows the monthly popularity ranking of open source
operating systems, Linux distributions, BSD variants, and desktop
environments based on page hits on OpenSourceFeed.</p>

<p>It reflects community interest trends and helps users discover
actively followed open source projects.</p>
    {% assign last_updated = site.data.rank.meta.currentDate | default: site.data.rank.meta.current_date %}
    {% if last_updated %}
    <p class="text-muted small mb-3">Last updated:
        <time datetime="{{ last_updated | date_to_xmlschema }}" itemprop="dateModified">{{ last_updated | date: "%B %-d, %Y" }}</time>
    </p>
    {% endif %}
    <hr>
    <p class="small text-muted info-note">Sorted by current month page views.</p>
    <div class="row">
        <div class="col-12">
        <ul class="nav nav-tabs mb-3" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="distribution-tab" data-bs-toggle="pill" data-bs-target="#distribution" type="button" role="tab" aria-controls="distribution" aria-selected="true">Operating System</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="desktop-tab" data-bs-toggle="pill" data-bs-target="#desktop" type="button" role="tab" aria-controls="desktop" aria-selected="false">Desktop</button>
            </li>
        </ul>
        <p class="small text-muted d-md-none swipe-hint">Swipe the table horizontally to view all columns.</p>
        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="distribution" role="tabpanel" aria-labelledby="distribution-tab">
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
                        {% for distribution in site.data.rank.distributions %}
                            {% assign match = nil %}
                            {% for page in site.pages %}
                                {% if page.url == distribution.url %}
                                    {% assign match = page %}
                                    {% break %}
                                {% endif %}
                            {% endfor %}

                            {% if match %}
                            <tr>
                                <td>{{distribution.current.rank}}</td>
                                <td class="name-col">
                                    <a href="{{match.url}}">{{match.title}}</a>
                                </td>
                                <td class="status-indicator">
                                    {% if distribution.current.rank < distribution.previous.rank %}
                                    <span title="Moved up from {{distribution.previous.rank}}" class="text-success" aria-label="Moved up from previous rank {{distribution.previous.rank}}">&uarr;<span class="visually-hidden">Moved up from previous rank {{distribution.previous.rank}}</span></span>
                                    {% elsif distribution.previous.rank < distribution.current.rank %}
                                    <span title="Moved down from {{distribution.previous.rank}}" class="text-danger" aria-label="Moved down from previous rank {{distribution.previous.rank}}">&darr;<span class="visually-hidden">Moved down from previous rank {{distribution.previous.rank}}</span></span>
                                    {% else %}
                                    <span title="No change from {{distribution.previous.rank}}" class="text-muted" aria-label="No change from previous rank {{distribution.previous.rank}}">&rarr;<span class="visually-hidden">No change from previous rank {{distribution.previous.rank}}</span></span>
                                    {% endif %}
                                </td>
                                <td class="text-end views-col">{{distribution.current.count}}</td>
                            </tr>
                            {% endif %}
                        {% endfor %}
                    </tbody>
                </table>
                </div>
            </div>
            <div class="tab-pane fade" id="desktop" role="tabpanel" aria-labelledby="desktop-tab">
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
                        {% for desktop in site.data.rank.desktops %}
                        <tr>
                            <td >{{desktop.current.rank}}</td>
                            <td class="name-col">
                                {% for page in site.pages %}
                                    {% if page.url == desktop.url %}
                                        <a href="{{page.url}}">{{page.title}}</a>
                                        {% break %}
                                    {% endif %}
                                {% endfor %}
                            </td>
                            <td class="status-indicator">
                                {% if desktop.current.rank < desktop.previous.rank %}
                                <span title="Moved up from {{desktop.previous.rank}}" class="text-success" aria-label="Moved up from previous rank {{desktop.previous.rank}}">&uarr;<span class="visually-hidden">Moved up from previous rank {{desktop.previous.rank}}</span></span>
                                {% elsif desktop.previous.rank < desktop.current.rank %}
                                <span title="Moved down from {{desktop.previous.rank}}" class="text-danger" aria-label="Moved down from previous rank {{desktop.previous.rank}}">&darr;<span class="visually-hidden">Moved down from previous rank {{desktop.previous.rank}}</span></span>
                                {% else %}
                                <span title="No change from {{desktop.previous.rank}}" class="text-muted" aria-label="No change from previous rank {{desktop.previous.rank}}">&rarr;<span class="visually-hidden">No change from previous rank {{desktop.previous.rank}}</span></span>
                                {% endif %}
                            </td>
                            <td class="text-end views-col">{{desktop.current.count}}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                </div>
            </div>
        </div>
        </div>
    </div>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <!-- post body2 -->
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
    <p><strong>Data Precision:</strong> Please note that the hit count provides a general overview and may not precisely reflect the quality or efficiency of the distribution or desktop environment. It is intended as a directional metric rather than an absolute measure.</p>
    <p><strong>Data Update Frequency:</strong> Kindly be aware that the displayed data is not updated in real-time. It may take several days for changes to be accurately reflected due to the nature of data collection and processing.</p>
    <p>We appreciate your understanding and patience as we work to provide you with insights into our website's performance.</p>
      </div>
    </details>
    <h2>Express your views on distributions & desktop environments.</h2>
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
