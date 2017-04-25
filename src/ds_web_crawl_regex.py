
# coding: utf-8

# In[11]:

import re
p=re.compile('href="(http://.*?)"')
num=p.findall(_html)
print "http url은 몇 개?", len(num)
for i, n in enumerate(num):
    print i,n


# In[12]:

import re
p=re.compile('<h1>(.*?)</h1>')
h1Tag=p.findall(_html)
for tag in h1Tag:
    print tag


# In[14]:

import re
p=re.compile('<p>(.*?)</p>')
pTag=p.findall(_html)
print len(pTag)


# In[16]:

print pTag[0]

