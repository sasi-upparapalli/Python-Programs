###Bubble Sort

x=list(map(int,input().split()))
 for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
 print(x)
'''
 4 5 5 1 7 3 9 
[1, 3, 4, 5, 5, 7, 9]
'''
