import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
import platform


class Email:
    def __init__(self):
        # 发件人邮箱账号
        self.my_sender = 'caoxuefeng@ynbyjk.com'
        # 授权码
        self.my_pass = '4L9KAiazY7LW7kPV'

    @staticmethod
    def email_content():
        # 区分linux与windows，默认在windos执行是本地调试，不发送报告链接
        if platform.system().lower() == 'linux':
            html = """
                <html>
                            <head>
                                    <meta charset="utf-8">
                            <style>
                            td {
                            text-align: center;
                            }
                            </style>
                            </head>
                            <style>
                            </style>
                            <body>
                                <!-- 表格标签 -->
                                <!-- 表格绘制 -->
                                <table width="300px" border="1px" cellspacing="0" cellpadding="10">
                                <caption style="text-align:center;font-weight:bold;margin-bottom:15px;">
                                <font size=5>报告汇总</font>
                                </caption>
                        <tr align="left">
                        <td colspan="5"> 
                        <a style="font-size: 15px;" href="http://192.168.165.38:8888/auto_test_report/%s">点击查看报告详情(须连接内网)
                </a>
                </td>
                        </tr>
                        <tr>
                            <td>自动化通过率</td>
                            <td width=50%%>%s</td>
                        </tr>
                        <tr>
                            <td>执行时长</td>
                            <td width=50%%>%s</td>
                        </tr>
                        <tr>
                            <td>用例总数</td>
                            <td width=50%%>%d  个</td>
                        </tr>
                        <tr>
                            <td>用例通过</td>
                            <td width=50%%>%d  个</td>
                        </tr>
                        <tr>
                            <td>用例失败</td>
                            <td width=50%% style="color:%s">%d  个</td>
                        </tr>
                        <tr>
                            <td>执行错误</td>
                            <td width=50%% style="color:%s">%d  个</td>
                        </tr>
                        <tr>
                            <td>跳过执行</td>
                            <td width=50%%>%d  个</td>
                        </tr>
                    </table>
                            </body>
                            </html>
                    """
        else:
            html = """
                            <html>
                            <head>
                                    <meta charset="utf-8">
                            <style>
                            td {
                            text-align: center;
                            }
                            </style>
                            </head>
                            <style>
                            </style>
                            <body>
                                <!-- 表格标签 -->
                                <!-- 表格绘制 -->
                                <table width="300px" border="1px" cellspacing="0" cellpadding="10">
                                <caption style="text-align:center;font-weight:bold;margin-bottom:15px;">
                                <font size=5>报告汇总</font>
                                </caption>
                        <tr align="left">
                        <a %s"></a>
                        </tr>
                        <tr>
                            <td>自动化通过率</td>
                            <td width=50%%>%s</td>
                        </tr>
                        <tr>
                            <td>执行时长</td>
                            <td width=50%%>%s</td>
                        </tr>
                        <tr>
                            <td>用例总数</td>
                            <td width=50%%>%d  个</td>
                        </tr>
                        <tr>
                            <td>用例通过</td>
                            <td width=50%%>%d  个</td>
                        </tr>
                        <tr>
                            <td>用例失败</td>
                            <td width=50%% style="color:%s">%d  个</td>
                        </tr>
                        <tr>
                            <td>执行错误</td>
                            <td width=50%% style="color:%s">%d  个</td>
                        </tr>
                        <tr>
                            <td>跳过执行</td>
                            <td width=50%%>%d  个</td>
                        </tr>
                    </table>
                            </body>
                            </html>
                                """
        return html
    def send_email(self, file, filename, pass_rate, excute_time, total_case,
                   pass_case, fail_case, error_case, skip_case):
        """
        如果是在linux机器上跑，需要多添加一个报告链接
        :return:
        """
        try:
            # 邮件内容
            msg = MIMEMultipart()
            # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['From'] = formataddr(("caoxuefeng@ynbyjk.com", self.my_sender))
            # 添加收件人信息
            # msg_to = ['jiaohaijun@ynbyjk.com', 'caoxuefeng@ynbyjk.com', 'zhuboliang@ynbyjk.com', 'liumingsheng@ynbyjk.com', 'xiaohailong@ynbyjk.com',
            #           'zhuning@ynbyjk.com']
            msg_to = ['zhuboliang@ynbyjk.com', 'caoxuefeng@ynbyjk.com']
            msg['To'] = ','.join(msg_to)
            # 邮件的主题
            msg['Subject'] = "接口自动化测试结果"
            # 区分是否有错误或者失败用例，用红色字体展示
            fail_color, error_color = 'BLACK', 'BLACK'
            if fail_case > 0:
                fail_color = 'RED'
            if error_case > 0:
                error_color = 'RED'
            # 邮件正文,区分linux or windows
            msg.attach(MIMEText(self.email_content() % (filename, pass_rate, excute_time, total_case, pass_case,
                                                        fail_color, fail_case, error_color, error_case, skip_case),
                                'html', _charset="utf-8"))
            xlsxpart = MIMEApplication(open(file, 'rb').read())
            xlsxpart.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(xlsxpart)
            # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
            # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
            # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
            server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
            # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
            server.login(self.my_sender, self.my_pass)
            # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            # 判断失败用例是否大于0 或 跳过用例是否大于0
            if(fail_case > 0 or error_case > 0):
                server.sendmail(self.my_sender, msg_to, msg.as_string())
            # 关闭连接
            server.quit()
        except Exception as e:
            print(e.args)
        return None
