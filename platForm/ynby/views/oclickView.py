# Create your views here.
import time
from email.header import Header
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from platForm.oclick.logout.logouts import Cancellation, get_report
from platForm.oclick.logout.tool import Writeoff, Chargeback
import json
import requests
from platForm.oclick.change_order_point_time.some_oclick import change_order_end_time
from platForm.Utill.Baiyao_DB import baiyaodb
from platForm.Utill.Wanmi_DB import wanmidb
from platForm.oclick.change_order_point_time.wanmi_job import wanmi_job
from django.http import HttpResponse
from django.shortcuts import render
from platForm.ynby.models.models import User
import jwt
import random
import string
import datetime
from platForm.oclick.changeGiftGrowth import change
from platForm.oclick.queryGoodsMsg import queryMsg

# Create your views here.


@require_http_methods(["GET"])  # 注销身份及会员接口
def Logoff_all_identities(request):
    global response
    if request.method == 'GET':
        number = request.GET['phone']
        cancel = Cancellation(number=number, phone=number)
        response = json.loads(cancel.baiyao())
    else:
        pass
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 注销会员接口
def Logout_membership(request):
    global response
    if request.method == 'GET':
        phone_number = request.GET['phone']
        cancel = Cancellation(number=phone_number, phone=phone_number)
        response = json.loads(cancel.logoutmember())
    else:
        pass
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 变更积分成长值到账时间接口
def change_order_point_value_time(request):
    order = request.GET.get('order')
    end_time = request.GET.get('time')
    res = change_order_end_time(order=order, time=end_time)
    response = json.loads(res)
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 增加积分接口。
def addPoints(request):
    cell_phone = request.GET.get("phone")
    points = request.GET.get("points")
    sql = 'select id from skin_care_mgr.c_membership where cell_phone =%s and del_flag = 0 ' % (cell_phone)
    try:
        customerAccount = str(baiyaodb.select(sql)['id'])
    except Exception as e:
        return JsonResponse({'code': '403', 'message': '账号不存在或账号输入异常，请重新输入'}, json_dumps_params={'ensure_ascii': False})
    url = "http://192.168.165.38:6012/api/titleWord/addPoints"
    querystring = {"hphone": cell_phone, "points": points, "customerAccount": customerAccount,
                   "type": "1", "pointsType": "18"}
    headers = {
        'fronttype': "SystemCall",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    result = response.json()
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 增加成长值接口
def addGrowthValue(request):
    cell_phone = request.GET.get("phone")
    growthValue = request.GET.get("growthValue")
    sql = 'select id from skin_care_mgr.c_membership where cell_phone =%s and del_flag = 0 ' % (cell_phone)
    try:
        customerAccount = str(baiyaodb.select(sql)['id'])
    except Exception as e:
        return JsonResponse({'code': '403', 'message': '账号不存在或账号输入异常，请重新输入'}, json_dumps_params={'ensure_ascii': False})
    url = "http://192.168.165.38:6012/api/titleWord/addGrowthValue"
    querystring = {"hphone": cell_phone, "growthValue": growthValue,
                   "customerAccount": customerAccount, "type": "1", "growthType": "18"}
    headers = {
        'fronttype': "SystemCall",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 扣减积分接口
def deductPoints(request):
    cell_phone = request.GET.get("phone")
    points = request.GET.get("points")
    sql = 'select id from skin_care_mgr.c_membership where cell_phone =%s and del_flag = 0 ' % (cell_phone)
    try:
        customerAccount = str(baiyaodb.select(sql)['id'])
    except Exception as e:
        return JsonResponse({'code': '403', 'message': '账号不存在或账号输入异常，请重新输入'}, json_dumps_params={'ensure_ascii': False})
    url = "http://192.168.165.38:6012/api/titleWord/addPoints"
    querystring = {"hphone": cell_phone, "points": points,
                   "customerAccount": customerAccount, "type": "0", "pointsType": "18"}
    headers = {
        'fronttype': "SystemCall",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    result = response.json()
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 扣减成长值接口
def deductGrowthValue(request):
    cell_phone = request.GET.get("phone")
    growthValue = request.GET.get("growthValue")
    sql = 'select id from skin_care_mgr.c_membership where cell_phone =%s and del_flag = 0 ' % (cell_phone)
    try:
        customerAccount = str(baiyaodb.select(sql)['id'])
    except Exception as e:
        return JsonResponse({'code': '403', 'message': '账号不存在或账号输入异常，请重新输入'}, json_dumps_params={'ensure_ascii': False})
    url = "http://192.168.165.38:6012/api/titleWord/addGrowthValue"
    querystring = {"hphone": cell_phone, "growthValue": growthValue,
                   "customerAccount": customerAccount, "type": "0", "growthType": "18"}
    headers = {
        'fronttype': "SystemCall",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 获取会员信息接口
def Getmember(request):
    global response
    if request.method == 'GET':
        phone = request.GET['phone']
        cancel = Cancellation(number=phone, phone=phone)
        response = json.loads(cancel.querymember())
    else:
        response = {'code': '33333', 'msg': '请求错误！'}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 查询报告接口
def show_report(request):
    current = request.GET['current']
    size = request.GET['size']
    project = request.GET['project']
    env = request.GET['env']
    date = request.GET['date']
    response = get_report(current, size, project, env, date)
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def verificationorder(request):  # 一键核销订单接口
    global response
    if request.method == 'GET':
        order = request.GET['order']
        write = Writeoff(order=order)
        if order:
            response = json.loads(write.vertrade())
        else:
            response = {'code': '33333', 'msg': '缺少必填参数:order'}
    else:
        response = {'code': '33333', 'msg': '请求错误！'}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])  # 万米定时任务推送
def push_wanmi_job(request):
    job_id = request.GET.get("id")
    co = wanmi_job.get_cookies()
    cookie_str = str(co.content)
    cookie = cookie_str[3:-2]
    url = 'http://192.168.165.29:8990/xxl-job-admin/jobinfo/trigger'
    payload = 'id=%s&executorParam=' % (job_id)
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'XXL_JOB_LOGIN_IDENTITY=' + cookie
               }
    response = requests.request("POST", url=url, headers=headers, data=payload)
    text = response.text
    res = json.loads(text)
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False}, safe=False)


