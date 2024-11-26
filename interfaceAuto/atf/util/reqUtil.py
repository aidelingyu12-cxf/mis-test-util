from collections import defaultdict

import requests, json, time, threading
from interfaceAuto.atf.util.configReader import configReader
from interfaceAuto.atf.util.logUtil import Logger


"""
requestUtil
~~~~~~~~~~~~~


A reqUtil
usage:
    >>> from reqUtil import reqUtil
    >>> req = reqUtil()
    >>> req.getResp(method="method",uri="uri",headers="headers",params="params",payload="payload")
    >>> req.uploadSinglePic(fileName="fileName", filePath="filePath", uri="uri", headers="headers", params="params", formData="formData")

@author cxf
"""

class reqUtil():

    __singleLock = threading.Lock()  # 单例锁

    Logger = Logger()


    """
    获取响应
    data:接口列表，dict数据
    module:模块名称
    """
    def getResp(self, yml_content, project,uri=None, url=None):
        ##判断当前url是否是生产环境通用路径
        if(url is None):
            url = configReader().getDomain(project) + configReader().getDomainPath(project) + uri
        else:
            uri = url
        # data = dataMap[uri]    #获取接口数据集
        multipartResult = defaultdict(list)  # 结果集
        response = {}  # 单个结果

        paramsAndPayload = configReader().getParamsAndPayloadInfo(uri=uri, yml_content=yml_content)
        ##构造requests请求数据
        headers = paramsAndPayload['headers']
        token = configReader().getAuth(project)

        params = paramsAndPayload['params']
        payload = paramsAndPayload['payload']
        if (headers == '' or isinstance(headers,int) or isinstance(headers,float) or isinstance(headers, bool)):
            headers = {"Authorization": token}
        else:
            # headers = json.loads(headers)
            headers["Authorization"] = token

        # 开始请求,考虑所有情况
        # GET请求
        if (paramsAndPayload['method'] == 'GET'):
            if (type(params) == list):
                for param in params:
                    for key in param:
                        resp = self.__tryGET(url=url, params=param[key], headers=headers)
                        response[key] = resp.json()
                    time.sleep(2)
                return response
            else:
                resp = self.__tryGET(url=url, params=params, headers=headers)
                try:
                    return resp.json()
                except Exception as e:
                    return str(resp.text.encode('utf8'), 'utf8')
        # POST、PUT和DELETE请求
        elif(paramsAndPayload['method'] == 'POST' or paramsAndPayload['method'] == 'PUT' or paramsAndPayload['method'] == 'DELETE'):
            method = paramsAndPayload['method']
            if (params == None or type(params) != list):  # param为0,1;body为任意
                if (type(payload) == list):
                    for body in payload:
                        for key in body:
                            resp = self.__tryPOSTPUTDELETE(
                                url=url, payload=body[key], headers=headers, params=params, method=method)
                            response[key] = resp.json()
                        time.sleep(2)
                    return response
                else:
                    resp = self.__tryPOSTPUTDELETE(url=url, headers=headers, payload=payload, params=params, method=method)
                    return resp.json()
            elif (payload == None or type(payload) != list):  # body为0,1;param为任意
                if (type(params) == list):
                    for param in params:
                        for key in param:
                            resp = self.__tryPOSTPUTDELETE(url=url, params=param[key], headers=headers, payload=payload, method=method)
                            response[key] = resp.json()
                        time.sleep(2)
                    return response
                else:
                    resp = self.__tryPOSTPUTDELETE(url=url, headers=headers, params=params, payload=payload, method=method)
                    return resp.json()
            else:  # param和body都为任意
                for param in params:
                    for paramKey in param:
                        for body in payload:
                            for bodyKey in body:
                                resp = self.__tryPOSTPUTDELETE(url=url, params=param[paramKey], headers=headers, payload=body[bodyKey], method=method)
                                multipartResult[paramKey].append(resp.json())
                            time.sleep(2)
                self.Logger.info('The number of PARAM and PAYLOAD is greater than 2, please be cautions about the result, it is given in the form of DICT')
                self.Logger.error(
                    'The number of PARAM and PAYLOAD is greater than 2, please be cautions about the result, it is given in the form of DICT')
                return multipartResult
        else:
            pass



    @classmethod
    def __tryGET(cls, url, headers, params):
        try:
            response = requests.get(url=url, headers=headers, params=params)
            return response
        except Exception as e:
            Logger().critical(e.args)

    @classmethod
    def __tryPOSTPUTDELETE(cls, url, headers, params, payload, method):
        try:
            if (None == payload):
                if(method == 'POST'):
                    response = requests.post(url=url, headers=headers, params=params)
                elif(method == 'PUT'):
                    response = requests.put(url=url, headers=headers, params=params)
                elif(method == 'DELETE'):
                    response = requests.delete(url=url, headers=headers, params=params)
            elif (isinstance(payload, str)):
                if (method == 'POST'):
                    response = requests.post(url=url, headers=headers, params=params, data=payload)
                elif (method == 'PUT'):
                    response = requests.put(url=url, headers=headers, params=params, data=payload)
                elif (method == 'DELETE'):
                    response = requests.delete(url=url, headers=headers, params=params, data=payload)
            else:
                if (method == 'POST'):
                    response = requests.post(url=url, headers=headers, params=params, json=payload)
                elif (method == 'PUT'):
                    response = requests.put(url=url, headers=headers, params=params, json=payload)
                elif (method == 'DELETE'):
                    response = requests.delete(url=url, headers=headers, params=params, json=payload)
            return response
        except Exception as e:
            Logger().critical(e.args)