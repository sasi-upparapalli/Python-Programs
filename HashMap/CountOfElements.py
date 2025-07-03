a=[1,5,8,0,1,8,1,5,1]
dici={}
for i in a:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
for i in dici:
    print(i,"-->",dici[i])

'''
Output:-
1 --> 4
5 --> 2
8 --> 2
0 --> 1
'''
