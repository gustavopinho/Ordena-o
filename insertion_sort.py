# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:38:34 2015

@author: gustavo
"""
def insertion_sort(A, n):
    for i in range(n):
        for j in range(i, 0, -1):
            if A[j] > A[j - 1]:
                break
            A[j], A[j - 1] = A[j - 1], A[j]
    return A
    
if __name__ == '__main__':
    
    import timeit
    import matplotlib.pyplot as plt
    
    x = list()
    y_O = list()
    y_best = list()
    y_worse = list()
    
    for n in range(1000):
        best = 'insertion_sort(list(range('+str(n)+')),'+str(n)+')'
        worse = 'insertion_sort(list(range('+str(n)+', 0, -1)),'+str(n)+')'
        x.append(n)
        y_O.append((n**2)*0.0001)
        y_best.append((timeit.timeit(best, setup="from __main__ import insertion_sort", number=1)*1000))
        y_worse.append((timeit.timeit(worse, setup="from __main__ import insertion_sort", number=1)*1000))
    
    plt.plot(x, y_O)
    plt.plot(x, y_best)
    plt.plot(x, y_worse)
    plt.show()