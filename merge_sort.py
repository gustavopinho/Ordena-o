# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:44:27 2015

@author: gustavo
"""
def merge_sort(A, temp, left, rigth):

    if (rigth == left):
        return
    
    mid = int((left+rigth)/2)
    
    merge_sort(A, temp, left, mid)
    merge_sort(A, temp, mid+1, rigth)  
    
    for i in range(left, rigth+1):
        temp[i] = A[i]
    
    i1 = left
    i2 = mid+1
    
    for curr in range(left, rigth+1):
        if i1==mid+1:
            A[curr] = temp[i2]
            i2 = i2 +1
        elif i2>rigth:
            A[curr] = temp[i1]
            i1 = i1 +1
        elif temp[i1] < temp[i2]:
            A[curr] = temp[i1]
            i1 = i1 +1
        else:
            A[curr] = temp[i2]
            i2 = i2 +1

if __name__ == '__main__':
    
    import timeit
    import math
    import matplotlib.pyplot as plt
    
    #A = merge_sort(list(range(999, 0, -1)),list(range(999, 0, -1)),0,998)

    #print A
    
    x = list()
    y_O = list()
    y_best = list()
    y_worse = list()
    
    for n in range(1, 10001):
        best = 'merge_sort(list(range('+str(n)+')), list(range('+str(n)+')), 0,'+str(n-1)+')'
        worse = 'merge_sort(list(range('+str(n)+', 0, -1)),list(range('+str(n)+', 0, -1)),0,'+str(n-1)+')'
        
        x.append(n)
        y_O.append((n*math.log(n,2))*0.0001)
        y_best.append((timeit.timeit(best, setup="from __main__ import merge_sort", number=1)*300))
        y_worse.append((timeit.timeit(worse, setup="from __main__ import merge_sort", number=1)*300))
    
    plt.plot(x, y_O)
    plt.plot(x, y_best)
    plt.plot(x, y_worse)
    plt.show()