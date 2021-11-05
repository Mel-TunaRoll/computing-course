import numpy as np
import matplotlib.pyplot as plt

def rand_perm(n:int):
    """Returns random permutation of [0,...,n-1] using Fisher-Yates"""

    p = []
    x = [i for i in range(n)]
    for i in range(n):
        p.append(x.pop(np.random.randint(n-i)))
    return p

def max_cycle_length(p):
    """Returns the max length of cycles of p"""

    remaining = p.copy() #stores elements not yet in a cycle
    cycle_lengths = [] 

    while remaining != []:
        start = remaining[0] #sets start of new cycle
        remaining.remove(start) #removes it from remaining
        i = start #initialise index
        l = 1
        while p[i] != start: #repeatedly applies p to start index until it cycles back to start, recording no. of applications and removing elements from remaining as it goes.
            l += 1
            i = p[i]
            remaining.remove(i)
        cycle_lengths.append(l)
    
    return max(cycle_lengths)

def create_hist(n, sample_size):
        mcl = [max_cycle_length(rand_perm(n)) for i in range(sample_size)]
        plt.hist(mcl, bins = 40)
        plt.show()

create_hist(300,1000)


p = rand_perm(8)
print(p)       
print(max_cycle_length(p))   
