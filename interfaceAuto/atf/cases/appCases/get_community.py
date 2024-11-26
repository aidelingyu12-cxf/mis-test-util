import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from interfaceAuto import atf

class get_community(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        Logger.info('----------社区模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'community','interfaceAuto') # 获取接口集
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_community.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_community.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(cls):
        Logger.info('----------社区模块测试结束!----------')

    # 文章详情
    def test_articledetail(self):
        '''文章详情'''
        if atf.env == 'test':
            uri = '/article/detail/6ddc9607'
        elif atf.env == 'dev':
            uri = '/article/detail/04b0f1eb'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertIsNotNone(resp['data']['articleDetail']['id'])
            self.assertEqual(resp['message'], "success", "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '2000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
            self.assertEqual(resp['message'], '重复提交信息', "message:返回实际结果是->:%s" % resp['message'])

    # 文章点赞/取消点赞
    # 待定
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_communityblogslike(self):
        '''文章点赞/取消点赞'''
        if atf.env == 'test':
            uri = '/community/blogs/6ddc9607/like'
        elif atf.env == 'dev':
            uri = '/community/blogs/04b0f1eb/like'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertEqual(resp['current1']['message'], "success", "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertEqual(resp['current2']['message'], "success", "message:返回实际结果是->:%s" % resp['current2']['message'])

    # app首页和定制之旅
    # 7.5更新
    def test_articlegetAppHomeList(self):
        '''app首页和定制之旅'''
        uri = '/article/getAppHomeList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertTrue(isinstance(resp['current1']['data']['records'], list))  # 判断是否是数组list
        self.assertEqual(resp['current1']['message'], None, "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertTrue(resp['current2']['data'])
        self.assertTrue(isinstance(resp['current1']['data']['records'], list))
        self.assertEqual(resp['current2']['message'], None, "message:返回实际结果是->:%s" % resp['current2']['message'])
        self.assertEqual(resp['current3']['code'], '00000', "code:返回实际结果是->:%s" % resp['current3']['code'])
        self.assertTrue(resp['current3']['data'])
        self.assertTrue(isinstance(resp['current1']['data']['records'], list))
        self.assertEqual(resp['current3']['message'], None, "message:返回实际结果是->:%s" % resp['current3']['message'])
        self.assertEqual(resp['current4']['code'], '00000', "code:返回实际结果是->:%s" % resp['current4']['code'])
        self.assertTrue(resp['current4']['data'])
        self.assertTrue(isinstance(resp['current1']['data']['records'], list))
        self.assertEqual(resp['current4']['message'], None, "message:返回实际结果是->:%s" % resp['current4']['message'])
        self.assertEqual(resp['current5']['code'], '00000', "code:返回实际结果是->:%s" % resp['current5']['code'])
        self.assertTrue(resp['current5']['data'])
        self.assertTrue(isinstance(resp['current1']['data']['records'], list))
        self.assertEqual(resp['current5']['message'], None, "message:返回实际结果是->:%s" % resp['current5']['message'])

    # 探索发现/综合热搜
    # 7.6更新
    def test_articlegetHotSearchList(self):
        '''探索发现/综合热搜'''
        uri = '/article/getHotSearchList'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['current1']['code'], '00000', "code:返回实际结果是->:%s" % resp['current1']['code'])
        self.assertTrue(resp['current1']['data'])
        self.assertTrue(isinstance(resp['current1']['data'], list))# 判断是否是数组list
        self.assertGreaterEqual(len(resp['current1']['data']), 0)# 判断这个list个数大于0
        self.assertEqual(resp['current1']['message'], None, "message:返回实际结果是->:%s" % resp['current1']['message'])
        self.assertEqual(resp['current2']['code'], '00000', "code:返回实际结果是->:%s" % resp['current2']['code'])
        self.assertEqual(resp['current2']['message'], None, "message:返回实际结果是->:%s" % resp['current2']['message'])

    # 文章详情
    # 7.5更新
    def test_articledetails(self):
        '''文章详情'''
        if atf.env == 'test':
            uri = '/article/detail/bc3299f3b2bc98b5e894e3b771b43a75'
        elif atf.env == 'dev':
            uri = '/article/detail/6848a5d3d8effc36bd5887224fd86060'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], "success", "message:返回实际结果是->:%s" % resp['message'])

    # 阅读量修改
    # 7.5更新
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_articleaddReadNume(self):
        '''阅读量修改'''
        if atf.env == 'test':
            uri = '/article/addReadNum/c88493a6'
        elif atf.env == 'dev':
            uri = '/article/addReadNum/04b0f1eb'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:阅读量修改错误")
        self.assertEqual(resp['message'], "阅读量修改成功", "message:返回实际结果是->:%s" % resp['message'])