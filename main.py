import sqlite3
from flask import Flask, jsonify
from DB import getFromDB

api = Flask(__name__)


@api.route('/get', methods=['GET', 'POST'])
def get():
    t = getFromDB.getFromToday()
    return jsonify(t)


@api.route('/month', methods=['GET', 'POST'])
def month():
    t = getFromDB.getFromTomonth()
    return jsonify(t)


@api.route('/hour', methods=['GET', 'POST'])
def hour():
    t = getFromDB.getFromTohour()
    return jsonify(t)


@api.route('/weather', methods=['GET', 'POST'])
def weather():
    t = getFromDB.getFromTolocal()
    #temp = '측정장소:' + t[0] + '<br>' + '측정시간:' + t[1] + '<br>' + '미세먼지농도:' + t[2] + '㎍/m³' + '<br>' + '초미세먼지농도:' + t[3] + '㎍/m³'
    return jsonify(t)


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)

# 주의! 이거 끄면 서버 꺼짐. 건들지 말기

