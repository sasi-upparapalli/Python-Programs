# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"


class Solution:
    
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1 , len(num2)-1
        carry=0
        result=[]

        while i>=0 or j>=0 or carry:
            dig1=int(num1[i]) if i>=0 else 0
            dig2=int(num2[j]) if j>=0 else 0

            total=dig1+dig2+carry
            carry=total//10
            result.append(str(total%10))

            i-=1
            j-=1
        
        return "".join(reversed(result))
