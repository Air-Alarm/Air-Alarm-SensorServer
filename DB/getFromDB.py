import sqlite3
import sys, os

#conn = sqlite3.connect("DB/Test.db", check_same_thread=False)

path = os.path.abspath("DB/Test.db")
print(path)
conn = sqlite3.connect(path, check_same_thread=False)
cur = conn.cursor()

def getFromToday():
    cur.execute("SELECT rowid, * FROM today")
    rows = cur.fetchall()
    #conn.close()

    if not rows:
        print("empty DB")
        return "empty DB"

    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}

    return jsonDic


def getFromTohour():
    cur.execute("SELECT rowid, * FROM tohour")
    rows = cur.fetchall()
    #conn.close()

    if not rows:
        print("empty DB")
        return "empty DB"

    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}

    return jsonDic


def getFromTomonth():
    cur.execute("SELECT rowid, * FROM tomonth")
    rows = cur.fetchall()
    #conn.close()

    if not rows:
        print("empty DB")
        return "empty DB"

    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}

    return jsonDic


def getFromTolocal():
    cur.execute("SELECT rowid, * FROM tolocal")
    rows = cur.fetchall()
    #conn.close()

    if not rows:
        print("empty DB")
        return "empty DB"

    jsonDic = {"id": rows[-1][0], "Location": rows[-1][1], "dust10": rows[-1][2], "dust25": rows[-1][3],
               "humidity": rows[-1][4], "temperature": rows[-1][5]}

    return jsonDic

#print(getFromTohour())
#print(getFromTomonth())