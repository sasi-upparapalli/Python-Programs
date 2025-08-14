n=[1,2,3,1,1]
a=len(n)
l=0
k=3
temp=0
for i in range(a):
    temp+=n[i]
    if (i-l)==k:
        temp=temp-n[l]
        l+=1
    if (i-l+1)==k:
        print(temp)
