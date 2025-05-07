'''
Armstrong number
Write a program to check whether the given number is an Armstrongnumber or not.Armstrong Number:abcd ... = pow(a,n) + pow(b,n) +pow(c,n) + pow(d,n) + .... where n represents the number of digits

Input format:
Read a no

Output format:
Print "Yes" if armstrong no else print "No"

Sample input
153
Sample output
Yes
'''
'''PROGRAM'''
n=int(input())
z=len(str(n))
m=n
r=0
s=0
while n:
  r=n%10
  s=s+(r**z)
  n=n//10
if(s==m):
  print("Yes")
else:
  print("No")
