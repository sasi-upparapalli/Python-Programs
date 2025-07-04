# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        # j=set(j)
        # c=0
        # for i in s:
        #     if i in j:
        #         c+=1
        # return c
        dic={}
        for i in s:
            if i  not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        m=0
        for i in range(len(j)):
            c=j[i]
            if c in dic:
                m=m+dic[c]
        return m
        
    
