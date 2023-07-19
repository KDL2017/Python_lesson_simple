# 集合--可变,元素不可重复,无序
# 创建
s = {2,3,4,5,5,6,7,7}
print(s)
s1 = set(range(6))
s2 = set([1,2,3,5,6,8])
s3 = set((1,5,4,564))
s4 = set('Python')

# 判断--in | not in

# 新增
s.add(80)
s.update({200, 300, 400})  # update参数可以是集合，列表，元组

# 删除
s.remove(100)
# s.remove(500) 报错
s.discard(500)
s.pop()  # 删除一个任意元素
s.clear()

# 关系
# 是否相等：== | !=
# 子集：issubset
# 超集：issuperset
# 是否有交集：isdisjoint--没交集为True

# 数学操作--原集合不变
# 交集
print(s1.intersection(s2))
print(s1 & s2)
# 并集
print(s1.union(s2))
print(s1 | s2)
# 差集
print(s1.difference(s2))
print(s1 - s2)
# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 集合生成式
{i*i for i in range(10)}
