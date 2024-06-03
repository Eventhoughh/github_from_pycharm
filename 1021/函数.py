#
# @Time   : 2022/10/21 
# @Author : wuBerlin
# @File   : 函数.py
# 基于元组的可变参数
# def sum(*numbers):
#         aa = 0.0
#         for number in numbers:
#             aa += number
#         return aa
# print(sum(80,90,50))
# print(sum(500,1000))
#基于字典的可变参数
def show_info(**info):
    print("------show_info------")
    for key, value in info.items():
        print("{0} - {1}".format(key, value))
show_info(name="tony", age="18", sex=True)
show_info(student_name="tony", student_no="1000")
#  函数中变量的作用域
x=20

def qwe():
    # global x# 将x升为全局变量
    x = 10
    print("函数中的x", x)
qwe()
print("全局变量", x)

# 函数类型：python中的任意一个函数都有数据类型，这种数据类型是function， 被称为函数类型
# 一个函数可以作为另一个函数的返回值使用
# 一个函数可以作为另一个函数参数使用

# 过滤函数：filter()
# filter(function,iterable) function:提供过滤规则的函数、、。iterable:可迭代对象
def f1(x):
    return x>50

data1 = [50,60,40,20,15,16,96,85,74]
aaa = filter(f1, data1)
data2 = list(aaa)
print(data2)

# 映射函数map(function, iterable)
def f2(x):
    return x*2
data1 = [5,6,25,95]
aaa = map(f2, data1)
data2 = list(aaa)
print(data2)

# lambda函数:"lambda参数列表:lambda体"///////用于定义匿名函数
# 参数列表 没有括号，不换行
# lambda函数有输入和输出：输入是传入到参数列表argument_list的值，输出是根据表达式expression计算得到的值。
# 这里的expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，
# 并且表达式只能是单行的。以下都是合法的表达式：
#
#     1
#     None
#     a + b
#     sum(a)
#     1 if a >10 else 0


