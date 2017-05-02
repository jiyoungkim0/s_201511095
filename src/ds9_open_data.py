
# coding: utf-8

# In[1]:

import os
import mylib
import urlparse
import requests
import re

keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib.getKey(keyPath)
KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(1000)
LINE_NUM=str(2)

_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM))

data=requests.get(url).text

p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(Data)
for i in res:
    print i

