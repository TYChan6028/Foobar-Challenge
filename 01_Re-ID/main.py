from __future__ import print_function
from solution import solution
import timeit
import resource

# foobar accepts brilliant solution up until n = 5000

n = 10000

start = timeit.default_timer()
print(solution(n))
stop = timeit.default_timer()
print('Time for solution():', round(stop - start, 4), 'secs')
print('Peak memory usage:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 'KBs')
