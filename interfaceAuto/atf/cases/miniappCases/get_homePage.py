# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 16:02
# @Author  : 焦海俊
# @File    : get_homePage.py
# @Software: PyCharm
import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from interfaceAuto import atf


class GetHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info(msg='----------小程序首页模块测试开始!----------')
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_homepage.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_homepage.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(self):
        Logger.info('----------小程序首页模块测试结束!----------')


    # 打开检测引导
    def test_GetDailyCareTip(self):
        '''打开检测引导'''
        uri = '/skin/detection/guide'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '查询成功', "message:返回实际结果是->:%s" % resp['message'])


    # 是否已经查看过检测引导视频
    def test_getWatchGuideVideoStatus(self):
        '''是否已经查看过检测引导视频'''
        uri = '/skin/detection/get_watch_guide_video_status'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        if(resp['data']['watchGuideVideoStatus'] == '1'):
            self.assertEqual(resp['data']['watchGuideVideoStatus'], '1', "watchGuideVideoStatus:返回实际结果是->:%s" % resp['data']['watchGuideVideoStatus'])
        if (resp['data']['watchGuideVideoStatus'] == '0'):
            self.assertEqual(resp['data']['watchGuideVideoStatus'], '0',"watchGuideVideoStatus:返回实际结果是->:%s" % resp['data']['watchGuideVideoStatus'])

    # @unittest.skipIf(skip == True, 'POST请求跳过')
    # # 第一次检测查看视频引导
    # def test_updateWatchGuideVideoStatus(self):
    #     '''是否第一次检测引导视频'''
    #     uri = '/skin/detection/update_watch_guide_video_status'
    #     resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 查询会员信息
    def test_accountcustomerinfo(self):
        '''查询会员信息'''
        uri = '/account/customer_info'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 开始检测前验证是否有已填写的报告
    def test_haveValidQuestionaire(self):
        '''开始检测前验证是否有已填写的报告'''
        uri = '/questionaire/have_valid_questionaire'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
        if(resp['data']['hadValidSurvey'] == 'Y'):
            self.assertEqual(resp['data']['hadValidSurvey'], 'Y', "hadValidSurvey:返回实际结果是->:%s" % resp['data']['hadValidSurvey'])
        if(resp['data']['hadValidSurvey'] == 'N'):
            self.assertEqual(resp['data']['hadValidSurvey'], 'N', "hadValidSurvey:返回实际结果是->:%s" % resp['data']['hadValidSurvey'])

    # 获取问卷模板
    def test_questionaireTemplate(self):
        '''获取问卷模板'''
        uri = '/questionaire/template'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])


    # 开始填写新问卷
    def test_questionaireAnswer(self):
        '''开始填写新问卷'''
        uri = '/questionaire/answer'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 提交问卷
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_questionaire(self):
        '''提交问卷'''
        uri = '/questionaire'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:提交问卷错误")
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])


    # 查看肌肤档案列表
    def test_reportList(self):
        '''查看肌肤档案列表'''
        uri = '/skin/care/member/mobile/solution/report/list'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取指定肌肤档案
    def test_reportBanner(self):
        '''获取指定肌肤档案'''
        uri = '/activities/report_banner'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data'], None, "message:返回实际结果是->:%s" % resp['message'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取指定肌肤档案详情
    def test_getReportDetail(self):
        '''获取指定肌肤档案详情'''
        uri = '/skin/care/member/mobile/solution/report/detail'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data'], None, "message:返回实际结果是->:%s" % resp['message'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取703部分MIS套餐信息
    def test_getMisPackage703(self):
        '''获取703部分MIS套餐信息'''
        uri = '/package/by_skin_type_code'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:获取703部分MIS套餐信息错误")
            self.assertEqual(resp['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == '20000'):
            self.assertEqual(resp['code'], '20000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:获取703部分MIS套餐信息错误")
            self.assertEqual(resp['message'], "未查询到对应商品", "message:返回实际结果是->:%s" % resp['message'])

    # 查询用户肌肤图片
    def test_recordsHeadImage(self):
        '''查询用户肌肤图片'''
        uri = '/skin/records_head_image'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 报告页Banner配置
    def test_getActivitiesNew_activity(self):
        '''报告页Banner配置'''
        uri = '/activities/new_activity'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNone(resp['data'], "message:报告页Banner配置错误")
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 报告页活动页面配置
    def test_getActivitiesNewactivity(self):
        '''报告页活动页面配置'''
        uri = '/new_activities/detail'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:报告页活动页面配置错误")
            self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == 'APP017'):
            self.assertEqual(resp['code'], 'APP017', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:报告页活动页面配置错误")
            self.assertEqual(resp['message'], '活动已过期！', "message:返回实际结果是->:%s" % resp['message'])

    # 新活动检查
    def test_getNewactivitiesCheck(self):
        '''新活动检查'''
        uri = '/new_activities/check'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:新活动检查错误")
            self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == 'APP017'):
            self.assertEqual(resp['code'], 'APP017', "code:返回实际结果是->:%s" % resp['code'])
            self.assertIsNone(resp['data'], "message:新活动检查错误")
            self.assertEqual(resp['message'], '活动已过期！', "message:返回实际结果是->:%s" % resp['message'])