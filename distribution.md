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
            {% if page.Category == 'Distribution' and page.type != 'BSD' and page.type != 'Other' %}
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
	<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
	<!-- Feed sidebar -->
	<div class="ad">
		<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6380671811722843" data-ad-slot="8487642304" data-ad-format="auto"></ins>
	</div>
	<script>
		(adsbygoogle = window.adsbygoogle || []).push({});
	</script>
	<hr>
    <h2>Propose a Distribution</h2>
    <p>If you are not able to see a distribution of your interest, please comment below. We'll update it here</p>
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
