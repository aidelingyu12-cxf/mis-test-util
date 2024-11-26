import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip

## 报告页接口
class detect(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------检测模块测试开始!----------')
        self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'test')  # 获取接口集

    @classmethod
    def tearDownClass(self):
        Logger.info('----------检测模块测试结束!----------')


    # 打开检测引导
    def test_GetDailyCareTip(self):
        '''打开检测引导'''
        uri = '/skin/detection/guide'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '查询成功', "message:返回实际结果是->:%s" % resp['message'])


    # 是否已经查看过检测引导视频
    def test_getWatchGuideVideoStatus(self):
        '''是否已经查看过检测引导视频'''
        uri = '/skin/detection/get_watch_guide_video_status'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        if(resp['data']['watchGuideVideoStatus'] == '1'):
            self.assertEqual(resp['data']['watchGuideVideoStatus'], '1', "watchGuideVideoStatus:返回实际结果是->:%s" % resp['data']['watchGuideVideoStatus'])
        if (resp['data']['watchGuideVideoStatus'] == '0'):
            self.assertEqual(resp['data']['watchGuideVideoStatus'], '0',"watchGuideVideoStatus:返回实际结果是->:%s" % resp['data']['watchGuideVideoStatus'])

    # 开始检测前验证是否有已填写的报告
    def test_haveValidQuestionaire(self):
        '''开始检测前验证是否有已填写的报告'''
        uri = '/questionaire/have_valid_questionaire'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
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
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data']['surveyName'], '敏感肌肤问卷', "surveyName:返回实际结果是->:%s" % resp['data']['surveyName'])


    # 开始填写新问卷
    def test_questionaireAnswer(self):
        '''开始填写新问卷'''
        uri = '/questionaire/answer'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data']['score'], None, "score:返回实际结果是->:%s" % resp['data']['score'])

    # 提交问卷
    @unittest.skipIf(skip == True, 'POST请求跳过')
    def test_questionaire(self):
        '''提交问卷'''
        uri = '/questionaire'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data'], None, "data:返回实际结果是->:%s" % resp['data'])


    # 查看肌肤档案列表
    def test_reportList(self):
        '''查看肌肤档案列表'''
        uri = '/skin/care/member/mobile/solution/report/list'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取指定肌肤档案
    def test_reportBanner(self):
        '''获取指定肌肤档案'''
        uri = '/activities/report_banner'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data'], None, "data:返回实际结果是->:%s" % resp['data'])

    # 获取指定肌肤档案详情
    def test_getReportDetail(self):
        '''获取指定肌肤档案详情'''
        uri = '/skin/care/member/mobile/solution/report/detail'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])

    # 获取703部分MIS套餐信息
    def test_getMisPackage702(self):
        '''获取702部分MIS套餐信息'''
        uri = '/package/by_skin_type_code'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['data'], "ff8080817d98e058017d9da750a60220", "data:返回实际结果是->:%s" % resp['data'])
        self.assertEqual(resp['message'], "SUCCESS", "message:返回实际结果是->:%s" % resp['message'])

    # 查询用户肌肤图片
    def test_recordsHeadImage(self):
        '''查询用户肌肤图片'''
        uri = '/skin/records_head_image'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 报告页Banner配置
    def test_getActivitiesNew_activity(self):
        '''报告页Banner配置'''
        uri = '/activities/new_activity'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 报告页活动页面配置
    def test_getActivitiesNewactivity(self):
        '''报告页活动页面配置'''
        uri = '/new_activities/detail'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
        if (resp['code'] == 'APP017'):
            self.assertEqual(resp['code'], 'APP017', "code:返回实际结果是->:%s" % resp['code'])
            self.assertEqual(resp['message'], '活动已过期！', "message:返回实际结果是->:%s" % resp['message'])

    # 新活动检查
    def test_getNewactivitiesCheck(self):
        '''新活动检查'''
        uri = '/new_activities/check'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])