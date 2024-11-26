import pymysql

from platForm.Utill.Baiyaodb_config import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_CHARSET,MYSQL_AUTOCOMMIT


class Baiyao_DB():
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
baiyaodb = Baiyao_DB(MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_CHARSET,MYSQL_AUTOCOMMIT)
