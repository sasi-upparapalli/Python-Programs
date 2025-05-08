'''
Sum of odd digits
(Wipro 2022)

An e-commerce company plans to give their customers a discount for the New Years holiday. The discount will be calculated on the basis
of the bill amount of the order placed. The discount amount is th esum of all the odd digits on the customer's total bill amount. If no
odd digit is present in the bill amount, then the discount will be zero. Write an algorithm to find a discount for the given total bill amount.


Input format:
The input consists of an integer bill amount, representing the
customer's total bill amount.

Output format:
Print an integer representing the discount for the given total bill amount.

Sample input
2514795
Sample output
27
'''
'''PROGRAM'''
n=int(input())
r=0
S=0
le=len(str(n))
for i in range(le):
    r=n%10
    if r%2 != 0:
        s=s+r
        n=n//10
    else:
        r=0
        n=n//10
print(s)
