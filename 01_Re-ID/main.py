from __future__ import print_function
import solution as s1
import solution2 as s2
import timeit

# foobar accepts brilliant solution up until n = 5000

n = 10000

start = timeit.default_timer()
print(s1.solution(n))
stop = timeit.default_timer()
print('Time for s1: ', round(stop - start, 4), 'secs')
