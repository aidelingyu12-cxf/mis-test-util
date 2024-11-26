import unittest
from interfaceAuto.atf.cases import Logger, cr, req

class get_h5(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------小游戏模块测试开始!----------')
        self.dataMap_h5 = cr.getInterfaceCollections('h5InterfaceFile', 'h5','h5')  # 获取接口

    @classmethod
    def tearDownClass(self):
        Logger.info('----------小游戏模块测试结束!----------')

    # 进入百草园
    def test_getH5HTML(self):
        '''进入百草园'''
        url = 'https://cdn-h5.caizhiji.com.cn/baicaoyuan/user/index.html'
        result = req.getResp(dataMap=self.dataMap_h5, url=url,project='h5')
        resp = result[0:15]
        print(resp)
        self.assertEqual(resp, '<!DOCTYPE html>', "resp:返回实际结果是->:%s" % resp)

    # 获取收获CSS样式
    def test_getH5assetsCSS(self):
        '''获取收获CSS样式'''
        url = 'https://cdn-h5.caizhiji.com.cn/baicaoyuan/user/static/js/chunk-187538bd.1644997981763.js'
        result = req.getResp(dataMap=self.dataMap_h5, url=url,project='h5')
        resp = result[0:7]
        print(resp)
        self.assertEqual(resp, '(window', "resp:返回实际结果是->:%s" % resp)

    # 查询首页信息
    def test_getH5configINFO(self):
        '''首页信息'''
        uri = '/config/profile'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])

    #查询用户数据
    def test_getH5memberINFO(self):
        '''查询用户数据'''
        uri = '/member/profile'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['content'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 404, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])

    # 查询奖品兑换列表
    def test_getH5prizeLIST(self):
        '''查询奖品兑换列表'''
        uri = '/prize/list'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['content'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 404, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])

    # 查询我的兑换列表
    def test_getH5grassLIST(self):
        '''查询我的兑换列表'''
        uri = '/grass/list'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 404, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['success'])

    # 查询获取甘露信息
    def test_getH5signLIST(self):
        '''查询获取甘露信息'''
        uri = '/sign/list'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['content'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 404, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])