# Example 1:
# Input: s = "leetcode"
# Output: 0

# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1


s = "leetcode"
dic={}
a=[]
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        a.append(i)
if len(a)>0:
    print(s.index(a[0]))
else:
    print(-1)
