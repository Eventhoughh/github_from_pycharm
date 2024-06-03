#
# @Time   : 2022/11/14 
# @Author : wuBerlin
# @File   : 软件四班吴昀龙-学生管理系统文件版-填空.py
students = []
def load_stu():

    global students

try:

    f = open('students_info.txt')

    students = eval(f.read())

    f.close()

except Exception:

    pass
def save_info(student_info):

    try:

        students_txt = open("students.txt","w") # 以写模式打开，并清空文件内容

    except Exception as e:

        students_txt = open("students.txt", "x") # 文件不存在，创建文件并打开

    for info in student_info:

        students_txt.write(str(info)+" ") # 按行存储，添加换行符

        students_txt.close()