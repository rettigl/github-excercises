def fibonacci_rec(n):
    assert isinstance(n, int) and n>=0 # only allow non-negative integers
    if n==0 or n==1: # stop conditions
        return n                                                                             
    else: # recursion condition
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)  
    
    
def fibonacci_it(n):
    assert isinstance(n, int) and n>=0 # only allow non-negative integers
    if n == 0 or n==1:
        return n
    f_m1 = 0
    f_m2 = 1
    i = 0
    while (i < n): # build numbers up from bottom
        fib_n = f_m1 + f_m2
        f_m2 = f_m1
        f_m1 = fib_n
        i += 1
    return fib_n