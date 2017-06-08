
import os
import src.mylib
import urlparse
import requests
import re

def main():
    
    keyPath=os.path.join(os.getcwd(),'src','key.properties')
    key=src.mylib.getKey(keyPath)
    KEY=str(key['dataseoul'])
    TYPE='xml'
    SERVICE='CardBusTimeNew'
    BUS_ROUTE_NO=str(7016)

    li_month=[]
    li=[]
    count=0
    month=201600
    while (month<2016013):
        month=month+1
        USE_MON=str(month)
        #START_INDEX=str(54)
        #END_INDEX=str(54)


        if(month == 201601):
            START_INDEX=str(38)
            END_INDEX=str(38)
        elif (month > 201601 and month < 201607):
            START_INDEX=str(54)
            END_INDEX=str(54)
        elif (month == 201607):
            START_INDEX=str(47)
            END_INDEX=str(47)
        elif (month == 201608):
            START_INDEX=str(44)
            END_INDEX=str(44)
        elif (month == 201609 or month == 201611 or month == 201612 ):
            START_INDEX=str(54)
            END_INDEX=str(54)
        else:
            START_INDEX=str(36)
            END_INDEX=str(36)

        params=KEY+'/'+TYPE+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX+'/'+USE_MON+'/'+BUS_ROUTE_NO
        _url='http://openAPI.seoul.go.kr:8088/'
        url=urlparse.urljoin(_url,params)
        data=requests.get(url).text
        if(month == 201613):
            break


        p=re.compile('<USE_MON>(.+?)</USE_MON>')
        res=p.findall(data)
        li_month.append(res)

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</MIDNIGHT_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</ONE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TWO_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</THREE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</FOUR_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</FIVE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</SIX_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</SEVEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</EIGHT_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</NINE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</ELEVEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TWELVE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</THIRTEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</FOURTEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</FIFTEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</SIXTEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</SEVENTEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</EIGHTEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</NINETEEN_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TWENTY_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TWENTY_ONE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TWENTY_TWO_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

        p=re.compile('<(.+?)_RIDE_NUM>(.+?)</TWENTY_THREE_RIDE_NUM>')
        res=p.findall(data)
        li.append(res)
        count+=1

    #print li_month, li
    #print li_month[0][0], li[0][0][1]
    #print count

    li_month_int=[]
    for i in range(0,12):
        li_month_int.append(int(li_month[i][0]))
    #print li_month_int

    li_month_time=[]
    for i in range(0, 24):
        li_month_time.append(str(li[i][0][0]))
    #print li_month_time

    li_month_ride=[]
    for i in range(0,count):
        li_month_ride.append(int(li[i][0][1]))
    #print li_month_ride


    cnt=count/12 #24

    for j in range(0,12):
        MAX=0
        TIME=0
        for i in range(j*cnt,(j+1)*cnt):
            if(MAX < li_month_ride[i]):
                MAX = li_month_ride[i]
                TIME =i + 1
        print li_month_int[j], TIME-j*cnt-1,u"시", MAX,u"명 탑승"