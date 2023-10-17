import json
import os
import re
from fuzzywuzzy import fuzz
from collections import OrderedDict


Job_Data_Path = ['E://Project//Python//TechJob-Insights//app//Data//C#.json',
                 'E://Project//Python//TechJob-Insights//app//Data//C++.json',
                 'E://Project//Python//TechJob-Insights//app//Data//JAVA.json',
                 'E://Project//Python//TechJob-Insights//app//Data//PHP.json',
                 'E://Project//Python//TechJob-Insights//app//Data//Python.json']

#education_order = ['不限', '初中及以下', '中专/中技', '高中', '大专', '本科', '硕士', '博士']

#学历要求
def education_wanted():
    education_counts = {}
    for json_file_path in Job_Data_Path:
        with open(json_file_path) as f:
            data = json.load(f)
        for item in data:
            if len(item) > 4 :
                education = item[4]
                # 检查学历是否包含数字
                if any(char.isdigit() for char in education):
                    education_with_digits = item[5]
                    education_counts[education_with_digits] = education_counts.get(education_with_digits, 0) + 1
                else:
                    education_counts[education] = education_counts.get(education, 0) + 1

    #sorted_education_counts = OrderedDict((key, education_counts.get(key, 0)) for key in education_order)
    return education_counts

#城市分布
def city_distribution():
    city_counts = {}
    for json_file_path in Job_Data_Path:
        with open(json_file_path) as f:
            data = json.load(f)
        for item in data:
            if len(item) > 2 :
                city = item[1].split("·")[0].strip()
                city_counts[city] = city_counts.get(city, 0) + 1
    city_counts = dict(sorted(city_counts.items(), key=lambda item: item[1], reverse=True))
    #这里需要改成相对路径
    return city_counts

#经验要求
def experience_wanted():
    experience_counts = {}
    keywords_to_skip = ["5天/周", "4天/周", "在校/应届", "3天/周", "7天/周", "应届生", "6天/周", "2天/周"]
    for json_file_path in Job_Data_Path:
        with open(json_file_path) as f:
            data = json.load(f)
        for item in data:
            if len(item) > 3 :
                experience = item[3]
                if experience not in keywords_to_skip:
                    experience_counts[experience] = experience_counts.get(experience, 0) + 1
    return experience_counts

#福利信息
def welfare():
    welfare_counts = {}
    for json_file_path in Job_Data_Path:
        with open(json_file_path) as f:
            data = json.load(f)
        for item in data:
            if len(item) > 9 :
                welfare = item[9]
                keywords_list = welfare.split("，")
                for keyword in keywords_list :
                    keyword = keyword.strip()
                    if  re.match(r'^https?://', keyword):
                        continue
                    if keyword and keyword :
                        welfare_counts[keyword] = welfare_counts.get(keyword, 0) + 1
    welfare_counts_filtered = {k: v for k, v in welfare_counts.items() if v > 10}
    return welfare_counts_filtered

#模糊匹配函数
def merge_similar_job_info(job_info_counts):
    merged_counts = {}
    threshold = 75
    for job_info, count in job_info_counts.items():
        merged = False
        for merged_job_info in merged_counts.keys():
            similarity = fuzz.ratio(job_info, merged_job_info)
            if similarity >= threshold:
                merged_counts[merged_job_info] += count
                merged = True
                break
        if not merged:
            merged_counts[job_info] = count


    return merged_counts


#职业信息(模糊匹配)
def job_info():
    job_info_counts = {}
    for json_file_path in Job_Data_Path:
        with open(json_file_path) as f:
            data = json.load(f)
        for item in data:
            if len(item) > 0:
                job_info = item[0]
                job_info_counts[job_info] = job_info_counts.get(job_info, 0) + 1
    merged_job_info_counts = merge_similar_job_info(job_info_counts)
    merged_job_info_counts = dict(sorted(merged_job_info_counts.items(), key=lambda item: item[1], reverse=True))
    return merged_job_info_counts

#对函数进行测试
if __name__ == '__main__':
    print(education_wanted())
    print(city_distribution())
    print(experience_wanted())
    print(welfare())
    print(job_info())