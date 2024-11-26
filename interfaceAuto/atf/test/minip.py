import requests,time,random

url = "https://testapi.caizhiji.com.cn/mis/api/groupon/v1/groupon/singleBuyCallback"

payload = "{\n\t\"orderId\":\"116840216364044288\"}"
# headers1 = {
#     'content-type': "application/json",
#     'authorization': "Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJmMThkMGI4YzE5OWY0N2Y5OTBmNjM1NDBiZGNhZDk3YyIsInBob25lTnVtYmVyIjoiMTkxNzk3MTM3NjIiLCJvcGVuaWQiOiJvRHA5RzQybTRmS1lEUXUzTjhVZkJlNEJYSWFnIiwibWVtYmVyc2hpcElkIjoiZjE4ZDBiOGMxOTlmNDdmOTkwZjYzNTQwYmRjYWQ5N2MiLCJleHAiOjE2NDE4NjgyOTB9.RqejIgiqHHjm1aT-0IZ6TectIgWEsiOB3bXSYd11FPz-74uimD318KiGahVNymMt1jFQtOlZp1Z79pb_rdV_MvNSgx8Ko1NO_C4OVLLW8YnTShEsC436GL7OSrddJ8IQOCU6XcyZuLoegazccCCYfBVcxXftjQ_T9hVibn1L8kc",
#     }


# headers2 = {
#     'content-type': "application/json",
#     'authorization': "Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiIyMjI2NzNmMzFhOGQ0MzM2OGMyMjkxMzU3MzVhMTY4NSIsInBob25lTnVtYmVyIjoiMTU2MTc4OTEwMDMiLCJvcGVuaWQiOiJvRHA5RzRfbURDNW1BZXdNdTBQcUZIZXhCSVRZIiwibWVtYmVyc2hpcElkIjoiMjIyNjczZjMxYThkNDMzNjhjMjI5MTM1NzM1YTE2ODUiLCJleHAiOjE2NDIxNTIyODF9.J-HPKJvHzOyvVIgvEt8Vtp1P3eWVypJSm48PAWwPQ7s4L0X7ZefdQDQiupR_0_w1eppvPwIg2Wq2M4NMe419QQYmsZfV7Ir0ldUdx48R0Vb7ps4PH-0f8vdSxS6huzs42VkD-QK5O7bNgeyEFWrhNnUtULTeBiV02XPZdEucNac",
#     }

headers3 = {
    'content-type': "application/json",
    'authorization': "Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiIxMGYzMGE3OThlNDg0NWIwYWUyZWE4NDJlOGZmMDQxOSIsInBob25lTnVtYmVyIjoiMTM3MzMxNjUyMDIiLCJvcGVuaWQiOiJvRHA5RzQySDFIUEQ0dXRwNVlZYTdlYnZlb2lvIiwibWVtYmVyc2hpcElkIjoiMTBmMzBhNzk4ZTQ4NDViMGFlMmVhODQyZThmZjA0MTkiLCJleHAiOjE2NDIxNTUzMzN9.iX5OmlMS4Azh3S0HwQJs7McbU-b3Il69BGjigVZbmmswPFDvJgfifdlSTtz2INAMN3wP6hVQ4kBGsup-L8lp1n-Of9aSjQc9Oq1o3n0p2vxHQeOL_9vIMXSDLyTrgsdqGHIfRAxL2OCVW-_wS6jFQ0A128iNbVQCrDfW6hhSYOo",
    }

#list = [headers1,headers2,headers3]

def exe():
    #num = random.randint(0,2)
    #head = list[num]
    response = requests.request("POST", url, data=payload, headers=headers3)
    print(response.text)

for i in range(1,10000):
    exe()
    time.sleep(2)
