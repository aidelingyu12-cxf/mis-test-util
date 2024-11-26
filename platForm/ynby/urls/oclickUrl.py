from django.urls import path, re_path
from platForm.ynby.views import oclickView
from django.contrib import admin
urlpatterns = [
    re_path('logoff', oclickView.Logoff_all_identities),
    re_path('logout', oclickView.Logout_membership),
    re_path('change_order_time', oclickView.change_order_point_value_time),
    re_path('addPoints', oclickView.addPoints),
    re_path('addGrowthValue', oclickView.addGrowthValue),
    re_path('deductPoints', oclickView.deductPoints),
    re_path('deductGrowthValue', oclickView.deductGrowthValue),
    re_path('getmember', oclickView.Getmember),
    re_path('showReport', oclickView.show_report),
    re_path('verification', oclickView.verificationorder),
    re_path('getmember', oclickView.Getmember),
    re_path('pushWanmiJob', oclickView.push_wanmi_job),
    re_path('login', oclickView.login),
    re_path('get_cookie', oclickView.get_cookie),
    #re_path('atf-prod/', testView.automationInterfaceOnceProd),
    re_path('admin/', admin.site.urls),
    re_path('maker', oclickView.maker),
    # re_path('xye', oclickView.xye),
    re_path('getUserFeedBack', oclickView.getUserFeedBack),
    re_path('changeVip', oclickView.changeVip),
    re_path('getGoodsInfo', oclickView.get_goods_info),
    re_path('refund', oclickView.refund),
    re_path('valet', oclickView.valet)
]