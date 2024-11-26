import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
import json,yaml
import platform
from interfaceAuto import atf

class get_shopscene(unittest.TestCase):
    tid = 0
    parentTid = 0
    id = 0

    @classmethod
    def setUpClass(self):
        Logger.info('----------商城模块测试开始----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'shopscene','interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_shopscene.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_shopscene.yml', project='interfaceAuto')
        
    @classmethod
    def tearDownClass(self):
        Logger.info('----------商城模块测试结束!----------')

    # # 查询部分全部宝贝列表
    # def test_getGoodList(self):
    #     '''查询部分全部宝贝列表'''
    #     uri = '/goods_list'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     get_shopscene.id = resp['current1']['data']['records'][0]['id']
    #     print(resp)
    #     self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
    #     # self.assertEqual(resp['current1']['data']['current'], 1, "message:返回实际结果是->:%s" % resp['current1']['data']['current'])
    #     self.assertEqual(resp['current1']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current1']['message'])
    #     self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
    #     # self.assertEqual(resp['current2']['data']['current'], 2, "message:返回实际结果是->:%s" % resp['current2']['data']['current'])
    #     self.assertEqual(resp['current2']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 搜索商品（自动化）
    def test_goods_search_result(self):
        '''搜索商品（自动化）'''
        uri = '/goods_search_result'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        get_shopscene.id = resp['data']['records'][0]['id']
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['records']), 1)
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['message'])

    # 商品加入购物车
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_addGoodToCart(self):
        '''商品加入购物车'''
        uri = '/site/shop/cart/add'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                # conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/shopscene.yml", encoding='utf8').read()  # 配置文件内容
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            # 给tid值为 resp['data'][0]['tid']
            content['/site/shop/cart/add']['payload']['goodsInfoId'] = get_shopscene.id
            # 更改为有缩进json格式
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                # conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/shopscene.yml", encoding='utf8').read()  # 配置文件内容
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            # 给tid值为 resp['data'][0]['tid']
            content['/site/shop/cart/add']['payload']['goodsInfoId'] = get_shopscene.id
            # 更改为有缩进json格式
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:商品加入购物车错误")
            self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '2000'):
            self.assertEqual(resp['code'], '2000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:商品加入购物车错误")
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])

    # 编辑购物车商品
    @unittest.skipIf(skip == True, 'PUT请求跳过')
    def test_siteshopcartedit(self):
        '''编辑购物车商品'''
        uri = '/site/shop/cart/edit'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/site/shop/cart/edit']['payload']['goodsId'] = get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/site/shop/cart/edit']['payload']['goodsId'] = get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:编辑购物车商品错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 购物车结算
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_confirmShoppingCart(self):
        '''购物车结算'''
        uri = '/trade/confirm_shopping_cart'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/confirm_shopping_cart']['payload']['tradeItems'][0]['skuId']= get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/confirm_shopping_cart']['payload']['tradeItems'][0]['skuId']= get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购物车结算错误")
            self.assertEqual(resp['message'], '请勿重复提交', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购物车结算错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 预购买
    @unittest.skipIf(skip == True, '购买请求跳过')
    def test_preCommit(self):
        '''预购买'''
        uri = '/trade/purchase/preCommit'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if(resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertGreaterEqual(len(resp['data']['goodsInfos']), 1)
            self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], '您已从购物车成功下单了订单中的商品，如还需购买，请重新加入购物车。', "message:返回实际结果是->:%s" % resp['message'])

    # 拉起支付
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_commit(self):
        '''拉起支付'''
        uri = '/trade/commit'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        get_shopscene.tid = resp['data'][0]['tid']
        get_shopscene.parentTid = resp['data'][0]['parentTid']
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertGreaterEqual(len(resp['data']), 1)  # 判断这个list个数大于0
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])

    # aliPay（支付宝支付）
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_aliPay(self):
        '''aliPay（支付宝支付）'''
        uri = '/pay/interfaceAuto/aliPay'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            contents = yaml.load(conf, Loader=yaml.FullLoader)
            contents['/pay/interfaceAuto/aliPay']['payload']['tid'] = get_shopscene.parentTid
            contents['/pay/interfaceAuto/aliPay']['payload']['feeCode'] = "16110100"
            contents['/pay/interfaceAuto/aliPay']['payload']['channelItemId'] = 19
            json_str = json.dumps(contents, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            contents = yaml.load(conf, Loader=yaml.FullLoader)
            contents['/pay/interfaceAuto/aliPay']['payload']['tid'] = get_shopscene.parentTid
            contents['/pay/interfaceAuto/aliPay']['payload']['feeCode'] = "16110100"
            contents['/pay/interfaceAuto/aliPay']['payload']['channelItemId'] = 19
            json_str = json.dumps(contents, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '支付宝支付成功！', "message:返回实际结果是->:%s" % resp['message'])

    # 查询支付结果
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_payrecordstatus(self):
        '''查询支付结果'''
        uri = '/pay/record/status/'
        uri_new = uri + get_shopscene.parentTid
        self.ymlContent[uri_new] = self.ymlContent.pop(uri)
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            contents = yaml.load(conf, Loader=yaml.FullLoader)
            json_str = json.dumps(contents, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            contents = yaml.load(conf, Loader=yaml.FullLoader)
            json_str = json.dumps(contents, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri_new, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:查询支付结果")
        self.assertEqual(resp['message'], '查询支付记录状态！', "message:返回实际结果是->:%s" % resp['message'])



    # # wxPayUnifiedorderForApp（微信支付）
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_paywxPayUnifiedorderForApp(self):
    #     '''wxPayUnifiedorderForApp（微信支付）'''
    #     uri = '/pay/wxPayUnifiedorderForApp'
    #     if atf.env == 'test':
    #         if (platform.system().lower() == 'linux'):
    #             conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
    #         else:
    #             conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
    #         contents = yaml.load(conf, Loader=yaml.FullLoader)
    #         print(get_shopscene.parentTid)
    #         contents['/pay/wxPayUnifiedorderForApp']['payload']['tid'] = get_shopscene.parentTid
    #         contents['/pay/wxPayUnifiedorderForApp']['payload']['feeCode'] = "16110100"
    #         contents['/pay/wxPayUnifiedorderForApp']['payload']['channelItemId'] = 16
    #         json_str = json.dumps(contents, indent=4)
    #         if (platform.system().lower() == 'linux'):
    #             with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
    #                 f.write(json_str)
    #         else:
    #             with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
    #                 f.write(json_str)
    #     if atf.env == 'dev':
    #         if (platform.system().lower() == 'linux'):
    #             conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
    #         else:
    #             conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
    #         contents = yaml.load(conf, Loader=yaml.FullLoader)
    #         print(get_shopscene.parentTid)
    #         contents['/pay/wxPayUnifiedorderForApp']['payload']['tid'] = get_shopscene.parentTid
    #         contents['/pay/wxPayUnifiedorderForApp']['payload']['feeCode'] = "16110100"
    #         contents['/pay/wxPayUnifiedorderForApp']['payload']['channelItemId'] = 16
    #         json_str = json.dumps(contents, indent=4)
    #         if (platform.system().lower() == 'linux'):
    #             with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
    #                 f.write(json_str)
    #         else:
    #             with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
    #                 f.write(json_str)
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     if (resp['code'] == '00000'):
    #         self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #         self.assertTrue(resp['data'])
    #         self.assertEqual(resp['message'], '微信支付成功！', "message:返回实际结果是->:%s" % resp['message'])
    #     if (resp['code'] == '20000'):
    #         self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
    #         self.assertTrue(resp['data'])
    #         self.assertEqual(resp['message'], '订单状态异常，无法支付', "message:返回实际结果是->:%s" % resp['message'])

    # 取消订单
    @unittest.skipIf(skip == True, '未拉起支付跳过')
    def test_cancelPurchase(self):
        '''取消订单'''
        uri = '/trade/cancel'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/cancel']['params']['tid'] = get_shopscene.tid
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/cancel']['params']['tid'] = get_shopscene.tid
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:取消订单错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:取消订单错误")
            self.assertEqual(resp['message'], '订单已作废''', "message:返回实际结果是->:%s" % resp['message'])

    # 确认商品
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_checkGoods(self):
        '''确认商品'''
        uri = '/trade/check_goods'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/check_goods']['payload']['tradeItems'][0]['skuId'] = get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/check_goods']['payload']['tradeItems'][0]['skuId'] = get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:确认商品错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '2000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:确认商品错误")
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])

    # 立即购买
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_immediateBuy(self):
        '''立即购买'''
        uri = '/trade/immediate_buy'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/immediate_buy']['payload']['tradeItemRequests'][0]['skuId'] = get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        if atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/immediate_buy']['payload']['tradeItemRequests'][0]['skuId'] = get_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:立即购买错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '2000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:立即购买错误")
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])