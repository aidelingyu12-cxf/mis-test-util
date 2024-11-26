import unittest
from interfaceAuto.atf.cases import Logger, cr, req
from parameterized import parameterized
from interfaceAuto import atf

## 首页接口
class get_firstPage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------首页模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'firstPage', 'interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_firstPage.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_firstPage.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(self):
        Logger.info('----------首页模块测试结束!----------')

    # 获取banner列表
    def test_BannerList(self):
        '''获取首页banner列表'''
        uri = '/banner/list'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertEqual(resp['data'][0]['topOrBottom'], 'top', "topOrBottom:返回实际结果是->:%s" % resp['data'][0]['topOrBottom'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])

    # 获取首页banner信息GET
    @parameterized.expand([
        ['pageSize', '5']
    ])
    def test_GetBannerList(self, desc, expect):
        '''获取美肤泡泡'''
        uri = '/banner/pageList'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['rows']), 1)
        self.assertGreaterEqual((resp['data']['pageSize']), 1)
        self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])

    # 获取日常护理建议
    def test_GetDailyCareTip(self):
        '''获取日常护理建议'''
        uri = '/account/get_daily_care_tip'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertGreaterEqual(len(resp['data']), 1)
        # self.assertEqual(resp['data'][0]['id'], None, "id:返回实际结果是->:%s" % resp['data'][0]['id'])
        self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])

    # 扫设备二维码获
    # 取设备id（由于mis机关闭，该接口就会报服务异常，故无法进行自动化测试）
    # def test_getDeviceId(self):
    #     """扫设备二维码获取设备id"""
    #     uri = '/skin/detection/qr_check'
    #     resp = req.getResp(ymlFile='firstPage', uri=uri, project='interfaceAuto')
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
    #     self.assertEqual(resp['data']['device_id'], 'b5b8745caf4000c572449b94ddfcf7dc6489a136eb986a5cbe3424c77cba037d',
    #                      "message:扫设备二维码获取设备id接口错误")

    # 轮询检测结果
    def test_getCheckState(self):
        """轮询检测结果"""
        uri = '/skin/detection/task_status/385fe08a23934a639ccc68e2efdc5dde'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
        self.assertIsNotNone(resp['data']['task_status'], "message:轮询检测结果接口错误")