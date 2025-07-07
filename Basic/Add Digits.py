# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
def diG(n):
            r = 0
            s = 0
            while n>0:
                r=n%10
                s+=r
                n=n//10
            if len(str(s))>1:
                return diG(s)
            else:
                return s
n=38
print(diG(n))
