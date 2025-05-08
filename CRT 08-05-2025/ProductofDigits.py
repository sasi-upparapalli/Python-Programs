'''
Product of Digits
TCS Ninja 2022
A shop maintains a pricing format for all its products. A value N is printed on each product. When the scanner reads the value N on the
item. the product of all the digits in the value N is the price of the item. The task here is to design the software such that given the
code of any item N the product (multiplication) of all the digits of value should be computed(price).
If the input is negative, all digits should be considered as negative numbers.
Ignore digit 'O' in the given product value N.

Input format:
Read n value

Output format:
Product of digits


Sample input
5244
Sample output
160'''
'''PROGRAM'''
n=input ()
s =- 1 if int(n)<0 else 1
p=1
for i in n:
    if int(i)>0:
        p=p*int(i)
    else:
        break
print(p*s)
