import sqlite3
import sys, os

#conn = sqlite3.connect("DB/Test.db", check_same_thread=False)

path = os.path.abspath("DB/Test.db")
print(path)
conn = sqlite3.connect(path, check_same_thread=False)
cur = conn.cursor()

def getFrom(DB):
    cur.execute(f"SELECT rowid, * FROM {DB}")
    rows = cur.fetchall()
    #conn.close()

    if not rows:
        print("empty DB")
        return "empty DB"
    
    return rows
'''
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}

    return jsonDic
'''