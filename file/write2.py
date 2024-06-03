#
# @Time   : 2022/11/8 
# @Author : wuBerlin
# @File   : write2.py
#追加写append

with open ("poem.txt", "a", encoding="utf-8") as f:
    f.write("this is append line\n")

lines = ["床前明月光\n", "疑是地上霜\n", "举头望明月\n", "低头思故乡\n"]
with open ("poem.txt", "a", encoding="utf-8") as f:
    f.writelines(lines)
