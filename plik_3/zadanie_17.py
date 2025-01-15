def find_primes(limit):
    def check_prime(a):

        if a < 2:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    primes = []
    for num in range(2, limit + 1):
        if check_prime(num):
            primes.append(num)

    return primes


print(find_primes(30))
