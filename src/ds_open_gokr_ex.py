
# coding: utf-8
import os
import requests
import urlparse
import urllib
import mylib

def doIt():
    SERVICE='ArpltnInforInqireSvc'
    OPERATION_NAME='getMinuDustFrcstDspth'
    params1=os.path.join(SERVICE,OPERATION_NAME)
    
    _d=dict()
    _d['dataTerm']='month'
    params2 = urllib.urlencode(_d)

    keyPath=os.path.join(os.getcwd(), 'key.properties')
    key=mylib.getKey(keyPath)
    keygokr=key['gokr'] # keygokr='8Bx4C1%2B...'
    params=params1+'?'+'serviceKey='+keygokr+'&'+params2

    _url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
    url=urlparse.urljoin(_url,params)

    data=requests.get(url).text
    print data[:300]

doIt()