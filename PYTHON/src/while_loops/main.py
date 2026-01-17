def main():
    print("While loops in Python.")
    print(factorial(6))

    n = 5
    m = factorial(n)
    print(m)

    print("!0 is ", factorial(0)) # = 1
    # n! = n*(n-1)!
    # 1! = 1*0!
    # 1 = 0!    just math

    # print(factorial(-100)) # = 1, why? you never enter in the while loop (control flow)

    print("Sum of the first 100 positive integer is ", sum_first_n_integer(100))

    print(gauss_sum(100))

def euclid_gcd(a:int, b:int) -> int:
    # input: two inteegers
    # output: their GCD
    # approach: for as long as a != b, subtract smaller from larger
    # when they are equal, return one

def gauss_sum(n:int) -> int:
    """
    Sums the first n positive integers.

    Parameters:
    - n (int)

    Returns:
    int: Sum of the first n positive integers

    Raises an error if n < 0.
    """
    if n < 0:
        # handle nnegaive input with an error
        raise ValueError("Erroe: negative input given to sum_first_n_integer().")

    return (n+1)*(n/2)

def sum_first_n_integer(n:int) -> int:
    """
    Sums the first n positive integers.

    Parameters:
    - n (int)

    Returns:
    int: Sum of the first n positive integers

    Raises an error if n < 0.
    """
    if n < 0:
        # handle nnegaive input with an error
        raise ValueError("Erroe: negative input given to sum_first_n_integer().")

    s = 0

    i = 1 # counter variable

    while i <= n:
        s = s + i # shortand: s += i
        i = i + 1 # shortand: i += 1 (Python doesn't have i++)
    # at this point we know that i > n
    return s

def factorial(n:int) -> int:
    """
    Produce n! = n * (n-1) * ... 2 * 1

    Parameters:
    - n (int)

    Returns:
    int: n!

    Raises an error if n < 0.
    """
    if n < 0:
        # handle nnegaive input with an error
        raise ValueError("Erroe: negative input given to factorial().")

    p = 1   # think of p as the container that will represent my growing product
    i = 1   # this is a counter variable to keep track of how many multiplications we've done
    
    while i <= n:
        p = p * i   # left side: variable, right side: value
        i = i + 1   # update the counter -  if not presents infinite loop happens - stop the process with ctrl+c

    # we are here in the function when i > n
    return p 



if __name__ == "__main__":
    main()