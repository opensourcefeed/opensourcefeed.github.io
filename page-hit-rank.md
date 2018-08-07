--- 
layout: default
title: Page hit rank of free & open source operating systems
---
<div class="distribution">
    <h1>Page Hit Rank (Experimental)</h1>
    <hr>
    <div class="row">
        <div class="col-md-8 order-md-1">
            <table class="table">
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Distribution</th>
                        <th>Page Views</th>
                    </tr>
                </thead>
                <tbody>
                    {% for distribution in site.data.rank %}
                    <tr>
                        <td>{{distribution.rank}}</td>
                        <td>
                            <a href="/distribution/{{distribution.name}}">{{distribution.name}}</a>
                        </td>
                        <td>{{distribution.count}}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        <div class="col-md-2 order-md-0"></div>
        <div class="col-md-2 order-md-2"></div>
    </div>
</div>
