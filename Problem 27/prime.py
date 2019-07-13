def prime_sieve(n):
    primeList = []
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primeList.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primeList
