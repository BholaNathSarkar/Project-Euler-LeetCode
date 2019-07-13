from prime import prime_sieve
max = 0
pair = [0, 0]
primes = prime_sieve(110000)

for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        while abs(n ** 2 + a * n + b) in primes:
           n += 1
        if(n > max):
           max = n
           p = [a, b]

print(p[0] * p[1])
