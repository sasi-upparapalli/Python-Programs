# Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

k = "the quick brown fox jumps over the lazy dog"
dic = {}
for i in k:
    if i != " " and i not in dic:
        dic[i] = 1
s = ""
for i in dic:
    s += i
alp = "abcdefghijklmnopqrstuvwxyz"
z = dict(zip(s, alp))
me = "vkbs bs t suepuv"
res = ""
for i in me:
    if i == " ":
        res += " "
    else:
        res += z[i]
print(res)
