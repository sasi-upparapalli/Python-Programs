'''Wipro 2022
In an online maths tutorial a student is given a list of N
numbers. From this list, the student is required to sum each
element in the list such that the ith element in the output list
will be equal to the sum to the first element until the ith
element in the list.


Input format:
The first line of input consists of an integer - numSize
representing the count of total numbers in the list(N).The next
line consists of N space separated integers.element1,
element2, ...... element-n representing the numeric value in the
list.

Output format:
Print the elements

Sample input
5
14263

Sample output
1 5 7 13 16'''
n=int (input())
x=list(map(int,input().split()))
s=0
1=[]
for i in range(len(x)):
  s=s+x[i]
  l.append(s)
print(*l)
