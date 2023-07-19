# 函数
# 函数的创建与调用
def cal(a, b):
    c = a+b
    return c

result = cal(10, 20)
print(result)

# 函数的参数传递
cal(10, 20)  # 位置实参
cal(b=10, a=20)  # 关键字实参

# 如果是不可变对象，在函数体的修改不会影响实参的值
# 如果是可变对象，在函数体的修改会影响实参的值

# 函数的返回值
# 函数返回多个值时，结果为元组
def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))

# 函数的参数定义
# 个数可变的位置参数--只能是一个
def fun1(*args):
    print(args)

fun1(10)
fun1(10, 20, 30)

# 个数可变的关键字形参--只能是一个
def fun2(**args):
    print(args)

fun2(a=10)
fun2(a=10, b=20, c=30)

# 在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置参数
# 个数可变的位置参数必须放在有个数可变的关键字形参之前

def fun(a, b, *, c, d):  # 从*之后的参数，只能采用关键字参数传递
    pass


