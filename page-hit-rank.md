--- 
layout: default
title: Page hit rank of operating systems and desktop environments
description: Ranking of open source distributions & desktop environments, based on the number of page hits each distribution & desktop environment received in prevoius month.
image: "/assets/images/meta/logo-collage.png"
---
<div class="distribution">
    <h1>Page Hit Rank (Experimental)</h1>
    <div class="row">
        <div class="col-md-8 order-md-1">
        <ul class="nav nav-tabs mb-3" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="distribution-tab" data-bs-toggle="pill" data-bs-target="#distribution" type="button" role="tab" aria-controls="tabs-distribution" aria-selected="true">Distribution</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="desktop-tab" data-bs-toggle="pill" data-bs-target="#desktop" type="button" role="tab" aria-controls="tabs-profile" aria-selected="false">Desktop</button>
            </li>
        </ul>
        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="distribution" role="tabpanel" aria-labelledby="tabs-distribution">
                <table class="table table-sm">
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Distribution</th>
                            <th>Status</th>
                            <th class="text-end">Page Views</th>
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
                                <td>
                                    <a href="{{match.url}}">{{match.title}}</a>
                                </td>
                                <td>
                                    {% if distribution.current.rank < distribution.previous.rank %}
                                    <span title="Previous rank {{distribution.previous.rank}}" class="text-success"> &uarr;</span>
                                    {% elsif distribution.previous.rank < distribution.current.rank %}
                                    <span title="Previous rank {{distribution.previous.rank}}" class="text-danger"> &darr;</span>
                                    {% endif %}
                                </td>
                                <td class="text-end">{{distribution.current.count}}</td>
                            </tr>
                            {% endif %}
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            <div class="tab-pane fade" id="desktop" role="tabpanel" aria-labelledby="tabs-desktop">
                <table class="table table-sm">
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Desktop / WM</th>
                            <th>Status</th>
                            <th class="text-end">Page Views</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for desktop in site.data.rank.desktops %}
                        <tr>
                            <td>{{desktop.current.rank}}</td>
                            <td>
                                {% for page in site.pages %}
                                    {% if page.url == desktop.url %}
                                        <a href="{{page.url}}">{{page.title}}</a>
                                        {% break %}
                                    {% endif %}
                                {% endfor %}
                            </td>
                            <td>
                                {% if desktop.current.rank < desktop.previous.rank %}
                                <span title="Previous rank {{desktop.previous.rank}}" class="text-success"> &uarr;</span>
                                {% elsif desktop.previous.rank < desktop.current.rank %}
                                <span title="Previous rank {{desktop.previous.rank}}" class="text-danger"> &darr;</span>
                                {% endif %}
                            </td>
                            <td class="text-end">{{desktop.current.count}}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        </div>
        <div class="col-md-2 order-md-0"></div>
        <div class="col-md-2 order-md-2"></div>
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
    <div class="alert alert-info">
        <h2>Disclaimer - Page Hit Count Information</h2>
    <p><strong>Data Source:</strong> The page hit count displayed on this website is sourced from the <a href="https://developers.google.com/analytics/">Google Analytics API</a>. It serves as a general indicator of user interest and engagement with our content.</p>
    <p><strong>Data Precision:</strong> Please note that the hit count provides a general overview and may not precisely reflect the quality or efficiency of the distribution or desktop environment. It is intended as a directional metric rather than an absolute measure.</p>
    <p><strong>Data Update Frequency:</strong> Kindly be aware that the displayed data is not updated in real-time. It may take several days for changes to be accurately reflected due to the nature of data collection and processing.</p>
    <p>We appreciate your understanding and patience as we work to provide you with insights into our website's performance.</p>
    </div>
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
