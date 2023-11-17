import pymysql, jsonify

class connectDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='aaa', password='1234', db='aaa_db')
        self.cur = self.db.cursor()
        print("connect ok")

    # 새로운 사용자 ( 지문 정보 ) 등록
    def helloNew(self, name, fingerPrint):
        sql = "insert into memberDB(userName, userFingerPrint) values('{0}', '{1}')".format(name, fingerPrint)
        self.cur.execute(sql)
        self.db.commit()
        return jsonify({'msg':'등록 완료!'})
    
    # 사용자 이름으로 조회 후 잠금 해제 시도
    def whoAreYou(self, openName, fingerPrint):
        # sql 문 잘 모르니까 선생님께 꼭 여쭤보고 완성할 것
        sql = "select * from memberDB where fingerPrint = '{0}'".format(openName)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        if result is not None:
            return True
        else:
            return False