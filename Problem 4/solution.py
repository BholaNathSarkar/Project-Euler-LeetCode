pallindrome = []
for i in range(100,1000):
    for j in range(100,1000):
        val = str(i*j)
        if (val== val[::-1]):
            pallindrome.append(int(val))

print(max(pallindrome))
