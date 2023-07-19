# 继承
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name, self.__age)

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    # 方法重写
    def info(self):
        super().info()
        print('学号:{0}'.format(self.stu_no))

class Teacher(Person):
    def __init__(self, name, age, tea_no):
        super().__init__(name, age)
        self.tea_no = tea_no

# 多继承
class A(object):
    pass

class B(object):
    pass

class C(A, B):
    pass
