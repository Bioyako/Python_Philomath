def main():
    print("Hello, World!")

    print(int_div(6,2))
    print(remainder(35,2))
    print(euclid(378, 273))
    print(isprime(8))
    print(array_prime(11))

def int_div(n:int, p:int) -> int:           # n ≥ 0      p > 0
    i = 0
    while p * i <= n:
        i = i + 1
    return i - 1
    
def remainder(n:int, p:int):
    d = int_div(n,p)
    r = n - (p * d)
    return r

def euclid(a:int, b:int) -> int: 
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a, b

def isprime(p:int) -> bool:
    for i in range(2, p-1):
        if p % i == 0:
            return False
    return True

def array_prime(n:int):
    primeBooleans = [False] * (n+1)
    for p in range(2, n):
        if isprime(p) == True:
            primeBooleans = [True]
    return primeBooleans

#def fibonacci(n: int) -> int:



if __name__ == "__main__":
    main()