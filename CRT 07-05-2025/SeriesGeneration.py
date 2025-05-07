'''Series Generation
Write a program to generate the following series 7, 5, 8, 6, 9 ....

Input format:
Read n value

Output format:
Print series


Sample input
5
Sample output
7 5 8 6 9
'''

'''PROGRAM'''
n=int(input())
st=7
print(7,end=" ")
for i in range(1,n):
    if i%2 != 0:
        st=st-2
        print(st,end="")
    else:
        st=st+3
        print(st,end=" ")
