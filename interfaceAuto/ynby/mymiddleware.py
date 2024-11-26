# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Q
from interfaceAuto.ynby.models.models import User


try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 允许跨域请求的地址 (*代表所有地址)
        # response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Origin'] = "http://127.0.0.1"
        # 允许跨域请求的类型
        response['Access-Control-Allow-Headers'] = "X-Requested-With,Content-Type"
        # 允许跨域请求的方式
        response['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
        # 允许跨域请求携带cookie
        response['Access-Control-Allow-Credentials'] = "true"

        return response

    def process_request(self, request):
        # print(request.COOKIES)
        # print(headers['token'])
        if request.path != '/api/atf/login' and request.path != '/api/atf/login_check':
            if request.COOKIES.get('Authorization', None):
                token_cookie = request.COOKIES['Authorization']  # 请求的token
                # token_cookie += 'Authorization='
                customers = User.objects.filter(Q(token=token_cookie))
                if (len(customers) == 0):
                    response = {'code': '00105', 'data': 'null', 'message': '请输入正确的token', "messageTitle": 'null'}
                    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
                else:
                    pass
            else:
                # return HttpResponseRedirect('/login')
                response = {'code': '00106', 'data': 'null', 'msg': '请输入token', "messageTitle": 'null'}
                return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        # pass