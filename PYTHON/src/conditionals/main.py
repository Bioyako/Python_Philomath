def main():
    print("Conditionals in Python")

    print("The minimum off 3 and 4 is", min_2(4, 3))

    print(which_is_greater(3, 5))
    print(which_is_greater(42, 42))
    print(which_is_greater(-2, -7))

    print("Same sign checks.")
    print(same_sign(3, 5))
    print(same_sign(-2, 0))
    print(same_sign(-23, 17))

    # Index of comparison operators
    # < : less than
    # > : greater than
    # >= : greater tran or equal to
    # <= : less than or equal to
    # == : equal to
    # != : not equal to

def same_sign(x:int, y:int) -> bool:
    """
    Returns True if two input integers have the same sign
    and False otherwise.

    Parameters:
    - x (int)
    - y (int)

    Returns:
    bool: True if x and y have the same sign and False 
    otherwise (0 has the same sign as all integers)
    """
        # three cases:
        # 1. both positive (x * y >= 0, True)
        # 2. both negative (x * y >= 0, True)
        # 3. opposite signs (x * y < 0, False)
        #
        ## version 1
        # if (x >= 0 and y >= 0):
        #    return True
        # elif (x <= 0 and y <= 0):
        #    return True
        # velse:   # they can't have the same signs
        #    return False
        ## version 2
        # if x * y >= 0:
        #       return True
        # else:
        #       return False
        ## verion 3
        # if x * y >= 0:
        #    return True # function has returned
        # if I make it here, the function didnn't returnn
        # so I know that x * y < 0
        # return False
    ## verion 4
    return x * y >= 0

def min_2(a:int, b:int) -> int:
    """
    Takes two integers and returns their minimum.
        
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: minimum of a and b
    :rtype: int
    """
    if a < b:
        return a # a is smaller
    else: # b is greater than or equal to a
        return b

def which_is_greater(x:int, y:int) -> int:
    """  
    Takes two integers as input and returns 1 if the first
    one is larger, 0 if theey're equal, and -1 if the second
    one is larger

    Parameters:
    - x (int)
    - y (int)

    Returns:
    int: 1 if x > y, -1 if x < y, 0 if x =y
    """
    # x = y   # set the variable x equal to value y
    if x == y:
        return 0
    elif x > y:
        return 1
    else:    # we know here that x < y
        return -1




if __name__ == "__main__":
    main()