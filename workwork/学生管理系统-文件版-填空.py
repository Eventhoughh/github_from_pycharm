#  本系统能够对学生信息进行日常管理，如：增删改查操作。程序退出前将数据保存到文件。
# @File   : 学生管理系统-文件版.py
# 本程序涉及知识点：
#  字典，列表，函数，全局变量，csv文件读写


import csv

title = ['姓名', '性别', '手机号码']
data_file = "student.csv"

# 用列表保存所有学生信息，每个学生的信息用字典保存
students = []


# 打印功能提示
def print_menu():
    print("=" * 30)
    print("学生管理系统V1.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示所有学生信息")
    print("0.退出系统")
    print("=" * 30)


# 装载学生信息
def load_data():
    pass


# 保存学生信息到文件
def save_to_file():
    pass


# 添加一个学生信息
def add_info():
    new_name = input("请输入新学生的名字：")
    new_sex = input("请输入新学生的性别:(男/女)：")
    new_phone = input("请输入新学生的手机号码：")
    student = {'姓名': new_name, '性别': new_sex, '手机号码': new_phone}
    global students
    students.append(student)  # 列表追加


# 删除指定序号的学生
def del_info():
    global students
    del_number = int(input("请输入要删除的序号：")) - 1
    del students[del_number]


# 修改指定序号的学生
def modify_info():
    student_id = int(input("请输入要修改的学生的序号："))
    new_name = input("请输入新学生的名字：")
    new_sex = input("请输入新学生的性别:(男/女)：")
    new_phone = input("请输入新学生的手机号码：")
    global students
    students[student_id - 1]['name'] = new_name
    students[student_id - 1]['sex'] = new_sex
    students[student_id - 1]['phone'] = new_phone


def show_info():
    print("=" * 30)
    print("学生的信息如下：")
    print("=" * 30)
    print("序号，姓名，性别，手机号码")
    i = 1
    for temp in students:
        print(f"{i}，{ temp['姓名']}，{ temp['性别']}，{temp['手机号码']}")
        i += 1


def main():
    load_data()
    while True:
        print_menu()
        key = input("请输入功能对应的数字：")
        if key == '1':
            add_info()
        elif key == '2':
            del_info()
        elif key == '3':
            modify_info()
        elif key == '4':
            show_info()
        elif key == '0':
            quit_confirm = input("亲，真的要退出么？(Y or N):")
            if quit_confirm == "Y" or quit_confirm == "y":
                save_to_file()
                break
            else:
                print("输入有误，请重新输入")


main()
