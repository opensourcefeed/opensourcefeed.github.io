#! /usr/bin/python3

'''
Python script to retrieve content from atom feed
Copyright @ TheOpenSourceFeed 2017
'''

import dateutil.parser
import feedparser

# Constants
PAGE_MARK = '---\n'
PADDING = '  '
LINE_BREAK = '\n'
COLUN = ': '
TITLE = 'title'
DATE = 'date'
SUMMARY = 'summary'
LINK = 'link'

atom = feedparser.parse('http://www.open-source-feed.com/atom.xml?max-results=10')

posts = atom.entries

with open("../_data/feed.yaml", 'w') as output:
    for post in posts:
        title = post.title
        link = post.link
        published_date = post.published
        published_date = dateutil.parser.parse(published_date).strftime("%d/%m/%y")
        summary = post.summary.replace("\n", "")[:200] + '...'
        output.write('- ' + TITLE + COLUN + "\"" +title + "\"" + LINE_BREAK)
        output.write(PADDING + DATE + COLUN + "\"" + published_date + "\"" + LINE_BREAK)
        output.write(PADDING + SUMMARY + COLUN + "\"" + summary + "\"" + LINE_BREAK)
        output.write(PADDING + LINK + COLUN + "\"" + link + "\"" + LINE_BREAK + LINE_BREAK)
