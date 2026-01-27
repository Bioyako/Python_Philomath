"""
Pseudoccode below

TrivialPrimeFinder(n)
    primeBooleans <- array off n+1 false boolean variables 
    for every inteeger  from 2 to n
        if IsPrime(p) iss ture
            primeBooleans[p] <- true
    return primeBooleans
"""

import math
import time
import math

def trivial_prime_finder(n:int) -> list[bool]:
    """
    Finds all prime numbers up to and possibly including n.

    Parameters:
    - n: int

    Output:
    list[bool]: list of length n+1 whose element at index p
    will be True if p is prime and False iff it is not
    (i.e., prime_booleans[p] = True if p is prime)
    """

    if n < 0:
        raise ValueError("Error: negative integer given as input.")

    prime_booleans = [False]*(n+1) # set default values

    for p in range(2, n+1): # we know 0 and 1 are not prime
        # is the case that p is prime?
        prime_booleans[p] = is_prime(p)

    return prime_booleans

def is_prime(p:int) -> bool:
    """
    Returns True if input integer is prime and False otherwise.

    Parameters:
    - p (int)

    Output:
    bool: True if p is a prime and False otherwise
    """

    if p < 0:
        raise ValueError("Error: negative integer given as input.")
    
    for k in range(2, int(math.sqrt(p))+1):
        # is k a divisor of p?
        if p % k == 0:
            # yes, divisor of p, so p is not prime
            return False
    # if we survive all the divisor checks, we know that p is prime
    return True

# if p = k * b with k <= b, then k <= sqrt(p)
# if k > sqrt(p) (so b > sqrt(p))
# then k * b > (sqrt(p)*sqrt(p)) = p
# so k > sqrt(p cannot be true)

def sieve_of_erastothenes(n:int) -> list[bool]:
    """
    Finds all prime numbers up to and possibly including n,
    using Erastothenes' approach from ancient Greece. 

    Parameters:
    - n: int

    Output:
    list[bool]: list of length n+1 whose element at index p
    will be True if p is prime and False iff it is not
    (i.e., prime_booleans[p] = True if p is prime)
    """

    if n < 0:
        raise ValueError("Error: negative integer given as input.")

    prime_booleans = [True] * (n+1)

    # 0 and 1 are definetely not prime
    prime_booleans[0] = False
    prime_booleans[1] = False

    # range p from 2 to sqrt(n)
    for p in range(2, int(math.sqrt(n))+1):
        # cross off the multiples of p as composite
        if prime_booleans[p]: # (== True:) automatically checked, not need to add # think of this as a gray value on the table (gif)
            # cross off multiples of p
            prime_booleans = cross_off_multiples(prime_booleans, p)


    return prime_booleans

def cross_off_multiples(prime_booleans:list[bool], p:int) -> list[bool]:
    """
    Crosses off all the multiples of a given integer in a 
    table holding primality of collection of integers between 0 and n+1.

    Parameters:
    - prime_booleas (list[bool])
    - p (int)

    Output:
    list[bool]: update version of prime_booleans corresponding to setting prime_booleans[k] = False
    for every integer k that is a multiple of p
    """

    if p < 2:
        raise ValueError("Error: value of p too small.")
    
    if len(prime_booleans) < 2:
        raise ValueError("Error: prime booleans list too short")

    # make sure that n is declared
    # len(prime_booleans) = n+1
    # len(prime_booleans) - 1 = n
    n = len(prime_booleans)-1

    # range over all indices of prime_booleans that are multiples
    # of p and "cross them off"
    for k in range(2*p, n+1, p): # adding p each time
        # is it the case that k is a multiple of p?
        if k % p == 0:
            prime_booleans[k] = False

    return prime_booleans

def list_primes(n:int) -> list[int]:
    """
    Returns a list of all primes up to and (possibly including) .
    
    Parameters:
    - n (int)

    Output:
    list[int]: list of all primes up to and including n.
    """

    if n < 2:
        raise ValueError("Error: negative integer given as input.")
    
    # I don't know how big the list is going to ultimately be. And that's OK.

    prime_list = [] # or list()

    # we already havvve code to find the primes
    prime_booleans = sieve_of_erastothenes(n)

    # range through this list and identify which ones are True
    for p, is_prime in enumerate(prime_booleans):
        if is_prime:
             # append the current integer to list
             prime_list.append(p)
    
    return prime_list

# how many prime numbers are there?
# infinite: Why? It's proven!

# how many prime numbers are there <= n?
# is there a formula in terms of n?

# Let's plot all the primes up to n

#def prime_count_array(n:int) ->

def main():
    print("Prime finding.")

    n = 11
    prime_booleans = trivial_prime_finder(n)

    print(prime_booleans)
    print(is_prime(7)) # first check the simplest subroutine function

    print(sieve_of_erastothenes(n))

    # timing the two algorithms
    n = 100
    start = time.time()
    trivial_prime_finder(n)
    elapsed_trivial = time.time() - start
    print(f"Trivial prime finder took {elapsed_trivial:.6f} seconds.")

    start = time.time()
    sieve_of_erastothenes(n)
    elapsed_sieve = time.time() - start
    print(f"Sieve of Erastothenes took {elapsed_trivial:.6f} seconds.")

    speedup = elapsed_trivial/elapsed_sieve
    print(f"Speedup: {speedup:.2f}x faster")

    prime_list = list_primes(23)
    print(prime_list)

if __name__ == "__main__":
    main()