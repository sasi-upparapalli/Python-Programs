s=input()
u=0
l=0
d=0
c=0
for i in s:
   if i.isupper():
     u=u+1
   elif i.islower():
       l=l+1
   elif i.isdigit():
     d=d+1
   else:
     c=c+1
print("Upper",u)
print("Lower",l)
print("Digits",d)
print("Special Characters",c)

'''
Upper 3
Lower 3
Digits 2
Characters '''
