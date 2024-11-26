import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from interfaceAuto import atf

class get_shop(unittest.TestCase):
    tid = 0
    @classmethod
    def setUpClass(self):
        Logger.info('----------商城模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'shop','interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_shop.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_shop.yml', project='interfaceAuto')
        
    @classmethod
    def tearDownClass(self):
        Logger.info('----------商城模块测试结束!----------')

    # 查询商品分类
    def test_getCategories(self):
        '''查询商品分类'''
        uri = '/categories'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 查询购物车商品数量
    def test_getShopCart(self):
        '''查询购物车商品数量'''
        uri = '/site/shop/cart/total'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertGreaterEqual(resp['data'], 0)  # 判断data大于等于0
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 查询所有套餐
    def test_getPackageList(self):
        '''查询所有套餐'''
        uri = '/general_package_list'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(resp['data']['total'], 1)  # 判断data大于等于1
        self.assertGreaterEqual(len(resp['data']['records']), 1)  # 判断data大于等于1
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])
        # self.assertEqual(resp['data']['size'], 100, "code:返回实际结果是->:%s" % resp['data']['size'])

    # 查询部分全部宝贝列表
    def test_getGoodList(self):
        '''查询部分全部宝贝列表'''
        uri = '/goods_list'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertGreaterEqual(resp['current1']['data']['total'], 1)  # 判断data大于等于1
        self.assertGreaterEqual(len(resp['current1']['data']['records']), 1)  # 判断data大于等于1
        # self.assertEqual(resp['current1']['data']['current'], 1, "message:返回实际结果是->:%s" % resp['current1']['data']['current'])
        self.assertEqual(resp['current1']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertGreaterEqual(resp['current2']['data']['total'], 1)  # 判断data大于等于1
        self.assertGreaterEqual(len(resp['current2']['data']['records']), 1)  # 判断data大于等于1
        # self.assertEqual(resp['current2']['data']['current'], 2, "message:返回实际结果是->:%s" % resp['current2']['data']['current'])
        self.assertEqual(resp['current2']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertGreaterEqual(resp['current3']['data']['total'], 1)  # 判断data大于等于1
        self.assertGreaterEqual(len(resp['current3']['data']['records']), 1)  # 判断data大于等于1
        self.assertEqual(resp['current3']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current3']['message'])
        self.assertEqual(resp['current4']['code'], '00000', "code:返回实际结果是->:%s" % resp['current4']['code'])
        self.assertTrue(resp['current4']['data'])
        self.assertGreaterEqual(resp['current4']['data']['total'], 1)  # 判断data大于等于1
        self.assertGreaterEqual(len(resp['current4']['data']['records']), 1)  # 判断data大于等于1
        self.assertEqual(resp['current4']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current4']['message'])


    # 商品加入购物车
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_addGoodToCart(self):
        '''商品加入购物车'''
        uri = '/site/shop/cart/add'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:商品加入购物车错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 编辑购物车商品
    @unittest.skipIf(skip == True, 'PUT请求跳过')
    def test_siteshopcartedit(self):
        '''编辑购物车商品'''
        uri = '/site/shop/cart/edit'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:编辑购物车商品错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 购物车列表
    def test_goodsCart(self):
        '''购物车列表'''
        uri = '/site/shop/cart'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(isinstance(resp['data'], list))  # 判断是否是数组list
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 购物车结算
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_confirmShoppingCart(self):
        '''购物车结算'''
        uri = '/trade/confirm_shopping_cart'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购物车结算错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购物车结算错误")
            self.assertEqual(resp['message'], '很抱歉，您的订单中包含不存在的商品，可能是已被删除或已被下单，如还需购买，请重新加入购物车。', "message:返回实际结果是->:%s" % resp['message'])

    # 删除购物车商品
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_removeFromCart(self):
        '''删除购物车商品'''
        uri = '/site/shop/cart/remove'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:删除购物车商品错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

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

    # # 拉起支付
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_commit(self):
    #     '''拉起支付'''
    #     uri = '/trade/commit'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     if (resp['code'] == '00000'):
    #         self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #         self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
    #     if (resp['code'] == '20000'):
    #         self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
    #         self.assertEqual(resp['message'], '您已从购物车成功下单了订单中的商品，如还需购买，请重新加入购物车。', "message:返回实际结果是->:%s" % resp['message'])

    # # aliPay
    # def test_aliPay(self):
    #     '''aliPay'''
    #     uri = '/pay/interfaceAuto/aliPay'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     if(resp['code'] == '00000'):
    #         self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #         self.assertEqual(resp['message'], '支付宝支付成功！', "message:返回实际结果是->:%s" % resp['message'])

    # 取消订单
    def test_cancelPurchase(self):
        '''取消订单'''
        uri = '/trade/cancel'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:取消订单错误")
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 确认商品
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_checkGoods(self):
        '''确认商品'''
        uri = '/trade/check_goods'
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

    # 查询默认收货地址
    def test_findDefaultAddress(self):
        '''查询默认收货地址'''
        uri = '/customer/findDefaultAddress'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertIsNotNone(resp['data']['customerId'], "message:查询默认收货地址错误")
        self.assertEqual(resp['message'], '查询默认收货地址成功！', "message:返回实际结果是->:%s" % resp['message'])
        # self.assertEqual(resp['data']['address'], '龙花园8号楼4单元401', "address:返回实际结果是->:%s" % resp['data']['address'])

    # 验证优惠码
    def test_checkAngleCode(self):
        '''验证优惠码'''
        uri = '/shop/goods/angle_code_valid'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:验证优惠码错误")
            self.assertEqual(resp['message'], '优惠码有效', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:验证优惠码错误")
            self.assertEqual(resp['message'], '优惠码无效', "message:返回实际结果是->:%s" % resp['message'])

    # 待支付订单列表
    def test_tradepage(self):
        '''待支付订单列表'''
        uri = '/trade/page'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['data']), 1)
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 获取有门店的且包含该服务项的省市区列表
    def test_storesqueryDistrict(self):
        '''获取有门店的且包含该服务项的省市区列表'''
        uri = '/stores/queryDistrict'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

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

    # 门店列表
    def test_store_liste(self):
        '''门店列表'''
        uri = '/shop/store_list'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if(resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:门店列表错误")
            self.assertEqual(resp['message'], '您已从购物车成功下单了订单中的商品，如还需购买，请重新加入购物车。', "message:返回实际结果是->:%s" % resp['message'])

    # 进入搜索页面
    def test_goods_search_recommends(self):
        '''进入搜索页面'''
        uri = '/goods_search_recommends'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertGreaterEqual(len(resp['data']), 1)
        self.assertTrue(isinstance(resp['data'], list))  # 判断是否是数组list
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 搜索结果列表
    def test_goods_search_result(self):
        '''搜索结果列表'''
        uri = '/goods_search_result'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['records']), 1)
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['message'])

    # 搜索结果
    def test_goods_search_associations(self):
        '''搜索结果'''
        uri = '/goods_search_associations'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])


    # 查询标题文字
    def test_getApiTitleWordGetWord(self):
        '''查询标题文字'''
        uri = '/api/titleWord/getWord'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertIsNotNone(resp['data']['id'])
        self.assertEqual(resp['message'], '标题文字查询成功', "message:返回实际结果是->:%s" % resp['message'])

    # 购物车列表（区分有效、失效）
    # 7.6更新
    def test_siteshopcart_all(self):
        '''购物车列表（区分有效、失效）'''
        uri = '/site/shop/cart_all'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertTrue(isinstance(resp['data']['effectiveGoods'], list))  # 判断是否是数组list
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 看了又看
    # 7.6更新
    def test_seeMore(self):
        '''看了又看'''
        uri = '/seeMore'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # # 女神节活动详情
    # # 7.6更新
    # def test_activityactivitiesDetail(self):
    #     '''女神节活动详情'''
    #     uri = '/activity/activitiesDetail'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     if atf.env == 'test':
    #         self.assertTrue(resp['data'])
    #     elif atf.env == 'dev':
    #         self.assertIsNone(resp['data'], "message:女神节活动详情错误")
    #     self.assertEqual(resp['message'], '活动页列表详情查询成功', "message:返回实际结果是->:%s" % resp['message'])

    # # 女神检查优惠券是否可以领取
    # # 7.6更新
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_couponcheckCoupon(self):
    #     '''女神检查优惠券是否可以领取'''
    #     uri = '/coupon/checkCoupon'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], 'app优惠券领取情况查询成功', "message:返回实际结果是->:%s" % resp['message'])

    # # 女神活动发放优惠券
    # # 7.6更新
    # def test_couponcheckCoupons(self):
    #     '''女神活动发放优惠券'''
    #     uri = '/coupon/sendCoupon'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertIsNone(resp['data'], "message:女神活动发放优惠券错误")
    #     self.assertEqual(resp['message'], '优惠券发放成功', "message:返回实际结果是->:%s" % resp['message'])

    # 获取分类和标签列表
    # 7.6更新
    def test_allCate(self):
        '''获取分类和标签列表'''
        uri = '/allCate'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 根据分类id或标签id获取商品列表
    # 7.6更新
    def test_cateGoodsList(self):
        '''根据分类id或标签id获取商品列表'''
        if atf.env == 'test':
            uri = '/cateGoodsList/52'
        elif atf.env == 'dev':
            uri = '/cateGoodsList/1382'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['records']), 1)
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 商品评论列表
    # 7.8更新
    def test_goods_evaluatedetail_evaluatelist(self):
        '''商品评论列表'''
        uri = '/goods_evaluate/detail_evaluate/list'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['records']), 0)
        self.assertGreaterEqual((resp['data']['total']), 0)
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 新人首单礼活动商品查询
    # 7.8更新
    def test_activitynewcomergoods(self):
        '''新人首单礼活动商品查询'''
        uri = '/activity/newcomer/goods'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 新人首单礼活动用户完成情况查询
    # 7.8更新
    def test_activitynewcomerstatus(self):
        '''新人首单礼活动用户完成情况查询'''
        uri = '/activity/newcomer/status'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 活动专区列表
    # 7.8更新
    def test_activityAreaappActivityAreaList(self):
        '''活动专区列表'''
        uri = '/activityArea/appActivityAreaList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertGreaterEqual(len(resp['data']), 1)
        self.assertTrue(isinstance(resp['data'], list))
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 顶部banner列表
    # 7.8更新
    def test_topBannergetAPPBannerList(self):
        '''顶部banner列表'''
        uri = '/topBanner/getAPPBannerList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 领取新人优惠券
    # 7.8更新
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_couponreceive_coupon(self):
        '''领取新人优惠券'''
        uri = '/coupon/receive_coupon'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if(resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:领取新人优惠券错误")
            self.assertEqual(resp['message'], '领取成功！', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:领取新人优惠券错误")
            self.assertEqual(resp['message'], '您已领取过新人优惠券了哦', "message:返回实际结果是->:%s" % resp['message'])

    # 会员登录查询商品详情接口
    # 7.8更新
    def test_goods_detail_to_vip(self):
        '''会员登录查询商品详情接口'''
        uri = '/goods_detail_to_vip'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertIsNotNone(resp['data']['id'])
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 优惠卷列表
    # 7.8更新
    def test_tradepurchaseconfirmation(self):
        '''优惠卷列表'''
        uri = '/trade/purchase/confirmation'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if(resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:优惠卷列表错误")
            self.assertEqual(resp['message'], '您已从购物车成功下单了订单中的商品，如还需购买，请重新加入购物车。', "message:返回实际结果是->:%s" % resp['message'])