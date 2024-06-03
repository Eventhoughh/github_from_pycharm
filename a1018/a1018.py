#
# @Time   : 2022/10/18 
# @Author : wuBerlin
# @File   : a1018.py
import random
# 0, 1 之间的随机小数
print(random.random())
# 10, 100 之间的随机小数
print(random.uniform())
# 10，100之间的整数
print(random.randint())

# 从序列中随机选择一个元素
seq = [1,2,3,4,5,6]
print(random.choice(seq))
# 将序列seq中的元素打乱
random.shuffle(seq)



