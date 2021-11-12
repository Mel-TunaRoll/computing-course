import numpy as np
import matplotlib.pyplot as plt

def rand_perm(n:int):
    """Returns random uniformly distributed permutation of [0,...,n-1] using Fisher-Yates"""

    p = []
    x = [i for i in range(n)]
    for i in range(n):
        p.append(x.pop(np.random.randint(n-i)))
    return p

def cyc_decomp(p):
    """Returns the cycle decomposition of a permutation p"""

    remaining = p.copy() #stores elements not yet in a cycle
    cycles = [] 

    while remaining != []:
        start = p.index(remaining[0]) #sets start of new cycle
        remaining.remove(start) #removes it from remaining
        i = start #initialise index
        c = [start]
        while p[i] != start: #repeatedly applies p to start index until it cycles back to start, recording no. of applications and removing elements from remaining as it goes.
            i = p[i]
            c.append(i)
            remaining.remove(i)
        cycles.append(c)
    
    return cycles

def max_cyc_len(p):
    """Returns the maximal length of a cycle of a permutation p"""
    cyc_len = [len(c) for c in cyc_decomp(p)] 
    return(max(cyc_len))

def gen_mcl_hist(n, sample_size = 10000):
    """Generates a histogram of the maximal cycle lengths of a sample of uniformly distributed n-permutations."""
    perms = [rand_perm(n) for i in range(sample_size)] #makes list of random permuations
    mcls = [max_cyc_len(p) for p in perms] #calculates their max cycle length
    freqs = {k: mcls.count(k) for k in range(1,20)} #creates a dictionary of frequencies
    print(freqs)
    plt.bar(range(50),mcls)
    plt.show()

gen_mcl_hist(50)
