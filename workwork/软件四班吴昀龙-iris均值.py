#
# @Time   : 2022/11/14 
# @Author : wuBerlin
# @File   : 软件四班吴昀龙-iris均值.py
import csv
import numpy as np
fileN = 'C:\\Users\\HP\\Desktop\\iris.csv'
with open(fileN,'r') as FileN:
    reader = csv.DictReader(FileN)
    aa = [row['Sepal.Length'] for row in reader]
    a1 = []
    for col1 in aa:
        a1.append(float(col1))
    FileN.close()
print(np.mean(a1))
with open(fileN, 'r') as FileN:
    reader = csv.DictReader(FileN)
    bb = [row['Sepal.Width'] for row in reader]
    b2 = []
    for col2 in bb:
        b2.append(float(col2))
    FileN.close()
print(np.mean(b2))
with open(fileN, 'r') as FileN:
    reader = csv.DictReader(FileN)
    cc = [row['Petal.Length'] for row in reader]
    c3 = []
    for col3 in cc:
        c3.append(float(col3))
    FileN.close()
print(np.mean(c3))
with open(fileN, 'r') as FileN:
    reader = csv.DictReader(FileN)
    dd = [row['Petal.Width'] for row in reader]
    d4 = []
    for col4 in dd:
        d4.append(float(col4))
    FileN.close()
print(np.mean(d4))

with open(fileN, 'r') as FileN:
    reader = csv.DictReader(FileN)
    iris1 = [iris_item for iris_item in reader]

file_name = 'C:\\Users\\HP\\Desktop\\my_iris.csv'
key = []
for i in iris1[0].keys():
   key.append(i)
with open(file_name, 'w', newline = '') as f:
    write_csv = csv.DictWriter(f, key)
    write_csv.writeheader()
    write_csv.writerows(iris1)


csvFile = open("C:\\Users\\HP\\Desktop\\my_iris.csv", "a")
fileheader = ["aa平均值"]
dict_writer = csv.DictWriter(csvFile, fileheader)
dict_writer.writerow(dict(zip(fileheader, fileheader)))
dict_writer.writerow({"aa平均值": np.mean(a1)})

fileheader = ["bb平均值"]
dict_writer = csv.DictWriter(csvFile, fileheader)
dict_writer.writerow(dict(zip(fileheader, fileheader)))
dict_writer.writerow({"bb平均值": np.mean(b2)})

fileheader = ["cc平均值"]
dict_writer = csv.DictWriter(csvFile, fileheader)
dict_writer.writerow(dict(zip(fileheader, fileheader)))
dict_writer.writerow({"cc平均值": np.mean(c3)})

fileheader = ["dd平均值"]
dict_writer = csv.DictWriter(csvFile, fileheader)
dict_writer.writerow(dict(zip(fileheader, fileheader)))
dict_writer.writerow({"dd平均值": np.mean(d4)})
csvFile.close()
