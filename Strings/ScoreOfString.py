#Find out the sum of the absolute difference between the adjecent letters of string
#INPUT:- s="hello"
#OUTPUT:- 13
s="hello"
su=0
for i in range(len(s)-1):
  a=ord(s[i])
  b=ord(s[i+1])
  m=abs(a-b)
  su+=m
print(su)
