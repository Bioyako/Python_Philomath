def main():
    print("Arrays in Python (tuples and lists).")

    # tuples are useful if we know the values in advance
    primes = (2, 3, 5, 9, 11)
    print(primes)

    # tuples are immutable
    # oh no, 9 is not prime
    # tuples are 0-index
    # primes[3] = 7 # this will not work because you can't change individual elements of a tuple
    empty_list = [] # or = list()

    # sometimes, I just want a buncch of values
    n = 6
    a = [0]*6 # [0, 0, 0, 0, 0, 0]

    # let's make a small list
    # it can even have diffeerent types
    mixed_list = [1, 3.14, -42, "Python stinks", True]

    print(empty_list)
    print(a)
    print(mixed_list) 

    # lists use 0-based indexing (indices range from 0 to n-1, where n in the length of the list)

    a[0] = -8   # initial element

    i = 3
    k = 4
    a[2*i-4] = (k//2)**4 + 1 # a[2] = 17

    # len(a) gives number of elements in list a

    # how do I set the final element of a list?

    # elements indices of a list range from 0 to len(a) - 1
    a[len(a) - 1] = 43 # sets the last element OR a[-1] = 43

    print("a is now ", a)

    # lists are mutable

    # negative indexing (ignoring if you want)
    # a[-1]: last element of a
    # a[-2]: penultimate element
    # a[-3]: antepenutlimatee element
    # ... this goes back how far?
    # a[-len(a)]: first element of a

    # What happeens if you give Python something weird
    # indices outside the range frfom -len(a) to len(a) - 1 produce IndexErrors
    # a[-len(a)-1] = 2

    n = 10
    print("Factorial up to", n, "are", factorial_array(n))

    c = [3, 2, 1]
    print(min_integer_array(c))

    print("Minimum of 3, 4 and -7 is", min_integers(3, 4, -7))

    # integers, strings, floats, are pass by value (copy is created when
    # they go into a function)
    # lists are not pass by value, they are pass by reference
    # you die in the function, you die IRL
    c = [0]*6
    change_first_element(c)

    print(c)

def factorial_array(n:int) -> list[int]:
    """
    Produce a list of all factorials from 0! to n!

    Parameters:
    - n (int)

    Return:
    list(int): A list of length n+1 wheere the k-th element is k!
    """

    if n < 0:
        raise ValueError("Error: negative input given.")
    
    fact = [0]*(n+1) # preview: this can produce many nightmares also

    fact[0] = 1

    # range through and set k! = k*(k-1)!
    for k in range(1, n+1):
        fact[k] = fact[k-1]*k
    
        return fact

def min_integer_array(a: list[int]) -> int:
    if len(a) == 0:
        raise ValueError("Error: empty list given to function.")
    
    m = a[0] # stores our minimum

    for val in a:        # OR i in range(len(a)):
        # is current value better than what I currently have?
        if val < m:      # a[i] < m:
            # update m appropriately
            m = val      # m = a[i]
    
    return m

# min() in Python can take ann arbitrary number of inputs
# *numbers indicates that we can have an arbitrary number of inputs
def min_integers(*numbers: int) -> int:
    # numbers is a tuple
    m = min_integer_array(list(numbers))
    return m

def change_first_element(a: list[int]):
    if len(a) == 0:
        raise ValueError("Bad")
    a[0] = 1


if __name__ == "__main__":
    main()