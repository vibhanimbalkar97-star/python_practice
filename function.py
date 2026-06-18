# Create a function that prints "Hello World"
# def greet():
#     print("Hello world")
# greet()

# Create a function that prints your name
# def name(name):
#     print(f"Welcome {name}")
# name("Karan")

# Create a function that adds two numbers
# def sum(a,b):
#     print(f"Sum is {a+b}")
# sum(5,8)

# Create a function that returns the square of a number
# def square(a):
#     return a*a
# res_square=square(9)
# print(res_square)

# Create a function that returns the cube of a number
# def cube(a):
#     return a*a*a
# res_cube=cube(5)
# print(res_cube)

# Check if a number is even or odd
# def even_odd(a):
#     if a%2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
# even_odd(5)
# even_odd(6)

# Find the larger of two numbers
# def largest(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# res = largest(20, 30)
# res = largest(-20, 40)
# print(res)

# Check if a person is eligible to vote
# def voter(age):
#     if age>=18:
#         print("Eligible")
#     else:
#          print("Not Eligible")
# voter(20)
# voter(9)

# Check if a year is a leap year
# def leap_year(year):
#     if year%100 == 0 and year % 400 == 0:
#         print("Leap year")
#     elif year%100 != 0 and year % 4 == 0:
#         print("Leap year")
#     else:
#         print("Not a leap year")
# leap_year(2000)
# leap_year(2026)

# Find the sum of numbers from 1 to n
# def sum(n):
#     sum=0
#     for i in range(1, n+1):
#         sum = sum + i
#     return sum
# res = sum(6)
# print(res)

# Print multiplication table of a number
# def mul(n):
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n*i}")
# mul(5)
# mul(15)

# Count vowels in a string
# def vowel(str):
#     count=0
#     for i in str:
#         if i.lower() in "aeiou":
#             count+=1
#     print(count)
# vowel("abcde")


# Reverse a string
# def reverse(str):
#     rev = ""
#     for i in range(len(str)-1, -1, -1):
#         rev = rev + str[i]
#     print(rev)
# reverse("hello")
# reverse("karag")

# Count digits in a number
# def count_digit(num):
#     if num == 0:
#         return 1
#     count = 0
#     while num > 0:
#         count+=1
#         num = num // 10
#     return count
# res= count_digit(0)
# res= count_digit(12345678)
# print(res)

# Reverse a number
# def rev_num(num):
#     rev=0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10
#     print(rev)
# rev_num(1234)

# Find sum of digits
# def sum_digits(num):
#     sum = 0
#     while num > 0: 
#         digit = num % 10
#         sum = sum + digit
#         num = num // 10
#     print(sum)
# sum_digits(123456)
              
# Check if a number is palindrome
# def pallindrome(num):
#     rev = 0
#     original = num
#     while num > 0:
#        digit = num % 10
#        rev = rev * 10 + digit
#        num = num // 10
#     if rev == original:
#         print(f"{original} is pallindrome")
#     else:
#         print(f"{original} is not pallindrome")
# pallindrome(1211)

# Check if a number is palindrome return false or true
# def pallindrome(num):
#     rev = 0
#     original = num
#     while num > 0:
#        digit = num % 10
#        rev = rev * 10 + digit
#        num = num // 10
#     return rev == original
# print(pallindrome(121))

# Find factorial of a number
# def fact(num):
#     fact=1
#     while num > 0:
#        fact = fact * num 
#        num = num-1
#     return fact
# print(fact(6))

# Check if a number is prime
# def prime(num):
#     if num < 2:
#        print("Not prime")
#        return
#     i=2
#     while i < num:
#         if num % i == 0:
#             print("Not prime")
#             return
#         i += 1
#     print("Prime")
# prime(7)

# Check if a number is prime give response in false or true
# def is_prime(num):
#     if num < 2:
#         return False

#     i = 2

#     while i < num:
#         if num % i == 0:
#             return False
#         i += 1

#     return True

# print(is_prime(7))
# print(is_prime(8))



    
