'''Sum of series
Write a Python program to find the sum of the series 2 +22 + 222 +2222 + .. n terms

Input format:
Line 1: < Integer Number>

Output format:
<Integer Number - sum of the series>


Sample input
5
Sample output
24690'''

'''PROGRAM'''
n=int(input())
for i in range(1,n+1):
  z="2"*i
  s=s+int(z)
print(s)
