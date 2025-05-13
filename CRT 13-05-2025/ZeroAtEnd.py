'''A chocolate factory is packing chocolates into the packets.
The chocolate packets here represent an array arrt of N
number of integer values. The task is to find the empty
packets(O) of chocolate and push it to the end of the
conveyor belt(array).
For Example:N=7 and arr = [4,5,0,1.9,0,5,0].There are 3 empty
packets in the given set. These 3 empty packets represented
as O should be pushed towards the end of the array
Input forat:
Read size of the arrayRead elements of the array line by line

Output format:
Print the elements

Sample input
7
4
5
0
1
9
0
5

Sample output
4 5 1 9 5 0 0'''
n=int (input())
l=[]
x=[]
y=[]
for i in range(n):
  m=int(input())
  l. append(m)
for i in l:
if i != 0:
  x. append(i)
else:
  y. append(i)
print(*(x+y))
