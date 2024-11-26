from django.urls import path, re_path
from interfaceAuto.ynby.views import atfView

urlpatterns = [

    re_path('atf/appCron', atfView.automationInterfaceAppCron),
    re_path('atf/appOnce', atfView.automationInterfaceAppOnce),

    # # 生产环境
    # re_path('atf/dev/appCron', atfView.automationDevInterfaceAppCron),
    # re_path('atf/dev/appOnce', atfView.automationDevInterfaceAppOnce),

    re_path('atf/miniapp', atfView.automationInterfaceMiniAppOnce),
    re_path('atf/apph5', atfView.automationInterfaceApph5Once)
]