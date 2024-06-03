#
# @Time   : 2023/3/17 
# @Author : wuBerlin
# @File   : 开爬.py
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41"
}
for start_num in range(0,250,25):#从0 到250 步长25
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)#f：去格式化
    html = response.text
    soup = BeautifulSoup(html, "html.parser")#parser:解析器
    all_titles = soup.findAll("span", attrs={"class":"title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
