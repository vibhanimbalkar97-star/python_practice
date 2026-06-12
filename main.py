# n = int(input("Enter num:- "))

# for i in range(n):
#     print("hello world")

# for i in range(1, n+1):
#     print(i)

# for i in range(n, 0, -1):
#     print(i)

# sum=0;

# for i in range(1,n+1):
#     sum = sum + i;

# print(sum)

# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# even=0
# odd=0

# for i in range(1, n+1):
#     if(i % 2 == 0):
#         even = even + i
#     else:
#         odd = odd + i
# print(f"sum of even numbers: {even} and odd: {odd}")


# for i in range(1, n+1):
#     if(n % i == 0):
#         print(i)

# sum=0
# for i in range(1,n):
#     if(n%i==0):
#         sum=sum + i
# if(n == sum):
#     print(f"{n} is perfect no")
# else:
#     print(f"{n} is not perfect no")

# count=0
# for i in range(1, n+1):
#     if(n%i == 0):
#         count = count + 1
# if count == 2:
#     print(f"{n} is prime no.")
# else:
#     print(f"{n} is not prime no.")

# a = "helle"
# b=""

# for i in range(len(a)-1,-1, -1):
#     b = b + a[i]
# print(b)

# a= "naman"
# b=""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# if(b == a):
#     print("Pallindrome")
# else:
#     print("not Pallindrome")

str1 = "P@#yn26at^&i5ve"

digit =0
char=0
s=0

for i in str1:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        char = char + 1
    else:
        s = s + 1
print(digit, char,s)

    