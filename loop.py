# -*- coding: utf-8 -*-
names = ['Michael','Bob','Joey']
for name in names:
    print('hello',name)

sum = 0;
for x in range(101):
    sum = sum+x
print(sum)

#冒泡法排序
read =1
numbers = []
while read >0:
    t = input('Please input a number,# end')
    if t!='#':
        numbers.append(int(t))
    else:
        read=0;

n=len(numbers)
for i in range(n-1):
    for j in range(n-1-i):
        if numbers[j]>numbers[j+1]:
            t=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=t
print(numbers)




