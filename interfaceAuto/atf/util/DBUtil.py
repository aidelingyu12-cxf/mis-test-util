import pymysql, threading
from interfaceAuto.atf.util.configReader import configReader
from interfaceAuto.atf.util.logUtil import Logger

"""
DBUtil
~~~~~~~~~~~~~

DBUtil

usage:
    >>> from DBUtil import DBUtil
    >>> db = DBUtil()
    >>> db.getConnection()
    >>> db.excuteSql()
    >>> cr.getOne()
    >>> cr.closeDB()

@author cxf
"""
class DBUtil():

    __cr = configReader()
    __conn = None
    __cursor = None
    __singleLock = threading.Lock()  # 单例锁

    """
    初始化数据库连接信息
    """
    def __init__(self):
        self.__host = self.__cr.getDB("host")
        self.__username = self.__cr.getDB("username")
        self.__password = self.__cr.getDB("password")
        self.__port = self.__cr.getDB("port")
        self.__database = self.__cr.getDB("database")

    """
    new,单例锁
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(DBUtil, "_instance"):
            with DBUtil.__singleLock:
                if not hasattr(DBUtil, "_instance"):
                    DBUtil._instance = object.__new__(cls)
        return DBUtil._instance

    """
    获取数据库连接
    """
    def getConnection(self):
        try:
            if(self.__conn != None):
                return self.__conn
            else:
                self.__conn = pymysql.connect(host=self.__host, user=self.__username,
                                              password=str(self.__password), port=self.__port,
                                              database=self.__database)
                return self.__conn
        except Exception as e:
            Logger().critical(e.args)

    """
    执行sql
    """
    def excuteSql(self, sql):
        # 获取游标
        if (self.__conn == None):
            Logger().critical("no database connection!")
        else:
            self.__cursor = self.__conn.cursor()
            return self.__cursor.execute(sql)

    """
    获取一个查询结果
    """
    def getOne(self):
        if(self.__cursor == None):
            Logger().critical("no database connection!")
        else:
            result = self.__cursor.fetchone()
            return result

    # def get_all(self, cursor):
    #     if (self.__cursor == None):
    #         print("no connection!")
    #     else:
    #         result = self.__cursor.fetchall()
    #         return result

    """
    关闭数据库连接
    """
    def closeDB(self):
        if(self.__conn == None):
            Logger().critical("no database connection!")
        else:
            self.__conn.close()
            Logger().warning("database closed!")