# 登录验证
def login(request):
    '''登录校验'''
    try:
        # if request.method == 'GET':
        #     return render(request, 'login.html')
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            customers = User.objects.filter(Q(username=username))
            if (len(customers) == 0):
                # return HttpResponse('用户名不存在，请输入正确的用户名')
                response = {'code': '00101', 'data': 'null', 'message': '用户名不存在，请输入正确的用户名', "messageTitle": 'null'}
                return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
            else:
                if (customers.values('password')[0]['password'] == password):
                    token = jwt.encode({'username': username, 'password': password, 'name': '云南白药测试管理平台'}, 'secret_key',
                                       algorithm='HS256')
                    response = {'code': '00000', 'data': 'null', 'message': '登录成功', "messageTitle": 'null'}
                    response['cookie'] = 'Authorization=' + token
                    # token += 'Authorization='
                    print(token)
                    response = JsonResponse(response, json_dumps_params={'ensure_ascii': False})
                    response.set_cookie('Authorization', token, max_age=7 * 24 * 3600)  # 设置cookie
                    r = User.objects.filter(username=username).update(token=token)
                    return response
                else:
                    # return HttpResponse('密码错误，请输入正确的用户密码')
                    response = {'code': '00102', 'data': 'null', 'message': '密码错误，请输入正确的用户密码', "messageTitle": 'null'}
                    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        # return HttpResponse('请使用post方法执行此接口')
        response = {'code': '00103', 'data': 'null', 'message': '请使用post方法执行此接口', "messageTitle": 'null'}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        pass
    # return HttpResponse('报错结束')
    response = {'code': '00104', 'data': 'null', 'message': '报错结束', "messageTitle": 'null'}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


