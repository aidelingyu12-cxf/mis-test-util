import unittest
import time
import json

from selenium import webdriver
from selenium.webdriver import ChromeOptions

class MyTestCase(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(r'F:\chromeDriver\\chromedriver.exe',options=option)
        self.driver.implicitly_wait(10)                                                      #设置隐式等待时间

    def test_search(self):
        u''' test search '''
        driver = self.driver
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

        results = []
        for i in range(1,2):
            base_url = 'https://app.nmpaic.org.cn:8088/cfdaic-cosmetic/cosmetic/search?keyword=&pageNum=' + str(i) + '&productType=&size=20&tableName=NMPA_ZLZL_BAXXGSB_GC_NEW%24NMPA_ZLZL_BAXXGSB_GC_OLD&token=JRCr9x7ULk5qwYSr7iq5PQ4fjYWH1pIK4X6XODbny0HZPDyh34AE0qXxJY7ndxS3oUw0Cic5kAQkNSBpecwUIbwaOWswyltj0W57cmB3L-g9Ti0K1LivBH6_MoOoL34GAuLhEaLYIK9eJqnGnIEGtRZiy9RPnZIgULxev-eSQN2EDdtPpuMBXa9UMnpSwCQAf6p26vxFW3Cd1ikecWSKBfDObIu8UOYCZqO3mqLOowx-gnRXHhkt8Juo4CXZoIsiB1Y_hS35Wxs%3D'
            driver.get(base_url)
            resultList = json.loads(driver.find_element_by_xpath('/html/body/pre').text)
            for j in range(0,10):
                results.append(resultList['data']['dataList'][j][0]['value'])
            time.sleep(3)
        print(results)

        with open(r'C:\Users\TMdoubletriblekill\Desktop\云南白药\文档整理\xxx.txt', mode='a') as file:
            for line in results:
                file.write(line + '\n')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    MyTestCase().test_search()
    # with open('report_search.html','wb') as fp:                                              #当前路径下打开一个文件，用于报告写入
    #     runner = HTMLTestRunner.HTMLTestRunner(                                              #使用HTMLTestRunner生成报告
    #         stream=fp,
    #         title='report_search',
    #         description=u'running case:'
    #     )
    #     runner.run(MyTestCase('test_search'))
