import time
"""
TrivialGCD(a,b)
    d ← 1
    m ← Min2(a,b)
    for every integer p between 1 and m
        if p is a divisor of both a and b
            d ← p
    return d

EuclidGCD(a,b)
    while a ≠ b
        if a > b
            a ← a - b
        else
            b ← b - a
    return a   
"""

def faster_euclid_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using a Euclid's algorithm.
    
    Parameters:
    - a (int)
    - b (int)

    Returns;
    int: GCD of a and b
    """

    # if you have negaive values, flip their signs
    if a < 0:
         a = -a
    if b < 0:
         b = -b
    
    # we're going to keep going for how long?
    while (a != 0) and (b != 0):
         if a > b:
              a = a % b
         else:
              b = b % a

    # so if we make it here, either a or b is 0 (they might both be 0)
    # ... we are in the realm of the mathematicians
    if a == 0:
         return b
    else:
         # b = 0
         return a



def euclid_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using a Euclid's algorithm.
    
    Parameters:
    - a (int)
    - b (int)

    Returns;
    int: GCD of a and b
    """
    # if you have negaive values, flip their signs
    if a < 0:
         a = -a
    if b < 0:
         b = -b
    
    # GCD(0, a) = a if a > 0
    if a == 0:
         return b   # this works even if they're both 0
    
    if b == 0:
         return a

    #if a < 0 or b < 0:
         #raise ValueError("Error: negative input given to function.")
    
    # critical fact: GCD(a, b) = GCD(a-b, b) when a > b ## (a, b-a) when b > a

    while a != b:
        # two cases depending on whether a > b or b > a
        if a > b:
             a = a - b
        else:
             b = b - a
    return a # or b

def trivial_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using a trivial algorithm
    that tries every possible divisor of a and b.
    
    Parameters:
    - a (int)
    - b (int)

    Returns;
    int: GCD of a and b
    """
    # if you have negaive values, flip their signs
    if a < 0:
         a = -a
    if b < 0:
         b = -b

    # GCD(0, a) = a if a > 0
    if a == 0:
         return b   # this works even if they're both 0
    
    if b == 0:
         return a
    
    #if a < 0 or b < 0:
         #raise ValueError("Error: negative input given to function.")
    
    d = 1

    m = min(a, b)

    # try every possible candidate divisor up to and
    # including m, and update d every time we find a divisor
    for p in range(2, m+1):
        # if p is a divisor of both, then d = p
        if a % p == 0 and b % p == 0: 
                d = p
                # if the first statement in an 'and' is False, them the whole thing
                # is immediately False and the secoonnd condition isn't even read

    return d



def main():
    print("Studying GCD algorithms.")

    print(trivial_gcd(63, 42))
    print(euclid_gcd(63, 42))

    x = 3782026
    y = 2731479
    
    # 1- time the trivial approach
    start = time.time() # starts a stopwatch
    trivial_gcd(x, y)
    elapsed_trivial = time.time() - start # stops the watch

    # print the time in a pretty way
    print(f"trivial_gcd took {elapsed_trivial:.6f} seconds.") # f means format in a nice way

    # 2-
    start = time.time() 
    euclid_gcd(x, y)
    elapsed_euclid = time.time() - start 
    print(f"euclid_gcd took {elapsed_euclid:.6f} seconds.") # f means format in a nice way

    # the speedup provided by an algorithm 1 compared to algorithm 2 is the ratio
    # of the runtime of algorithm 2 to algorithm 1
    speedup = elapsed_trivial/elapsed_euclid
    print(f"Speedup of Euclid vs Trivial: {speedup:.2f}x faster")

    # 3-
    start = time.time() 
    faster_euclid_gcd(x, y)
    elapsed_f_euclid = time.time() - start 
    print(f"faster_euclid_gcd took {elapsed_f_euclid:.6f} seconds.") # f means format in a nice way

    # the speedup provided by an algorithm 1 compared to algorithm 2 is the ratio
    # of the runtime of algorithm 2 to algorithm 1
    speedup = elapsed_trivial/elapsed_f_euclid
    print(f"Speedup of Fast Euclid vs Normal Euclid: {speedup:.2f}x faster")

if __name__ == "__main__":
    main()