
def lin_comb(mx, n):

    """Returns all non-negative integer linear combinations of the numbers in n less than mx """
    
    a = n[0]

    if len(n) == 1:
        return [c*a for c in range(int(mx/a) + 1)]
    
    lc = set()

    for c in range(int(mx/a) + 1): #iterates through possible coefficients of n_0 leading to a combination less than n
        for m in lin_comb(mx - c*a, n[1:]): # calculates all linear combinations m = c_1*n_1+ ... + c_k*n_k less than mx - c*n_0 so that c*n_0 + m represents all lin combs with n_0's coeff being c.
            lc.add(c*a + m)
    
    return lc

mcnuggets = lin_comb(100,[6,9,20])

for i in range(100):
    if 100 - i not in mcnuggets:
        print(100 - i)
        break