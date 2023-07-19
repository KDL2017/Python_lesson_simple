# 元组--不可变,没有增删改操作,有序
# 创建
t = ('Python', 'world', 98)
t1 = tuple(('Python', 'world', 98))
t2 = (10,)  # 如果只有一个元素，逗号不能省

# 可变与不可变
t3 = (10, [20, 30], 9)
# t3[1]=100 不可行
t3[1].append(100)  # 可行

# 遍历
for item in t:
    print(item)

