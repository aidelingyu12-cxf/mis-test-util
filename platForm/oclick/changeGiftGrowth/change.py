# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 10:10
# @Author  : 焦海俊
# @File    : change.py
# @Software: PyCharm
from platForm.Utill.Baiyao_DB import baiyaodb
import requests


def change(cell_phone,gift_num,reduce_growth):
    id_sql = 'select id from skin_care_mgr.c_membership where cell_phone = %s and del_flag = 0' % (cell_phone)
    membership_id = str(baiyaodb.select(id_sql)['id'])
    if membership_id:
        change_groupon_sql = "update `skin_care_mgr`.c_membership_groupon set is_vip = 0 where membership_id = '%s' " % (
            membership_id)
        change_res = baiyaodb.operate(change_groupon_sql)
        query_groupon_sql = "select is_vip from `skin_care_mgr`.c_membership_groupon where membership_id = '%s' " % (
            membership_id)
        isvip = str(baiyaodb.select(query_groupon_sql)['is_vip'])
        if isvip == '0':
            change_num_sql = "update `groupon`.groupon_gift_log set total_num = %s, surp_total_num = %s where member_ship_id = '%s' " % (
                gift_num, gift_num, membership_id)
            change_num_res = baiyaodb.operate(change_num_sql)
            print(change_num_res)
            query_num_sql = "select surp_total_num from groupon.groupon_gift_log where member_ship_id = '%s' " % (
                membership_id)
            surp_gift_num = baiyaodb.select(query_num_sql)['surp_total_num']
            print(surp_gift_num)
            print(type(surp_gift_num))
            if surp_gift_num == gift_num:
                return 'gift_ok'
            else:
                return 'gift_fail'
        else:
            return 'change_vip_fail'
    else:
        return 'phone_error'


def reduceGrowthValue(cell_phone,reduce_growth):
    url = "http://192.168.165.38:8000/api/deductGrowthValue"
    payload = {"phone": cell_phone, "growthValue": reduce_growth}
    headers = {
        "cookie": "Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJuYW1lIjoiXHU0ZTkxXHU1MzU3XHU3NjdkXHU4MzZmXHU2ZDRiXHU4YmQ1XHU3YmExXHU3NDA2XHU1ZTczXHU1M2YwIn0.8qnTA6_1BQIub4mImNketz09yysnGmnfL7WOxhANYOM",
    }
    update_level = requests.request("GET", url, headers=headers, params=payload)
    res_data = update_level.json()
    if res_data['code'] == '20000':
        res = {'code': '0000', 'msg': 'vip信息、用户礼包总数、剩余礼包以及用户等级变更成功'}
    else:
        res = ({'code': '5003', 'msg': '万米接口报错', 'msg_list': '%s' % res_data})
    return res