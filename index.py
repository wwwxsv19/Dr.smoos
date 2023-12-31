from flask import Flask, request, render_template, jsonify
import connectDB, buzzer, servo
import time

app = Flask(__name__)
ddbb = connectDB.connectDB()
bz = buzzer.Buzzer()
sv = servo.Servo()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signUp", methods=["POST"])
def signUpInfor():
    data = request.get_json()
    name = data.get("key")  # js 의 key 이름 삽입할 것!

    fingerPrint = 1 
    # 연결된 지문 인식 센서로부터 정보를 받아오는 코드

    if fingerPrint or name is not None:
        result = ddbb.helloNew(name, fingerPrint)
        return result
    else:
        return jsonify({"msg": "등록 실패"})


@app.route("/openTheDoor")
def takeInfor():
    data = request.get_json()
    name = data.get("key")  # js 의 key 이름 삽입할 것!

    fingerPrint = 1
    # 연결된 지문 인식 센서로부터 정보를 받아오는 코드

    if ddbb.whoAreYou(name, fingerPrint):
        bz.Welcome()
        sv.control_servo(90)
        time.sleep(2000)
        sv.control_servo(0)
        return jsonify({"msg": "문이 정상 작동했습니다"})
    else:
        bz.Emergency
        return jsonify({"msg": "미등록 사용자 출입 시도 감지"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0")