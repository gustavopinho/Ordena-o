# -*- coding: utf-8 -*-

def bubblesort(A, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A;
    
def bubblesort_(vetor):
   for j in range(len(vetor)):
       for i in range(len(vetor)-1, j, -1):
           if vetor[i]<vetor[i-1]:
               vetor[i-1], vetor[i] = vetor[i], vetor[i-1]


if __name__ == '__main__':
    
    import timeit
    import matplotlib.pyplot as plt
    import sys
    sys.setrecursionlimit(100000)
    
    x = list()
    y_best = list()
    y_worse = list()
    
    for n in range(0, 1000, 10):
        print n
        best = 'bubblesort(list(range('+str(n)+')),'+str(n)+')'
        worse = 'bubblesort(list(range('+str(n)+', 0, -1)),'+str(n)+')'
        x.append(n)
        y_best.append((timeit.timeit(best, setup="from __main__ import bubblesort", number=1)))
        y_worse.append((timeit.timeit(worse, setup="from __main__ import bubblesort", number=1)))
    
    plt.plot(x, y_best)
    plt.plot(x, y_worse)
    plt.ylabel(u'Tempo de Execução')
    plt.xlabel(u'Crescimento')
    plt.show()