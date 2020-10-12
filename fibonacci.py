def fib_iter(n):
    if n < 2:
        return n
    cnt = 1
    cur = 1
    i = 0
    while cnt < n:
        cnt += 1
        cur = cur + i
        i = cur - i
    return cur


def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a_n_1 = fib_rec(n - 1)
    a_n_2 = fib_rec(n - 2)
    a_n = a_n_1 + a_n_2
    return a_n
