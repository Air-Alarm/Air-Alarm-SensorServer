import sqlite3
from flask import Flask, jsonify
from DB import getFromDB

api = Flask(__name__)


@api.route('/get', methods=['GET', 'POST'])
def get():
    rows = getFromDB.getFrom("today")
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}
    return jsonify(jsonDic)

@api.route('/getall', methods=['GET', 'POST'])
def getall():
    t = getFromDB.getFrom("today")
    return jsonify(t)


@api.route('/month', methods=['GET', 'POST'])
def month():
    rows = getFromDB.getFrom("tomonth")
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}
    return jsonify(jsonDic)

@api.route('/monthall', methods=['GET', 'POST'])
def monthall():
    t = getFromDB.getFrom("tomonth")
    return jsonify(t)


@api.route('/hour', methods=['GET', 'POST'])
def hour():
    rows = getFromDB.getFrom("tohour")
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": rows[-1][4], "CO2": rows[-1][5]}
    return jsonify(jsonDic)

@api.route('/hourall', methods=['GET', 'POST'])
def hourall():
    t = getFromDB.getFrom("tohour")
    return jsonify(t)


@api.route('/weather', methods=['GET', 'POST'])
def weather():
    rows = getFromDB.getFrom("tolocal")
    jsonDic = {"id": rows[-1][0], "Location": rows[-1][1], "dust10": rows[-1][2], "dust25": rows[-1][3],
               "humidity": rows[-1][4], "temperature": rows[-1][5]}
    return jsonify(jsonDic)

@api.route('/weatherall', methods=['GET', 'POST'])
def weatherall():
    t = getFromDB.getFrom("tolocal")
    #temp = '측정장소:' + t[0] + '<br>' + '측정시간:' + t[1] + '<br>' + '미세먼지농도:' + t[2] + '㎍/m³' + '<br>' + '초미세먼지농도:' + t[3] + '㎍/m³'
    return jsonify(t)


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)
    api.config['JSON_AS_ASCII'] = False

# 주의! 이거 끄면 서버 꺼짐. 건들지 말기

