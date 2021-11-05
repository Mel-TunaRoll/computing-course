def lin_comb(maxi, n):

    """Returns all non-negative integer linear combinations c_0*n_0 + ... + c_k*n_k <= maxi, where the generators are n = [n_0, ..., n_k] """
    
    a = n[0]

    #return obvious answer if there's only 1 generator
    if len(n) == 1:
        return [c*a for c in range(int(maxi/a) + 1)] 
    
    #otherwise, for each possible c_0, return linear combinations c_1*n_1 + ... + c_k*n_k <= maxi - c_0*n_0
    lc = set()

    for c in range(int(maxi/a) + 1):
        for m in lin_comb(maxi - c*a, n[1:]):
            lc.add(c*a + m)
    
    return lc

n = 10000
mcnuggets = lin_comb(n,[6,9,20])

for i in range(n):
    if n - i not in mcnuggets:
        print(n - i)
        break