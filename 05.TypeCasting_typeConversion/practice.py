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

# # Lists
# print(list("Python"))                     # ['P', 'y', 't', 'h', 'o', 'n']
# print(tuple("ABC"))                       # ('A', 'B', 'C')
# print(set("Hello"))                       # {'H', 'o', 'l', 'e'}

# print(tuple([1,2,3]))                     # (1, 2, 3)
# print(tuple(["Hello", "ABC"]))            # ('Hello', 'ABC')

# print(list((4,5,6)))                      # [4, 5, 6]
# print(list(("ABC", "Hello1", "Hello2")))  # ['ABC', 'Hello1', 'Hello2']

# print(set([1,2,3,4,5,6,6]))               # {1, 2, 3, 4, 5, 6}
# print(list({10,11,12,13,14}))             # [10, 11, 12, 13, 14]

# data = {"a": 10, "b":20}
# print(list(data))                         # ['a', 'b']
# print(tuple(data))                        # ('a', 'b')
# print(set(data))                          # {'b', 'a'}

# print(list(range(0, 5)))                  # [0, 1, 2, 3, 4]

# print(list(123)) type error cannot iterable through integer


"""dict() rules"""
# # list to dict
# print(dict([("name", "ABC"), ("age", 20)]))        # {'name':'ABC', 'age':20}

# #  tuple to dict
# print(dict((("name", "ABC"), ("age", 20))))        # {'name':'ABC', 'age':20}

# # dict to dict
# print(dict({"name":"ABC", "age":20}))              # {'name':'ABC', 'age':20}

# #  duplicate keys
# print(dict([("name", "ABC"), ("age", 20), ("age", 25)])) # {'name':'ABC', 'age':25}

# Incorrect pair length gives ValueError
# print(dict([("name", "ABC", "RRR")]))        # value error

# Integer cannot directly convert into dict
# print(dict(10))        # type error


"""Automatic Type Conversion in Arithmetic"""
print(10 + 2.5)       # 12.5
print(10 + 2)         # 12
print(10.5 + 2.5)     # 13.0
print(True + False)   # 1
# print(10 + "2.5")     # type error
print(10 + int(float("2.5")))# 12
print("10" + "2")     # 102
print("10" * 3)       # 101010
print("10" + "2")     # 102
print(3 * "HI")       # HIHIHI
# print("HI" * 2.5)     # type error
print(10 / 2)         # 5.0
print(10 // 2)        # 5
print(10 // 3)        # 3
print(-10 // 3)       # -3.33 => -4
print(10 % -3)        # -3.33 => -4 => -4 * -3 => 12 => 10 - 12 => -2
print(10 % 3)         # 3.33 => 3 => 3 * 3 => 9 => 10-9 => 1
print(2 ** 3)          # 8
print(2 ** -2)         # 1 / 2 ** 2 => 1/ 4 => 0.25









