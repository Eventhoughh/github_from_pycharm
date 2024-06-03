#
# @Time   : 2023/3/15 
# @Author : wuBerlin
# @File   : get.py
import requests
re = requests.get("https://www.douban.com//")
if re.ok:
    print(re.status_code)
else:
    print("请求失败")




