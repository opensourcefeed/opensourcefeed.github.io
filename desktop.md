--- 
layout: default
title: A list of free and open source window managers & desktop environments.
---
<div class="desktop">
    <h1>OPEN SOURCE DESKTOP ENVIRONMENTS & WINDOW MANAGERS</h1>
    <hr>    
    <div class="row">
        {% for page in site.pages %}
            {% if page.Category == 'Desktop'%}
                <div class="col-md-3">
                    <a href="{{page.url}}">{{page.title}}</a>
                </div>
            {% endif %}
        {% endfor %}
    </div>
</div>