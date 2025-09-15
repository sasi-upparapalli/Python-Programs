def s(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*s(n-1)
n=3
print(s(n))

# Op:
# 6
