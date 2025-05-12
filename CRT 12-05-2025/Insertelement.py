'''Insert an element
Write a program to insert an element in an array at the given
position. If the position where the element is to be inserted is
greater than the size of the array display "Invalid Input".


Input format:
The first integer corresponds to the size of the array.Read n
elements into an array line by lineNext integer corresponds to
the position where the element is to be inserted.Next integer
corresponds to the element to be inserted.


Output format:
Print array after insertion'''

n=int(input())
l=[]
for _ in range(n):
     l. append(int(input()))
ele=int(input())
if pos‹0 or pos>n+1:
    print("Invalid Input")
else:
     1.insert(pos-1,ele)
for i in 1:
print(i)
