#!/bin/env python3 
import urllib.request, sys
#enter feeds
feeds = ['https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt']
results = []
query = sys.argv[1]

for f in feeds:
    feed = urllib.request.urlopen(f)
    #decode bytes into string based on response charset
    content = feed.read().decode('utf-8')
    if content.find(query) != -1:
        print(query + " found in " + f)

