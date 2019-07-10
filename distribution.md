--- 
layout: default
title: Collection of Free and Open Source operating systems
description: Collection of Free and Open Source operating systems including GNU/Linux and BSD distributions.
---
<div class="distribution">
    <h1>OPEN SOURCE OPERATING SYSTEM</h1>
    
    <h2>GNU/Linux</h2>
    <div class="row">
        {% for page in site.pages %}
            {% if page.Category == 'Distribution' and page.type == 'Linux' %}
                <div class="col-md-3 col-sm-6">
                    <a href="{{page.url}}">{{page.title}}</a>
                </div>
            {% endif %}
        {% endfor %}
    </div>

    <h2>BSD</h2>
    <div class="row">
        {% for page in site.pages %}
            {% if page.Category == 'Distribution' and page.type == 'BSD' %}
                <div class="col-md-3 col-sm-6">
                     <a href="{{page.url}}">{{page.title}}</a>
                </div>
            {% endif %}
        {% endfor %}
    </div>

    <h2>Others</h2>
    <div class="row">
        {% for page in site.pages %}
            {% if page.Category == 'Distribution' and page.type == 'Other'%}
                <div class="col-md-3 col-sm-6">
                     <a href="{{page.url}}">{{page.title}}</a>
                </div>
            {% endif %}
        {% endfor %}
    </div>
    <hr>
    <h2>Propose a Distribution</h2>
    <p>If you are able to see a distribution of your interest, please suggest it in below comment box. We'll update it here</p>
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