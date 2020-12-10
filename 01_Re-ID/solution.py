import math

# prime numbers up to 20219


def solution(n):
    ct = 2
    max_ = 30000
    p_list = [2, 3]
    for x in xrange(5, max_, 2):
        for p in p_list:
            if x % p == 0:
                break
        else:
            p_list.append(x)
            ct += int(math.log10(x)) + 1
        if ct >= n + 5:
            break

    s = ''
    for p in p_list:
        s += str(p)

    return s[n:n + 5]
