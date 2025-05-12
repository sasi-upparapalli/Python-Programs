'''Cab Service for employees
Wipro 2022
A company wishes to provide cab service for their N employees. The
employees have distance ranging from 0 to N-1. The company has
calculated the total distance from an employee's residence to the
company, considering the path to be followed by the cab is a straight
path. The distance of the side of the company is represented with a
negative sign. The distance for the employees who live to the right
side of the company is represented with a positive sign. The cab will
be allotted a range of distance. The company wishes to find the
distance for the employees who live within the particular distance
range. Write an algorithm to find the distance for the employees who
live within the distance range.
Input format:
The first line of the input consists of three space-separated integers-
num, start and end
representing the size of the list (N);
the starting value of the range:
and the ending value of the range, respectively.'''

a, b, c=map(int, input().split())
x=list(map(int, input().split()))
z=0
for i in range(a):
    if x[i]>=b and x[i] <= c:
    Z+=1
print(x[i],end=' ')
if z == 0:
    print(-1)
