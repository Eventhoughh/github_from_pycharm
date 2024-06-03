# @Time   : 2022/10/21
# @Author : wuBerlin
# @File   : 类与对象.py
# 面向对象是一种编程思想，即按照真实世界的思维方式构建软件系统
#定义一个类
# class 类名[(父类)]://object是所有类的父类，可省
#      类体
#有类，就可以通过类，来创建对象,叫创建对象的过程也叫做实例化的过程
# class Car:
#     pass
# car = Car()



# 类的成员包括：

# 成员变量（实例变量（个人的，实例的），类变量（公有的））
# 构造方法
# 成员方法（实例方法（属于实例的方法），类方法（属于类的方法））
# 属性(property)


# 实例变量：就是对象个体独有的“数据”，例如狗狗的名称和年龄等
class dog:
    def __init__(self,name,age):# __init__()方法是构造方法，构造方法用来初始化实例变量
        self.name = name#创建和初始化实例变量name
        self.age = age  #创建和初始化实例变量age
d = dog("qiuqiu", 6)#  创建对象
print(f"我们家的狗狗名叫{d.name},{d.age}岁了")# 实例变量通过"对象.实例变量"形式访问

# 构造方法__init__()也是一种实例方法特殊的

class zaza:
    def __init__(self, name, age ,sex="雌性"):
        self.name=name
        self.age=age
        self.sex=sex

d1 = zaza("qiuqiu", 6)
d2=zaza("bubu", 4, "雄性")
d3=zaza(name="lele", sex = "雌性", age = 9)

print(f"{d1.name},{d1.age}岁,{d1.sex}")
print(f"{d2.name},{d2.age}岁,{d2.sex}")
print(f"{d3.name},{d3.age}岁,{d3.sex}")
# qiuqiu,6岁,雌性
# bubu,4岁,雄性
# lele,9岁,雌性

# 实例方法
class nana:
    def __init__(self, name, age , sex="雌性"):
        self.name=name
        self.age = age
        self.sex = sex
    def run(self):
        print(f"{self.name}在跑...")
    def speak(self, sound):
        print(f"{self.name}在叫， {sound}！")

# 类变量  类变量是属于类的变量，不属于单个对象

class Account:
    interest_rate = 0.0568#类变量利率interest_rate
    def __init__(self, owner, amount):
        self.owner=owner
        self.amount=amount
account = Account("Tony", 800000.0)

print(f"账户名:{account.owner}")
print(f"账户金额:{account.amount}")
print(f"利率:{Account.interest_rate}")#类变量通过“类名.类变量”形式访问

# 类方法与类变量蕾西，属于类，不属于个体实例
class Account:
    interest_rate = 0.0568#类变量利率interest_rate
    def __init__(self, owner, amount):
        self.owner=owner
        self.amount=amount
        

    @classmethod#类方法
    def interest_by(cls, amt):
            return cls.interest_rate * amt

interest = Account.interest_by(12000.0)
print(f"计算利息：{interest}")

