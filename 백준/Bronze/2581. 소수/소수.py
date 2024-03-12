M = int(input())
N = int(input())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**(1/2)) + 1):
    if is_prime[i] == False:
        continue
    
    for j in range(i * i, N + 1, i):
        is_prime[j] = False
        

primes = [x for x in range(M, N + 1) if is_prime[x] == True]
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes), primes[0])