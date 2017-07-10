# -*- coding: utf-8 -*-
#给定一个数组，每个数字代表该点能向后走的最大步数，求从第一个点走到终点用最少步数的方法
def PathPlan(*numbers):
    step = [x for x in range(len(numbers))] #用来记录每个点走到终点的最小步数
    MinstepIndex=[x for x in range(len(numbers)-1)] #用来记录各个点在最优方式下走到下一个点的绝对位置
    for n in range(len(numbers)):
        i=len(numbers)-n-1
        if i==len(numbers)-1: #从最后一个位置开始考虑
            step[i]=0
        else:
            t=numbers[i] #这个位置能走的最大步数
            if (i+t)>len(numbers)-1:
                t=len(numbers)-i-1
            temp=[]
            j=1
            while j<t+1: #列出这个位置能到达的其它所有位置到达终点的最小步数
                temp.append(step[i+j])
                j=j+1
            step[i]=min(temp)+1
            MinstepIndex[i]=temp.index(min(temp))+i+1 #这个点应该走到的绝对位置
            
    print('需要的最小步数是',step[0]) #第0个点到达终点的最小步数就是所求最小步数
    print('经过的点有')
    index = 0
    for n in range(step[0]):
        print('a%s' %MinstepIndex[index])
        index = index + MinstepIndex[index]


a = [3,2,5,1,1,4,3,5,2,2,1]
PathPlan(*a)
            


