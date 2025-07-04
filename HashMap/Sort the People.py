# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        m=list(zip(h,n))
        l=[]
        for i in range(len(m)):
            m=sorted(m,reverse=True)
            l.append(m[i][1])
        return l
        # dic={}
        # a=0
        # for i in n:
        #     dic[i]=h[a]
        #     a=a+1
        # dic=sorted(dic,key=dic.get)
        # print(dic[::-1])
obj=Solution()
n = ["Mary","John","Emma"]
h= [180,165,170]
print(obj.sortPeople(nums))
