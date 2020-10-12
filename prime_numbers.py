def is_prime(x):
    if type(x) != int or x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def get_primes(max_num):
    cnt = 2
    while cnt < max_num:
        if is_prime(cnt):
            yield cnt
        cnt += 1