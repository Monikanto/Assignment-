# 1. Print “Hello World”. 
print("Hello World")

# 2. Take name input and print greeting. 
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 3. Add two numbers. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1 + num2)

# 4. Swap two numbers. 
a = 5
b = 10
a, b = b, a
print(a, b)

# 5. Convert Celsius to Fahrenheit. 
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# 6. Convert km to miles. 
km = float(input("Enter kilometers: "))
miles = km * 0.621371
print(miles)

# 7. Find square and cube of a number. 
num = float(input("Enter number: "))
print(f"Square: {num**2}, Cube: {num**3}")

# 8. Calculate simple interest. 
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print(si)

# 9. Calculate compound interest. 
p, r, t = 1000, 5, 2
ci = p * (pow((1 + r / 100), t)) - p
print(ci)

# 10. Find area of circle/rectangle/triangle. 
import math
r = 5
print(f"Circle: {math.pi * r**2}")
l, w = 10, 5
print(f"Rectangle: {l * w}")
b, h = 10, 5
print(f"Triangle: {0.5 * b * h}")

# 11. Check even or odd. 
n = int(input("Enter number: "))
print("Even" if n % 2 == 0 else "Odd")

# 12. Find largest of two numbers. 
a, b = 10, 20
print(max(a, b))

# 13. Find largest of three numbers. 
a, b, c = 10, 30, 20
print(max(a, b, c))

# 14. Check positive/negative/zero. 
n = float(input("Enter number: "))
if n > 0: print("Positive")
elif n < 0: print("Negative")
else: print("Zero")

# 15. Convert seconds into hours/minutes/seconds. 
s = int(input("Enter seconds: "))
h = s // 3600
m = (s % 3600) // 60
sec = s % 60
print(f"{h}h:{m}m:{sec}s")

# 16. Print numbers 1–100. 
for i in range(1, 101):
    print(i, end=" ")

# 17. Print even numbers up to N. 
n = 50
for i in range(2, n + 1, 2):
    print(i, end=" ")

# 18. Print multiplication table of a number. 
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 19. Find sum of first N natural numbers. 
n = 10
print(sum(range(1, n + 1)))

# 20. Find factorial using loop. 
n = 5
f = 1
for i in range(1, n + 1):
    f *= i
print(f)

# 21. Generate Fibonacci series. 
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 22. Reverse a number. 
num = 1234
print(int(str(num)[::-1]))

# 23. Count digits in number. 
num = 12345
print(len(str(num)))

# 24. Sum of digits. 
num = 12345
print(sum(int(d) for d in str(num)))

# 25. Check palindrome number. 
s = "121"
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# 26. Check Armstrong number. 
n = 153
s = str(n)
l = len(s)
print(n == sum(int(d)**l for d in s))

# 27. Check prime number. 
n = 17
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print(is_prime)

# 28. Print all primes in range. 
start, end = 1, 50
for n in range(start, end + 1):
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        print(n, end=" ")

# 29. Find GCD and LCM. 
import math
a, b = 12, 18
gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd
print(f"GCD: {gcd}, LCM: {lcm}")

# 30. Print star patterns (* pyramid, triangle). 
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 31. Guess the number game. 
import random
target = random.randint(1, 10)
guess = int(input("Guess 1-10: "))
print("Correct!" if guess == target else f"Wrong, it was {target}")

# 32. Print ASCII values. 
char = 'A'
print(ord(char))

# 33. Print powers of 2 up to N. 
n = 10
for i in range(n + 1):
    print(2**i, end=" ")

# 34. Find largest digit in number. 
num = 48291
print(max(str(num)))

# 35. Count vowels and consonants. 
text = "hello world"
v = sum(1 for c in text if c.lower() in 'aeiou')
c = sum(1 for c in text if c.isalpha() and c.lower() not in 'aeiou')
print(f"Vowels: {v}, Consonants: {c}")