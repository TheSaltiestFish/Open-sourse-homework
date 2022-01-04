import bs4,requests,csv
from bs4 import BeautifulSoup
list=[]
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=Java&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='java'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=C%2B%2B&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='c++'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=PHP&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='PHP'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=Android&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='Android'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=iOS&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='iOS'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=Python&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='Python'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
for i in range(10):
    response=requests.get(f"https://www.lagou.com/wn/jobs?px=new&pn={i+1}&kd=web%E5%89%8D%E7%AB%AF&city=%E5%85%A8%E5%9B%BD")
    text = response.text
    soup=BeautifulSoup(text)
    for job in soup.find_all(class_='item__10RTO'):
        job_type='web前端'
        job_name=job.find(class_="p-top__1F7CL").a.text
        job_sal=job.find(class_="money__3Lkgq").text
        res=[job_type,job_name,job_sal]
        list.append(res)
with open("job.csv", "w", newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    for l in list:
        writer.writerow(l)