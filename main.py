""" for loops examples"""

""" Numbers questions """

# n = int(input("Enter a number:- "))

# 1. Print numbers 1 to n
# for i in range(1, n+1):
#     print(i)

# 2. Print numbers in reverse e.g. 50 to 1.
# for i in range(n, 0, -1):
#     print(i)

# 3.Print all even numbers.
# for i in range(1, n+1):
#     if(i%2==0):
#         print(i)

# Print all odd numbers from 1 to 100.
# for i in range(1, n+1):
#     if(i%2 != 0):
#         print(i)

# Find the sum of numbers from 1 to 50.
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

# Print the multiplication table of any number.
# for i in range(n, n*10+1, n):
#     print(i)

# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")

# Find the factorial of a number.
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# Accept an integer and Print hello world n times
# for i in range(n):
#     print("hello world")

# Sum up to n terms
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

# Factorial of a number
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# Print the sum of all even & odd numbers in a range
# separately
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"{even} and {odd}")

# Print all the factors of a number
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)

# - Accept a number and check if it a perfect number or not.
# count =0
# for i in range(1, n):
#     if n%i == 0:
#         count = count + i
# if count == n:
#     print("perfect number")
# else: 
#     print("not perfect number")
       

# Check wether the number is prime or not
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("prime number")
# else:
#     print("not a prime number")

""" strings questions"""

# n = input("Enter a string:- ")

# Count how many vowels are in a string.
# count = 0
# for i in n:
#     if i.lower() in "aeiou":
#         count = count + 1
# print(count)

#  Print each character of a string
# for i in n:
#     print(i)

# - Reverse a string without using in build functions.
# print(n[: : -1])
# rev = ""
# for i in range(len(n)-1, -1, -1):
#     rev = rev + n[i]
# print(rev)

# - Check string is Pallindrome or not
# rev = ""
# for i in range(len(n)-1, -1, -1):
#     rev = rev + n[i]
# if rev == n:
#     print("pallindrome")
# else:
#     print("not a pallindrome")

# - Count all letters, digits, and special symbols from a given
# string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4
# digit = 0
# char= 0
# spchar= 0

# for i in n:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchar += 1
# print(f"{digit}, {char}, {spchar}")

"""while loop"""
# Separate each digit of a number and print it on the new line
# while n > 0:
#     digit = n % 10
#     n = n // 10
#     print(digit)


#  Accept a number and print its reverse 
# n = int(input("Enter a number:- "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n//10
# print(rev)

#  Accept a number and check if it is a pallindromic number (If
# number and its reverse are equal?
# n = int(input("Enter a number:- "))
# copy = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if rev == copy:
#     print("Pallindrome number")
# else:
#     print("Not a Pallindrome number")
    
#  Create a random number guessing game with python.
# import random
# num = random.randint(1, 10)
# tries = 0

# while True:
#     guess = int(input("Enter the number between 1 to 10:- "))
#     if num == guess:
#         tries+=1
#         print(f"You guessed right number in {tries} tries")
#         break
#     elif num > guess:
#         print(f"Go little higher")
#         tries+=1
#     elif num < guess:
#         print(f"Go little lower")
#         tries+=1
#     else:
#         tries+=1
#         print("sorry you are wrong")