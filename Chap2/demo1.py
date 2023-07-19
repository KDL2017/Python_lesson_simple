# 列表--有序，可存储重复数据,动态分配和回收内存
# 创建
lst = ['hello', 'world', 98, 'hello']
lst2 = list(['hello', 'world', 98])

# 查询
print(lst.index('hello'))  # 如果有相同元素，只返回第一个的索引
print(lst.index('hello', 1, 3))

# 获取
print(lst[2])
print(lst[-3])

# 切片
# 列表名[start:stop:step]

# 判断
# in 和 not in

# 遍历
for item in lst:
    print(item)

# 添加
# append() 末尾添加一个
# extend() 末尾至少添加一个
# insert() 任意位置添加一个
# 切片      任意位置添加任意个

# 删除
# remove() 移除一个元素，重复元素移除第一个
# pop() 指定索引，不指定移除最后一个
# 切片
# clear() 清空列表
# delete() 删除列表

# 修改
# 指定元素索引 或 指定切片

# 排序
# lst.sort() 默认升序,reverse=True降序
# sorted(lst) 生成一个新列表

# 列表生成式
# [i*i for i in range(1,10)]

