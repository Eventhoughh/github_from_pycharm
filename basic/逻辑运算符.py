#
# @Time   : 2022/10/18 
# @Author : wuBerlin
# @File   : shi.py
# 逻辑运算符:"非 " not a a为True 结果为False a为False 结果为True
#            “与” and 全True为True 否则就是False
#            “或” or 全False为False 否则就是True
a=1
b=2
def f1():
    print("进入f1函数")
    return True

zhi=a<b or f1()
print(zhi)
zhi2=a>b or f1()
print("==================================")
zhi3=a<b and f1()
zhi4=a>b and f1()
print(zhi4)




