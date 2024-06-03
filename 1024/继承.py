#
# @Time   : 2022/10/24 
# @Author : wuBerlin
# @File   : 继承.py

class Animal:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        return "动物的名字：{0}".format(self.name)
    def move(self):
        print("动一动...")
class Cat(Animal):#继承Animal这个父类
    def __init__(self,name,age):
        super().__init__(name)# super调用父类的构造方法，用于初始化父类的成员变量
        self.age = age
cat = Cat("Tom", 2)
cat.move()
print(cat.show_info())

# 多继承：一个子类可以有多个父类
