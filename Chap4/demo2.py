# 封装
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)

stu = Student('张三', 20)
stu.show()

print(stu.name)
print(stu._Student__age)  # 在类的外部可以通过 _Student__age 进行访问
