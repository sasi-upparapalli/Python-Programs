'''
Fibonacci Series
(Wipro 2022)

An e-commerce website wishes to find the lucky customer who will be eligible for full value cash back. For this purpose, a number N is
fed to the system. It will return another number that is calculated by an algorithm. In the algorithm, a sequence is generated, in which
each number is the sum of the two proceeding numbers. Initially the sequence will have two 1's in it. The system will return the Nth number
from the generated sequence which is treated as the order ID. The lucky customer will be the one who has placed that order.
Write an algorithm to help the website find the lucky customer.

Input format:
The input consists of an integer token, representing the number fed to the system (N).


Output format:
Print an integer representing the order ID of the lucky customer.'''

'''PROGRAM'''

n=int(input())
n=n-1
n1,n2=0,1
while n:
    n1,n2=n2,n2+n1
    n=n-1
print(n2)

'''OUTPUT
8 (i/p)
21 (o/p)'''
