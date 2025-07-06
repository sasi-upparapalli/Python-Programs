# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
word = "abcdefd"
ch = "d"
idx = word.find(ch) 
if idx == -1:
    print(word) 
print(word[:idx+1][::-1] + word[idx+1:])
