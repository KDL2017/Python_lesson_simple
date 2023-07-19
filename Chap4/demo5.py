# 多态
class Animal(object):
    def eat(self):
        print('动物要吃东西')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Person(object):
    def eat(self):
        print('人吃五谷杂粮')

    def __new__(cls, *args, **kwargs):
        print('__new__被调用了，cls的id值为{0}'.format(id(cls)))
        obj = super.__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Person())

# 特殊属性
x = Animal()
print(x.__dict__)  # 实例对象的属性字典
print(Animal.__dict__)
print(x.__class__)
print(Cat.__bases__)  # 父类
print(Cat.__mro__)  # 类的层次结构
print(Animal.__subclasses__())  # 子类

# 特殊方法
# __len__()
# __add__()
# __new__()
# __init__()


