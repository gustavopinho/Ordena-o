# -*- coding: utf-8 -*-

def partition(A, r, p):
    x = A[r]
    i = p-1
    for j in range(p, r-1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

if __name__ == '__main__':
    
    import timeit
    import matplotlib.pyplot as plt
    import sys
    sys.setrecursionlimit(10000000)
        
    x = list()
    y_best = list()
    y_worse = list()
    
    for n in range(0, 10000, 100):
        print n        
        best = 'quick_sort(list(range('+str(n)+')), 0,'+str(n-1)+')'
        worse = 'quick_sort(list(range('+str(n)+', 0, -1)),0,'+str(n-1)+')'
        x.append(n)
        y_best.append((timeit.timeit(best, setup="from __main__ import quick_sort", number=1)))
        y_worse.append((timeit.timeit(worse, setup="from __main__ import quick_sort", number=1)))
    
    plt.plot(x, y_best)
    plt.plot(x, y_worse)
    plt.show()