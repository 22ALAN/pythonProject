#coding:gbk
fp = open('/home/alan/1.txt','a+')
print("hello world",file=fp)
print(r"hello\nworld\n")
print(ord('乘'))
import keyword
print(keyword.kwlist)
print(0b0101)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.3'))

for item in range(100,1000):
    ge = item%10
    shi = item//10%10
    bai = item//100

    if ge**3+shi**3+bai**3==item:
        print(item)

for i in range(1,10):
    for i in range(1,i+1):
        print('*',end='\t')
    print()


list1=['hello','world',85,'hello']
print(list1.index('hello'))
print(list1.index('hello',1,4))
lst=[10,20,30,40,50,60,70]
print(lst[1:6:1])
print(lst[1:6])