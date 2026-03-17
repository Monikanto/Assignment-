import math



# 1. Sum of digits (No String)
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
n=int(input("Enter the number: "))
print("SUm of digitis:",sum_digits(n))







# 2. Product of digits (No String)
def product_digits(n):
    p = 1
    n = abs(n)
    while n > 0:
        p *= n % 10
        n //= 10
    return p
n=int(input("Enter the number: "))
print("SUm of digitis:",product_digits(n))






# 3. Reverse a number (No String)
def reverse_number(n):
    rev = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n > 0:
        rev = rev*10 + n%10
        n //= 10
    return sign * rev




# 4. Palindrome number
def is_palindrome(n):
    return n == reverse_number(n)



# 5. Armstrong number (n-digit)
def is_armstrong(n):
    temp = n
    digits = 0
    t = n
    while t > 0:
        digits += 1
        t //= 10

    s = 0
    while temp > 0:
        d = temp % 10
        s += d**digits
        temp //= 10
    return s == n



# 6. Perfect number
def is_perfect(n):
    s = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            s += i
    return s == n



# 7. Strong number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def is_strong(n):
    temp = n
    s = 0
    while temp > 0:
        d = temp % 10
        s += factorial(d)
        temp //= 10
    return s == n




# 8. Harshad Number
def is_harshad(n):
    return n % sum_digits(n) == 0



# 9. Automorphic Numberdef is_automorphic(n):
    sq = n*n
    temp = n
    while temp > 0:
        if temp % 10 != sq % 10:
            return False
        temp //= 10
        sq //= 10
    return True



# 10. Neon Number
def is_neon(n):
    return sum_digits(n*n) == n



# 11. GCD (Euclid Algorithm)
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a




# 12. LCM using GCD
def lcm(a,b):
    return abs(a*b)//gcd(a,b)



# 13. HCF of Three Numbers
def hcf_three(a,b,c):
    return gcd(gcd(a,b),c)



# 14. Power a^b using loop
def power(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result



# 15. Power a^b mod m (Fast Exponentiation)
def power_mod(a,b,m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res*a) % m
        a = (a*a) % m
        b //= 2
    return res




# 16. Prime Factors
def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors




# 17. Check Prime (√n optimized)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True




#18. Sieve of Eratosthenes
def sieve(n):
    prime = [True]*(n+1)
    prime[0]=prime[1]=False
    for i in range(2,int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i,n+1,i):
                prime[j]=False
    return [i for i in range(n+1) if prime[i]]



# 19. Twin Primes in Range
def twin_primes(n):
    primes = sieve(n)
    twins = []
    for i in range(len(primes)-1):
        if primes[i+1]-primes[i]==2:
            twins.append((primes[i],primes[i+1]))
    return twins





# 20. Factorial using Recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)



# 21. nCr
def nCr(n,r):
    return fact(n)//(fact(r)*fact(n-r))


# 22. nPr
def nPr(n,r):
    return fact(n)//fact(n-r)



# 23. Harmonic Series
def harmonic(n):
    s=0
    for i in range(1,n+1):
        s+=1/i
    return s




# 24. sin(x) using Taylor Series (x in radians)
def sin_taylor(x,n):
    s=0
    for i in range(n):
        term = ((-1)**i)*(x**(2*i+1))/fact(2*i+1)
        s+=term
    return s





# 25. e^x using Taylor Series
def exp_taylor(x,n):
    s=0
    for i in range(n):
        s += (x**i)/fact(i)
    return s

