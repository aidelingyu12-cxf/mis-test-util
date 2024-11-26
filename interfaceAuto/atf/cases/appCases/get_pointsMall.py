import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from interfaceAuto import atf

class get_pointsMall(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------积分商城模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'pointsMall','interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_pointsMall.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_pointsMall.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(self):
        Logger.info('----------积分商城获取积分规则模块测试结束!----------')

    # 获取积分商城某个分类
    def test_goodsPage(self):
        '''获取积分商城某个分类'''
        uri = '/points_mall/goods_page'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(isinstance(resp['current1']['data']['data'], list))
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 查询积分商城兑换记录
    def test_pointstradePage(self):
        '''查询积分商城兑换记录'''
        uri = '/points_trade/page'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertTrue(isinstance(resp['data']['data'], list))
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 查询某个积分商品详情
    def test_goodsDetail(self):
        '''查询某个积分商品详情'''
        uri = '/points_mall/goods_detail'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['carouselImgList']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])


    # 积分商品订单详情
    def test_points_trade_detail(self):
        '''积分商品订单详情'''
        uri = '/points_trade/detail'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        # if (resp['code'] == '00000'):
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertIsNotNone(resp['data']['id'])
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])
        # if (resp['code'] == '20000'):
        #     self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
        #     self.assertEqual(resp['message'], '会员不存在', "message:返回实际结果是->:%s" % resp['message'])

    # 接收任务奖励
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_signreceive_task_rewards(self):
        '''接收任务奖励'''
        uri = '/sign/receive_task_rewards'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], 'APP023', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:接收任务奖励错误")
        self.assertEqual(resp['message'], '抱歉！您已经领取过该任务奖励，不可重复领取', "message:返回实际结果是->:%s" % resp['message'])

    # 签名
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_sign(self):
        '''签名'''
        uri = '/sign'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 积分兑换优惠卷列表
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_points_mallpageCoupon(self):
        '''积分兑换优惠卷列表'''
        uri = '/points_mall/pageCoupon'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['data']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 奖励清单
    def test_signreward_list(self):
        '''奖励清单'''
        uri = '/sign/reward_list'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertTrue(isinstance(resp['data'], list))
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # # 积分领取优惠卷
    # @unittest.skipIf(skip == True, '积分兑换优惠卷')
    # def test_points_mallfetchPointsCoupon(self):
    #     '''积分领取优惠卷'''
    #     uri = '/points_mall/fetchPointsCoupon'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 积分任务
    def test_signpoints_tasks(self):
        '''积分任务'''
        uri = '/sign/points_tasks'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertTrue(isinstance(resp['data'], list))
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # # 兑换商品
    # # 7.8更新
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_points_tradecommit(self):
    #     '''兑换商品'''
    #     uri = '/points_trade/commit'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 获取随机10种积分商品列表(推荐商品)
    # 7.8更新
    def testpointstradecommit(self):
        '''获取随机10种积分商品列表(推荐商品)'''
        uri = '/points_mall/recommend_goods'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertTrue(isinstance(resp['data'], list))
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])