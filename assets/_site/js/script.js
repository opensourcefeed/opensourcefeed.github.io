var FEED_URL = "/assets/atom.xml";

$(function() {
  if($('#recent-posts').length) {
    $.getFeed({
      url: FEED_URL,
      success: function(feed) {
      
        var items = feed.items;
        for(var i = 0; i < items.length; i++) {
          var item = items[i];

          var post_row = document.createElement('div');
          var post_col = document.createElement('div');
          var meta = document.createElement('span');
          var title = document.createElement('h2');
          var title_link = document.createElement('a');
          var summary = document.createElement('p');

          $(post_row).addClass('row post-thumbnail');
          $(post_col).addClass('col-md-12');
          $(meta).addClass('post-meta date');
          $(title_link).addClass('post-link');

          post_row.appendChild(post_col);
          post_col.appendChild(meta);
          post_col.appendChild(title);
          title.appendChild(title_link);
          post_col.appendChild(summary);

          var date = new Date(item.updated);

          $(meta).text(date.toDateString());
          $(title_link).text(item.title);
          $(title_link).attr("href", item.link);
          $(summary).text(item.summary);

          $("#recent-posts").append(post_row);
      }


    }
 });

  }
});

// <div class="row post-thumbnail">
//     <div class="col-md-12">
//         <span class="post-meta date">{{ post.date | date: "%b %-d, %Y" }}</span>
//         <h2>
//             <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
//         </h2>
//         {{ post.excerpt | slice: 0, 200}}...
//     </div>
// </div>