n = int(input("Enter n: "))

res = []

# If n is odd, include 0
if n % 2 == 1:
    res.append(0)

# Add pairs (i, -i)
for i in range(1, n // 2 + 1):
    res.append(i)
    res.append(-i)

print(res)
