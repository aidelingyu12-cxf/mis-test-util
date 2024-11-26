import json
import datetime
'''
dumps的原功能是将dict转化为str格式，不支持转化时间，所以需要将json类部分内容重新改写，来处理这种特殊日期格式
'''
class DateEncoder(json.JSONEncoder):#时间格式数据进行转化类
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        # elif isinstance(obj, datetime.date):
        #     return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    DateEncoder()