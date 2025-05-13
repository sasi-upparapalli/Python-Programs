'''TCS Ninja 2022
A party has been organised on cruise. The party is organised
for a limited time(T). The number of guests entering (E[i]) and
leaving (L[I]) the party at every hour is represented as
elements of the array. The task is to find the maximum
number of guests present on the cruise at any given instance
within T hours.
Input format:
Read size of the arrayRead elements for in-guest arrayRead
elements for out-guest array
Output format:
Print highest guests available in a party based on hours
Sample input
5
7 0 5 1 3
1 2 1 3 4

Sample output
8'''
n=int (input())
e=list(map(int, input().split()))
o=list(map(int, input().split()))
s=0
z=[]
for i in range(n) :
  s=s+e[i]-o[i]
  z.append(s)
print(max(z))
