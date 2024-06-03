#
# @Time   : 2023/3/13 
# @Author : wuBerlin
# @File   : 多态.py
def start(obj):
    obj.speak()
class Animal:
    def speak(self):
        print("动物叫，但不知道那种动物叫")
class Dog(Animal):
    def speak(self):
        print("小狗：汪汪叫")
class Cat(Animal):
    def speak(self):
        print("小猫：喵喵叫")
class Car:
    def speak(self):
        print("小汽车：滴滴~")

start(Car())
start(Cat())
start(Dog())
# 鸭子类型测试也是实现多态的一种手段