import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from parameterized import parameterized
import time
import json, yaml
import platform, requests


class post_postMethod(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        Logger.info('----------小游戏模块测试开始!----------')
        self.dataMap_h5 = cr.getInterfaceCollections('h5InterfaceFile', 'h5', 'h5')  # 获取接口

    @classmethod
    def tearDownClass(cls):
        Logger.info('----------小游戏测试结束!----------')


    # 小游戏登录
    def test_h5login(self):
        '''小游戏登录'''
        uri = '/login'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['success'], True, "data:返回实际结果是->:%s" % resp['success'])

    # 小游戏浇水
    def test_h5grasswater(self):
        '''小游戏'''
        uri = '/grass/water'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['success'], True, "data:返回实际结果是->:%s" % resp['success'])

    # 获取任务列表
    def test_h5missionLIST(self):
        '''获取任务列表'''
        uri = '/mission/integral/list'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['success'], True, "data:返回实际结果是->:%s" % resp['content'])

    # 签到
    def test_h5sign(self):
        '''签到'''
        uri = '/sign'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['content'])
        if resp['code'] == 10002:
            self.assertEqual(resp['code'], 10002, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])

    # 分享提交
    def test_h5sharesubmit(self):
        '''分享提交'''
        uri = '/share/submit'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 404, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['success'])

    # 分享完成
    def test_h5sharecomplete(self):
        '''分享完成'''
        uri = '/share/complete'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 404, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['success'])

    # 领取福袋
    def test_h5luckbagACCEPT(self):
        '''领取福袋'''
        uri = '/mission/luck/bag/accept'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] == 20003:
            self.assertEqual(resp['code'], 20003, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['errMsg'])

    # 阳光值任务
    def test_h5sunshineLIST(self):
        '''阳光值任务'''
        uri = '/mission/sunshine/list'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['content'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 2003, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])

    # 选择种子
    def test_h5grassCHOOSE(self):
        '''选择种子'''
        uri = '/grass/choose'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] == 10001:
            self.assertEqual(resp['code'], 10001, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['errMsg'])

    # 选择种子
    def test_h5acceptGift(self):
        '''领取种子'''
        uri = '/member/accept/noviceGift'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 500, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])

    # 任务通知
    def test_h5missionNOTICE(self):
        '''任务通知'''
        uri = '/mission/complete/game/notice'
        resp = req.getResp(dataMap=self.dataMap_h5, uri=uri,project='h5')
        print(resp)
        if resp['code'] == 200:
            self.assertEqual(resp['code'], 200, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], True, "message:返回实际结果是->:%s" % resp['success'])
        if resp['code'] != 200:
            self.assertEqual(resp['code'], 500, "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['success'], False, "message:返回实际结果是->:%s" % resp['content'])