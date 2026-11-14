---
layout: wide
title: Open Source Desktop Environments & Window Managers - Comprehensive Collection
description: Explore a curated list of open source Linux desktop environments and window managers with details, screenshots, and links to help you choose the best desktop.
seo:
  type: ItemList
---

<style>
.desktop h1{
    text-align:center;
    margin-bottom:10px;
    font-weight:600;
}

.desktop-intro{
    text-align:center;
    max-width:800px;
    margin:0 auto 18px auto;
    color:var(--osf-color-text-secondary);
}

.desktop-card{
    border:0;
    border-radius:var(--osf-radius-lg);
    box-shadow:var(--osf-shadow-sm);
    padding:15px;
    text-align:center;
    background:var(--osf-color-surface);
    transition:0.2s ease;
    height:100%;
    text-decoration: none;
    color: inherit;
    display: block;
}

.desktop-card:hover{
    box-shadow:var(--osf-shadow-md);
    transform:translateY(-2px);
}

.desktop-card:focus-visible{
    outline:none;
    box-shadow:var(--osf-shadow-focus), var(--osf-shadow-sm);
}

.desktop-card-media{
    height:64px;
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:12px;
}

.desktop-card img{
    max-height:48px;
    max-width:100%;
    object-fit:contain;
}

.desktop-card-fallback{
    width:48px;
    height:48px;
    border-radius:var(--osf-radius-md);
    background:var(--osf-color-surface-sunk);
    color:var(--osf-color-text-muted);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:0.8rem;
    font-weight:600;
    letter-spacing:0.04em;
}

.desktop-card h3{
    font-weight:600;
    color:var(--osf-color-heading);
    font-size:1.1rem;
    margin:0;
    line-height:1.3;
}

.desktop-card:hover h3,
.desktop-card:focus-visible h3{
    color:var(--osf-color-primary);
}

.section-title{
    margin-top:28px;
    margin-bottom:20px;
    font-weight:600;
    border-left:3px solid var(--osf-color-primary);
    padding-left:10px;
}

.section-block{
    padding-top:8px;
    margin-bottom:2rem;
}

.desktop-ad{
    margin:2rem 0;
}

.desktop-comments{
    margin-top:2rem;
}

.desktop-comments .btn{
    margin-top:0.5rem;
    margin-bottom:1rem;
}
</style>

<div class="desktop">

<h1>Open Source Desktop Environments & Window Managers</h1>

<p class="desktop-intro">
Explore major free and open source desktop environments and window managers for Linux and Unix-like systems.
Browse detailed pages, screenshots, and technical information to choose the best desktop for your workflow.
</p>

<hr>

<section class="section-block">
<h2 class="section-title">Desktop Environments</h2>
{% assign desktop_pages = site.pages | where: "Category", "Desktop" | where_exp: "item", "item.window_manager != true" | sort: "title" %}
<div class="row g-3">
{% for page in desktop_pages %}
<div class="col-12 col-sm-6 col-lg-3">
<a href="{{ page.url }}" class="desktop-card">
    <div class="desktop-card-media">
    {% if page.logo %}
      <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
           onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
      <div class="desktop-card-fallback" aria-hidden="true" style="display:none">DE</div>
    {% else %}
      <div class="desktop-card-fallback" aria-hidden="true">DE</div>
    {% endif %}
    </div>
    <h3>{{ page.title }}</h3>
</a>

</div>
{% endfor %}
</div>
</section>

<section class="section-block">
<h2 class="section-title">Window Managers</h2>
{% assign window_manager_pages = site.pages | where: "Category", "Desktop" | where: "window_manager", true | sort: "title" %}
<div class="row g-3">
{% for page in window_manager_pages %}
<div class="col-12 col-sm-6 col-lg-4">
<a href="{{ page.url }}" class="desktop-card">
    <div class="desktop-card-media">
    {% if page.logo %}
      <img src="/assets/images/logo/{{ page.logo }}" alt="{{ page.title }} logo" loading="lazy"
           onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
      <div class="desktop-card-fallback" aria-hidden="true" style="display:none">WM</div>
    {% else %}
      <div class="desktop-card-fallback" aria-hidden="true">WM</div>
    {% endif %}
    </div>
    <h3>{{ page.title }}</h3>
</a>

</div>
{% endfor %}
</div>
</section>

<div class="desktop-ad">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<div class="ad">
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6380671811722843"
     data-ad-slot="8487642304"
     data-ad-format="auto"></ins>
</div>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

<div class="desktop-comments">
<h2 class="section-title">Propose a Desktop Environment</h2>
<p>
If a desktop environment or window manager is missing, comment below and we'll review and add it.
</p>

{% include echothread.html %}
</div>

</div>
