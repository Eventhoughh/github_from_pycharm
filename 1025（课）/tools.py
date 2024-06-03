#
# @Time   : 2022/11/1 
# @Author : wuBerlin
# @File   : tools.py
n = str(input("请输入要判断的字符串"))

def is_hui(n):
    if len(n) < 2:
        return True
    if n[0] == n[-1]:
        return is_hui(n[1:-1])#       [1:-1]  =>  掐头去尾1个数

    else:
        return False
print(is_hui(n))

print(f"__name__:变量的值{__name__}")
s = "斗鸡山上山鸡斗"
result = is_hui(s)
print("是回文") if result else print("不是回文")