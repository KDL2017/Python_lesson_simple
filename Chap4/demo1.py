# 类的创建
class Student:
    native_place = '吉林'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print(self.name+'在吃饭...')

    # 静态方法
    @staticmethod
    def sm():
        print('我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法')

# 对象的创建
stu1 = Student('张三', 20)
stu1.eat()  # Student.eat(stu1)
print(stu1.name)
print(stu1.age)

# 类方法的使用
Student.cm()

# 静态方法的使用
Student.sm()

# 动态绑定属性
stu1.gender = '男'
print(stu1.gender)

# 动态绑定方法
def show():
    print('这是一个动态绑定的方法')
stu1.show = show


