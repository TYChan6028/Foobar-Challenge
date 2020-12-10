import math


# prime numbers up to 20219
def solution(n):
    num = 100
    List = []

    for x in xrange(2, num):  # add numbers from 2 to num - 1 to List
        List.append(x)
    # note the above statement is equivalent to List = range(2, num)

    p = 2  # p is a prime

    # continue to mark out primes until square root of p is less than num
    while not int(math.sqrt(p)) + 1 > num:
        # remove all the multiples of p
        for x in xrange(p * 2, num, p):
            List[x - 2] = 0
        p += 1
        # assign p to the next integer. Next prime is the next non zero number in the list
        while p - 2 < len(List) and List[p - 2] == 0:
            p += 1

    s = ''
    for x in List:
        if x != 0:
            s = s + str(x)

    return s[n:n + 5]
