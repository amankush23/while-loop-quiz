''' 

Write a program that generates and prints the first n terms of the Fibonacci
sequence using a while loop.

'''
n=int(input("enter the number:"))
i=2
a=0
b=1
while n==0 or n==1:
    print (n)
    break

while i<=n:
    c=a+b
    a=b
    b=c
    i+=1
    print(c)