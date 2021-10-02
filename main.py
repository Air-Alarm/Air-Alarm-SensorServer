from flask import Flask, jsonify
from DB import getFromDB

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.route('/get', methods=['GET', 'POST'])
def get():
    rows = getFromDB.getFrom("tonow")
    temp = int(rows[-1][4])
    temp2 = int(rows[-1][5])
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": temp, "CO2": temp2}
    return jsonify(jsonDic)

@api.route('/getall', methods=['GET', 'POST'])
def getall():
    t = getFromDB.getFrom("tonow")
    jsonArr = []

    for i in range(len(t)):
        temp = int(t[i][4])
        temp2 = int(t[i][5])
        jsonArr.append({
            "id": t[i][0], "time": t[i][1], "temperature": t[i][2],
            "humidity": t[i][3], "dust": temp, "CO2": temp2
        })

    return jsonify(jsonArr)


@api.route('/day', methods=['GET', 'POST'])
def day():
    rows = getFromDB.getFrom("today")
    temp = int(rows[-1][4])
    temp2 = int(rows[-1][5])
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": temp, "CO2": temp2}
    return jsonify(jsonDic)

@api.route('/dayall', methods=['GET', 'POST'])
def dayall():
    t = getFromDB.getFrom("today")
    jsonArr = []

    for i in range(len(t)):
        temp = int(t[i][4])
        temp2 = int(t[i][5])
        jsonArr.append({
            "id": t[i][0], "time": t[i][1], "temperature": t[i][2],
            "humidity": t[i][3], "dust": temp, "CO2": temp2
        })

    return jsonify(jsonArr)


@api.route('/hour', methods=['GET', 'POST'])
def hour():
    rows = getFromDB.getFrom("tohour")
    temp = int(rows[-1][4])
    temp2 = int(rows[-1][5])
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": temp, "CO2": temp2}
    return jsonify(jsonDic)

@api.route('/hourall', methods=['GET', 'POST'])
def hourall():
    t = getFromDB.getFrom("tohour")

    jsonArr = []

    for i in range(len(t)):
        temp = int(t[i][4])
        temp2 = int(t[i][5])
        jsonArr.append({
            "id": t[i][0], "time": t[i][1], "temperature": t[i][2],
            "humidity": t[i][3], "dust": temp, "CO2": temp2
        })

    return jsonify(jsonArr)


@api.route('/weather', methods=['GET', 'POST'])
def weather():
    rows = getFromDB.getFrom("tolocal")
    jsonDic = {"id": rows[-1][0], "Location": rows[-1][1], "time": rows[-1][2], "dust10": rows[-1][3], "dust25": rows[-1][4],
               "humidity": rows[-1][5], "temperature": rows[-1][6]}
    return jsonify(jsonDic)

@api.route('/weatherall', methods=['GET', 'POST'])
def weatherall():
    t = getFromDB.getFrom("tolocal")
    #temp = '측정장소:' + t[0] + '<br>' + '측정시간:' + t[1] + '<br>' + '미세먼지농도:' + t[2] + '㎍/m³' + '<br>' + '초미세먼지농도:' + t[3] + '㎍/m³'
    return jsonify(t)


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)

# 주의! 이거 끄면 서버 꺼짐. 건들지 말기

