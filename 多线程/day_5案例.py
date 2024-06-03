#
# @Time   : 2023/3/31 
# @Author : wuBerlin
# @File   : day_5案例.py
import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    # 1，拼接源文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    # 2，打开源文件和目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:

            # 3，循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':

    # 一，定义源文件夹所在路径，目标文件夹所在路径
    source_dir = "D:"
    dest_dir = "C:"
    # 二，创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("该文件夹已创建")
    # 三，通过os.listdir获取原目录中的文件列表
    file_list = os.listdir(source_dir)
    # 四，遍历每个文件，定义一个函数，专门实现文件拷贝
    for file_name in file_list:
        # 五，采用进程实现多任务，完成高并发拷贝
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()
