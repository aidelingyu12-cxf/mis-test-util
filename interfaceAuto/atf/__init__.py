import unittest, traceback, os, sys
from BeautifulReport import BeautifulReport
import json

projectPath = os.path.dirname(__file__)       # 工程主路径
reportPath = projectPath + "/resources/report"         # 测试报告路径
templatePath = os.path.split(os.path.split(projectPath)[0])[0] + '/templates/'
#casePath = projectPath + "/cases"         # 测试用例路径
#configFilePath = projectPath + "/resources/dev_conf.yml"        #配置文件路径
successReport = templatePath + 'successModel.html'
filename = ""
env = ''


##修改TestLoader使用例可按顺序执行
class MyTestLoader(unittest.TestLoader):

    def getTestCaseNames(self, testcase_class):
        # 调用父类的获取“测试方法”函数
        test_names = super().getTestCaseNames(testcase_class)
        # 拿到测试方法list
        testcase_methods = list(testcase_class.__dict__.keys())
        # 根据list的索引对testcase_methods进行排序
        test_names.sort(key=testcase_methods.index)
        # 返回测试方法名称
        return test_names




##修改BeautifulReport使assert的log中不打印无用日志
class MyBeautifulReport(BeautifulReport):

    def __init__(self, suites):
        super().__init__(suites)

    @staticmethod
    def error_or_failure_text(err) -> str:
        """
            获取sys.exc_info()的参数并返回字符串类型的数据, 去掉t6 error
        :param err:
        :return:
        """
        result = ['']
        res = traceback.format_exception(*err)
        result[0] = res[len(res)-1]
        return result

    # def report(self, description, filename: str = None, report_dir='.', log_path=None, theme='theme_default'):
    #     """
    #                 生成测试报告,并放在当前运行路径下
    #             :param report_dir: 生成report的文件存储路径
    #             :param filename: 生成文件的filename
    #             :param description: 生成文件的注释
    #             :param theme: 报告主题名 theme_default theme_cyan theme_candy theme_memories
    #             :return:
    #             """
    #     if log_path:
    #         import warnings
    #         message = ('"log_path" is deprecated, please replace with "report_dir"\n'
    #                    "e.g. result.report(filename='测试报告_demo', description='测试报告', report_dir='report')")
    #         warnings.warn(message)
    #
    #     if filename:
    #         self.filename = filename if filename.endswith('.html') else filename + '.html'
    #
    #     if description:
    #         self.title = description
    #
    #
    #     self.suites.run(result=self)
    #     self.stopTestRun(self.title)
    #     if (self.fields["testFail"] > 0 or self.fields["testError"] > 0):
    #         self.report_dir = os.path.abspath(report_dir)
    #         os.makedirs(self.report_dir, exist_ok=True)
    #         self.output_report(theme)
    #         text = '\n测试已全部完成, 可打开 {} 查看报告'.format(os.path.join(self.report_dir, self.filename))
    #     else:
    #         text = '总共' + self.fields["testAll"].__str__() + '条用例，执行通过' + self.fields["testPass"].__str__() + '条，执行跳过' + self.fields["testSkip"].__str__() + '条，用例执行通过！'
    #
    #     print(text)

    def report(self, description, filename: str = None, report_dir='.', log_path=None, theme='theme_default'):
        """
            生成测试报告,并放在当前运行路径下
        :param report_dir: 生成report的文件存储路径
        :param filename: 生成文件的filename
        :param description: 生成文件的注释
        :param theme: 报告主题名 theme_default theme_cyan theme_candy theme_memories
        :return:
        """
        if log_path:
            import warnings
            message = ('"log_path" is deprecated, please replace with "report_dir"\n'
                       "e.g. result.report(filename='测试报告_demo', description='测试报告', report_dir='report')")
            warnings.warn(message)

        if filename:
            self.filename = filename if filename.endswith('.html') else filename + '.html'

        if description:
            self.title = description

        self.report_dir = os.path.abspath(report_dir)
        os.makedirs(self.report_dir, exist_ok=True)
        self.suites.run(result=self)
        self.stopTestRun(self.title)

        # 去除POST用例
        if(self.fields['testPass'] == 0):
            pass
        else:
            self.fields['testAll'] = self.fields['testAll'] - self.fields['testSkip']
            self.fields['testSkip'] = 0
        self.output_report(theme)
        text = '\n测试已全部完成, 可打开 {} 查看报告'.format(os.path.join(self.report_dir, self.filename))
        print(text)


    def output_report(self, theme):
        """
            生成测试报告到指定路径下
        :return:
        """

        def render_template(params: dict, template: str):
            for name, value in params.items():
                name = '${' + name + '}'
                template = template.replace(name, value)
            return template

        template_path = self.config_tmp_path
        with open(os.path.join(self.template_path, theme + '.json'), 'r') as theme:
            render_params = {
                **json.load(theme),
                'resultData': json.dumps(self.fields, ensure_ascii=False, indent=4)
            }

        override_path = os.path.abspath(self.report_dir) if \
            os.path.abspath(self.report_dir).endswith('/') else \
            os.path.abspath(self.report_dir) + '/'

        with open(template_path, 'rb') as file:
            body = file.read().decode('utf-8')


        with open((override_path + self.filename), 'w', encoding='utf-8', newline='\n') as write_file:
            html = render_template(render_params, body)
            write_file.write(html)

