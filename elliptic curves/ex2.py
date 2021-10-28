import numpy as np
from fractions import Fraction

def is_a_square(n: int):
    if n < 0:
        return False
    
    root_n = np.sqrt(n)
    test = root_n - int(root_n)
    if test == 0:
        return True
    else:
        return False

sols = set()
temp1 = None
temp2 = None


for q in range(1,7):
    for p in range(-6,7):
        temp1 = Fraction(p,q)
        temp2 = Fraction((p+q)*(p+4*q)*(p-5*q),q**3)       #this creates a rational object in lowest terms   
        if is_a_square(temp2.numerator) and is_a_square(temp2.denominator):
            sols.update(str(temp1.numerator)+'/'+str(temp1.denominator))

print(sols)
