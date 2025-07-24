# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
# Example 1:
# Input: nums = [1,2,3]
# Output: 6
# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6


n = [-100,-98,-1,2,3,4]
n.sort()
p1=n[-1]*n[-2]*n[-3]
p2=n[0]*n[1]*n[-1]
print(max(p1,p2))
 
