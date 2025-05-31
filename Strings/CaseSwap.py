#4
s=input()
for i in s:
 if i.isdigit():
 print("INVALID INPUT")
 else:
 if i.isupper():
 i=i.lower()
 else:
 i=i.upper()
 print(i,end="")
'''
 SasIii
sASiII
'''
