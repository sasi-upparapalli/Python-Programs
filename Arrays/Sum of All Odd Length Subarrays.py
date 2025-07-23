# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# Example 2:

# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.


arr = [1,4,2,5,3]
res = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        m=arr[i:j+1]
        if len(m)%2!=0:
            res=res+sum(m)
#######or##########
for i in range(len(arr)):
    sub_arr = [arr[i]]
    res += arr[i]
    for j in range(i + 1, len(arr)):
        sub_arr.append(arr[i])
        print(sub_arr)
        if len(sub_arr) % 2 != 0:
            res += sum(sub_arr)
print(res)
