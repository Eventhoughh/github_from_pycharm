#     可变参数：序列可变参数，，“一个*号表示”，，，字典可变参数“两个**表示”
# args的类型为元组

def test(*args):
    for v in args:
        print(v)

test(1,2,3)   # () 为元组  传入多个实参
test(*(4,5,6)) # 上下表示的皆为元组, *[解包]，   传入元组的时候解压=传入多个实参
test((40,50,60), (60,70,80))# 传入多个实参

#       序列可变参数，求平均值
def average(*args):
    sum=0
    for v in args:
        sum+=v
    return  sum/len(args)

print(average(90,95,60,56,43,15))

print(average(80,43,56,84,54,15))
#         字典可变参数
def test2(**args):
    for key,  value in args.items():
        print(key, value)
    #     a, 实参传递参数用“键=值”对
    #     b, 实参参数用字典
test2(**{"a":1, "b":2})
test2(a=80, b=90)

def order(table_no, *foods, waitress):
    print(f"桌号:{table_no}, 服务生:{waitress}")
    for food in foods:
        print(food)
# 调用函数时位置参数和关键字参数混合使用
# 规则：位置参数必须在关键字参数之前
# print(deliver("张四", address="上海"))
# 可变参数后的固定参数只能用关键字参数
my_food = ["饺子", "米饭", "排骨汤"]
order(1,*my_food, waitress="小李子")
# my_food = ["饺子", "米饭", "排骨汤"]
# order(1,"饺子", "米饭", "排骨汤", waitress="小李子")

#      穿不可变对象和传可变对象
def change_int(aa):
    aa = 10
    print(f"函数里的a={aa}")
myaa = 100
change_int(myaa)
print("函数外的myaa", myaa)



def change_list(lista):
    lista.append([1,2,3])
    print(f"函数内的lista={lista}")

mylist=[100,200]
change_list(mylist)
print(f"函数外的 mylist={mylist}")
# 当向函数传递不可变对象：
# 在函数中对这个对象进行修改不不会改变原始对象的值， 因为会产生一个新的对象
# 当向函数传递可变对象：
# 在函数中对这个对象进行修改，是会影响到原来的对象的
#                   变量的作用域（局部变量，全局变量）
#                       局部变量在函数外无法访问
# 当内部作用域想修改外部作用域的变量是，就用用global关键字，使用global关键字可以在函数中改变全局变量的值

# def func():
#     global num
#     print(num)
#     num = 123
#     print(num)
#
# num = 1
# func()
# print(num)
#   判断一个数是不是素数
def isPrime(n):
    """

    判断一个整数是不是素数
    :param n: 整数
    :return: Ture/False
    """

    flag= True

    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
        return flag

result = isPrime(10)
print("是素数") if result else print("不是素数")


# 找出100以内的素数

for i in range(101):
    result = isPrime(i)
    print("是素数", i) if result else print("不是素数", i)