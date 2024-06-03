#
# @Time   : 2023/3/13 
# @Author : wuBerlin
# @File   : chunai.py
class Horse:
    def __init__(self,name):
        self.name = name #实例变量name
    def show_info(self):
        return "ma的名字：{0}".format(self.name)
    def run(self):
        print("ma跑")

class Donkey:
    def __init__(self,name):
        self.name = name  #实例变量name
    def show_info(self):
        return "驴的名字：{0}".format(self.name)
    def run(self):
        print("驴跑。")
    def roll(self):
        print("驴打滚。。。")
class AI(Horse,Donkey):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age #实例变量age
    def show_info(self):
        return "骡：{0}, {1}岁".format(self.name, self.age)

m = AI("骡保利", 1)
m.run()
m.roll()
print(m.show_info())
