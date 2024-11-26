import yaml, os, pandas, threading
import interfaceAuto.atf as atf
from interfaceAuto.atf.util.optionUtil import Deprecated
import interfaceAuto.ynby.urls as urls

"""
configReader, core module
~~~~~~~~~~~~~

A reader to fetch configurations such as db,auth,domain and so on from configuration files
You should give the __ConfigFilePath = __parentPath + yourPath firstly
usage:
    >>> from configReader import configReader
    >>> cr = configReader()
    >>> cr.getDB("host")
    >>> cr.getDB("username")
    >>> cr.getDB("password")
    >>> cr.getDB("port")
    >>> cr.getDB("database")

@author cxf
"""


class configReader():
    __singleLock = threading.Lock()  # 单例锁
    __parentPath = atf.projectPath  # 获取父文件路径
    ConfigFileContent_app = None
    ConfigFileContent_h5 = None

    """
    new,单例锁
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(configReader, "_instance"):
            with configReader.__singleLock:
                if not hasattr(configReader, "_instance"):
                    configReader._instance = object.__new__(cls)
        return configReader._instance

    """
    init
    """

    def __init__(self, ConfigFileContent=None):
        pass

    """
    读取单个文件并获取其内容，文件格式为yaml
    """

    def readYaml(self, file, project):
        if project == 'interfaceAuto':
            file = atf.projectPath + "/resources/requestData/appData/" + file
        elif project == 'h5':
            file = atf.projectPath + "/resources/requestData/apph5Data/" + file
        else:
            file = atf.projectPath + "/resources/requestData/miniappData/" + file
        try:
            fileContent = open(file, encoding='utf8').read()
        except Exception as e:
            var = e.args[1] == 'No such file or directory'
            return None
        return yaml.load(fileContent, Loader=yaml.FullLoader)

    """
    获取数据库连接信息
    包括host,port,database,username,password等
    """

    def getDB(self, connectInfo, project):
        if project == 'interfaceAuto':
            configFile = self.ConfigFileContent_app
            return configFile["DataBase"][connectInfo]
        elif project == 'h5':
            configFile = self.ConfigFileContent_h5
            return configFile["DataBase"][connectInfo]

    """
    获取token
    """

    def getAuth(self, project):
        if project == 'interfaceAuto':
            configFile = self.ConfigFileContent_app
            return configFile["Authorization"]["Token"]
        elif project == 'h5':
            configFile = self.ConfigFileContent_h5
            return configFile["Authorization"]["Token"]

    """
    获取domain
    """

    def getDomain(self, project):
        if project == 'interfaceAuto':
            configFile = self.ConfigFileContent_app
            return configFile["Domain"]
        elif project == 'h5':
            configFile = self.ConfigFileContent_h5
            return configFile["Domain"]

    """
    获取domainPath
    """

    def getDomainPath(self, project):
        if project == 'interfaceAuto':
            configFile = self.ConfigFileContent_app
            return configFile["DomainPath"]
        elif project == 'h5':
            configFile = self.ConfigFileContent_h5
            return configFile["DomainPath"]

    """
    获取报告
    """

    def getReport(self, project):
        if project == 'interfaceAuto':
            configFile = self.ConfigFileContent_app
            return configFile["Report"]
        elif project == 'h5':
            configFile = self.ConfigFileContent_h5
            return configFile["Report"]

    """
    获取日志路径
    """

    def getLoggerPath(self, project):
        if project == 'interfaceAuto':
            return self.__parentPath + self.ConfigFileContent_app["LoggerPath"]
        elif project == 'h5':
            return self.__parentPath + self.ConfigFileContent_h5["LoggerPath"]

    """
    根据传入的模块名称读取模块请求参数文件，从而获取请求参数
    """

    def getParamsInfo(self, moduleInfo):
        return self.getContent(moduleInfo, "params")

    """
    根据传入的模块名称读取模块请求头文件，从而获取请求头
    """

    @Deprecated
    def getHeadersInfo(self, moduleInfo):
        return self.getContent(moduleInfo, "headers")

    """
    根据传入的模块名称读取模块请求体文件，从而获取请求体
    """

    @Deprecated
    def getPayloadInfo(self, moduleInfo):
        return self.getContent(moduleInfo, "payload")

    """
        根据传入的模块名称读取模块请求头和请求参数文件，从而获取请求头和请求文件
    """

    def getParamsAndPayloadInfo(self, uri, yml_content):
        return self.__getContentFromYaml(uri, yml_content)

    """
    根据传入的模块名称读取模块请求体文件，从而获取请求体
    """

    @Deprecated
    def getContent(self, moduleInfo, type):
        if (type == "params"):
            paramsFile = self.__parentPath + self.ConfigFileContent["ParamsPath"] + "/" + moduleInfo
            fileContent = self.readYaml(paramsFile)
        elif (type == "payload"):
            payloadFile = self.__parentPath + self.ConfigFileContent["PayloadPath"] + "/" + moduleInfo
            fileContent = self.readYaml(payloadFile)
        else:
            headerFile = self.__parentPath + self.ConfigFileContent["HeadersPath"] + "/" + moduleInfo
            fileContent = self.readYaml(headerFile)
        return fileContent

    """
        根据传入的模块名称读取模块请求体文件，从而获取请求体
    """

    def __getContentFromYaml(self, uri, yml_content):
        result = {'params': None, 'payload': None, 'headers': None, 'token': None, 'description': None, 'method': None}
        if yml_content.__contains__(uri):
            if yml_content[uri] is None:
                return result
            if yml_content[uri].__contains__('params'):
                result['params'] = yml_content[uri]['params']
            if yml_content[uri].__contains__('payload'):
                result['payload'] = yml_content[uri]['payload']
            if yml_content[uri].__contains__('headers'):
                result['headers'] = yml_content[uri]['headers']
            if yml_content[uri].__contains__('token'):
                result['token'] = yml_content[uri]['token']
            if yml_content[uri].__contains__('description'):
                result['description'] = yml_content[uri]['description']
            if yml_content[uri].__contains__('method'):
                result['method'] = yml_content[uri]['method']
        else:
            return result
        return result

    """
    获取请求接口信息集合，需要根据getInterfaceInfoFilePath方法先获取所有接口信息
    """

    def getInterfaceCollections(self, interfaceExcel, module, project):  # 构造请求接口
        interCollections = {}
        ConfigFileContent = None
        if project == 'interfaceAuto':
            ConfigFileContent = self.ConfigFileContent_app
        elif project == 'h5':
            ConfigFileContent = self.ConfigFileContent_h5
        filePath = self.__parentPath + ConfigFileContent[interfaceExcel]
        interfaceInfos = self.readInterface_ByExcel(filePath, module)  # 获取接口列表
        for interface in interfaceInfos:
            uri = interface['uri']
            interCollections[uri] = interface
        return interCollections

    """
    获取通过excel读取文件
    """

    def readInterface_ByExcel(self, excel, module):
        sheet = pandas.read_excel(excel, sheet_name='Sheet1', keep_default_na=False)  # 默认读取第一个sheet的内容
        headList = list(sheet.columns)  # 拿到表头: [A, B, C, D]
        resultList = []
        for i in sheet.values:  # i 为每一行的value的列表：[a2, b2, c3, d2]
            if (i[len(headList) - 1] == module):
                lineData = dict(zip(headList, i))
                resultList.append(lineData)
        return resultList
