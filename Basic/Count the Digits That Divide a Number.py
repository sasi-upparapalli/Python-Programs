# Example 1:
# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

# Example 2:
# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

n=121
a=list(str(n))
s=0
for i in range(len(a)):
    if n%int(a[i])==0:
        s=s+1
print(s)
