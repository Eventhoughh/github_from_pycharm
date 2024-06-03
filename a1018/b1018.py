#
# @Time   : 2022/10/18 
# @Author : wuBerlin
# @File   : b1018.py
# def hello():
#     """
#     输出 hello world
#     :return:
#     """
# #     print("hello world")
# #
# #
# # hello()
# def hello(msg):
#     """
#     输出消息
#     :param msg: 消息
#     :return:
#     """
#     print(msg)
#
#
# hello("lue zbl")
# hello("one love zbl")
#
#===================================================================
# def get_max(x, y):
#     """
#
#     :param x: 数1
#     :param y: 数2
#     :return: 两数的最大值
#     """
#     return x if x > y else y
#
#
# wuwuwu = get_max(8, 9)
# print(wuwuwu)
# print(get_max(88, 33))
#
#===================================================================
# def f(x, y=1):
#     """
#     求两数的加减乘除
#     :param x:
#     :param y:
#     :return:
#     """
#     return x + y, x - y, x * y, x / y
#
# # 序列的打包，解包
# t1, t2, t3, t4 = f(3, 6)
# print(t1, t2, t3, t4)
# t1, t2, t3, t4 = f(6)
# print(t1, t2, t3, t4)


#-======================================================================
##定义函数时使用固定参数（形参）[wuhan]
# def deliver(name, address="wuhan"):
#     return"包裹投递给"+address+"的"+name
# #可设置默认值
# #调用函数时使用位置参数（实参）[zhangsan][wuhan]
# print(deliver("zhangsan", "wuhan"))
# print(deliver("zhangsi", "shanghai"))
# print(deliver("lisi", "shanghai"))
# print(deliver("wangwu"))
# #调用函数时使用关键字参数（实参）
# print(deliver(name="wangwu", address="shanghai"))
# print(deliver(address="shanghai", name="wangwu"))
#
# #调用函数时位置参数和关键字参数混合使用
# #！！！！！！规则：位置参数必须在关键参数之前
# print(deliver("zhangsi", address="shanghai "))
# print(deliver(name="zhangsi " ,"shanghai"))[错误示范]
# =======================================================================

