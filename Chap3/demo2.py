# 递归函数
# 使用递归计算阶乘
def fac(n):
    if n == 1:
        return 1;
    else:
        return n*fac(n-1)

print(fac(5))

# 斐波那契数列
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
