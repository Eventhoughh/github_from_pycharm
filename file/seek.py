#
# @Time   : 2022/11/8 
# @Author : wuBerlin
# @File   : seek.py
with open('test.txt', 'r', encoding= 'utf-8')as f:
    words=f.read(len("hello!")+1)
    print(words)
    print(f.tell())
