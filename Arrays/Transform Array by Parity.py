# Example 1:

# Input: nums = [4,3,2,1]

# Output: [0,0,1,1]

# Explanation:

# Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
# After sorting nums in non-descending order, nums = [0, 0, 1, 1].
# Example 2:

# Input: nums = [1,5,1,4,2]

# Output: [0,0,1,1,1]

# Explanation:

# Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
# After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].


n= [4,3,2,1]
a=[]
for i in n:
    if i%2==0:
        a.append(0)
    else:
        a.append(1)
a.sort()
print(a)
