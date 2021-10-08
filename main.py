from flask import Flask, jsonify
from DB import getFromDB

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

"""
모든 페이지는 뒤에 all 붙일시 DB에 쌓인 모든 값 볼 수 있음.
ex) /get은 최신 1개 센서값, /getall은 쌓여있는 모든 센서값
"""

def changeToJson(DB):
    rows = getFromDB.getFrom(f"to{DB}")
    temp = int(rows[-1][4])  # 소수 값 정수화
    temp2 = int(rows[-1][5])  # 소수 값 정수화
    jsonDic = {"id": rows[-1][0], "time": rows[-1][1], "temperature": rows[-1][2], "humidity": rows[-1][3],
               "dust": temp, "CO2": temp2}
    return jsonDic

def changeToJsonAll(DB):
    t = getFromDB.getFrom(f"to{DB}")
    jsonArr = []
    for i in range(len(t)):
        temp = int(t[i][4])
        temp2 = int(t[i][5])
        jsonArr.append({
            "id": t[i][0], "time": t[i][1], "temperature": t[i][2],
            "humidity": t[i][3], "dust": temp, "CO2": temp2
        })
    return jsonArr


# 실시간 센서 값
@api.route('/get', methods=['GET', 'POST'])
def get():
    return jsonify(changeToJson("now"))

@api.route('/getall', methods=['GET', 'POST'])
def getall():
    return jsonify(changeToJsonAll("now"))

'''
@api.route('/day', methods=['GET', 'POST'])
def day():
    return jsonify(changeToJson("day"))
'''

@api.route('/dayall', methods=['GET', 'POST'])
def dayall():
    return jsonify(changeToJsonAll("day"))


'''
@api.route('/hour', methods=['GET', 'POST'])
def hour():
    return jsonify(changeToJson("hour"))
'''

@api.route('/hourall', methods=['GET', 'POST'])
def hourall():
    return jsonify(changeToJsonAll("hour"))

@api.route('/weak', methods=['GET', 'POST'])
def weak():
    t = getFromDB.getFrom(f"today")
    jsonArr = []
    for i in range(len(t) - 8, len(t)):
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
    temp = int(rows[-1][3])
    temp2 = int(rows[-1][4])
    jsonDic = {"id": rows[-1][0], "Location": rows[-1][1], "time": rows[-1][2], "dust10": temp, "dust25": temp2,
               "humidity": rows[-1][5], "temperature": rows[-1][6]}
    return jsonify(jsonDic)

@api.route('/weatherall', methods=['GET', 'POST'])
def weatherall():
    t = getFromDB.getFrom("tolocal")
    #temp = '측정장소:' + t[0] + '<br>' + '측정시간:' + t[1] + '<br>' + '미세먼지농도:' + t[2] + '㎍/m³' + '<br>' + '초미세먼지농도:' + t[3] + '㎍/m³'
    jsonArr = []
    
    for i in range(len(t)):
        print(t[i][3], t[i][4])
        try:
            temp = int(t[i][3])
            temp2 = int(t[i][4])
        except Exception as e:
            temp = 0
            temp2 = 0
        jsonArr.append({
            "id": t[i][0], "Location": t[i][1], "time": t[i][2],
            "dust10": temp, "dust25": temp2, "humidity": t[i][5], "temperature": t[i][6]
        })
    
    return jsonify(jsonArr)


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)

# 주의! 이거 끄면 서버 꺼짐. 건들지 말기

