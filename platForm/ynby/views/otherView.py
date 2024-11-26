import shutil

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
import  os

from django.utils.encoding import escape_uri_path
from django.views.decorators.csrf import csrf_exempt
from platForm.otherUtil.xmind_to_excel.xmind_to_excel import xmind_to_xls
from platForm.otherUtil.excel_to_xmind import excel_to_xmind




def upload(request):
    return render(request, 'upload.html')

def upload_excel(request):
    return render(request, 'upload-excel.html')

@csrf_exempt
def success(request):
    return render(request, 'convertSuccess.html')

@csrf_exempt
def convert(request):
    file = request.FILES.get('upload_file')
    title = xmind_to_xls().readXmind(file)
    if title:
        return render(request, 'convertSuccess.html')
        # return JsonResponse({'code': 0, 'data': title, 'message': 'ok'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'code': -1, 'data': {}, 'message': '运行错误，请重新上传'}, json_dumps_params={'ensure_ascii': False})


def convert_to_xmind(request):
    files = request.FILES.getlist('upload_file')
    user_info = request.POST.get('dirName')
    root_path = os.path.abspath(os.path.dirname(__file__)).split('platForm')[0]
    save_path = root_path + user_info + r'-save_xmind'
    if user_info + r'-save_xmind' not in os.listdir('./'):
        os.mkdir(save_path)
    else:
        shutil.rmtree(save_path)
        os.mkdir(save_path)
    num = 0
    for file in files:
        filename = file.name[0:-5]
        print(filename)
        msg = excel_to_xmind.gen_xmind_file(file, save_path, filename)
        if msg == 'OK':
            num += 1
    # print('msg=',msg)
    if num == len(files):
        return JsonResponse({'code': 0, 'data': {}, 'message': '转化成功，请尽快下载'}, json_dumps_params={'ensure_ascii': False})
        # return JsonResponse({'code': 0, 'data': title, 'message': 'ok'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'code': -1, 'data': {}, 'message': '运行错误，请重新上传'}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def download(request):
    path = os.getcwd()
    path_list = os.listdir(path)
    for filename in path_list:
        if os.path.splitext(filename)[1] == '.xls':
            file = open(filename, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="case.xls"'
            return response


def xmind(request):
    dirname = request.GET.get('dirName')
    root_path = os.path.abspath(os.path.dirname(__file__)).split('platForm')[0]
    path = root_path + dirname + r'-save_xmind'
    zipfile = excel_to_xmind.zip_ya(path)
    file = open(zipfile, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(escape_uri_path(zipfile))
    return response