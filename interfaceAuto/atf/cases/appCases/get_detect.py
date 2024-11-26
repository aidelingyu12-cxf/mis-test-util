import json
import unittest
from interfaceAuto.atf.cases import Logger, cr, req, skip
from interfaceAuto import atf
## 报告页接口
class get_detect(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Logger.info('----------检测模块测试开始!----------')
        # self.dataMap = cr.getInterfaceCollections('APPInterfaceFile', 'detect','interfaceAuto')  # 获取接口集
        # print(self.dataMap)
        # 读取yml文件
        if atf.env == 'test':
            self.ymlContent = cr.readYaml(file='test_detect.yml', project='interfaceAuto')
        elif atf.env == 'dev':
            self.ymlContent = cr.readYaml(file='dev_detect.yml', project='interfaceAuto')

    @classmethod
    def tearDownClass(self):
        Logger.info('----------检测模块测试结束!----------')


    # 打开检测引导
    def test_GetDailyCareTip(self):
        '''打开检测引导'''
        uri = '/skin/detection/guide'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertIsNotNone(resp['data']['id'], "message:mis检测引导接口错误")
        self.assertEqual(resp['message'], '查询成功', "message:返回实际结果是->:%s" % resp['message'])


    # 是否已经查看过检测引导视频
    def test_getWatchGuideVideoStatus(self):
        '''是否已经查看过检测引导视频'''
        uri = '/skin/detection/get_watch_guide_video_status'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        if(resp['data']['watchGuideVideoStatus'] == '1'):
            self.assertEqual(resp['data']['watchGuideVideoStatus'], '1', "watchGuideVideoStatus:返回实际结果是->:%s" % resp['data']['watchGuideVideoStatus'])
        if (resp['data']['watchGuideVideoStatus'] == '0'):
            self.assertEqual(resp['data']['watchGuideVideoStatus'], '0', "watchGuideVideoStatus:返回实际结果是->:%s" % resp['data']['watchGuideVideoStatus'])

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
        self.assertGreaterEqual(len(resp['data']['couponIdList']), 1)
        self.assertGreaterEqual(len(resp['data']['couponNameList']), 1)
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
        self.assertGreaterEqual((len(json.loads(resp['data']['surveyDefinition'])['question_list'])), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])


    # 开始填写新问卷
    def test_questionaireAnswer(self):
        '''开始填写新问卷'''
        uri = '/questionaire/answer'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['contents']), 1)
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
        self.assertGreaterEqual(len(resp['data']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 获取指定肌肤档案
    def test_reportBanner(self):
        '''获取指定肌肤档案'''
        uri = '/activities/report_banner'
        resp = req.getResp(uri=uri, project='interfaceAuto', yml_content=self.ymlContent)
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
        self.assertTrue(resp['data'])
        self.assertGreaterEqual(len(resp['data']['symptomScores']), 1)
        self.assertGreaterEqual(len(resp['data']['riskAssessments']), 1)
        self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])

    # 报告页查询MIS套餐
    def test_getMisPackage703(self):
        '''报告页查询MIS套餐'''
        uri = '/package/by_skin_type_code'
        resp = req.getResp(uri=uri, project='interfaceAuto',yml_content=self.ymlContent)
        print(resp)
        if (resp['code'] == '00000'):
            self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
            self.assertTrue(resp['data'])
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
        self.assertGreaterEqual(len(resp['data']), 1)
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

    # # 肌肤档案列表
    # # 7.19更新
    # def test_skincaremembermobilesolutionreportphase4_list(self):
    #     '''肌肤档案列表'''
    #     uri = '/skin/care/member/mobile/solution/report/phase4_list'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 报告详情
    # # 7.19更新
    # def test_skincaremembermobilesolutionreportphase4_detail(self):
    #     '''报告详情'''
    #     uri = '/skin/care/member/mobile/solution/report/phase4_detail'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 报告详情2
    # # 7.19更新
    # def test_skinrecords_head_image_phase4(self):
    #     '''报告详情2'''
    #     uri = '/skin/records_head_image_phase4'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 定制方案查询商品
    # # 7.19更新
    # def test_customizedtaskgoodslistBySkuIds(self):
    #     '''定制方案查询商品'''
    #     uri = '/customized/task/goods/listBySkuIds'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 护肤推荐查询商品
    # # 7.19更新
    # def test_customizedtaskgoodslistByTaskId(self):
    #     '''护肤推荐查询商品'''
    #     uri = '/customized/task/goods/listByTaskId'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '当前肌肤分型没有对应的healthy_muscle商品', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 根据taskId查询购物车商品
    # # 7.19更新
    # def test_customizedtaskgoodscartListByTaskId(self):
    #     '''根据taskId查询购物车商品'''
    #     uri = '/customized/task/goods/cartListByTaskId'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertTrue(resp['data'])
    #     self.assertEqual(resp['message'], '', "message:返回实际结果是->:%s" % resp['message'])
    #
    # # 保存商品到购物车
    # # 7.19更新
    # def test_customizedtaskgoodssavecartList(self):
    #     '''保存商品到购物车'''
    #     uri = '/customized/task/goods/save/cartList'
    #     resp = req.getResp(uri=uri, project='app',yml_content=self.ymlContent)
    #     print(resp)
    #     self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    #     self.assertIsNone(resp['data'], "message:保存商品到购物车错误")
    #     self.assertEqual(resp['message'], '购物车修改成功', "message:返回实际结果是->:%s" % resp['message'])