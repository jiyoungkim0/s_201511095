
# coding: utf-8

# In[6]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_crawl_ieee.py', u'# coding utf-8\nimport lxml.html\nfrom lxml.cssselect import CSSSelector\nimport requests\nfrom lxml.cssselect import CSSSelector\nimport requests\nrequest = requests.get(\'http://www.ieee.org/conferences_events/conferences/search/index.html\')\n_html=lxml.html.fromstring(request.text)\nselec=CSSSelector(\'div.content-r-full table.nogrid-nopad tr p>a[href]\')\nnode = selec(_html)\nfor n in node:\n    print n.text\n    print "-----------------"')


# In[7]:

get_ipython().system(u'python src/ds_web_crawl_ieee.py')

