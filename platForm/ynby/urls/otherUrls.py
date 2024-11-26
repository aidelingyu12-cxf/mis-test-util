from django.urls import path, re_path
from platForm.ynby.views import otherView

urlpatterns = [
    re_path('xmind-to-excel/', otherView.upload),
    re_path('excel-to-xmind/', otherView.upload_excel),
    re_path('success/', otherView.success),
    re_path('convert/', otherView.convert),
    re_path('convert-to-xmind/', otherView.convert_to_xmind),
    re_path('download', otherView.download),
    re_path('xmind', otherView.xmind),
    #re_path('atf-prod/', testView.automationInterfaceOnceProd),
]