from flask import Flask, request, render_template, jsonify
import connectDB

app = Flask(__name__)
ddbb = connectDB.connectDB()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/signUp')
def signUpInfor():
    data = request.get_json()
    name = data.get('''''') # js 의 key 이름 삽입할 것!
    
    # fingerPrint = # 연결된 지문 인식 센서로부터 정보를 받아오는 코드
    
    if fingerPrint or name is not None:
        result = ddbb.helloNew(name, fingerPrint)
        return result
    else:
        return jsonify({'msg':'등록 실패'})

@app.route('/openTheDoor')
def takeInfor():
    data = request.get_json()
    name = data.get('''''') # js 의 key 이름 삽입할 것!

    # fingerPrint = # 연결된 지문 인식 센서로부터 정보를 받아오는 코드

    if fingerPrint or name is not None:
        result = ddbb.whoAreYou(name, fingerPrint)
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')