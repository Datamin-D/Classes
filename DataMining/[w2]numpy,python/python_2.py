# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:53:11 2020

@author: kjw
"""
print("Hello","World!")
print("Hello","World!",sep="")
print("a\tb\t\nc\nd")

num=3
print("I eat %d apples."%num)
s_num="three"
print("I eat %s apples."%s_num)
print("I eat %d apples and %s oranges."%(num,s_num))

print("I eat {0} apples.".format(3))
print("I eat {0} apples and {1} oranges.".format(num,s_num))
print("I eat {0:<10} apples.".format(3))

pi=3.141592
print("pi = {0}".format(pi))
print("pi = {0:0.4f}".format(pi))
print("pi = {0:10.4f}".format(pi))

#variable creation
a=3
a,b=('one','two')
(c,d)=5,3
[e,f]=['three','four']

# if else
costs=eval(input("Enter total costs:"))
revenue=eval(input("Enter total revenue:"))

if costs==revenue:
    result="Break even."
else:
    if costs<revenue:
        profit=revenue-costs
        result="Profit is ${0:,.2f}.".format(profit)
    else:
        loss=costs-revenue
        result="Loss is ${0:,.2f}.".format(loss)
print(result)

# if elif else
costs=eval(input("Enter total costs:"))
revenue=eval(input("Enter total revenue:"))

if costs==revenue:
    result="Break even."
elif costs<revenue:
    profit=revenue-costs
    result="Profit is ${0:,.2f}.".format(profit)
else:
    loss=costs-revenue
    result="Loss is ${0:,.2f}.".format(loss)
print(result)

# for multiplication
for m in range(2,10):
    for n in range(1,10):
        print(m,"*",n,"=",m*n)
    print("--------------")
    
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end="")
    print()

word=input("Enter a word:")
reversedWord=""
for ch in word:
    reversedWord=ch+reversedWord
print("The reversed word is "+reversedWord+".")

# while multiplication
m=2
while m<10:
    n=1
    while n<10:
        print(m,"*",n,"=",m*n)
        n=n+1
    print("--------------")
    m=m+1
    
# function

def triple(num):
    num=3*num
    return num

num=2
print(triple(num))
print(num)

# many arguments

a=5
b=2
c=3
d=10

def sum_n(*args):
    temp_sum=0
    for i in args:
        temp_sum=temp_sum+i
    return temp_sum

sum_n(a,b,c)

sum_n(a,b,d,c)
