import datetime
import requests
from bs4 import BeautifulSoup


def weatherApi():

    now = datetime.datetime.now()
    delta = datetime.timedelta(hours=1)
    base = now - delta
    base_date = base.strftime('%Y%m%d')
    base_time = base.strftime('%H00')

    nx = 38
    ny = 127

    M=f"&pageNo=1&numOfRows=50&dataType=XML&base_date={base_date}&base_time={base_time}00&nx={nx}&ny={ny}"
    key="oH3Iy4hZlzlzonDOb7vQlJBmeHig1XMtjcio0V%2B3rZAjoPsLLBwDodrfVGMRvJo5tcW5Cgc8ScGYzLzOHS7KPg%3D%3D"
    url="http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=" + key + M

    response=requests.get(url)

    soup=BeautifulSoup(response.text,"html.parser")

    t = []  # 기온T1H 습도REH
    for item in soup.findAll('item'):
        if item.category.text == "T1H":
            t.append(item.obsrvalue.text)
        elif item.category.text == "REH":
            t.append(item.obsrvalue.text)

    return t