import json
from django.http import JsonResponse
import requests


class Wanmi_job():
    """
    暂时不用
    """
    def get_cookies(self):
        url = 'http://192.168.165.29:8990/xxl-job-admin/login'
        payload = 'userName=admin&password=520WanMi'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        session = requests.session()
        session.post(url=url, headers=headers, data=payload)
        cookie_jar = requests.sessions.RequestsCookieJar()
        session.cookies.update(cookie_jar)
        cookie = session.cookies.get_dict()['XXL_JOB_LOGIN_IDENTITY']
        return JsonResponse(cookie, json_dumps_params={'ensure_ascii': False}, safe=False)

    # def push_point_value_job(self):
    #     url = 'http://192.168.165.29:8990/xxl-job-admin/jobinfo/trigger'
    #     payload = 'id=3&executorParam='
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded',
    #                'Cookie': 'XXL_JOB_LOGIN_IDENTITY=' +wanmi_job.get_cookies()
    #                }
    #     response = requests.request("POST", url=url, headers=headers, date=payload)
    #     print(response)
    #     return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, safe=False)

    # def push_points_values_job(self, job_id):
    #     co = wanmi_job.get_cookies()
    #     cookie_str = str(co.content)
    #     cookie = cookie_str[3:-2]
    #     print(cookie)
    #     url = 'http://192.168.165.29:8990/xxl-job-admin/jobinfo/trigger'
    #     payload = "id='%s'&executorParam=" %(job_id)
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded',
    #                'Cookie': 'XXL_JOB_LOGIN_IDENTITY=' + cookie
    #                }
    #     response = requests.request("POST", url=url, headers=headers, data=payload)
    #     # response = json.loads()
    #     text = response.text
    #     print(text)
    #     print(type(text))
    #     # return response.status_code
    #     res = json.loads(text)
    #     return JsonResponse(res, json_dumps_params={'ensure_ascii': False}, safe=False)


wanmi_job = Wanmi_job()