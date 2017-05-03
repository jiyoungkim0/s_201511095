
# coding: utf-8

# In[4]:

#2015년 서울시 지하철역별 월별 승하차인원 구하기
import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key="586b416f766a796b3738565673626e"
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
#_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
_api=_url+'/'+_key+'/'+_type+'/'+_service+'/'+str(_start_index)+'/'+str(_end_index)+'/'+_use_mon


# In[5]:

response = requests.get(_api).text
print response

