from flask import Flask, request, render_template, jsonify
import connectDB, buzzer

app = Flask(__name__)
ddbb = connectDB.connectDB()
bz = buzzer.Buzzer()

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

    if ddbb.whoAreYou(fingerPrint):
        bz.Welcome()
        return jsonify({'msg':'환영합니다!'})
    else:
        bz.Emergency
        return jsonify({'msg':'미등록 사용자 출입 시도 감지'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')