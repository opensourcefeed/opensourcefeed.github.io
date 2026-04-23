---
layout: wide
title: Collection of Free and Open Source operating systems
description: Collection of Free and Open Source operating systems including GNU/Linux and BSD distributions.
seo:
  type: ItemList
---

<style>
.distribution h1{
    text-align:center;
    margin-bottom:10px;
    font-weight:600;
}

.distribution-intro{
    text-align:center;
    max-width:840px;
    margin:0 auto 20px auto;
    color:#555;
}

.distribution-section{
    margin-bottom:2rem;
}

.distribution-section-header{
    display:flex;
    align-items:baseline;
    gap:0.75rem;
    margin:0 0 0.9rem 0;
}

.distribution-section-header h2{
    margin:0;
    font-weight:600;
    border-left:4px solid #007acc;
    padding-left:10px;
}

.distribution-count{
    color:#6b7280;
    font-size:0.95rem;
}

.distribution-grid{
    display:grid;
    grid-template-columns:repeat(auto-fill, minmax(210px, 1fr));
    gap:12px;
}

.distribution-card{
    display:flex;
    align-items:center;
    gap:12px;
    min-height:78px;
    padding:12px 14px;
    border:1px solid #e7e7e7;
    border-radius:12px;
    background:#fff;
    color:inherit;
    text-decoration:none;
    transition:transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.distribution-card:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    border-color:#d9e9f8;
}

.distribution-card:focus-visible{
    outline:3px solid rgba(0, 122, 204, 0.25);
    outline-offset:2px;
}

.distribution-card-media{
    width:52px;
    height:52px;
    flex:0 0 52px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:12px;
    background:#f7f9fb;
}

.distribution-card-media img{
    max-width:40px;
    max-height:40px;
    object-fit:contain;
}

.distribution-card-fallback{
    color:#6b7280;
    font-size:0.78rem;
    font-weight:700;
    letter-spacing:0.04em;
}

.distribution-card-title{
    font-weight:600;
    line-height:1.3;
    color:#222;
}

.distribution-card:hover .distribution-card-title,
.distribution-card:focus-visible .distribution-card-title{
    color:#007acc;
}

.distribution-ad{
    margin:2rem 0;
}

.distribution-comments{
    margin-top:2rem;
}

.distribution-comments h2{
    margin:0 0 0.5rem 0;
    font-weight:600;
    border-left:4px solid #007acc;
    padding-left:10px;
}

.distribution-comments .btn{
    margin-top:0.5rem;
    margin-bottom:1rem;
}
</style>

<div class="distribution">
    <h1>Open Source Operating Systems</h1>
    <p class="distribution-intro">
        Explore free and open source operating systems across GNU/Linux, BSD, and other independent projects.
        Browse the collection to compare distributions, discover alternatives, and jump into detailed pages.
    </p>

    <hr>

    {% assign linux_distributions = site.pages | where: "Category", "Distribution" | where_exp: "item", "item.type != 'BSD'" | where_exp: "item", "item.type != 'Other'" | sort: "title" %}
    {% assign bsd_distributions = site.pages | where: "Category", "Distribution" | where: "type", "BSD" | sort: "title" %}
    {% assign other_distributions = site.pages | where: "Category", "Distribution" | where: "type", "Other" | sort: "title" %}

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>GNU/Linux</h2>
            <span class="distribution-count">{{ linux_distributions | size }} distributions</span>
        </div>
        <div class="distribution-grid">
            {% for page in linux_distributions %}
            <a href="{{ page.url }}" class="distribution-card">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy">
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">OS</div>
                    {% endif %}
                </div>
                <div class="distribution-card-title">{{ page.title }}</div>
            </a>
            {% endfor %}
        </div>
    </section>

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>BSD</h2>
            <span class="distribution-count">{{ bsd_distributions | size }} distributions</span>
        </div>
        <div class="distribution-grid">
            {% for page in bsd_distributions %}
            <a href="{{ page.url }}" class="distribution-card">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy">
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">BSD</div>
                    {% endif %}
                </div>
                <div class="distribution-card-title">{{ page.title }}</div>
            </a>
            {% endfor %}
        </div>
    </section>

    <section class="distribution-section">
        <div class="distribution-section-header">
            <h2>Others</h2>
            <span class="distribution-count">{{ other_distributions | size }} distributions</span>
        </div>
        <div class="distribution-grid">
            {% for page in other_distributions %}
            <a href="{{ page.url }}" class="distribution-card">
                <div class="distribution-card-media">
                    {% if page.logo %}
                    <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy">
                    {% else %}
                    <div class="distribution-card-fallback" aria-hidden="true">OS</div>
                    {% endif %}
                </div>
                <div class="distribution-card-title">{{ page.title }}</div>
            </a>
            {% endfor %}
        </div>
    </section>

    <div class="distribution-ad">
        <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <div class="ad">
            <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6380671811722843" data-ad-slot="8487642304" data-ad-format="auto"></ins>
        </div>
        <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>

    <div class="distribution-comments">
        <h2>Propose a Distribution</h2>
        <p>If you are not able to see a distribution of your interest, comment below and we'll review and add it.</p>
        <div id="disqus_thread"></div>
        <button type="button" class="btn btn-primary" id="load-comments">Load comments</button>
        <script>
        document.getElementById('load-comments').addEventListener('click', function () {
          var d = document;
          var s = d.createElement('script');
          s.src = 'https://theopensourcefeed.disqus.com/embed.js';
          s.setAttribute('data-timestamp', +new Date());
          (d.head || d.body).appendChild(s);
          this.remove();
        }, { once: true });
        </script>
        <noscript>Please enable JavaScript to view comments powered by Disqus.</noscript>
    </div>
</div>
