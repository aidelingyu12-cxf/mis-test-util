from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from interfaceAuto.ynby.models.testModel import Testers
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, FileResponse, HttpResponse
import json, datetime, os
from interfaceAuto.atf.startUp import start
import interfaceAuto.atf as atf
from apscheduler.schedulers.blocking import BlockingScheduler
from interfaceAuto.atf.util.configContent import confContent
from interfaceAuto.atf.util.configReader import configReader
import interfaceAuto.ynby.urls as urls
# Create your views here.

# 定时任务周一至周五  8-23点每小时执行一次
@require_http_methods(["GET"])
def automationInterfaceAppCron(request):
    atf.env = request.GET.get('env')
    configReader.ConfigFileContent_app = confContent().getAppConfigs(test_or_dev=atf.env)
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(start, 'cron', day_of_week='0-4', hour='8-23', next_run_time=datetime.datetime.now(),
                      args=["/cases/appCases", request.GET.get("pattern")])
    # 每5分钟执行一次
    # scheduler.add_job(start, 'cron', minute='*/5', next_run_time=datetime.datetime.now(),
    #                   args=["/cases/appCases", request.GET.get("pattern")])
    scheduler.start()
    # scheduler.add_job(start, 'cron', day_of_week='0-4', hour='8-23', next_run_time=datetime.datetime.now())
    # scheduler.start(whichCasePath="/cases/appCases", testCasePattern=request.GET.get("pattern"))
    return render(request, atf.filename)

@require_http_methods(["GET"])
def automationInterfaceAppOnce(request):
    atf.env = request.GET.get('env')
    configReader.ConfigFileContent_app = confContent().getAppConfigs(test_or_dev=atf.env)
    ifReport = start(whichCasePath="/cases/appCases", testCasePattern=request.GET.get("pattern"))
    return render(request, atf.filename)
    # if(ifReport == 0):
    #     return render(request, atf.successReport)
    # else:
    #     return render(request, atf.filename)

@require_http_methods(["GET"])
def automationInterfaceMiniAppOnce(request):
    atf.env = request.GET.get('env')
    configReader.ConfigFileContent = confContent().getMiniAppConfigs(test_or_dev=atf.env)
    ifReport = start(whichCasePath="/cases/miniappCases")
    if(ifReport == 0):
        return render(request, atf.successReport)
    else:
        return render(request, atf.filename)

@require_http_methods(["GET"])
def automationInterfaceApph5Once(request):
    configReader.ConfigFileContent_h5 = confContent().getApph5Configs()
    ifReport = start(whichCasePath="/cases/apph5Cases", testCasePattern=request.GET.get("pattern"))
    return render(request, atf.filename)
    # if(ifReport == 0):
    #     return render(request, atf.successReport)
    # else:
    #     return render(request, atf.filename)




