start, end = map(int, input().split())

for num in range(start, end + 1):
    if num == 1:
        continue
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)