# 登录验证
def get_cookie(request):
    '''登录校验'''
    # token_cookie = request.COOKIES['Authorization']  # 请求的token
    # print(token_cookie)
    # customers = User.objects.filter(Q(token=token_cookie))
    # print(customers)
    # if (len(customers) == 0):
    #     response = {'code': '44444', 'data': 'null', 'message': '验证失败', "messageTitle": 'null'}
    #     return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    # else:
    #     response = {'code': '20000', 'data': 'null', 'message': '验证成功', "messageTitle": 'null'}
    #     return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


# 入驻创客
def maker(request):
    phone_number = request.GET.get("phone_number")  # 手机号
    name = request.GET.get("name")  # 创客姓名
    sql_id = 'select id from skin_care_mgr.c_membership where cell_phone =%s and del_flag = 0 ' % (phone_number)
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取日期到秒
    ran_strs = ''.join(random.sample(string.ascii_letters + string.digits, 32))  # 获得32位随机数
    id_number = 230204199909090909 + random.randint(1000, 9999)  # 获得4位随机数身份证
    try:
        customerAccount = str(baiyaodb.select(sql_id)['id'])
    except Exception as e:
        return JsonResponse({'code': '10001', 'message': '账号不存在或账号输入异常，请重新输入'},
                            json_dumps_params={'ensure_ascii': False})

    sql_phone_number = 'select account_id from ynby.maker where phone_number =%s and del_flag = 0 ' % (phone_number)
    try:
        str(baiyaodb.select(sql_phone_number)['account_id'])
        return JsonResponse({'code': '10002', 'message': '该账号创客已存在，请更换账号注册'}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        pass
    # 向数据库增加数据
    sql = 'INSERT INTO ynby.maker(id,name,phone_number,' \
          'health_certificate,' \
          'id_photos,del_flag,' \
          'address,account_id,audit_flag,default_flag,id_number,provincial_agent_id,' \
          'location_city_id,location_district_id,location_province_id,nick_name,contract,' \
          'xye_flag,id_address,cert_date,signature,' \
          'maker_level_id,create_time,update_time,contract_create_time,retrial_success_time) ' \
          'VALUES ("%s","%s","%s",' \
          '"https://oss-cdn.baiyaodajiankang.com/thumbnails_9156121284205636873.png?e=&token=tJiEki3R3OJA7ItTqIBXKaTYU6xhpahxgyjswJP5",' \
          '"https://oss-cdn.baiyaodajiankang.com/thumbnails_1839303190705239021.png?e=&token=tJiEki3R3OJA7ItTqIBXKaTYU6xhpahxgyjswJP5,https://oss-cdn.baiyaodajiankang.com/thumbnails_7086473793695738985.png?e=&token=tJiEki3R3OJA7ItTqIBXKaTYU6xhpahxgyjswJP5",0,' \
          '"上海市 普陀区 长风新村街道 中江路 388弄 国盛中心","%s",6,0,"%s","075a981bd3fb478bbeeee3ac98d7d7ee",' \
          '"310100","310107","310000","%s","https://mis-app-v10.oss-cn-shanghai.aliyuncs.com/mis-mgnt-dev/test/j9dDJ_9nJ4hhzzXYtyTUU.pdf",' \
          '2,"上海市 普陀区 长风新村街道 中江路 388弄 国盛中心","2999-12-31","https://oss-cdn.baiyaodajiankang.com/thumbnails_1926863341413856042.png?e=&token=tJiEki3R3OJA7ItTqIBXKaTYU6xhpahxgyjswJP5",' \
          '28,"%s","%s","%s","%s")' % (
              (ran_strs), (name), (phone_number), (id_number), (customerAccount), (name), (now_time), (now_time),
              (now_time), (now_time))  # 加入多条数据
    # 执行该条sql命令
    str(baiyaodb.select(sql))
    # 调用小鱼儿注册
    # xye(request)
    # 创客同步万米
    url = 'http://192.168.165.38:6015/api/makers/sync/maker'
    account_id = str(baiyaodb.select(sql_phone_number)['account_id'])
    data = {'accountId': account_id}
    response = requests.request("POST", url=url, data=data)
    result = response.json()
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


# # 手机号同步小鱼儿
# @require_http_methods(["GET"])
# def xye(request):
#     phone_number = request.GET.get("phone_number")
#     sql_phone_number = 'select account_id from ynby.maker where phone_number =%s and del_flag = 0 ' % (phone_number)
#     url = 'http://192.168.165.38:6015/api/xye/register'
#     account_id = str(baiyaodb.select(sql_phone_number)['account_id'])
#     payload = {"accountId": account_id, "type": "0"}
#     headers = {"Host": '192.168.165.38:6015'}
#     response = requests.request("GET", url=url, headers=headers, params=payload)
#     result = response.json()
#     return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


def getUserFeedBack(request):
    try:
        current = request.GET.get('current')
        size = request.GET.get('size')
        url = "http://192.168.165.67:10010/question/feedback/infoList"
        payload = {"current": current, "size": size}
        r = requests.request("GET", url=url, params=payload)
        result = r.json()
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'code': '10000', 'message': '系统异常！'}, json_dumps_params={'ensure_ascii': False})


