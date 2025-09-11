# Example 1:

# Input: s = "lEetcOde"
# Output: "lEOtcede"
# Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
# Example 2:

# Input: s = "lYmpH"
# Output: "lYmpH"
# Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".


s = "lEetcOde"
a=""
b=""
for i in s:
   if i in "aeiou" or i in "AEIOU":
      a=a+i
   else:
      b=b+i
z=list(a)
z.sort()
m=''
j=0
k=0
for i in range(len(s)):
   if s[i] in "aeiou" or s[i] in "AEIOU":
      m=m+z[j]
      j=j+1
   else:
      m=m+b[k]
      k=k+1
print(m)
