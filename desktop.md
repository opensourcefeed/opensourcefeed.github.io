--- 
layout: default
title: Collection of free and open source desktop environments & window managers
description: Collection of free and open source desktop environments and window managers
---
<div class="desktop">
    <h1>OPEN SOURCE DESKTOP ENVIRONMENTS & WINDOW MANAGERS</h1>
    <hr>
    <h2>Desktop Environments</h2>
    <div class="row">
        {% for page in site.pages %}
            {% if page.Category == 'Desktop' and page.window_manager != true%}
                <div class="col-md-3 col-sm-6">
                    <a href="{{page.url}}">{{page.title}}</a>
                </div>
            {% endif %}
        {% endfor %}
    </div>
    <hr>
    <h2>Window Managers</h2>
    <div class="row">
        {% for page in site.pages %}
            {% if page.Category == 'Desktop' and page.window_manager == true%}
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
    <h2>Propose a Desktop Environment</h2>
    <p>If you are not able to see a desktop environment of your interest, please comment below. We'll update it here</p>
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
