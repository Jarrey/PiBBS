#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib2
import json
import feedparser

def RestGet(url, headers = None):
    http = httplib2.Http(timeout=10)
    try:
        response, content = http.request( url, 'GET', headers = headers)
    except:
        return ""
    return json.loads(content)
    
def RSSGet(url):
    return  feedparser.parse(url)      