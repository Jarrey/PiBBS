#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib2
import json

def RestGet(url, headers = None):
    http = httplib2.Http(timeout = 10)
    try:
        response, content = http.request( url, 'GET', headers = headers)
    except:
        return ""
    return json.loads(content)    