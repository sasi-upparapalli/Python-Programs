n = [5,5,5,25]
alice=0
bob=0
for i in n:
    if i<10:
        alice+=i
    else:
        bob+=i
print(alice,bob)
if alice>bob or alice<bob:
    print("true")
else:
    print("false")
