import feedparser
import yaml
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# url of blog feed
feed_url = "https://blog.opensourcefeed.org/feed/atom/"

blog_feed = feedparser.parse(feed_url)





count = 0
content = {}
content["entries"] = []
for entry in blog_feed.entries:
  if count == 6: break
  parsed_html = BeautifulSoup(entry.content[0].value)
  img = parsed_html.find("img")
  content["entries"].append({
    'title': entry.title,
    'link': entry.link,
    'date': entry.published.split('T')[0],
    'description': entry.summary,
    'img': img['src'] if img else None
  })
  count += 1

print(content)


with open("../../_data/feed.yaml", "w") as file:
  file.write(yaml.safe_dump(content, default_flow_style=False))
