import math

# prime numbers up to 20231


def solution(n):
    max_ = 21000  # upper bound for prime number check
    p_list = [2, 3]  # list of found prime numbers
    ct = 2  # overall prime digit count

    for x in xrange(5, max_, 2):  # skip multiples of 2
        for p in p_list:
            if x % p == 0:  # if divisable by any prime
                break  # not a prime
        else:  # found new prime
            p_list.append(x)
            ct += int(math.log10(x)) + 1  # count digits

        if ct >= n + 5:  # if overall digits are enough
            break

    s = ''
    for p in p_list:  # concatenate list of primes
        s += str(p)

    return s[n:n + 5]
