from typing import Counter
import pymongo
import csv
from pymongo import collection
from pymongo.mongo_client import MongoClient

def conn(): #连接数据库，选中所需集合
    myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    mydb = myclient['mongoproject']
    mycol = mydb['job']
    db=myclient.mongoproject
    set1 = db.job
    return set1

def insert_to_db(set1):#从爬出的csv文件中筛选出想要的关键字并插入job里
    with open("job.csv",encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for each in reader:
            del each['info']
            del each['edge']
            del each['min1']
            del each['max1']
            set1.insert_one(each)

def find_by_type(job_type):#根据职业类型查找
    set2 = conn()
    return set2.find({'area':job_type})

def main():
    set1 = conn()
    insert_to_db(set1)

main()