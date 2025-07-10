# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

def chi(s):
    s=s.split()
    z=" "
    for i in s:
        i=i[::-1]
        z=z+" "+i
        z=z.strip()
    return z
s="Let's take LeetCode contest"
print(chi(s))
