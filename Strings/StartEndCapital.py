 n=input()
 n=n.split()
 for i in range(len(n)):
    if len(n[i])>1:
        n[i]=n[i][0].upper()+n[i][1:-1]+n[i][-1].upper()
    else:
        s[i]=s[i].upper()
 print(" ".join(n))
'''
 raghu college
 RaghU CollegE
 '''
