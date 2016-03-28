# -*- coding: utf-8 -*-
if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    import sys
    import math
    sys.setrecursionlimit(100000)
    
    x = list()
    theta = list()
    
    for n in range(1, 100000, 10):
        print n
        x.append(n)
        theta.append(n*(math.log(n,2)))
       
    plt.plot(x, theta)
    plt.ylabel(u'Tempo de Execução Θ(nlogn)')
    plt.xlabel(u'Crescimento')
    plt.show()