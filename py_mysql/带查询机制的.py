#
# @Time   : 2023/3/20 
# @Author : wuBerlin
# @File   : 待查询机制的.py
from pymysql import Connection
conn = Connection(
    host = "localhost",#主机名（IP地址）
    port=3306,# 端口，默认3306
    user="root",#账户名
    password=""#密码
)
cursor = conn.cursor()   #获取到游标对象
conn.select_db("wz_jt")    # 选择数据库
cursor.execute("select * from dept")


ku = cursor.fetchall()
for r in ku:
    print(r)

conn.close()
