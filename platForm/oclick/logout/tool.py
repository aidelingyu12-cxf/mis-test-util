import pymysql
from platForm.oclick.logout.set import YNBYDB_INFO, WaMIDB_INFO
import requests
import json
from pydash import at
import datetime


def ynby_db(sql):
    coon = pymysql.connect(**YNBYDB_INFO)
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchone()
    coon.commit()
    cur.close()
    coon.close()
    return res


def wami_db(sql):
    coon = pymysql.connect(**WaMIDB_INFO)
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchone()
    coon.commit()
    cur.close()
    coon.close()
    return res


class Writeoff(object):
    def __init__(self, order):
        self.order = order
        self.login_url = "http://192.168.165.31:8390/employee/login"
        self.login_param = {"account": "MTMxMDAwMDAwMDA=", "password": "MDAwMDAw"}
        self.trade_url = 'http://192.168.165.31:8390/trade/%s' % self.order
        self.verif_url = "http://192.168.165.38:6014/api/stores/trade/write_off"
        self.header = {'Content-Type': 'application/json;charset=UTF-8'}

    """
    获取token
    """

    def gettoken(self):
        paramdata = json.dumps(self.login_param)
        try:
            r = requests.post(self.login_url, data=paramdata, headers=self.header)
            token = json.loads(r.text)["context"]["token"]
            r.raise_for_status()  # 如果响应状态码不是 200，主动抛出异常
            return json.dumps(token, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    """
    获取订单信息
    """

    def gettradeinfo(self):
        autho = eval(self.gettoken())
        authorization = 'Bearer %s' % autho
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': authorization}
        try:
            r = requests.get(self.trade_url, headers=headers)
            re = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(re, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    """
    调用万米核销接口
    """

    def verification(self, ver, num, *args, **kwargs):
        data = json.loads(self.gettradeinfo())
        shop_code = data["context"]["shopCode"]
        param = {
            "shopCode": "%s" % shop_code,
            "tradeNo": "%s" % self.order,
            "verificationCode": "%s" % ver,
            "skuNo": "8035747638",
            "num": num
        }
        paramdata = json.dumps(param)
        try:
            r = requests.post(url=self.verif_url, data=paramdata, headers=self.header)
            res = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    """
    根据订单号进行核销
    """

    def vertrade(self):
        global res
        trade_data = json.loads(self.gettradeinfo())["context"]
        if trade_data["id"] is None or trade_data["tradeItems"] is []:
            res = {'code': '44444', 'msg': '订单不存在'}
        elif self.order.endswith("S") is True:
            trade_items = trade_data["tradeItems"]
            shop_code = trade_data["shopCode"]
            goods_num = int(len(trade_items))
            for i in range(goods_num):
                goods_list = at(trade_items[i], 'verificationCode', 'num', 'serviceTimes', 'consumeTimes')
                ver = goods_list[0]
                num = goods_list[1] * goods_list[2] - goods_list[3]
                data = json.loads(self.verification(ver, num))
                if data["code"] == "00000":
                    res = {'code': '00000',
                           'msg': '核销成功',
                           '订单号': '%s' % self.order,
                           '商品数量': '%s' % goods_num,
                           '门店编码': '%s' % shop_code
                           }
                else:
                    res = {'code': '99999',
                           'msg': '无核销次数',
                           '商品数量': '%s' % goods_num,
                           '门店编码': '%s' % shop_code
                           }
        elif self.order.endswith("N") is True:
            trade_items = trade_data["tradeItems"]
            shop_code = trade_data["shopCode"]
            goods_num = int(len(trade_items))
            verificat = trade_data["verificationCode"]
            data = json.loads(self.verification(verificat, 1))
            if data["code"] == "00000":
                res = {'code': '00000',
                       'msg': '核销成功',
                       '订单号': '%s' % self.order,
                       '商品数量': '%s' % goods_num,
                       '门店编码': '%s' % shop_code
                       }
            else:
                res = {'code': '99999',
                       'msg': '无核销次数',
                       '商品数量': '%s' % goods_num,
                       '门店编码': '%s' % shop_code
                       }
        else:
            trade_items = trade_data["tradeItems"]
            shop_code = trade_data["shopCode"]
            goods_num = int(len(trade_items))
            trade_type = trade_data["tradeState"]["orderGoodsType"]
            if trade_type == "SERVICE":
                for i in range(goods_num):
                    goods_list = at(trade_items[i], 'verificationCode', 'num', 'serviceTimes', 'consumeTimes')
                    ver = goods_list[0]
                    num = goods_list[1] * goods_list[2] - goods_list[3]
                    data = json.loads(self.verification(ver, num))
                    if data["code"] == "00000":
                        res = {'code': '00000',
                               'msg': '核销成功',
                               '订单号': '%s' % self.order,
                               '商品数量': '%s' % goods_num,
                               '门店编码': '%s' % shop_code
                               }
                    else:
                        res = {'code': '99999',
                               'msg': '无核销次数',
                               '商品数量': '%s' % goods_num,
                               '门店编码': '%s' % shop_code
                               }
            else:
                verificat = trade_data["verificationCode"]
                data = json.loads(self.verification(verificat, 1))
                if data["code"] == "00000":
                    res = {'code': '00000',
                           'msg': '核销成功',
                           '订单号': '%s' % self.order,
                           '商品数量': '%s' % goods_num,
                           '门店编码': '%s' % shop_code
                           }
                else:
                    res = {'code': '99999',
                           'msg': '无核销次数',
                           '商品数量': '%s' % goods_num,
                           '门店编码': '%s' % shop_code
                           }
        return json.dumps(res, ensure_ascii=False)


class Chargeback(object):
    def __init__(self, order=None):
        self.order = order
        self.boss_login = "http://192.168.165.31:8290/employee/login"
        self.boss_param = {"account": "c3lzdGVt", "password": "c3lzdGVt"}
        self.supp_login = "http://192.168.165.31:8390/employee/login"
        self.supp_param = {"account": "MTMxMDAwMDAwMDA=", "password": "MDAwMDAw"}
        self.trade_url = 'http://192.168.165.31:8390/trade/%s' % self.order
        self.apply_url = 'http://192.168.165.31:8390/return/add'
        self.commit_url = 'http://192.168.165.31:8390/return/edit/price/'
        self.logistics_url = 'http://192.168.165.31:8390/return/deliver/'
        self.confirm_url = 'http://192.168.165.31:8390/return/receive/'
        self.boss_examine = 'http://192.168.165.31:8290/return/refund/'
        self.header = {'Content-Type': 'application/json;charset=UTF-8'}
        self.return_url = 'http://192.168.165.31:8390/trade/list/return'

    def getBossToken(self):
        boss_data = json.dumps(self.boss_param)
        try:
            r = requests.post(self.boss_login, data=boss_data, headers=self.header)
            token = json.loads(r.text)["context"]["token"]
            boss_token = json.dumps(token)
            authorization = eval(boss_token)
            boss_token = 'Bearer %s' % authorization
            r.raise_for_status()
            return boss_token
        except requests.RequestException as e:
            print(e)

    def getSuppToken(self):
        supp_data = json.dumps(self.supp_param)
        try:
            r = requests.post(self.supp_login, data=supp_data, headers=self.header)
            token = json.loads(r.text)["context"]["token"]
            supp_token = json.dumps(token)
            authorization = eval(supp_token)
            supp_token = 'Bearer %s' % authorization
            r.raise_for_status()
            return supp_token
        except requests.RequestException as e:
            print(e)

    def getTradeInfo(self):
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getSuppToken()}
        try:
            r = requests.get(self.trade_url, headers=headers)
            re = json.loads(r.text)
            r.raise_for_status()
            return re
        except requests.RequestException as e:
            print(e)

    '''申请退单'''

    def applyOrder(self):
        data = self.getTradeInfo()["context"]
        tradeItems = data["tradeItems"]
        totalPrice = data["tradePrice"]["totalPrice"]
        points = data["tradePrice"]["points"]
        null_points = 0
        if points is None:
            points = null_points
        else:
            points = points
        param = {
            "tid": "%s" % self.order,
            "returnReason": {
                "4": 0
            },
            "description": "测试",
            "images": [],
            "returnItems": tradeItems,
            "returnPrice": {
                "applyPrice": totalPrice,
                "applyStatus": "false",
                "totalPrice": totalPrice
            },
            "returnPoints": {
                "applyPoints": points
            }
        }
        paramdata = json.dumps(param)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getSuppToken()}
        try:
            r = requests.post(url=self.apply_url, data=paramdata, headers=headers)
            res = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    '''提交退单'''

    def commitOrder(self, returnId):
        data = self.getTradeInfo()["context"]["tradePrice"]
        actualReturnPrice = data["totalPrice"]
        actualReturnPoints = data["points"]
        null_points = 0
        if actualReturnPoints is None:
            points = null_points
        else:
            points = actualReturnPoints
        param = {
            "actualReturnPrice": actualReturnPrice,
            "actualReturnPoints": points
        }
        paramdata = json.dumps(param)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getSuppToken()}
        try:
            r = requests.post(url=self.commit_url + '%s' % returnId, data=paramdata, headers=headers)
            res = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    '''提交物流信息'''

    def submitLogisticsInfo(self, returnId):
        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取日期到秒
        param = {
            "code": "guotongkuaidi",
            "company": "国通快递",
            "no": "TESTGT",
            "createTime": create_time
        }
        paramdata = json.dumps(param)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getSuppToken()}
        try:
            r = requests.post(url=self.logistics_url + '%s' % returnId, data=paramdata, headers=headers)
            res = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    '''确认收货'''

    def confirmReceipt(self, returnId):
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getSuppToken()}
        try:
            r = requests.post(url=self.confirm_url + '%s' % returnId, headers=headers)
            res = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    '''审核退款'''

    def reviewRefund(self, returnId):
        param = {}
        paramdata = json.dumps(param)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getBossToken()}
        try:
            r = requests.post(url=self.boss_examine + '%s' % returnId + '/online', data=paramdata, headers=headers)
            res = json.loads(r.text)
            r.raise_for_status()
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    '''查询订单状态'''

    def checkOrderStatus(self):
        global res
        trade_info = self.getTradeInfo()["context"]
        trade_state = trade_info["tradeState"]
        order_source = trade_info["orderSource"]
        try:
            if trade_info["id"] is None or trade_info["tradeItems"] is []:
                res = {'code': 0, 'message': '订单不存在'}
            elif trade_state["payState"] == "NOT_PAID":
                res = {'code': 1, 'message': '订单未付款无法申请退单'}
            elif trade_state["flowState"] == "VOID":
                res = {'code': 2, 'message': '订单已作废无法申请退单'}
            elif trade_state["flowState"] == "DELIVERED" and trade_state["payState"] == "PAID" and trade_state[
                "deliverStatus"] == "SHIPPED":
                res = {'code': 3, 'message': '订单已发货请确认收货后再申请退单'}
            elif trade_state["flowState"] == "AUDIT" and trade_state["payState"] == "PAID" and trade_state[
                "deliverStatus"] == "NOT_YET_SHIPPED":
                res = {'code': 4, 'message': '已支付待发货/待使用订单可直接申请退单'}
            elif trade_state["flowState"] == "COMPLETED" and trade_state["payState"] == "PAID" and trade_state[
                "deliverStatus"] == "SHIPPED":
                res = {'code': 5, 'message': '已支付已完成订单需填写物流信息再申请退单'}
            elif order_source == "SHOP":
                res = {'code': 6, 'message': '线下订单请在云POS端进行退单'}
            else:
                res = {'code': 7, 'message': '订单状态有误', 'date': trade_state}
            return json.dumps(res, ensure_ascii=False)
        except requests.RequestException as e:
            print(e)

    '''一键退单'''

    def quickRefund(self):
        trade_date = json.loads(self.checkOrderStatus())['code']
        if trade_date == 0:
            res = {'code': '4000', 'message': '订单不存在'}
        elif trade_date == 1:
            res = {'code': '4001', 'message': '订单未付款无法申请退单'}
        elif trade_date == 2:
            res = {'code': '4002', 'message': '订单已作废无法申请退单'}
        elif trade_date == 3:
            res = {'code': '4003', 'message': '订单已发货请确认收货后再申请退单'}
        elif trade_date == 4:
            apply_date = json.loads(self.applyOrder())
            if apply_date["code"] == "K-000000":
                return_id = apply_date["context"]["returnOrderId"]
                res = {'code': '0000', 'message': '退单申请成功', 'returnOrderId': return_id}
                print(res)
                commit_date = json.loads(self.commitOrder(returnId=return_id))
                if commit_date["code"] == "K-000000":
                    res = {'code': '0000', 'message': '退单提交成功', 'returnOrderId': return_id}
                    print(res)
                    review_date = json.loads(self.reviewRefund(returnId=return_id))
                    if review_date["code"] == "K-000000":
                        res = {'code': '0000', 'message': '退单审核成功',
                               'orderId': '%s' % self.order, 'returnOrderId': return_id,
                               'context': review_date["context"]}
                        print(res)
                    else:
                        res = {'code': '1111', 'message': '退单审核失败',
                               'orderId': '%s' % self.order, 'date': review_date}
                else:
                    res = {'code': '1111', 'message': '退单提交失败',
                           'orderId': '%s' % self.order, 'date': commit_date}
            else:
                res = {'code': '1111', 'message': '退单申请失败',
                       'orderId': '%s' % self.order, 'date': apply_date}
        elif trade_date == 5:
            apply_date = json.loads(self.applyOrder())
            if apply_date["code"] == "K-000000":
                return_id = apply_date["context"]["returnOrderId"]
                res = {'code': '0000', 'message': '退单申请成功', 'returnOrderId': return_id}
                print(res)
                logistics_date = json.loads(self.submitLogisticsInfo(returnId=return_id))
                if logistics_date["code"] == "K-000000":
                    res = {'code': '0000', 'message': '物流信息填写成功', 'returnOrderId': return_id}
                    print(res)
                    confirm_date = json.loads(self.confirmReceipt(returnId=return_id))
                    if confirm_date["code"] == "K-000000":
                        res = {'code': '0000', 'message': '确认收货成功', 'returnOrderId': return_id}
                        print(res)
                        commit_date = json.loads(self.commitOrder(returnId=return_id))
                        if commit_date["code"] == "K-000000":
                            res = {'code': '0000', 'message': '退单提交成功', 'returnOrderId': return_id}
                            print(res)
                            review_date = json.loads(self.reviewRefund(returnId=return_id))
                            if review_date["code"] == "K-000000":
                                res = {"code": "0000", "message": "退单审核成功", 'orderId': '%s' % self.order,
                                       "returnOrderId": return_id,
                                       "context": review_date["context"]}
                                print(res)
                            else:
                                res = {'code': '1111', 'message': '退单审核失败',
                                       'orderId': '%s' % self.order, 'date': review_date}
                                print(res)
                        else:
                            res = {'code': '1111', 'message': '退单提交失败',
                                   'orderId': '%s' % self.order, 'date': commit_date}
                            print(res)
                    else:
                        res = {'code': '1111', 'message': '确认收货失败',
                               'orderId': '%s' % self.order, 'date': confirm_date}
                else:
                    res = {'code': '1111', 'message': '物流信息填写失败',
                           'orderId': '%s' % self.order, 'date': logistics_date}
            else:
                res = {'code': '1111', 'message': '退单申请失败请',
                       'orderId': '%s' % self.order, 'date': apply_date}
        elif trade_date == 6:
            res = {'code': '4004', 'message': '线下订单请在云POS端进行退单'}
        else:
            res = {'code': '4005', 'message': '订单状态错误'}
        return json.dumps(res, ensure_ascii=False)

    '''获取代客退单列表'''

    def valetChargebackList(self, phone):
        global order
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Authorization': self.getSuppToken()}
        param = {
            "goodsOptions": "skuName",
            "buyerSelect": "buyerAccount",
            "receiverSelect": "consigneeName",
            "id": "",
            "skuName": "",
            "buyerAccount": "%s" % phone,
            "consigneeName": "",
            "pageNum": 0,
            "pageSize": 10
        }
        paramdata = json.dumps(param)
        try:
            r = requests.post(self.return_url, data=paramdata, headers=headers)
            re = json.loads(r.text)['content']
            return re
        except requests.RequestException as e:
            print(e)
