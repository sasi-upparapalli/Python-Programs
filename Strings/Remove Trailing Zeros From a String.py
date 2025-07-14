# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
# Example 2:

# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".



n= "51230100"
n=int(n)
r=0
while n!=0:
    r=n%10
    if r==0:
        n=n//10
    else:
        break
print(n)
