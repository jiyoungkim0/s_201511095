
# coding: utf-8

# In[3]:

#2013년 1년 동안 지하철역 승하차 인원
import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key='586b416f766a796b3738565673626e'
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'


# In[6]:

_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=_url+'/'+_key+'/'+_type+'/'+_service+'/'+str(_start_index)+'/'+str(_end_index)+'/'+_use_mon
    #print _api
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1

