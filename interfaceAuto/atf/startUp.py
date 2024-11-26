import sys, time, interfaceAuto

from apscheduler.schedulers.blocking import BlockingScheduler

sys.path.append('../')
from interfaceAuto.atf.util.logUtil import Logger
from interfaceAuto.atf.util.mail import Email
import interfaceAuto.atf as atf
import interfaceAuto.atf.cases
import requests,os

def start(whichCasePath, testCasePattern):
    defaultTestLoader = interfaceAuto.atf.MyTestLoader()
    BeautifulReport = interfaceAuto.atf.MyBeautifulReport
    reportPath = atf.templatePath  # 获取测试报告路径
    casePath = atf.projectPath + whichCasePath  # 测试用例路径
    templatePath = atf.templatePath  # 获取测试报告模板路径
    interfaceAuto.atf.cases.skip = True  # 标记所有用例是否跳过
    # interfaceAuto.atf.cases.skip = False  # 标记所有用例是否跳过

    ##开始测试
    begin_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    Logger().info("--------------" + begin_time + "测试开始" + "--------------")
    report_date = ''.join(list(begin_time)[0:10])

    # 统计所有的case
    test_suite = defaultTestLoader.discover(casePath, pattern=testCasePattern + '.py')

    # 开始执行，并以开始执行的时间命名，生成指定的测试报告
    filename = begin_time + '测试报告.html'
    atf.filename = filename
    result = BeautifulReport(test_suite)
    # 执行结果汇总
    result_summary = result.fields


    result.report(filename=filename, description='测试deafult报告', report_dir=templatePath, theme='theme_default')

    requests.packages.urllib3.disable_warnings()

    url = "https://jkp.baiyaodajiankang.com/mis/test/api/admin/v1/oss/upload"
    case_path = ""
    env = ''
    print(env)
    if atf.env == 'test':
        env = 'sit'
    else:
        env = 'dev'
    if whichCasePath=="/cases/appCases":
        case_path = "app"
    elif whichCasePath=="/cases/apph5Cases":
        case_path = "xyx"
    payload = {'fileName': 'auto-test/htmlReport/%s/%s/%s/%s'%(case_path,env,report_date,filename),
               'isAsync': 'true'}
    file = os.path.join(templatePath, filename)
    files = [
        ('file', (filename, open(file, 'rb'),
                  'text/html'))
    ]

    requests.post(url, data=payload, files=files, verify=False)

    pass_rate = format(result_summary['testPass'] / result_summary['testAll'], '.2%')


    # 调用mail()发送生成的html文件
    mail_file = reportPath + '/' + filename
    # 如果skip = False时候执行 跳过用例为0
    if (result_summary['testSkip'] == 0):
        Email().send_email(mail_file, filename, pass_rate, result_summary['totalTime'], result_summary['testAll']-result_summary['testSkip'],
                           result_summary['testPass'], result_summary['testFail'], result_summary['testError'],
                           0)
    # 如果skip = True时候执行 跳过用例不为0
    else:
        pass_rate = result_summary['testPass'] / (result_summary['testAll'] - result_summary['testSkip'])
        pass_rate_Skip = "%.2f%%" % (pass_rate * 100)
        Email().send_email(mail_file, filename, pass_rate_Skip, result_summary['totalTime'], result_summary['testAll'],
                           result_summary['testPass'], result_summary['testFail'], result_summary['testError'],
                           result_summary['testSkip'])

    # 执行结束
    end_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    Logger().info("---------------" + end_time + "测试结束---------------")
    time.sleep(5)

    # 返回是否生成测试报告，0否，1是
    # if (result_summary['testFail'] == 0 and result_summary['testError'] == 0):
    #     return 0
    # else:
    #     return
