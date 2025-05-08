'''
Trailing Zeros
(Wipro 2022)

You are playing an online game. In the game, a numbers is displayedon the screen. In order to win the game, you have to Count the
trailing zeros in the factorial value of the given number. Write analgorithm to count the trailing zeros in the factorial value of the given number.


Input format:
The input consists of an integer num, representing the number
displayed on the screen

Output format:
Print An integer representing the count of trailing zeros in the
factorial of the given numbers.


Sample input
5
Sample output
'''PROGRAM'''
n=int(input())
fact=1
r=0
c=0
for i in range(1,n+1Z):
    fact=fact*i
for i in range(len(str(fact))):
    r=fact%10
    if r == 0:
        c=c+1
        fact=fact//10
    else:
        break
        fact=fact//10
print(c)
