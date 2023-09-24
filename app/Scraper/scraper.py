import requests
from fake_useragent import UserAgent
from app import db
from app.models import Job
import time
import random

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def run():
    page = 1
    # Cookie = input("请输入Cookie:\n")
    url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?"
    user_agent = UserAgent()
    headers = {
        "User-Agent": user_agent.random,
    }
    Cookie = {
        "__zp_stoken__": "f68beWDpFaSBNOiwsJBk1FwYDbR4aRTp8RnRIeQRvWwtMG0oePCJ4dnEqPRYTCkpaJkx%2BQGUwLm8tNV1AcHRBPD4uMAtXFB4FJRFqD1QNLx9LKycNZS5if1sHagYYRBEMZHVMP2BODQ1gdEY%3D",
    }
    responseTemp = None
    while True:
        params = {
            "scene": 1,
            "query": "",
            "city":100010000,
            "experience": "",
            "payType": "",
            "partTime": "",
            "degree": "",
            "industry": "",
            "scale": "",
            "stage": "",
            "position":100101,
            "jobType": "",
            "salary": "",
            "multiBusinessDistrict": "",
            "multiSubway": "",
            "page": page,
            "pageSize":30,
        }
        proxy = get_proxy().get("proxy")
        response = requests.get(url, params=params, headers=headers, cookies=Cookie, proxies={"http": "http://{}".format(proxy)})
        if response.status_code == 200:
            # print(response.text)
            data = response.json()
            if responseTemp == data:
                break
            responseTemp = data
            if data.get('code', 99) in [37,99,5002]:
                print("访问异常已退出 报错信息 ",data.get('message', 'None'))
                exit(0)
            job_list = data.get('zpData', {}).get('jobList', [])
            for job_data in job_list:
                job = Job(
                    job_name=job_data.get('jobName'),
                    company=job_data.get('bossName'),
                    city=job_data.get('cityName'),
                    requirements=job_data.get('jobExperience'),
                    wage=job_data.get('salaryDesc'),
                    url=job_data.get('jobDetailUrl')
                )
                # db.session.add(job)
                print(job)
            # db.session.commit()
            page += 1
        else:
            print(f"请求失败，状态码: {response.status_code}")
        time.sleep(random.randint(1,4))



