import unittest
from interfaceAuto.atf.cases import Logger, cr, req
from interfaceAuto import atf

class get_popup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------我的模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'popup','interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_popup.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_popup.yml', project='interfaceAuto')
        
    @classmethod
    def tearDownClass(self):
        Logger.info('----------我的模块测试结束!----------')

    # 开屏广告查询接口（手机端）
    def test_getSplashAdvShow(self):
        '''开屏广告查询接口（手机端）'''
        uri = '/splashAdv/show'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        if atf.env == 'test':
            self.assertIsNone(resp['data'], "message:屏广告查询接口（手机端）错误")
        elif atf.env == 'dev':
            self.assertTrue(resp['data'])
            self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "code:返回实际结果是->:%s" % resp['message'])

    # 灰度版本检测
    def test_getGray_releaseShow(self):
        '''灰度版本检测'''
        uri = '/gray_release/show'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:灰度版本检测错误")
        self.assertEqual(resp['message'], '', "code:返回实际结果是->:%s" % resp['message'])

    # 弹窗显示
    def test_getPopupShow(self):
        '''弹窗显示'''
        uri = '/popup/show'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        if atf.env == 'test':
            self.assertIsNotNone(resp['current1']['data']['id'], "message:弹窗显示错误")
        elif atf.env == 'dev':
            self.assertIsNone(resp['current1']['data'], "message:弹窗显示错误")
        self.assertEqual(resp['current1']['message'], '', "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        if atf.env == 'test':
            self.assertTrue(resp['current2']['data'])
        elif atf.env == 'dev':
            self.assertIsNone(resp['current2']['data'], "message:弹窗显示错误")
        self.assertEqual(resp['current2']['message'], '', "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 配置项查询
    def test_miniProgrambannerconfigsToGet(self):
        '''配置项查询'''
        uri = '/miniProgram/banner/configsToGet'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertGreaterEqual(len(resp['current1']['data']), 1)
        self.assertEqual(resp['current1']['message'], '配置项查询成功', "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertGreaterEqual(len(resp['current2']['data']), 1)
        self.assertEqual(resp['current2']['message'], '配置项查询成功', "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertGreaterEqual(len(resp['current3']['data']), 1)
        self.assertEqual(resp['current3']['message'], '配置项查询成功', "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current4']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current4']['data'])
        self.assertGreaterEqual(len(resp['current4']['data']), 1)
        self.assertEqual(resp['current4']['message'], '配置项查询成功', "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 获取token
    def test_accountupdate_token(self):
        '''获取token'''
        uri = '/account/update_token'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], 'success', "code:返回实际结果是->:%s" % resp['message'])

    # 有效期内礼品卡数量
    def test_giftcardgiftCardNum(self):
        '''有效期内礼品卡数量'''
        uri = '/giftcard/giftCardNum'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertGreaterEqual(resp['data'], 0) # 判断data大于等于0
        self.assertEqual(resp['message'], '查询成功！', "code:返回实际结果是->:%s" % resp['message'])

    # 轮播图列表
    def test_slideshowgetAPPSlideshowList(self):
        '''轮播图列表'''
        uri = '/slideshow/getAPPSlideshowList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertGreaterEqual(len(resp['data']), 1)
            self.assertEqual(resp['message'], None, "code:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], None, "code:返回实际结果是->:%s" % resp['message'])