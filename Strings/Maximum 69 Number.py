# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.

def maximum69Number (num):
      z=str(num)
      return int(z.replace('6','9',1))
num=9669
print(maximum69Number(num))


n = 9669
a=n
pos=0
z=-1
r=0
while n!=0:
    r=n%10
    if r==6:
        z=pos
    n=n//10
    pos+=1
if z!=-1:
    a+=(10**(z)*3)
print(a)
