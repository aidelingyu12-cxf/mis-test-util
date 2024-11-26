# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 12:12
# @Author  : 焦海俊
# @File    : xmind_xls.py
# @Software: PyCharm
import os

from xmindparser import xmind_to_dict
import xlwt, time
from tkinter.messagebox import showinfo
import tkinter.messagebox


class xmind_to_xls():

    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    @staticmethod
    def xmind_title():
        """获取xmind标题内容"""
        t = str(time.time())
        return t

    def writeExcel(self, row, case, excelName):
        sort = 0
        row0 = ["一级模块", '二级模块', '用例名称', '前置条件', '步骤描述', "预期结果", '用例类型', '优先级', '维护人']
        # 生成第一行
        for i in range(0, len(row0)):
            self.worksheet.write(0, i, row0[i])

        for key, value in case.items():
            self.worksheet.write(row, sort, value)
            sort = sort + 1
        self.workbook.save(excelName + '_测试用例.xls')

    def readXmind(self, FileName):
        root_path = os.path.abspath(os.path.dirname(__file__)).split('interfaceAuto')[0]
        print(os.getcwd())
        os.chdir(root_path + r'save_xls')
        path = os.getcwd()
        path_list = os.listdir(path)
        for filename in path_list:
            os.remove(filename)
        self.rowNum = 0  # 计算测试用例的条数
        self.caseDict = {}
        title = self.xmind_title()
        try:
            self.XmindContent = xmind_to_dict(FileName)[0]['topic']  # xmind内容
            for a in self.XmindContent['topics']:
                for b in a['topics']:
                    for c in b['topics']:
                        for d in c['topics']:
                            for e in d['topics']:
                                for f in e['topics']:
                                    for g in f['topics']:
                                        for h in g['topics']:
                                            for i in h['topics']:
                                                self.caseDict['firstModule'] = b['title']
                                                self.caseDict['secondModule'] = d['title']
                                                self.caseDict['case_name'] = e['title']
                                                self.caseDict['pre_condition'] = f['title']
                                                self.caseDict['test_step'] = g['title']
                                                self.caseDict['expected_results'] = h['title']
                                                self.caseDict['case_type'] = c['title']
                                                self.caseDict['priority'] = i['title']
                                                self.caseDict['creator'] = a['title']
                                                self.rowNum = self.rowNum + 1
                                                self.writeExcel(self.rowNum, self.caseDict, title)
            # title = self.xmind_title() + '_测试用例.xls'
            return self.xmind_title() + '_测试用例.xls'
        except:
            pass


if __name__ == '__main__':
    # XmindFile = os.path.join(os.path.dirname(__file__), 'xmind_excel.xmind')  # xmind文件
    xmind_to_xls().readXmind(r'C:\Users\UZIQAQ\Desktop\云南白药\2021.12\创客拉新需求.xmind')
