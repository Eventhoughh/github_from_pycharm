#
# @Time   : 2022/10/21 
# @Author : wuBerlin
# @File   : 软件 20304-吴昀龙-函数.py
# def isPrime(n):
#     """
#
#     判断一个整数是不是素数
#     :param n: 整数
#     :return: Ture/False
#     """
#
#
#     flag = True
#     for i in range(2, n):
#             if n % i == 0:
#                 flag = False
#     if flag:
#             return True
#     else:
#             return False
#
#
# n = int(input("请输入你需要判断的数"))
# if isPrime(n):
#     print(f"{n}是素数")
# else:
#     print(f"{n}不是素数")
# count=0
# list = []
# for i in range(2, n):
#     result = isPrime(i)
#     if result:
#         print(i,"是素数")
#         list.append(i)
#         count += 1
#
#
# print(f"该数以内的素数一共有{count}个")

# 判断一个年份是否是闰年

# def is_run(n):
#     if n%4 == 0 and  n%100==0 and n%400==0:
#         return True
#     else:
#         return False
#
# print(is_run(2100))

# 判断是一个数，是否是回文数
# 12321
# n = str(input("请输入要判断的字符串"))
#
# def is_hui(n):
#     if len(n) < 2:
#         return True
#     if n[0] == n[-1]:
#         return is_hui(n[1:-1])#       [1:-1]  =>  掐头去尾1个数
#
#     else:
#         return False
# print(is_hui(n))



# 编写一个函数计算一个整数各个数字之和，使用下面的函数头. 然后编写程序提示用户输入一个整数，显示该整数各个数字之和
# num = int(input("请输入一个数字:"))
# def aaa(num):
#     sum = 0#初始值
#     while num != 0:
#         n = num % 10#求余可得最后一位数
#         sum += n
#         num = num // 10#除以10去掉末尾的数
#     print(sum)
# aaa(num)#传参


#编写一个函数将毫秒换成小时数、分钟数、和秒数，使用下面的函数头。编写程序提示用户输入一个毫秒数，然后显示形如“天：小时：分钟：秒”的字符串
# def hmhuansuan():
#     ms = int(input('请输入毫秒数：'))
#     # 保留两位小数，
#     s = round(ms / 1000, 2)
#     m = round(s / 60, 2)
#     h = round(m / 60, 2)
#     d = round(h / 24, 2)
#     print('{0}换算后等于{1}秒，等于{2}分钟，等于{3}小时,等于{4}天'.format(ms, s, m, h,d))
#
#
# hmhuansuan()