# 更改购卡会员为非会员、剩余礼包和会员等级
@require_http_methods(["GET"])
def changeVip(request):
    global res
    cell_phone = request.GET.get('phone')
    surp_total_num = int(request.GET.get('num'))
    growthValue = request.GET.get('values')
    result = change.change(cell_phone=cell_phone,gift_num=surp_total_num,reduce_growth=growthValue)
    if result=='gift_ok':
        res = change.reduceGrowthValue(cell_phone=cell_phone,reduce_growth=growthValue)
    elif result=='gift_fail':
        res = ({'code': '50002', 'msg': '礼包数量更改失败，请查询后重试'})
    elif result=='change_vip_fail':
        res = ({'code': '50001', 'msg': 'isVip更改失败，请查询后重试'})
    elif result=='phone_error':
        res = ({'code': '10001', 'msg': '账号不存在或账号输入有误，请核对后重新输入'})
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


# 一键查询商品套餐名称、sku、skuid等信息
@require_http_methods(["GET"])
def get_goods_info(request):
    input_data = request.GET.get('data')
    if not input_data:
        res = ({'code': '40001', 'msg': 'data值不能为空，请输入信息'})
        return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
    res = queryMsg.queryBySkuId(input_data=input_data)
    if res is None:
        res = queryMsg.queryBySkuNo(input_data=input_data)
        if res is None:
            res = queryMsg.queryByName(input_data=input_data)
            if res is None:
                res = queryMsg.queryByBarcode(input_data=input_data)
                if res is None:
                    res = ({'code': '40001', 'msg': '商品不存在！'})
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


# 一键退单
@require_http_methods(["GET"])
def refund(request):
    global response
    if request.method == 'GET':
        order = request.GET['order']
        charge = Chargeback(order=order)
        if order:
            response = json.loads(charge.quickRefund())
        else:
            response = {'code': '44444', 'msg': '缺少必填参数:order'}
    else:
        response = {'code': '44444', 'msg': '请求错误！'}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


# 批量申请退单
def valet(request):
    global response
    if request.method == 'GET':
        phone = request.GET['phone']
        charge = Chargeback()
        if phone and len(phone) == 11:
            id = charge.valetChargebackList(phone=phone)
            if not id:
                response = {'code': '1111', 'message': '账号没有可申请退款的订单'}
            else:
                refund_list = []
                for i in range(len(id)):
                    order = id[i]["id"]
                    char = Chargeback(order=order)
                    refund_date = json.loads(char.quickRefund())
                    time.sleep(5)
                    refund_list.append(refund_date)
                response = {'code': '0000', 'message': '批量退单成功！', 'list': refund_list}
        else:
            response = {'code': '44444', 'message': '参数有误请重新输入！'}
    else:
        response = {'code': '55555', 'msg': '请求错误！'}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
