# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Example 2:
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.


n =[1,1,2,2,2,3]
dic={}
for i in n:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
res=[]
s= dict(sorted(dic.items(), key=lambda item: (item[1],-item[0])))
for key, value in s.items():
            res.extend([key]*value)
print(res)

