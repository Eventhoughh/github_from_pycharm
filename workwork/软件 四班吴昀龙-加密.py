#
# @Time   : 2022/11/13 
# @Author : wuBerlin
# @File   : 软件 四班吴昀龙-作业.py
file=open("111.txt","r")
content=file.readline()
list1=list(content)
file.close()


for i in range(0,len(list1)):
    if list1[i].islower():
        if list1[i]=='z':
            list1[i]=chr(97)
            continue

        num=ord(list1[i])
        list1[i]=chr(num+1)
    if list1[i].isupper():
        if list1[i]=='Z':
            list1[i]=chr(65)
            continue
        num=ord(list1[i])
        list1[i]=chr(num+1)
new_Str=''.join(list1)
print(new_Str)
file=open("111.txt","w+")
file.write(new_Str)
file.close()



