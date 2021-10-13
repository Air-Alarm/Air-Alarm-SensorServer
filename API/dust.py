import datetime
import requests
from bs4 import BeautifulSoup


def dustApi():

    city = "구로구"
    M=f"&returnType=xml&numOfRows=100&pageNo=1&sidoName=서울&searchCondition=DAILY"
    key="oH3Iy4hZlzlzonDOb7vQlJBmeHig1XMtjcio0V%2B3rZAjoPsLLBwDodrfVGMRvJo5tcW5Cgc8ScGYzLzOHS7KPg%3D%3D"
    url="http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst?serviceKey=" + key + M

    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    t = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(hours=1)
    base = now - delta

    now = base.strftime('%Y-%m-%d %H:00')
    for item in soup.findAll('item'):
        if item.cityname.text == city and item.datatime.text == now:
            t.append(item.find('cityname').text)  # 측정장소
            t.append(item.find('datatime').text)  # 측정시간
            t.append(item.find('pm10value').text)  # 10 농도
            t.append(item.find('pm25value').text)  # 25 농도


    return t


