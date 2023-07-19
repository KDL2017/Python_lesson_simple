# 异常处理机制
# try-except
try:
    n1 = int(input('请输入一个整数：'))
    n2 = int(input('请输入另一个整数：'))
    result = n1/n2
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError:
    print('只能输入数字串')
except BaseException as e:
    print(e)
print('程序结束')

# try-except-else-finally
try:
    n1 = int(input('请输入一个整数：'))
    n2 = int(input('请输入另一个整数：'))
    result = n1/n2
except BaseException as e:
    print('出错了')
    print(e)
else:
    print('结果为：', result)
finally:
    print('无论是否产生异常，总会被执行的代码')
print('程序结束')
