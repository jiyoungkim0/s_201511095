
# coding: utf-8

# In[4]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
request = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')

_html = lxml.html.fromstring(request.text)


# In[7]:

sel=CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
n = sel(_html)


# In[8]:

for n in node[:10]:
    print n.text
    print "----------------"

