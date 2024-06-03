#
# @Time   : 2022/10/20 
# @Author : wuBerlin
# @File   : 字符串.py

# 格式化字符串
#使用  %
# value = 5623
# format = "这个数的十六进制数为%x"
# print(format % value)
#使用format()方法 格式为str.format(values)

# name= ["张博琳", "吴昀龙"]
# age= (18 , 20)
# string = "姓名:{0} 年龄:{1}"#{}是必要的
# print(string.format(name, age))
# # ==========================================
# name= ["张博琳", "吴昀龙"]
# age= (18 , 20)
# string = "姓名:{name} 年龄:{age}"# 字符串的{}中可以指定名称, 字符串中的{}依次替换为名称是name， age的变量存储的数据
# print(string.format(name=name, age=age))
#使用f-string  格式为f("{变量名}") 或者F("{变量名}")

# age = 18
# gender = "女"
# print(f"年龄：{age}， 性别：{gender}")




#  字符串的常见操作

# 1  查找 find()方法的语法格式  str.find(sub[, strat[, end]])
# sub:指定要查找的子串
# strat:开始索引，默认为0
# end:结束索引，默认为字符串的长度
# t = "t"
# zifuchuan = "python"
# result = zifuchuan.find(t)
# print(result)
# result=2  符合索引开始为0的要求



#2 字符串的替换 语法格式为str.replace(old, new[, count])
# old:被替换的旧子串
# new:替换旧子串的新子串
# count:表示替换旧字符串的次数，默认全部替换
# string = "All thins Are difficult before they Are easy. "
# new_string = string.replace("Are", "are",1) #指定替换一次
# print(new_string)




#3 字符串的分割与拼接
# split()方法可以按照指定分隔符对字符串进行分隔，改方法会返回有分隔后的子串组成的列表
# split()格式为str.split(sep=None,  maxsplit = -1)
# sep:分隔符，默认为空字符
# maxsplit:分隔次数，默认值为-1，表示不限制分割次数
# string = "The more efforts you make, the more fortune you get."
# result = string.split()
# #['The', 'more', 'efforts', 'you', 'make,', 'the', 'more', 'fortune', 'you', 'get.']
# result = string.split("m")
# # ['The ', 'ore efforts you ', 'ake, the ', 'ore fortune you get.']
# result = string.split("e", 2)
# # ['Th', ' mor', ' efforts you make, the more fortune you get.']
# print(result)

#字符串的拼接 join()  格式为  str.join(iterable)// interable 表示连接各个字符串的字符
# interable = "%"
# string = "python"
# result1 = interable.join(string)
# print(result1)
# # p%y%t%h%o%n





# 4  删除字符串的指定字符

# strip()移除头部和尾部的字符
# lstrip()移除字符换头部的指定字符
# rstrip()移除字符串尾部的指定字符
# 语法格式str.strip([chars])//chars表示被移除的字符



# 5  字符串的大小写转换

# upper():将字符串中的小写字母全部转换为大写字母
# lower():将字符串中的大写字母全部转换为小写字母
# capitalize():将字符串中第一个字母转换为大写形式
# titl():将字符串中每个单词的首字母转换为大写形式

# 6 字符串对齐方式

# center() str.center(width[,fillchar])//返回长度为width的字符串，原字符串居中显示
# ljust() str.ljust(width[,fillchar])//返回长度为width的字符串，原字符串左对齐显示
# rjust{} str.rjust(width[,fillchar])//返回长度为width的字符串，原字符串右对齐显示
# 所列的方法中都有相同的参数width和fillchar
# width表示字符串的长度，如果指定的长度小于或等于原字符串的长度，那么以上各个方法会返回原字符串
# fillchar表示参数width指定的长度大于原字符串长度时填充的字符，默认为空格

# sentence = "hello word"
# center_str=sentence.center(2, "-")
# ljust_str=sentence.ljust(20, "*")
# rjust_str=sentence.rjust(20, "&")
#
# print(f"居中对齐的结果为：{center_str}")
# print(f"左对齐的结果为：{ljust_str}")
# print(f"右对齐的结果为：{rjust_str}")