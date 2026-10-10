# prime_find
count = 0
n = 2
while count < 10:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(n)
        count += 1
    n += 1