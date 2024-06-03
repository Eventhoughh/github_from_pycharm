import csv

def read_csv(file_path):
    data = []
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过标题行
        for row in reader:
            data.append(row[0])
    return data

customer_names = ["李明1", "李明2", "李明3"]

# 在这里可以使用customer_names列表进行参数化测试
for name in customer_names:
    new_customer_name = name
    # 执行新增客户的操作，将new_customer_name传递给相应的函数或方法
    # 例如，可以调用一个名为add_customer的函数，并将new_customer_name作为参数传递
    add_customer(new_customer_name)