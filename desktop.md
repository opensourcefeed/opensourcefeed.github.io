--- 
layout: default
title: Collection of free and open source desktop environments & window managers.
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
</div>