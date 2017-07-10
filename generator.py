# -*- coding: utf-8 -*-

def fib(max): #斐波拉契数列
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles(max): #杨辉三角形
    L = [1]
    n = 0
    while n<max:
        yield L
        L = [L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        n = n+1
        

for i in fib(6):
    print(i)

for i in triangles(6):
    print(i)



