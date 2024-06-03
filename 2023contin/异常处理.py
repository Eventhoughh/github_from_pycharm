# #
# # @Time   : 2023/3/13
# # @Author : wuBerlin
# # @File   : 异常处理.py
# 第一个异常：除零异常
i = input("请输入一个数")
n = 1120
# result = n/int(i)
# print(result)
# print("{0}除以{1}等于{2}".format(n, i,result))
# 语法：：：：
# try:
#     <可能会引发异常的语句>
# except[异常类型]:
#     <处理异常>
try:
    result = n/ int(i)
    print(result)
    print("{0}除以{1}等于{2}".format(n, i, result))
except ZeroDivisionError as e:
    print("emergency！不能除以0，异常：{}".format(e))
except ValueError as v:
    print("emergency输入的非数字,异常：{}".format(v))
# 多重异常捕获
# except(ZeroDivisionError,ValueError) as e:
#     print("异常发生：{}".format(e))


