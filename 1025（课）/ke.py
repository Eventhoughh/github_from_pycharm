#
# @Time   : 2022/10/25 
# @Author : wuBerlin
# @File   : ke.py
# import math
#
#
# def make_statistics(*args):
#     """
#     计算若干个数的均值，方差，标准差
#     :param args: 若干个数
#     :return:均值，方差，标准差
#     """
#     n = len(args)
#     mean = sum(args) / n
#     sum1 = 0
#     for i in args:
#         sum1 += (i - mean) ** 2
#     var = sum1 / n
#     atd = math.sqrt(var)  # math包中的开平方sqrt
#
#     return mean, var, atd
#
#
# result = make_statistics(2, 3, 4, 5, 6)
# print(result)
# r1, r2, r3 = make_statistics(2, 3, 4, 5, 6)
# print(r1, r2, r3)
# x = int(input("请输入一个数，求平方"))
# pf = lambda x : x*x#  pf 可直接当做函数名使用
# print(pf(x))
# bidaxiao = lambda x,y:x if x>y else y
# print(bidaxiao(8,9))
# lambda函数有输入和输出：输入是传入到参数列表argument_list的值，输出是根据表达式expression计算得到的值。
# 这里的expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，
# 并且表达式只能是单行的。以下都是合法的表达式：
#
#     1
#     None
#     a + b
#     sum(a)
#     1 if a >10 else 0



# 生成器：在循环中一边循环一边产生(yield)的机制，称为生成器：generator

# 生成器表达式语法格式：
# (expression for value in iterable[if cond_expr])
# 例(gen = x * x for x in range(10))
# 生成器并非创建完整的数据，而是返回一个生成器对象，此对象在每次计算出一个数据后，
# 把这个数据产生(yield)出来。
# 在循环的过程中不断推算出后续元素
# 返回值不是一个值，而是生成器，其函数体内的代码不会被执行
# 1.生成器是可迭代对象。需要使用for循环来访问生成器的元素
# 2.
# gen = (x*x for x in range(10))
# print("生成器对象:", gen)


# def gen(n):
# #     x=0
# #     while x<n:
# #         yield x*x
# #         x+=1
# # for i in gen(10):
# #     print(i)

# 利用生成器函数产生菲波那切数列

def fib_gen(n):
    count = 0
    a ,b=0,1
    while count<n:
        yield a
        a,b=b,a+b
        count+=1
for i in fib_gen(10):
    print(i)


def f2(x):
    return x*x
data1 = [1,2,3,4,5,6,7,8,9]
aaa = map(f2, data1)
data2 = list(aaa)
print(data2)


# reduce 函数





