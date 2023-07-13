DISCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return str(n)
