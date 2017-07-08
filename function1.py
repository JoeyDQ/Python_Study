# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    f = b**2 - 4*a*c
    if f < 0:
        return ("方程无解")
    elif f == 0:
        return (-b/(2*a))
    else:
        x1=(-b+math.sqrt(f))/(2*a)
        x2=(-b-math.sqrt(f))/(2*a)
        return x1,x2
#定义可变参数函数，numbers接收到的是一个tuple
def calc(*numbers):
    sum=0
    for n in numbers:
        sum = sum+n*n
    return sum

#a = int(input('请输入a的值: '))
#b = int(input('请输入b的值: '))
#c = int(input('请输入c的值: '))
#print(quadratic(a,b,c))
print(calc(1,2,3))
nums = [1,2,3]
print(calc(*nums))



