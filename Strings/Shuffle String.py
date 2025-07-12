# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.


s = "codeleet"
l=[4,5,6,7,0,2,1,3]
z=list(zip(l,s))
z.sort()
a=''
for i in range(len(z)):
    a+=(z[i][1])
print(a)
