--- 
layout: default
title: Page hit rank of free & open source operating systems
description: A ranking of open source distributions based on the number of page hits each distribution received in prevoius month. This ranking is powered by google analytics.
image: "/assets/images/meta/logo-collage.png"
---
<div class="distribution">
    <h1>Page Hit Rank (Experimental)</h1>
    <div class="row">
        <div class="col-md-8 order-md-1">
            <table class="table table-sm">
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Distribution</th>
                        <th>Status</th>
                        <th>Page Views</th>
                    </tr>
                </thead>
                <tbody>
                    {% for distribution in site.data.rank.distributions %}
                    <tr>
                        <td>{{distribution.current.rank}}</td>
                        <td>
                            {% for page in site.pages %}
                                {% if page.url == distribution.url %}
                                    <a href="{{page.url}}">{{page.title}}</a>
                                    {% break %}
                                {% endif %}
                            {% endfor %}
                        </td>
                        <td>
                            {% if distribution.current.rank < distribution.previous.rank %}
                            <span title="Previous rank {{distribution.previous.rank}}" class="text-success"> &uarr;</span>
                            {% elsif distribution.previous.rank < distribution.current.rank %}
                            <span title="Previous rank {{distribution.previous.rank}}" class="text-danger"> &darr;</span>
                            {% endif %}
                        </td>
                        <td>{{distribution.current.count}}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        <div class="col-md-2 order-md-0"></div>
        <div class="col-md-2 order-md-2"></div>
    </div>
    <div class="alert alert-info">
        <strong>Disclaimer</strong> : The page hit count used in this page is retrieved using <a href="https://developers.google.com/analytics/">Google Analytics API</a>. It gives a vague idea about the distributions in which users are interested in. In no way, it is related to the quality or efficiency of the distribution. 
    </div>
</div>
