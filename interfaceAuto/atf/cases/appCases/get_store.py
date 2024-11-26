import unittest
from interfaceAuto.atf.cases import Logger, cr, req
from interfaceAuto import atf


class get_store(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------门店模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'store','interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_store.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_store.yml', project='interfaceAuto')
    @classmethod
    def tearDownClass(self):
        Logger.info('----------门店模块测试结束!----------')

    # 查询当前地区
    def test_getStoresPosition(self):
        '''查询当前地区'''
        uri = '/stores/position'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertEqual(resp['data']['province'], '上海市', "province:返回实际结果是->:%s" % resp['data']['province'])
        self.assertTrue(resp['data']['districtId'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 查询指定地区的普通门店,TOP3以后的门店
    def test_getNormalStores(self):
        '''查询指定地区的普通门店,TOP3以后的门店'''
        uri = '/stores/selected'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertEqual(resp['data']['total'], 0, "total:返回实际结果是->:%s" % resp['data']['total'])
        self.assertGreaterEqual(resp['data']['total'], 1)
        self.assertGreaterEqual(len(resp['data']['list']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 查询指定地区的星选门店
    def test_getHotStores(self):
        '''查询指定地区的星选门店'''
        uri = '/stores/hot_store'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 查询所有城市
    def test_getCityList(self):
        '''查询所有城市'''
        uri = '/stores/city'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 查询门店详情
    def test_getStoresDetail(self):
        '''查询门店详情'''
        uri = '/stores/detail'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertEqual(resp['data']['name'], '云南白药采之汲Ai私定肌肤管理中心', "name:返回实际结果是->:%s" % resp['data']['name'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['misMachines']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # # 查询当前城市门店信息
    # def test_get(self):
    #     '''查询当前城市门店信息'''
    #     uri = '/stores/commonly'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     # self.assertEqual(resp['data'], '您当前的城市暂未开放服务，敬请期待吧！', "data:返回实际结果是->:%s" % resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 购买会员卡门店自提
    # 7.6更新
    def test_storenear_bySkuid(self):
        '''购买会员卡门店自提'''
        uri = '/store/near_bySkuid'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertGreaterEqual(len(resp['data']['list']), 1)
            self.assertGreaterEqual(resp['data']['total'], 1)
            self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], '附近暂无可选门店，敬请期待', "message:返回实际结果是->:%s" % resp['message'])
