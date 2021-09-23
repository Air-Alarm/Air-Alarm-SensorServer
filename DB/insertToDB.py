import sqlite3
import datetime
import time
import arduino
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from API import dust, weather

import random   

#conn = sqlite3.connect("Test.db", check_same_thread=False)
path = os.path.abspath("Test.db")
print(path)
conn = sqlite3.connect(path, check_same_thread=False)
cur = conn.cursor()


def insertTo():
    # 테이블이 없으면 생성, 있으면 에러메시지 출력
    # 센서에서 값 못받아오면 그냥 종료
    try:
        temperature, humidity, dust, CO2 = arduino.Slicing()
    except Exception as e:
        print("arduino error: ", e)
        return

    nowtime = datetime.datetime.now()
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')

    try:
        t = [nowtime, temperature, humidity, dust, CO2]
        cur.execute('INSERT INTO tonow VALUES (?, ?, ?, ?, ?)', t)
        conn.commit()
        #conn.close()
        print("insert complete")
    except Exception as e:
        print("insertTo error : ", e)


# 디비에서 모든 값을 불러와서 리턴하고 해당 디비는 전체 삭제
def timeChange(DB):
    cur.execute(f"SELECT rowid, * FROM {DB}")
    rows = cur.fetchall()
    if not rows:
        return rows
    cur.execute(f"DELETE FROM {DB}")
    conn.commit()
    #conn.close()
    return rows

def insertToHour(hour):
    rows = timeChange("tonow") #실시간 디비 가져오기
    if not rows:
        print("empty DB!! return")
        return
    temperature, humidity, dust, CO2 = 0, 0, 0, 0
    id = rows[-1][0]  # 마지막 값의 아이디
    
    for i in rows:
        temperature += i[2]
        humidity += i[3]
        dust += i[4]
        CO2 += i[5]
        
    t = [hour, round(temperature / id), round(humidity / id), round(dust / id), round(CO2 / id)]
    cur.execute('INSERT INTO tohour VALUES (?, ?, ?, ?, ?)', t)
    conn.commit()
    # conn.close()

#실시간 디비에서 불러온 값의 평균을 개월간 디비에 저장
def insertToDay(day):
    rows = timeChange("tohour") #시간당 디비 가져오기
    if not rows:
        print("empty DB!! return")
        return
    temperature, humidity, dust, CO2 = 0.0, 0.0, 0.0, 0.0
    id = rows[-1][0]  # 마지막 값의 아이디
    for i in rows:
        temperature += i[2]
        humidity += i[3]
        dust += i[4]
        CO2 += i[5]
    t = [day, round(temperature / id), round(humidity / id), round(dust / id), round(CO2 / id)]
    print("insert to tohour")
    cur.execute('INSERT INTO today VALUES (?, ?, ?, ?, ?)', t)
    conn.commit()
    #conn.close()

def insertToLocal():
    try:
        t = dust.dustApi()
        t += weather.weatherApi()
        cur.execute('INSERT INTO tolocal VALUES (?, ?, ?, ?, ?, ?)', t)
        conn.commit()
        #conn.close()
        print("weather insert complete")
    except Exception as e:
        print("weather error: ", e)
        return


#각 테이블 생성, 얘는 한번씩만 실행되면 됨
try:
    conn.execute('CREATE TABLE tonow(time TEXT, temperature real, humidity real, dust real, CO2 real)') #실시간 디비
except (sqlite3.OperationalError, sqlite3.ProgrammingError) as e:
    print("dbMakeError : ", e)

try:
    conn.execute('CREATE TABLE tohour(time TEXT, temperature real, humidity real, dust real, CO2 real)') #시간당 평균 디비
except (sqlite3.OperationalError, sqlite3.ProgrammingError) as e:
    print("dbMakeError : ", e)

try:
    conn.execute('CREATE TABLE today(time TEXT, temperature real, humidity real, dust real, CO2 real)') #일 평균 디비
except sqlite3.OperationalError as e:
    print("dbMakeError : ", e)

try:
    conn.execute(
        'CREATE TABLE tolocal(Location TEXT, time TEXT, dust10 real, dust25 real, humidity real, temperature real)') #API용 디비
except sqlite3.OperationalError as e:
    print("dbMakeError : ", e)


now = datetime.datetime.now()
tempday = now
#tempminute = now


while True:
    now = datetime.datetime.now()
    '''
    if tempminute.second != now.second:  # 즉, 날짜가 바뀌면
        insertToHour(tempminute.strftime('%Y-%m-%d %H:%M:%S'))
        tempminute = now
        now = datetime.datetime.now()
    '''
    print(tempday, now)
    if tempday.day != now.day:  # 즉, 날짜가 바뀌면
        insertToDay(tempday.strftime('%Y-%m-%d %H:%M:%S'))
        insertToLocal()
        tempday = now
        now = datetime.datetime.now()
    
    elif tempday.hour != now.hour:  # 즉, 시간이가 바뀌면
        insertToHour(tempday.strftime('%Y-%m-%d %H:%M:%S'))
        insertToLocal()
        tempday = now
        now = datetime.datetime.now()


    insertTo()
    time.sleep(1)
