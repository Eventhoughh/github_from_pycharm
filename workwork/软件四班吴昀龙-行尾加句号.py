#
# @Time   : 2022/11/14 
# @Author : wuBerlin
# @File   : 软件四班吴昀龙-行尾加句号.py
filename = ('C:\Users\xiaoming\Nox_share\AppShare\demo.py')
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))

lines = [line.rstrip().ljust(maxLength)+''
for index, line in enumerate(lines)]
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)

