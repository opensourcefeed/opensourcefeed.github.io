--- 
layout: default
title: Exclusive list of Free and Open Source operating systems
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
</div>