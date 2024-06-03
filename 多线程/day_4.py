#
# @Time   : 2023/3/31 
# @Author : wuBerlin
# @File   : day_4.py
import multiprocessing
import time


def Work():
    for i in range(10):
        print("工作中。。。")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=Work)
    work_process.daemon = True #守护子进程，主进程一结束，子进程自动销毁，不再执行
    work_process.start()
    time.sleep(1)
    print('主进程')
