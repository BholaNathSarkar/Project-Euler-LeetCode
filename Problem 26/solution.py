num =1
max=1
for d in range(3, 1000, 2):
    if (d % 5 == 0):
        continue

#Fermat’s little theorem that says: 1/d has a cycle of n digits if 10**n − 1 mod d = 0 for prime d.
    n = 1
    while ((10 ** n - 1) % d != 0):
        n+= 1

    if n >max:
        max=n
        num=d

print(num)
