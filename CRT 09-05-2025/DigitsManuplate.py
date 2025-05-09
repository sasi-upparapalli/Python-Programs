'''
Input : 48513
Output :59402
'''
'''Program'''
n=input()
for i in n:
  if int(i)%2==0:
    print(int(i)+1,end="")
  else:
    print(int(i)-1,end="")
