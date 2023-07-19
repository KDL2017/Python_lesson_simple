# 字符串--不可变
# 驻留机制
a = 'Python'
b = "Python"
print(id(a))
print(id(b))
print(a is b)

# 查询
# index() 第一次出现 rindex() 最后一次出现  --会抛异常
# find() 第一次出现 rfind() 最后一次出现    --找不到返回-1

# 大小写转化
# upper() 全转为大写
# lower() 全转为小写
# swapcase() 大变小，小变大
# capitalize() 第一个字符大写，其余小写
# title() 每个单词的第一个字符大写，剩余字符小写

# 对齐
# center() 居中
s = 'hello,Python'
print(s.center(20, '*'))
# ljust() 左对齐
print(s.ljust(20, '*'))
# rjust() 右对齐
print(s.rjust(20, '*'))
# zfill() 右对齐，0填充
print(s.zfill(20))

# 分割
# split()默认分隔符为空格
# split(sep='|')指定分隔符为|
# split(sep='|', maxsplit=1)最大分割次数为1
# rsplit()从右侧开始分割

# 判断
s.isidentifier()  # 判断是不是合法的标识符
s.isspace()  # 判断是否全部由空白字符组成（回车，换行，水平制表符）
s.isalpha()  # 判断是否全部由字母组成
s.isdecimal()  # 判断是否全部由十进制数字组成
s.isnumeric()  # 判断是否全部由数字组成
s.isalnum()  # 判断是否全部由字母和数字组成

# 替换与合并
print(s.replace('Python', 'Java'))
print(s.replace('Python', 'Java', 2))  # 第三个参数指定最大替换次数

lst = ['hello', 'Python', 'Java']  # 元组也行
print('|'.join(lst))
print('*'.join('Python'))

# 比较
# > >= < <= == !=

# 切片--将产生新的对象

# 格式化字符串
name = '张三'
age = 20
print('他叫%s,今年%d岁' % (name, age))
print('他叫{0},今年{1}岁'.format(name, age))
print(f'他叫{name},今年{age}岁')
print('%10d' % 99)  # 10表示宽度
print('%.3f' % 3.1415926)  # .3表示小数点后三位
print('{0:.4}'.format(3.1415926))  # .4表示4位数
print('{0:.3f}'.format(3.1415926))  # .3f表示小数点后三位

# 编码转换
s1 = '天涯共此时'
print(s1.encode(encoding='GBK'))
print(s1.encode(encoding='UTF-8'))

byte = s1.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
