from bs4 import BeautifulSoup
import requests
import json
import random
url = "http://tj.xiaozhu.com/fangzi/28657302903.html"
wb_data = requests.get(url)
print(wb_data.text)
soup = BeautifulSoup(wb_data.text,"lxml")
titles = soup.select("body > div > div > div > h4 > em")
names = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p")
print(names)
for title,name in zip(titles,names):
    data ={
        "title" : title.get_text(),
        "name" : title.get_text()
    }


resp = requests.get("http://tor1024.com/static/proxy_pool.txt")
ips_txt = resp.text.strip().split("\n")
ips = []
for i in ips_txt:
    try:
        k = json.loads(i)
        ips.append(k)
    except Exception as e:
        print(e)
r = requests.get("http://bj.ganji.com/",proxies=random.choice(ips),timeout=6)
print(r)