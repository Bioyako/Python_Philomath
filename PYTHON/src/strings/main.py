def main():
    print("String.")

    s = 'Hi'
    t = "Lovers"

    # concatenations = glues together strings
    u = s + t # or add space + " " +
    print(u)

    print(s*3) # multiplication with strings is repeated concatenation

    # strings arre (kinda) tuples(= + lists: arrays) of symbol

    # so we can access individual elements of a string
    print("The ffirs symbol of u is", u[0])

    print("The final symbol of u is", u[len(u)-1])

    if t[2] == "v":  # symbol is case sensitive (capital letter or not)
        print("The symbol at position 2 of t is v.")

    # strings, like tuples, are immutable
    # t[2] = 's' # this is not allowed, I can't change individual letters

    # I can change the entire string
    s = "Yo"
    print(s)

    # we can use += shortcut too!
    s += "-Yo"
    s = s + "Ma"
    print(s)

    dna = "ACCGAT"
    print(complement(dna))
    print(reverse(dna))
    print(reverse_complement(dna))


def reverse_complement(dna: str) -> str:
    """
    Produces the reverse complemtent of a DNA string (A, C, G, 
    and symbols only), meaning the string corresponding to a complementary
    strand.

    e.g., the reverse complement of "AGTC" is "GACT"

    Parameters:
    - dna: str

    Output:
    str: reverse complement of the input string
    """

    # dna = complement(dna) # complement of "AGTC" is "TCAG"      ## important thing during coding: don't struggle to find one direct solution od the problem; decomposed in many parts.. be lazy & you can re-use functions in other problems & easier debugging problem
    # dna = reverse(dna)  # reverses the symbol in string
    # return dna
    return reverse(complement(dna)) # you can change the funtions, the result donnot change

def reverse(s: str) -> str:
    """
    Reverse the symbols in input string

    Parameters:
    - s: str

    Returns:
    str: The reverse of s
    """

    # rev = ""
    characters = []

    n = len(s)
    for i in range(n):
        # rev += s[(n-1)-1] # many letters means big deal...
        characters.append(s[n-1-i])
    # now we need to cconvert this list to a string
    return "".join(characters)

    ## return rev
    # i     index of s
    # 0     n-1
    # 1     n-2
    # 2     n-3
    # i     ??? = (n-1)-1
    # n-1   0

def complement(dna: str) -> str:
    """
    Finds the 'complementary' strand off a givem DNA string 
    without reversinng it

    Parameters:
    - dna (str)

    Returns:
    string: the string whose i-th symbol is the complementary 
    nucleotide of the i=th symbol of the imput string (A-T, C-G, T-A, G-A)      
    """

    dna2 = ""

    # range over the strings, take the complements at each position
        
    # python will use a match statement (elif elif elif): called a switch in other languages

    # for i, symbol in enumerate(dna): # each symbol at each stage
    for symbol in dna:     
        # what is the current symbol in my string?
        match symbol:
            case "A":
                dna2 += "T"
            case "C":
                dna2 += "G"
            case "G":
                dna2 += "C"
            case "T":
                dna2 += "A"
            case _:
                raise ValueError("Error: symbol in string is not a DNA nucleotide")
    return dna2

            #if symbol == "A":
                # dna[i] = "T"
                #dna2 += "T"
            #elif symbol == "C":
                # dna[i] = "G"
                #dna2 += "G"
            #elif symbol == "G":
                # dna[i] = "C"
                #dna2 += "C"
            #elif symbol == "T":
                # dna[i] = "A"
                #dna2 += "A"
            #else:
                #raise ValueError("Error: symbol in string is not a DNA nucleotide")
        #return dna2



if __name__ == "__main__":
    main()