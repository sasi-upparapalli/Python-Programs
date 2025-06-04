n=int(input())
for i in range(n):
 for j in range(i+1,n+1):
 print(j,end=" ")
 for j in range(1,i+1):
 print(j,end=" ")
 print()
  '''
 5
1 2 3 4 5 
2 3 4 5 1 
3 4 5 1 2 
4 5 1 2 3 
5 1 2 3 4 '''
