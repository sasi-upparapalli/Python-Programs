'''Sum of Numbers
Write a program to print the sum of the given numbers. The values must be scanned until the user enters -1 as value.

Input format:
Input consists of a list of integers.

Output format:
The output consists of the sum of the given integers.

Sample input
1
2
3
4
-1
Sample output
10'''
'''PROGRAM'''
s=0
while(1):
    n=int(input ())
    if n>0:
        s=s+n
    else:
        break
print(s)
