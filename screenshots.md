--- 
layout: default
title: GNU/Linux and BSD screenshots
description: Collection of GNU/Linux and BSD screenshots. The screenshots usually starts from the initial desktop impression to system shutdown confirmation. 
---
<div class="screenshots">
    <h1>GNU/Linux & BSD Screenshots</h1>
    <hr>
    <div class="row">
    {% for page in site.pages %}
        {% if page.Category == 'Distribution' and page.screenshots%}
            {% for screenshot in page.screenshots %}
                <div class="col-md-3 col-sm-6">
                    <a href="{{screenshot[1]}}">{{screenshot[0]}}</a>
                </div>
            {% endfor %}
        {% endif %}
    {% endfor %}
    </div>
</div>