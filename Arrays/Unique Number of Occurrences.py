# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false

a= [1,2,2,1,1,3,2]
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
counts = list(dic.values())
f = len(counts) == len(set(counts))
print(f)
