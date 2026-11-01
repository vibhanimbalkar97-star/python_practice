# print(int("10"))                  # 10
# print(float("10"))                # 10.0
# print(str(10))                    # "10"
# print(bool(1))                    # True
# print(list("123"))                # ['1', '2', '3']
# print(tuple([1,2,3,4,5]))         # (1,2,3,4,5)
# print(set([1,2,3]))               # {1,2,3}
# print(dict([("a", 20)]))            # {"a": 20}
# print(complex(10))                # (10+0j)

# # type casting = need to store that value in a variable

# """ int rules"""
# a = "10"
# int(a)
# print(a)  # "10"
# print(type(a)) # str

# b = "20"
# c = int(b)
# print(type(c)) # int

# # Rules of int() – String to Integer
# print(int("100")) # 100 
# print(int("-100")) # -100
# print(int("+100")) # 100

# # print(int("5.6"))  # value error
# print(int(float("5.6")))  # 5

# print(int(5.9))  # 5
# print(round(5.9)) # 6

# print(int(True))   # 1 type = int
# print(int(False))   # 0

# # print(int(""))   #value error bcz no numeric to convert

# print(int("  10  ")) #spaces allowed 10

# # print(int("abc")) #value error

# print(int("1010", 2))  # 10
# print(int("10", 8))    # 8
# print(int("10", 16))   # 16
# # print(int("inf"))    # value error


# """float rules"""
# print(float(5))     # 5.0
# print(float("8"))   # 8.0
# print(float("8.9")) # 8.9
# print(float(4.5))   # 4.5
# print(float(True))  # 1.0
# print(float(" 9 ")) # 9.0
# # print(float("abc")) # value error
# # print(float(""))    # value error

# # special float values
# print(float("inf")) #inf
# print(float("-inf")) #-inf
# print(float("nan")) #nan

# """ str rules()"""
# print(str(40))   # "40"
# print(str("40.0"))   # "40.0"

# print(str(True))   # "True"

# a = str(False)
# print(bool(a))    # True

# print(str([1,2,3]))   # "[1,2,3]"

# print(str(None))    # "None"

# """bool() rules"""
# # Numeric values
# print(bool(0))    # False
# print(bool(0.5))    # True
# print(bool(1))    # True
# print(bool(-1))    # True
# print(bool(0.0))    # False
# print(bool(-0.5))    # True

# # Strings
# print(bool(""))    # False
# print(bool(" "))    # True
# print(bool("hello"))    # True
# print(bool("0"))    # True
# print(bool("False"))    # True

# # Lists
# print(bool([]))    # False
# print(bool([1,2]))    # True
# print(bool([0]))    # True
# print(bool([""]))    # True

# # Tuples
# print(bool(()))    # False
# print(bool((1,)))    # True
# print(bool((0)))    # True

# # Sets
# print(bool(set()))    # False
# print(bool({1,2}))    # True

# # Dictonaries
# print(bool({}))    # False
# print(bool({"a":1}))    # True

# # None
# print(bool(None))    # False bcz none represents absence of value

# # NaN
# print(bool(float("nan")))  # True bcz it is floating value not a number

# Lists
print(list("Python"))                     # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple("ABC"))                       # ('A', 'B', 'C')
print(set("Hello"))                       # {'H', 'o', 'l', 'e'}

print(tuple([1,2,3]))                     # (1, 2, 3)
print(tuple(["Hello", "ABC"]))            # ('Hello', 'ABC')

print(list((4,5,6)))                      # [4, 5, 6]
print(list(("ABC", "Hello1", "Hello2")))  # ['ABC', 'Hello1', 'Hello2']

print(set([1,2,3,4,5,6,6]))               # {1, 2, 3, 4, 5, 6}
print(list({10,11,12,13,14}))             # [10, 11, 12, 13, 14]

data = {"a": 10, "b":20}
print(list(data))                         # ['a', 'b']
print(tuple(data))                        # ('a', 'b')
print(set(data))                          # {'b', 'a'}

print(list(range(0, 5)))                  # [0, 1, 2, 3, 4]

# print(list(123)) type error cannot iterable through integer








