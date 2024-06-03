#
# @Time   : 2023/3/29 
# @Author : wuBerlin
# @File   : day_1.py
import multiprocessing
import time


def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(0.5)

if __name__ == '__main__':

# 创建子进程
    sing_processing= multiprocessing.Process(target=sing)
    dance_processing=multiprocessing.Process(target=dance)
# 启动子进程
    sing_processing.start()
    dance_processing.start()