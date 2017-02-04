/* jFeed : $ feed parser plugin
 * Copyright (C) 2007 Jean-François Hovinne - http://www.hovinne.com/
 * Dual licensed under the MIT (MIT-license.txt)
 * and GPL (GPL-license.txt) licenses.
 */

$.getFeed = function(options) {

    options = $.extend({

        url: null,
        data: null,
        cache: true,
        success: null,
        failure: null,
        error: null,
        global: true

    }, options);

    if (options.url) {
        
        if ($.isFunction(options.failure) && $.type(options.error)==='null') {
          // Handle legacy failure option
          options.error = function(xhr, msg, e){
            options.failure(msg, e);
          }
        } else if ($.type(options.failure) === $.type(options.error) === 'null') {
          // Default error behavior if failure & error both unspecified
          options.error = function(xhr, msg, e){
            window.console&&console.log('getFeed failed to load feed', xhr, msg, e);
          }
        }

        return $.ajax({
            type: 'GET',
            url: options.url,
            data: options.data,
            cache: options.cache,
            dataType: "xml",
            success: function(xml) {
                var feed = new JFeed(xml);
                if ($.isFunction(options.success)) options.success(feed);
            },
            error: options.error,
            global: options.global
        });
    }
};

function JFeed(xml) {
    if (xml) this.parse(xml);
}
;

JFeed.prototype = {

    type: '',
    version: '',
    title: '',
    link: '',
    description: '',
    parse: function(xml) {

        // if ($.browser.msie) {
        //     var xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        //     xmlDoc.loadXML(xml);
        //     xml = xmlDoc;
        // }

        if ($('channel', xml).length == 1) {

            this.type = 'rss';
            var feedClass = new JRss(xml);

        } else if ($('feed', xml).length == 1) {

            this.type = 'atom';
            var feedClass = new JAtom(xml);
        }

        if (feedClass) $.extend(this, feedClass);
    }
};

function JFeedItem() {};

JFeedItem.prototype = {

    title: '',
    link: '',
    description: '',
    updated: '',
    id: '',
    summary: ''
};

function JAtom(xml) {
    this._parse(xml);
};

JAtom.prototype = {
    
    _parse: function(xml) {
    
        var channel = $('feed', xml).eq(0);

        this.version = '1.0';
        this.title = $(channel).find('title:first').text();
        this.link = $(channel).find('link:first').attr('href');
        this.description = $(channel).find('subtitle:first').text();
        this.language = $(channel).attr('xml:lang');
        this.updated = $(channel).find('updated:first').text();
        
        this.items = new Array();
        
        var feed = this;
        
        $('entry', xml).each( function() {
        
            var item = new JFeedItem();
            
            item.title = $(this).find('title').eq(0).text();
            item.link = $(this).find('link:last').attr('href');
            item.description = $(this).find('content').eq(0).text();
            item.updated = $(this).find('updated').eq(0).text();
            item.id = $(this).find('id').eq(0).text();
            item.summary = $(this).find('summary').text();

            feed.items.push(item);
        });
    }
};

