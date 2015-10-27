# -*- coding: utf-8 -*-

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
    y_best = list()
    y_worse = list()
    
    for n in range(0, 10000, 500):
        print n
        best = 'insertion_sort(list(range('+str(n)+')),'+str(n)+')'
        worse = 'insertion_sort(list(range('+str(n)+', 0, -1)),'+str(n)+')'
        x.append(n)
        y_best.append((timeit.timeit(best, setup="from __main__ import insertion_sort", number=1)))
        y_worse.append((timeit.timeit(worse, setup="from __main__ import insertion_sort", number=1)))
    
    plt.plot(x, y_best)
    plt.plot(x, y_worse)
    plt.show()
