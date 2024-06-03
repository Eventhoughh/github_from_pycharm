#
# @Time   : 2023/3/20 
# @Author : wuBerlin
# @File   : 数据插入.py
from pymysql import Connection
conn = Connection(
    host = "localhost",#主机名（IP地址）
    port=3306,# 端口，默认3306
    user="root",#账户名
    password=""#密码
)
#获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("wz_jt")
# 执行sql
cursor.execute("insert into dept values(50, '测试部', '武汉')")
#   第一种，，数据插入需要手动确认通过commit
conn.commit()

#关闭链接
conn.close()

# #   第二种，设置自动提交 autocommit = True
# from pymysql import Connection
# conn = Connection(
#     host = "localhost",#主机名（IP地址）
#     port=3306,# 端口，默认3306
#     user="root",#账户名
#     password="" #密码
#     autocommit = True #设置自动提交
# )



