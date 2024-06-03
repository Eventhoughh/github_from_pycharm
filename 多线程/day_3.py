#
# @Time   : 2023/3/29 
# @Author : wuBerlin
# @File   : day_3.py
#
# @Time   : 2023/3/29
# @Author : wuBerlin
# @File   : day_2.py
import multiprocessing
import time
import os
ppid = os.getppid()
pid = os.getpid()
def sing(num,name):
    print("唱歌进程的pid",pid)
    print("父进程",ppid)
    for i in range(num):

        print(name)
        print("唱歌")
        time.sleep(0.5)


def dance(num,name):
    print('跳舞进程的pid',pid)
    print("父进程", ppid)
    for i in range(num):
        print(name)
        print("跳舞")
        time.sleep(0.5)

if __name__ == '__main__':

# 创建子进程
    # 使用args：元组方式给指定任务传参   元组的元素顺序就是任务的参数顺序
    sing_processing= multiprocessing.Process(target=sing,args=(3,"xiaoming"))
    # kwargs:使用字典给指定任务传参   key名就是参数的名字
    dance_processing=multiprocessing.Process(target=dance,kwargs={"name":"zhangbolin",'num':2})
# 启动子进程
    sing_processing.start()
    dance_processing.start()