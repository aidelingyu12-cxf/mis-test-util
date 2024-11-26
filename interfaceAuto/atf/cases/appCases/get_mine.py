import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from parameterized import parameterized
from interfaceAuto import atf

class get_mine(unittest.TestCase):
    addressId = 0

    @classmethod
    def setUpClass(self):
        Logger.info('----------我的模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'mine','interfaceAuto')  # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_mine.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_mine.yml', project='interfaceAuto')
    @classmethod
    def tearDownClass(self):
        Logger.info('----------我的模块测试结束!----------')

    # 获取我的订单信息
    def test_getPurchaseList(self):
        '''获取我的订单信息'''
        uri = '/trade/todo_num'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], 'SUCCESS', "code:返回实际结果是->:%s" % resp['message'])

    # 获取全部消息
    def test_getMessage(self):
        '''获取全部消息'''
        uri = '/in_mails/by_user'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 查询会员信息
    def test_accountcustomerinfo(self):
        '''查询会员信息'''
        uri = '/account/customer_info'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取全部未读消息
    def test_getUnreadMessage(self):
        '''获取全部未读消息'''
        uri = '/in_mails/by_user/unread'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertGreaterEqual(resp['data'], 0) # 判断data大于等于0
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 全部消息已读按钮
    def test_allRead(self):
        '''全部消息已读按钮，in_mails/by_user/all_read'''
        uri = '/in_mails/by_user/all_read'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 问题反馈
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_getFeedBack(self):
        '''问题反馈'''
        uri = '/account/feedback'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '提交成功', "message:返回实际结果是->:%s" % resp['message'])

    # 账户详情
    def test_getAccountInfo(self):
        '''账户详情'''
        uri = '/account/info'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        # self.assertEqual(resp['data']['phone_number'], '17766008328', "phone_number:返回实际结果是->:%s" % resp['data']['phone_number'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取出生日期和性别
    def test_getBirthAndGender(self):
        '''获取出生日期和性别'''
        uri = '/account/get_birth_and_gender'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertIsNotNone(resp['data']['id'], "message:获取用户信息接口错误")
        self.assertEqual(resp['message'], "查询成功", "message:返回实际结果是->:%s" % resp['message'])


    # 更新用户生日与性别信息
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_editBirthAndGender(self):
        '''更新用户生日与性别信息'''
        uri = '/account/update_birth_and_gender'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['MALE']['code'], '00000', "code:返回实际结果是->:%s" % resp['MALE']['code'])
        self.assertIsNone(resp['MALE']['data'], "message:修改出生日期和性别错误")
        self.assertEqual(resp['MALE']['message'], '保存成功',  "message:返回实际结果是->:%s" % resp['MALE']['message'])
        if(resp['FEMALE']['code'] == '00000'):
            self.assertEqual(resp['FEMALE']['code'], '00000', "code':返回实际结果是->:%s" % resp['FEMALE']['code'])
            self.assertIsNone(resp['FEMALE']['data'], "message:修改出生日期和性别错误")
            self.assertEqual(resp['FEMALE']['message'], '保存成功',  "message:返回实际结果是->:%s" % resp['FEMALE']['message'])
        if (resp['FEMALE']['code'] == 2000):
            self.assertEqual(resp['FEMALE']['code'], 2000, "code':返回实际结果是->:%s" % resp['FEMALE']['code'])
            self.assertIsNone(resp['FEMALE']['data'], "message:修改出生日期和性别错误")
            self.assertEqual(resp['FEMALE']['message'], '重复提交信息',  "message:返回实际结果是->:%s" % resp['FEMALE']['message'])

    # 修改用户昵称
    @parameterized.expand([
        ['nick_name', '自动化账号']
    ])
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_updateNickname(self, desc, expect):
        '''修改用户昵称'''
        uri = '/account/update_nickname'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])
        self.assertEqual(resp['data']['nick_name'], '自动化账号', "nick_name:返回实际结果是->:%s" % resp['data']['nick_name'])

    # @pytest.mark.skip(reason="就是不想执行而已")
    # 获取app最新版本
    def test_getAppVersion(self):
        '''获取app最新版本'''
        uri = '/app_version/latest'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['1.1.1']['code'], '00000', "code:返回实际结果是->:%s" % resp['1.1.1']['code'])
        self.assertTrue(resp['1.1.1']['data'])
        self.assertEqual(resp['1.1.1']['message'], '查询成功', "message:返回实际结果是->:%s" % resp['1.1.1']['message'])
        self.assertEqual(resp['1.0.8']['code'], '00000', "code:返回实际结果是->:%s" % resp['1.0.8']['code'])
        self.assertTrue(resp['1.0.8']['data'])
        self.assertEqual(resp['1.0.8']['message'], '查询成功', "message:返回实际结果是->:%s" % resp['1.0.8']['message'])

    # 会员权益列表
    def test_getRightlist(self):
        '''会员权益列表'''
        uri = '/customer/level/rightsList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "查询成功", "message:返回实际结果是->:%s" % resp['message'])

    # 获取积分规则
    def test_getIntegrationRules(self):
        '''获取积分规则'''
        uri = '/integration_rule/query_integration_rules'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 新增收货地址
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_addAddressList(self):
        '''新增收货地址'''
        uri = '/customer/address_list/add'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        get_mine.addressId = resp['data']['addressId']
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "新增收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 新增默认收货地址
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_customerdefault_address(self):
        '''新增默认收货地址'''
        if atf.env == 'test':
            uri = '/customer/default_address/ff808081815ad99301815c41bc850005'
        if atf.env == 'dev':
            uri = '/customer/default_address/ff808081820215e10182142f2c60007c'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:新增默认收货地址错误")
        self.assertEqual(resp['message'], "新增默认收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 获取收货地址
    def test_getAddressList(self):
        '''获取收货地址'''
        uri = '/customer/address_list'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "查询收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 编辑收货地址
    @unittest.skipIf(skip == True, 'PUT请求跳过')
    def test_editAddressList(self):
        '''编辑收货地址'''
        uri = '/customer/address_list/edit'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data']['name'], "自动化账号", "name:返回实际结果是->:%s" % resp['data']['name'])
        self.assertEqual(resp['message'], "修改收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 删除收货地址
    @unittest.skipIf(skip == True, 'DELETE请求跳过')
    def test_deleteAddressList(self):
        '''删除收货地址'''
        print(get_mine.addressId)
        uri = '/customer/address_list/delete/'
        uri_new = uri + get_mine.addressId
        self.ymlContent[uri_new] = self.ymlContent.pop(uri)
        resp = req.getResp(uri=uri_new, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:删除收货地址错误")
        self.assertEqual(resp['message'], '删除收货地址成功！', "message:返回实际结果是->:%s" % resp['message'])

    # 查询优惠券或礼品卡
    def test_getCouponList(self):
        '''查询优惠券或礼品卡'''
        uri = '/coupon/couponCode/list'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], '查询成功！', "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertIsNone(resp['current2']['data'], "message:查询优惠券或礼品卡错误")
        self.assertEqual(resp['current2']['message'], '未查到任何优惠券信息！', "message:返回实际结果是->:%s" % resp['current1']['message'])

    # 获取我的积分详情
    def test_pointsdetail(self):
        '''获取我的积分详情'''
        uri = '/customer/points/detail'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['data']), 1)
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], "查询成功！", "message:返回实际结果是->:%s" % resp['message'])

    # # 修改用户头像
    # def test_account_update_avatar(self):
    #     '''修改用户头像'''
    #     uri = '/account/update_avatar'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])

    # 会员大礼包
    def test_giftbaggiftGoodsList(self):
        '''会员大礼包'''
        uri = '/giftbag/giftGoodsList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], "查询商品信息成功", "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], "查询商品信息成功", "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 折扣商品列表
    def test_discount_goodslist(self):
        '''折扣商品列表'''
        uri = '/discount_goods/list'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], None, "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], None, "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertEqual(resp['current3']['message'], None, "message:返回实际结果是->:%s" % resp['current3']['message'])
        self.assertEqual(resp['current4']['code'], '00000', "code:返回实际结果是->:%s" % resp['current4']['code'])
        self.assertTrue(resp['current4']['data'])
        self.assertEqual(resp['current4']['message'], None, "message:返回实际结果是->:%s" % resp['current4']['message'])

    # 会员卡信息
    def test_vipCardInfo(self):
        '''会员卡信息'''
        uri = '/vipCard/Info'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "查询成功", "message:返回实际结果是->:%s" % resp['message'])

    # 会员折扣
    def test_vipdiscount_economize(self):
        '''会员折扣'''
        uri = '/vip/discount_economize'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if atf.env == 'test':
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])
        elif atf.env == 'dev':
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])

    # 会员中心广告
    def test_advertisementgetByIdmember_center_advertisement(self):
        '''会员中心广告'''
        uri = '/advertisement/getById/member_center_advertisement'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 会员累积包邮已省次数
    def test_vippackage_economize(self):
        '''会员累积包邮已省次数'''
        uri = '/vip/package_economize'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])

    # 会员权益
    def test_viprights(self):
        '''会员权益'''
        uri = '/vip/rights'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "查询成功", "message:返回实际结果是->:%s" % resp['message'])

    # 我的优惠卷列表
    def test_couponcoupon_infolist(self):
        '''我的优惠卷列表'''
        uri = '/coupon/coupon_info/list'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], None, "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], None, "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertEqual(resp['current3']['message'], None, "message:返回实际结果是->:%s" % resp['current3']['message'])
        self.assertEqual(resp['current4']['code'], '00000', "code:返回实际结果是->:%s" % resp['current4']['code'])
        self.assertTrue(resp['current4']['data'])
        self.assertEqual(resp['current4']['message'], None, "message:返回实际结果是->:%s" % resp['current4']['message'])

    # 获取订单列表
    def test_tradepage(self):
        '''获取订单列表'''
        uri = '/trade/page'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertEqual(resp['current3']['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['current3']['message'])
        self.assertEqual(resp['current4']['code'], '00000', "code:返回实际结果是->:%s" % resp['current4']['code'])
        self.assertTrue(resp['current4']['data'])
        self.assertEqual(resp['current4']['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['current4']['message'])
        self.assertEqual(resp['current5']['code'], '00000', "code:返回实际结果是->:%s" % resp['current5']['code'])
        self.assertTrue(resp['current5']['data'])
        self.assertEqual(resp['current5']['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['current5']['message'])

    # 查询M+活动介绍页
    def test_mPlusActivitygetMPlusActivity(self):
        '''查询M+活动介绍页'''
        uri = '/mPlusActivity/getMPlusActivity'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 购买会员卡功能
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_vipCardsingleBuy(self):
        '''购买会员卡功能'''
        uri = '/vipCard/singleBuy'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if(resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], "提交订单成功！", "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购买会员卡功能错误")
            self.assertEqual(resp['message'], '您已是VIP，请勿重复购买', "message:返回实际结果是->:%s" % resp['message'])

    # 领取M+购卡礼包
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_giftbagconfirmReceive(self):
        '''领取M+购卡礼包'''
        uri = '/giftbag/confirmReceive'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], '礼包领取成功', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:领取M+购卡礼包错误")
            if atf.env == 'test':
                self.assertEqual(resp['message'], '当前无可领取礼包', "message:返回实际结果是->:%s" % resp['message'])
            elif atf.env == 'dev':
                self.assertEqual(resp['message'], '礼包记录数有误', "message:返回实际结果是->:%s" % resp['message'])

    # # 折扣商品详情
    # def test_discountgoodsdetail(self):
    #     '''折扣商品详情'''
    #     uri = '/discount_goods/detail/ff8080817e0bd855017e32d6acdf0170'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 获取订单详情
    # 测试
    def test_tradedetail(self):
        '''获取订单详情'''
        uri = '/trade/detail'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 修改常居地
    # 7.6更新
    def test_accountupdatelivecity(self):
        '''修改常居地'''
        uri = '/account/update_live_city'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:修改常居地错误")
        self.assertEqual(resp['message'], '操作成功', "message:返回实际结果是->:%s" % resp['message'])

    # 优惠卷列表
    # 7.6更新
    def test_couponquarterCouponList(self):
        '''优惠卷列表'''
        uri = '/coupon/quarterCouponList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertEqual(resp['current1']['message'], "查询季度优惠券信息成功", "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertEqual(resp['current2']['message'], "查询季度优惠券信息成功", "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertEqual(resp['current3']['message'], "查询季度优惠券信息成功", "message:返回实际结果是->:%s" % resp['current3']['message'])

    # 查询是否是创客
    # 7.6更新
    def test_accountmaker_info(self):
        '''查询是否是创客'''
        uri = '/account/maker_info'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 成长值明细
    # 7.7更新
    def test_growthValuepage(self):
        '''成长值明细'''
        uri = '/growthValue/page'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '查询成功', "message:返回实际结果是->:%s" % resp['message'])


    # # 领取优惠卷
    # # 7.7更新
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_coupongrantQuarterCoupon(self):
    #     '''领取优惠卷'''
    #     uri = '/coupon/grantQuarterCoupon'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '领取成功', "message:返回实际结果是->:%s" % resp['message'])

    # 查询活动信息列表
    # 7.7更新
    def test_integralactivitylist(self):
        '''查询活动信息列表'''
        uri = '/integral/activity/list'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '查询活动信息列表成功', "message:返回实际结果是->:%s" % resp['message'])