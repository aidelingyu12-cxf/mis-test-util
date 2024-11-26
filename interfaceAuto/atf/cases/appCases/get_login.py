import unittest
from interfaceAuto.atf.cases import Logger, cr, req
from interfaceAuto import atf

class get_login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------登录模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'login','interfaceAuto')  # 获取接口
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_login.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_login.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(self):
        Logger.info('----------登录模块测试结束!----------')

    # 获取用户协议
    def test_getUserProtocolHTML(self):
        '''获取用户协议'''
        url = 'https://resource.caizhiji.com.cn/protocol/user-protocol.html'
        result = req.getResp(url=url, project='interfaceAuto', yml_content=self.ymlContent)
        resp = result[0:15]
        print(resp)
        self.assertEqual(resp, '<!DOCTYPE html>', "resp:返回实际结果是->:%s" % resp)

    # 获取用户协议CSS样式
    def test_getUserProtocolCSS(self):
        '''获取用户协议CSS样式'''
        url = 'https://resource.caizhiji.com.cn/protocol/user-protocol.css'
        result = req.getResp(url=url, project='interfaceAuto', yml_content=self.ymlContent)
        resp = result[0:6]
        print(resp)
        self.assertEqual(resp, 'body {', "resp:返回实际结果是->:%s" % resp)

    # 获取隐私协议
    def test_getPrivacyProtocolHTML(self):
        '''获取隐私协议'''
        url = 'https://resource.caizhiji.com.cn/protocol/privacy-protocol.html'
        result = req.getResp(url=url, project='interfaceAuto', yml_content=self.ymlContent)
        resp = result[0:15]
        print(resp)
        self.assertEqual(resp, '<!DOCTYPE html>', "resp:返回实际结果是->:%s" % resp)

    # 获取隐私协议样式
    def test_getPrivacyProtocolCSS(self):
        '''获取隐私协议样式'''
        url = 'https://resource.caizhiji.com.cn/protocol/privacy-protocol.css'
        result = req.getResp(url=url, project='interfaceAuto', yml_content=self.ymlContent)
        resp = result[0:6]
        print(resp)
        self.assertEqual(resp, 'body {', "resp:返回实际结果是->:%s" % resp)

    # 使用密码登录
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_loginOrRegister(self):
        '''使用密码登录'''
        uri = '/account/login_or_register'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if atf.env == 'test':
            self.assertEqual(resp['current1']['data']['account']['phone_number'], '17766008328', "phone_number:返回实际结果是->:%s" % resp['current1']['data']['account']['phone_number'])
        if atf.env == 'dev':
            self.assertEqual(resp['current1']['data']['account']['phone_number'], '13260633273', "phone_number:返回实际结果是->:%s" % resp['current1']['data']['account']['phone_number'])
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertEqual(resp['current1']['message'], 'success', "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00106', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], "验证码不匹配", "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00104', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertEqual(resp['current3']['message'], '用户名或密码错误', "message:返回实际结果是->:%s" % resp['current3']['message'])

    # # 发送短信验证码
    # # 7.12更新
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_verificationcode(self):
    #     '''发送短信验证码'''
    #     uri = '/sms/verification_code/17766008328'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertEqual(resp['message'], 'OK', "message:返回实际结果是->:%s" % resp['message'])