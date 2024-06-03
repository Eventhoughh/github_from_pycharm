#
# @Time   : 2022/11/8 
# @Author : wuBerlin
# @File   : write.py
#清除写
with open("poem.txt", "w", encoding="UTf-8") as f:
    # 以写模式打开
    # 如果该文件不存在创建一个新文件，
    # 如果该文件已存在，打开文件时，将内容清除，文件游标放在文件头
    f.write("仰天大笑出门去\n")
    f.write("我辈岂是蓬蒿人\n")
    # write向文件中写入一个字符串
lines = ["仰天大笑出门去\n", "我辈岂是蓬蒿人\n"]
with open("poem2.txt", "w", encoding="UTf-8") as f:
    f.writelines(lines)
    # writelines向文件中写入一个序列（多个字符串构成的序列）
