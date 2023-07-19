# 字典--可变，无序, key不可重复但value可以
# 创建
scores = {'张三':100, '李四':98, '王五':45}
stu = dict(name='jack', age=20)

# 获取
scores['张三']
scores.get('张三')
scores.get('陈六', 99)

# key的判断
# in | not in

# 删除
# del scores['张三']
# clear() 清空

# 新增
# scores['陈六']=98

# 修改
# scores['陈六']=100

# 获取字典视图
# keys() values() items()

# 字典元素的遍历
for item in scores:
    print(item, scores[item])

# 字典生成式 zip()
items = ['Fruits', 'Books', 'Others']
prices = [96,78,85]
d = {item.upper():price for item,price in zip(items,prices)}
print(d)
