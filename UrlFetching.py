#using urllib moudule fetching URLs.
#Implemented in Python3 
"""
Created on Thu Jun 22 12:16:25 2017

@author: ichita
"""

import urllib

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page) # A Chinese website that contains so many jokes.
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent } #header verification
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    print (response.read())
except urllib.request.URLError:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)
