def main():
    print("Substrings (and sublists).")

    # Python uses text[i: i+k] to indicate the substring off text that starts at position i and goes up to (but not inccluded) i+k

    # Convenience: subtract too index - bottom index to give length (the string above has length k)

    s = "Hi Lovers"
    print(s[1:5]) # length 4, "i Lo"

    print(s[:7]) # Hi love, or s[0:7]
    print(s[4:])   # overs, or s[4:len(s)]

    a = [0] * 6
    for i in range(len(a)):
        a[i] = 2*i+1
    
    # a = [1, 3, 5, 7, 9, 11]
    print(a)
    print(a[3:5])
    print(a[:3])
    print(a[4:])

    pattern = "ATA"
    text = "ATATA"
    print(pattern_count(pattern, text))

    print(text.count(pattern)) # this does not include overlaps

    print(starting_indices(pattern, text))

def starting_indices(pattern: str, text: str) -> list[int]:
    """
    Finds thee occurences where a patterns occurs in a longer text string

    Parameters:
    - pattern (str)
    - tect (str): the longer string

    Returns:
    list[int]: the collection of starting positions where patterns occurs in textt, with overlaps.
    e.g., "ATA" occcurs at positions 0 and 2 in "ATATA"
    """
    k = len(pattern)
    n = len(text)

    if k == 0:
        raise ValueError("empty patern not allowed")
    
    if k > n:
        return 0
    
    positions = []    # keep track of the position

    # range over all starting positions, and if I find a match, append it to positions
    for i in range(n-k+1):
        if text[i:i+k] == pattern:
            positions.append(i)

    return positions # I'm returning a different object compared to the other function, a collection of starting position instead of an integer

# magic words; immutable(strings), subroutine 

def pattern_count(pattern: str, text: str) -> int:  
    """
    Finds the number of times that a pattern occurs in a longer text string.

    Parameters:
    - pattern (str)
    - text (str): the longer string

    Returns:
    int: The number of times that pattern occurs in text, with overlaps
    e.g., "ATA" occcurs twice in "ATATA"
    """  

    k = len(pattern)
    n = len(text)

    if k == 0:
        raise ValueError("empty patern not allowed")
    
    if k > n:
        return 0
    
    count = 0

    # range over text, incrementing count every time we find a pattern match
    # there are n-k+1 total substrings of lenght k in a string of lenght n (range from staring position 0 to n-k)
    for i in range(n-k+1): #n #n-k 
        # does the current substring of text of length k match pattern?
        print("Current substring is", text[i:i+k])  

        """"
            Current substring is ATA
            Current substring is TAT
            Current substring is ATA
            Current substring is TA
            Current substring is A
            2
        """

        if pattern == text[i:i+k]:
            count += 1 # I found a match!
    return count
    # one line function: delete from count=0 to the bottom and insert
    # return len(starting_indices(pattern, text))
    # - -- - -- - -- - --
    ## !!! anytime you see code that is repetead 
    # 1. there is problably subroutine working
    # 2. when you answer the general question the initial question becomes trivial

if __name__ == "__main__":
    main()