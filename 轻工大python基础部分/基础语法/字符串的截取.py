#
# @Time   : 2023/9/7 
# @Author : wuBerlin
# @File   : __init__.py.py
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长],Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
A = 'weimin'
print(A[0:5:3])
print(A)                 # 输出字符串
print(A[0:-1])           # 输出第一个到倒数第二个的所有字符
print(A[0])              # 输出字符串第一个字符
print(A[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(A[2:])             # 输出从第三个开始后的所有字符
print(A[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(A * 2)             # 输出字符串两次


