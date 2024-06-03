#
# @Time   : 2023/3/20 
# @Author : wuBerlin
# @File   : 创建数据库链接.py
from pymysql import Connection
conn = Connection(
    host = "localhost",#主机名（IP地址）
    port=3306,# 端口，默认3306
    user="root",#账户名
    password=""#密码
)
#获取游标对象
cursor = conn.cursor()
conn.select_db("wz_jt")    # 选择数据库
# 使用游标对象
cursor.execute("create table test_pymysql(id int)")

# 打印MySQL数据库软件信息
# print(conn.get_server_info())
# 关闭到数据库的链接
# conn.close()