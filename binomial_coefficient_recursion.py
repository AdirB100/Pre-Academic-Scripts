def binomial_coefficient(n, k):
    if k > n:
        return 0
    if n == k or k == 0:
        return 1
    # if k == n - 1 or k == 1:
    #     return n
    return binomial_coefficient(n - 1, k) + binomial_coefficient(n - 1, k - 1)
