# -*- coding: utf-8 -*-

steps = [] 
def hanoi(n, a="A", b="B", c="C"): #盘按大小从1到n
    if n == 1:
        step = a + str(n)+"-->" + c+str(n) #1个时，直接从A移到C
        steps.append(step)
    else:
        hanoi(n-1, a,c,b) #将n-1个借助C从A移到B 再把最大的从A移到C
        step =  a+str(n) + "-->" + c+str(n)
        steps.append(step)
        hanoi(n-1, b, a, c) #将n-1个借助A从B移到C
hanoi(5)
print("移动次数为：%d \n操作步骤为：\n%s" % (len(steps),steps))


