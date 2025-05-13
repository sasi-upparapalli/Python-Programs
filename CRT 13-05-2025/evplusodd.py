'''
Sample input
6
2 6 10 4 9 11

Sample output
6 9 10 4 2 11
'''
n=int (input())
x=list(map(int, input().split()))
x. sort()
l=[]
m=[]
for i in range(len(x)):
    if i%2 == 0:
      l.append(x[i])
    else:
      m.append(x[i])
print(*(l+m))
