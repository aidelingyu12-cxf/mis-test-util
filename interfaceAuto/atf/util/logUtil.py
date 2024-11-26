import logging.handlers, threading, os
import interfaceAuto.atf as atf


"""
logUtil
~~~~~~~~~~~~~

A logUtil
Pay attention please,log message with level "error" and "critical" will be
written into log files,other log message will only be shown in console 
usage:
    >>> from logUtil import Logger
    >>> logger = Logger()
    >>> logger.warning("msg")
    >>> logger.error("msg")
    >>> logger.critical("msg")

@author cxf
"""
class Logger():

    __singleLock = threading.Lock()  # 单例锁
    ##__logPath = configReader().getLoggerPath()
    __logging = logging
    __streamHandler = __logging.StreamHandler() #处理器
    __loggerPath = atf.projectPath + '/resources/logger'  # 获取日志文件目录

    __infoHandler = __logging.FileHandler(filename=__loggerPath + "/info.log", mode='a', encoding='utf-8')
    __errorHandler = __logging.FileHandler(filename=__loggerPath + "/error.log", mode='a', encoding='utf-8')
    __criticalHandler = __logging.FileHandler(filename=__loggerPath + "/critical.log", mode='a', encoding='utf-8')
    __formatter = __logging.Formatter("%(asctime)s  %(levelname)s %(lineno)s, %(message)s",
                                   datefmt='%F %T')

    __logger = __logging.getLogger()

    def __init__(self):
        self.__logger = Logger.__logger
        self.__streamHandler = Logger.__streamHandler
        self.__errorHandler = Logger.__errorHandler
        self.__criticalHandler = Logger.__criticalHandler
        self.__infoHandler = Logger.__infoHandler

    """
    new,单例锁
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(Logger, "_instance"):
            with Logger.__singleLock:
                if not hasattr(Logger, "_instance"):
                    Logger._instance = object.__new__(cls)
        return Logger._instance

    def load(self):
        pass
        # loggerPath = self.__loggerConfigPath
        # if os.path.exists(loggerPath):
        #     with open(loggerPath, 'rt', encoding="utf-8") as f:
        #         config = yaml.load(f.read(), Loader=yaml.FullLoader)
        # self.__logger = logging.getLogger("DEBUG")
        # return self.__logger
        # else:
        #     self.__logging.basicConfig(level=logging.WARNING)
        #     self.__logging.warning("can not find loggerConfigPath! Use default logging.")


    def __loadLogger(self, level, msg):
        streamHandler = self.__streamHandler
        streamHandler.setFormatter(self.__formatter)
        self.__logger.addHandler(streamHandler)
        self.__logger.setLevel(level)
        #ERROR和CRITICAL输出到控制台+日志文件
        if(level == "ERROR"):
            errorHandler = self.__errorHandler
            errorHandler.setFormatter(self.__formatter)
            self.__logger.addHandler(errorHandler)
            self.__logger.error(msg)
        elif(level == "CRITICAL"):
            criticalHandler = self.__criticalHandler
            criticalHandler.setFormatter(self.__formatter)
            self.__logger.addHandler(criticalHandler)
            self.__logger.critical(msg)
        elif (level == "DEBUG"):
            self.__logger.debug(msg)
        elif (level == "INFO"):
            infoHandler = self.__infoHandler
            infoHandler.setFormatter(self.__formatter)
            self.__logger.addHandler(infoHandler)
            self.__logger.info(msg)
        else:
            self.__logger.warning(msg)

    """
    请求方法，包括debug,info,warning,error和critical
    """
    def debug(self, msg):
        self.__loadLogger("DEBUG", msg)

    def info(self, msg):
        self.__loadLogger("INFO", msg)

    def warning(self, msg):
        self.__loadLogger("WARNING", msg)

    def error(self, msg):
        self.__loadLogger("ERROR", msg)

    def critical(self, msg):
        self.__loadLogger("CRITICAL", msg)

    def logPass(self, uri, desc):
        self.__loadLogger('INFO', uri + '  ' + desc + '  ' + '接口测试通过')

    def logFailed(self, uri, desc):
        self.__loadLogger('ERROR', uri + '  ' + desc + '  ' + '接口测试失败！')


