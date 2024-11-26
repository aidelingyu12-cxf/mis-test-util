import unittest
from interfaceAuto.atf.cases import Logger, cr, req
from parameterized import parameterized
import json, yaml
import platform
from interfaceAuto import atf

class post_postMethod(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        Logger.info('----------社区模块测试开始!----------')

        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent_community = cr.readYaml(file='test_community.yml', project='interfaceAuto')
            self.ymlContent_detect = cr.readYaml(file='test_detect.yml', project='interfaceAuto')
            self.ymlContent_login = cr.readYaml(file='test_login.yml', project='interfaceAuto')
            self.ymlContent_mine = cr.readYaml(file='test_mine.yml', project='interfaceAuto')
            self.ymlContent_pointsMall = cr.readYaml(file='test_pointsMall.yml', project='interfaceAuto')
            self.ymlContent_popup = cr.readYaml(file='test_popup.yml', project='interfaceAuto')
            self.ymlContent_shop = cr.readYaml(file='test_shop.yml', project='interfaceAuto')
            self.ymlContent_shopscene = cr.readYaml(file='test_shopscene.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent_community = cr.readYaml(file='dev_community.yml', project='interfaceAuto')
            self.ymlContent_detect = cr.readYaml(file='dev_detect.yml', project='interfaceAuto')
            self.ymlContent_login = cr.readYaml(file='dev_login.yml', project='interfaceAuto')
            self.ymlContent_mine = cr.readYaml(file='dev_mine.yml', project='interfaceAuto')
            self.ymlContent_pointsMall = cr.readYaml(file='dev_pointsMall.yml', project='interfaceAuto')
            self.ymlContent_popup = cr.readYaml(file='dev_popup.yml', project='interfaceAuto')
            self.ymlContent_shop = cr.readYaml(file='dev_shop.yml', project='interfaceAuto')
            self.ymlContent_shopscene = cr.readYaml(file='dev_shopscene.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(cls):
        Logger.info('----------社区模块测试结束!----------')

    # 社区点赞/取消点赞
    def test_CommunityBlogsLikeOrUnlike(self):
        '''文章点赞/取消点赞'''
        if atf.env == 'test':
            uri = '/community/blogs/6ddc9607/like'
        elif atf.env == 'dev':
            uri = '/community/blogs/04b0f1eb/like'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_community)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertEqual(resp['current1']['message'], "success", "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertEqual(resp['current2']['message'], "success", "message:返回实际结果是->:%s" % resp['current2']['message'])

    def test_articleReadNum(self):
        '''阅读量修改'''
        if atf.env == 'test':
            uri = '/article/addReadNum/c88493a6'
        elif atf.env == 'dev':
            uri = '/article/addReadNum/04b0f1eb'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_community)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:阅读量修改错误")
        self.assertEqual(resp['message'], "阅读量修改成功", "message:返回实际结果是->:%s" % resp['message'])

    # 提交问卷
    def test_questionaire(self):
        '''提交问卷'''
        uri = '/questionaire'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent_detect)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:提交问卷错误")
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 使用密码登录
    def test_loginOrRegister(self):
        '''使用密码登录'''
        uri = '/account/login_or_register'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_login)
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
    # def test_verificationcode(self):
    #     '''发送短信验证码'''
    #     uri = '/sms/verification_code/17766008328'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent_login)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertEqual(resp['message'], 'OK', "message:返回实际结果是->:%s" % resp['message'])

    # 问题反馈
    def test_getFeedBack(self):
        '''问题反馈'''
        uri = '/account/feedback'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '提交成功', "message:返回实际结果是->:%s" % resp['message'])

    # 更新用户生日与性别信息
    def test_editBirthAndGender(self):
        '''更新用户生日与性别信息'''
        uri = '/account/update_birth_and_gender'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        self.assertEqual(resp['MALE']['code'], '00000', "code:返回实际结果是->:%s" % resp['MALE']['code'])
        self.assertIsNone(resp['MALE']['data'], "message:修改出生日期和性别错误")
        self.assertEqual(resp['MALE']['message'], '保存成功', "message:返回实际结果是->:%s" % resp['MALE']['message'])
        if (resp['FEMALE']['code'] == '00000'):
            self.assertEqual(resp['FEMALE']['code'], '00000', "code':返回实际结果是->:%s" % resp['FEMALE']['code'])
            self.assertIsNone(resp['FEMALE']['data'], "message:修改出生日期和性别错误")
            self.assertEqual(resp['FEMALE']['message'], '保存成功', "message:返回实际结果是->:%s" % resp['FEMALE']['message'])
        if (resp['FEMALE']['code'] == 2000):
            self.assertEqual(resp['FEMALE']['code'], 2000, "code':返回实际结果是->:%s" % resp['FEMALE']['code'])
            self.assertIsNone(resp['FEMALE']['data'], "message:修改出生日期和性别错误")
            self.assertEqual(resp['FEMALE']['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['FEMALE']['message'])

    # 修改用户昵称
    @parameterized.expand([
        ['nick_name', '自动化账号']
    ])
    def test_updateNickname(self, desc, expect):
        '''修改用户昵称'''
        uri = '/account/update_nickname'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], "", "message:返回实际结果是->:%s" % resp['message'])
        self.assertEqual(resp['data']['nick_name'], '自动化账号', "nick_name:返回实际结果是->:%s" % resp['data']['nick_name'])

    # 新增收货地址
    def test_addAddressList(self):
        '''新增收货地址'''
        uri = '/customer/address_list/add'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        post_postMethod.addressId = resp['data']['addressId']
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "新增收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 新增默认收货地址
    def test_addDefaultAddressList(self):
        '''新增默认收货地址'''
        if atf.env == 'test':
            uri = '/customer/default_address/ff808081815ad99301815c41bc850005'
        if atf.env == 'dev':
            uri = '/customer/default_address/ff808081820215e10182142f2c60007c'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:新增默认收货地址错误")
        self.assertEqual(resp['message'], "新增默认收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 编辑收货地址
    def test_editAddressList(self):
        '''编辑收货地址'''
        uri = '/customer/address_list/edit'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data']['name'], "自动化账号", "name:返回实际结果是->:%s" % resp['data']['name'])
        self.assertEqual(resp['message'], "修改收货地址成功！", "message:返回实际结果是->:%s" % resp['message'])

    # 删除收货地址
    def test_deleteAddressList(self):
        '''删除收货地址'''
        print(post_postMethod.addressId)
        uri = '/customer/address_list/delete/'
        uri_new = uri + post_postMethod.addressId
        self.ymlContent_mine[uri_new] = self.ymlContent_mine.pop(uri)
        resp = req.getResp(uri=uri_new, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:删除收货地址错误")
        self.assertEqual(resp['message'], '删除收货地址成功！', "message:返回实际结果是->:%s" % resp['message'])

    # 购买会员卡功能
    def test_vipCardsingleBuy(self):
        '''购买会员卡功能'''
        uri = '/vipCard/singleBuy'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
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
    def test_giftbagconfirmReceive(self):
        '''领取M+购卡礼包'''
        uri = '/giftbag/confirmReceive'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], '礼包领取成功', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:领取M+购卡礼包错误")
            if atf.env == 'test':
                self.assertEqual(resp['message'], '当前无可领取礼包', "message:返回实际结果是->:%s" % resp['message'])
            elif atf.env == 'dev':
                self.assertEqual(resp['message'], '礼包记录数有误', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 首页弹窗
    # def test_getSplashAdvShow(self):
    #     '''首页弹窗'''
    #     uri = '/splashAdv/show'
    #     resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertIsNone(resp['data'], "message:屏广告查询接口（手机端）错误")
    #     self.assertEqual(resp['message'], '', "code:返回实际结果是->:%s" % resp['message'])

    # # 领取优惠卷
    # # 7.7更新
    # def test_coupongrantQuarterCoupon(self):
    #     '''领取优惠卷'''
    #     uri = '/coupon/grantQuarterCoupon'
    #     resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_mine)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '领取成功', "message:返回实际结果是->:%s" % resp['message'])

    # 商品加入购物车
    def test_addGoodToCart(self):
        '''商品加入购物车'''
        uri = '/site/shop/cart/add'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:商品加入购物车错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 编辑购物车商品
    def test_siteshopcartedit(self):
        '''编辑购物车商品'''
        uri = '/site/shop/cart/edit'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:编辑购物车商品错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 购物车结算
    def test_confirmShoppingCart(self):
        '''购物车结算'''
        uri = '/trade/confirm_shopping_cart'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
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
    def test_removeFromCart(self):
        '''删除购物车商品'''
        uri = '/site/shop/cart/remove'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:删除购物车商品错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 预购买
    def test_preCommit(self):
        '''预购买'''
        uri = '/trade/purchase/preCommit'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent_shopscene)
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

    # 确认商品
    def test_checkGoods(self):
        '''确认商品'''
        uri = '/trade/check_goods'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
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
    def test_immediateBuy(self):
        '''立即购买'''
        uri = '/trade/immediate_buy'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:立即购买错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '2000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:立即购买错误")
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])

    # # 女神检查优惠券是否可以领取
    # # 7.6更新
    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # def test_couponcheckCoupon(self):
    #     '''女神检查优惠券是否可以领取'''
    #     uri = '/coupon/checkCoupon'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent_shop)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], 'app优惠券领取情况查询成功', "message:返回实际结果是->:%s" % resp['message'])

    # 领取新人优惠券
    # 7.8更新
    def test_couponreceive_coupon(self):
        '''领取新人优惠券'''
        uri = '/coupon/receive_coupon'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shop)
        print(resp)
        if(resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:领取新人优惠券错误")
            self.assertEqual(resp['message'], '领取成功！', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:领取新人优惠券错误")
            self.assertEqual(resp['message'], '您已领取过新人优惠券了哦', "message:返回实际结果是->:%s" % resp['message'])

    # 积分兑换优惠卷列表
    def test_points_mallpageCoupon(self):
        '''积分兑换优惠卷列表'''
        uri = '/points_mall/pageCoupon'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_pointsMall)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['data']), 1)
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 签名
    def test_sign(self):
        '''签名'''
        uri = '/sign'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_pointsMall)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 接收任务奖励
    def test_signreceive_task_rewards(self):
        '''接收任务奖励'''
        uri = '/sign/receive_task_rewards'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_pointsMall)
        print(resp)
        self.assertEqual(resp['code'], 'APP023', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:接收任务奖励错误")
        self.assertEqual(resp['message'], '抱歉！您已经领取过该任务奖励，不可重复领取', "message:返回实际结果是->:%s" % resp['message'])

    # # 积分领取优惠卷
    # # @unittest.skipIf(skip == True, '积分兑换优惠卷')
    # def test_points_mallfetchPointsCoupon(self):
    #     '''积分领取优惠卷'''
    #     uri = '/points_mall/fetchPointsCoupon'
    #     resp = req.getResp(uri=uri, project='app', yml_content=self.ymlContent_pointsMall)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])


class post_shopscene(unittest.TestCase):
    tid = 0
    parentTid = 0
    id = 0

    @classmethod
    def setUpClass(self):
        # self.dataMap_shopscene = cr.getInterfaceCollections('APPInterfaceFile', 'shopscene','interfaceAuto')  # 获取接口集
        # 读取yml文件
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent_shopscene = cr.readYaml(file='test_shopscene.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent_shopscene = cr.readYaml(file='dev_shopscene.yml', project='interfaceAuto')


    # # 查询部分全部宝贝列表
    # def test_getGoodList(self):
    #     '''查询部分全部宝贝列表'''
    #     uri = '/goods_list'
    #     resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
    #     get_shopscene.id = resp['current1']['data']['records'][0]['id']
    #     print(resp)
    #     self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
    #     self.assertEqual(resp['current1']['data']['current'], 1, "message:返回实际结果是->:%s" % resp['current1']['data']['current'])
    #     self.assertEqual(resp['current1']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current1']['message'])
    #     self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
    #     self.assertEqual(resp['current2']['data']['current'], 2, "message:返回实际结果是->:%s" % resp['current2']['data']['current'])
    #     self.assertEqual(resp['current2']['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 搜索商品（自动化）
    def test_goods_search_result(self):
        '''搜索商品（自动化）'''
        uri = '/goods_search_result'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
        post_shopscene.id = resp['data']['records'][0]['id']
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['records']), 1)
        self.assertGreaterEqual((resp['data']['total']), 1)
        self.assertEqual(resp['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['message'])

    # 商品加入购物车
    def test_addGoodToCart(self):
        '''商品加入购物车'''
        uri = '/site/shop/cart/add'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            # 给tid值为 resp['data'][0]['tid']
            content['/site/shop/cart/add']['payload']['goodsInfoId'] = post_shopscene.id
            # 更改为有缩进json格式
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            # 给tid值为 resp['data'][0]['tid']
            content['/site/shop/cart/add']['payload']['goodsInfoId'] = post_shopscene.id
            # 更改为有缩进json格式
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent_shopscene)
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
    def test_siteshopcartedit(self):
        '''编辑购物车商品'''
        uri = '/site/shop/cart/edit'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/site/shop/cart/edit']['payload']['goodsId'] = post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/site/shop/cart/edit']['payload']['goodsId'] = post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:编辑购物车商品错误")
        self.assertEqual(resp['message'], 'SUCCESS', "message:返回实际结果是->:%s" % resp['message'])

    # 购物车结算
    def test_confirmShoppingCart(self):
        '''购物车结算'''
        uri = '/trade/confirm_shopping_cart'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/confirm_shopping_cart']['payload']['tradeItems'][0]['skuId']= post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/confirm_shopping_cart']['payload']['tradeItems'][0]['skuId']= post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
        print(resp)
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购物车结算错误")
            self.assertEqual(resp['message'], '请勿重复提交', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:购物车结算错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])

    # 预购买
    def test_preCommit(self):
        '''预购买'''
        uri = '/trade/purchase/preCommit'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent_shopscene)
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
    def test_commit(self):
        '''拉起支付'''
        uri = '/trade/commit'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent_shopscene)
        post_shopscene.tid = resp['data'][0]['tid']
        post_shopscene.parentTid = resp['data'][0]['parentTid']
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
    def test_aliPay(self):
        '''aliPay（支付宝支付）'''
        uri = '/pay/app/aliPay'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            contents = yaml.load(conf, Loader=yaml.FullLoader)
            print(post_shopscene.parentTid)
            contents['/pay/app/aliPay']['payload']['tid'] = post_shopscene.parentTid
            contents['/pay/app/aliPay']['payload']['feeCode'] = "16110100"
            contents['/pay/app/aliPay']['payload']['channelItemId'] = 19
            json_str = json.dumps(contents, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            contents = yaml.load(conf, Loader=yaml.FullLoader)
            contents['/pay/app/aliPay']['payload']['tid'] = post_shopscene.parentTid
            contents['/pay/app/aliPay']['payload']['feeCode'] = "16110100"
            contents['/pay/app/aliPay']['payload']['channelItemId'] = 19
            json_str = json.dumps(contents, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"../mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent_shopscene)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '支付宝支付成功！', "message:返回实际结果是->:%s" % resp['message'])


    # 查询支付结果
    def test_payrecordstatus(self):
        '''查询支付结果'''
        uri = '/pay/record/status/'
        uri_new = uri + post_shopscene.parentTid
        self.ymlContent_shopscene[uri_new] = self.ymlContent_shopscene.pop(uri)
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
        elif atf.env == 'dev':
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
        resp = req.getResp(uri=uri_new, project='interfaceAuto',yml_content=self.ymlContent_shopscene)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:查询支付结果")
        self.assertEqual(resp['message'], '查询支付记录状态！', "message:返回实际结果是->:%s" % resp['message'])

    # 取消订单
    def test_cancelPurchase(self):
        '''取消订单'''
        uri = '/trade/cancel'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/cancel']['params']['tid'] = post_shopscene.tid
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/cancel']['params']['tid'] = post_shopscene.tid
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
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
    def test_checkGoods(self):
        '''确认商品'''
        uri = '/trade/check_goods'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/check_goods']['payload']['tradeItems'][0]['skuId'] = post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/check_goods']['payload']['tradeItems'][0]['skuId'] = post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
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
    def test_immediateBuy(self):
        '''立即购买'''
        uri = '/trade/immediate_buy'
        if atf.env == 'test':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/immediate_buy']['payload']['tradeItemRequests'][0]['skuId'] = post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/test_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        elif atf.env == 'dev':
            if (platform.system().lower() == 'linux'):
                conf = open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            else:
                conf = open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", encoding='utf8').read()  # 配置文件内容
            content = yaml.load(conf, Loader=yaml.FullLoader)
            content['/trade/immediate_buy']['payload']['tradeItemRequests'][0]['skuId'] = post_shopscene.id
            json_str = json.dumps(content, indent=4)
            if (platform.system().lower() == 'linux'):
                with open(r"/opt/automation-test/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
            else:
                with open(r"/Users/macbook/PycharmProjects/mis-test-utils/interfaceAuto/atf/resources/requestData/appData/dev_shopscene.yml", 'w', encoding='utf8') as f:
                    f.write(json_str)
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent_shopscene)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:立即购买错误")
            self.assertEqual(resp['message'], None, "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '2000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:立即购买错误")
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])