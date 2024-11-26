import pymysql

from platForm.Utill.Wanmidb_config import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_CHARSET,MYSQL_AUTOCOMMIT


class Wanmi_DB():
    def __init__(self,host,port,user,password,charset,autocommit):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    # db=db,
                                    charset=charset,
                                    autocommit=autocommit)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def select(self,sql):
        #检查是否断开连接，若断开就重连
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data
    def operate(self,sql):
        try:
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
            data = self.cur.fetchone()
            return "变更成功，数据为: %s"%data
        except Exception as e:
            self.conn.rollback()
            return "操作错误，错误为: %s"%e
wanmidb = Wanmi_DB(MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_CHARSET,MYSQL_AUTOCOMMIT)
# db = MysqlDB()
# sql = "select * from `sbc-customer`.maker_information where maker_no ='78566179b3aa49f182138520ecb85db6'"
# data = db.select(sql)
# print(data)

# interfaceAuto = Flask(__name__)
# interfaceAuto.debug = True
# @interfaceAuto.route('/')
# def index():
#     return 'Hello world !'
# @interfaceAuto.route('/query')
# def query():
#     sql = "select * from `sbc-customer`.maker_information where maker_no ='78566179b3aa49f182138520ecb85db6'"
#     data = db.select(sql)
#     print("查询创客信息为： {}".format(data))# 在pycharm下打印信息
#     return jsonify(data)# 在页面输出返回信息的json格式

# @interfaceAuto.route('/update',methods=['GET','POST'])
# def update():
#
#
# if __name__ == '__main__':
#     interfaceAuto.run(host='127.0.0.1',port=5000,debug=True)