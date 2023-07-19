# 文件的读写操作
file = open('a.txt', 'r', encoding='UTF-8')
print(file.readline())
file.close()

# 常用文件打开模式
# r 只读模式，指针在文件开头
# w 只写模式，文件不存在则创建，存在则覆盖原内容，指针在文件开头
# a 追加模式
# b 以二进制方式打开文件，需要与其它模式一起使用，rb wb
# + 读写方式，需要与其它模式一起使用，a+

