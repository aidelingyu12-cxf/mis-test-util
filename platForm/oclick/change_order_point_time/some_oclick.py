from platForm.Utill.Wanmi_DB import wanmidb
import json
from platForm.oclick.change_order_point_time.datetime import DateEncoder#时间格式数据进行转化
# import importlib,sys
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')


def change_order_end_time(order=None,time=None):
    """
    变更订单截止时间，当前需求是下单后成长值立刻到账，积分需要等订单周期结束后才到账
    """
    sql = "update `sbc-order`.order_growth_value_temp set return_end_time = '%s' where order_no = '%s' " %(time,order)
    sql1 = "select * from `sbc-order`.order_growth_value_temp where order_no = '%s' " %(order)
    up_data = wanmidb.operate(sql)
    data = wanmidb.select(sql1)
    print(data)
    print(type(data))
    if data == None:
        res = {'massage': '订单号有误或不存在，请重新输入'}
        print(type(res))
        return json.dumps(res, ensure_ascii=False)#python对象编码成json字符串
    else:
        return json.dumps(data, ensure_ascii=False, cls=DateEncoder)#引入时间格式数据转化类处理特殊日期格式


if __name__ == '__main__':
    change_order_end_time()
