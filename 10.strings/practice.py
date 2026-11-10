# create string
# name1 = 'abc'
# name2 = "abc"
# name3 = """abc12 hello world
# heyy@"""    #multiline strings
# print(name3)

# quotes inside string
# greet = 'hi it\'s \'good\''
# print(greet)

# indexing
# str = "hello all"
# print(str[3])   #l
# print(str[-1])  #l
# print(str[-5])  #o, count space also
# print(str[5])  #""
# print(str[10]) #index error = out of range

# extract string = slice[start:end:step], start = included, end = excluded, step = how many position move to each time
# s = "python"
# print(s[:4:])   #pyth
# print(s[4::])   #on
# print(s[1:4:2]) #yh
# print(s[1:4:-1])   #""
# print(s[4:1:])   #""
# print(s[4:1:1])   #""
# print(s[-4::])   #thon
# print(s[-3:-5:])   #""
# print(s[-4:-6:])   #""
# print(s[-4:-1:2])   #to
# print(s[:-1:2])   #pto
# print(s[-4::2])   #to
# print(s[::-1])   #nohtyp = reverse string

# immutable
# s = "hello"
# s[0] ="j"    #type error

# s = "j" + s[1:]
# print(s)  #jello

# s = s.upper()
# print(s)   # JELLO

# s.upper()
# print(s)  #hello

# length = include space and symbol.
# s = "hello 123@"
# print(len(s))       #10
# print(len(""))       #0
# print(len(" "))     #1

# cases
# s = "Python programming"

# print(s.upper())   #PYTHON PROGRAMMING
# print(s.lower())   #python programming
# print(s.title())   #Python Programming
# print(s.capitalize())   #Python programming
# print(s.swapcase())   #pYTHON PROGRAMMING
# print(s.casefold())   #python programming

# remove spaces and characters
# s = "   hello   "
# print(s.strip())     #"hello"
# print(s.lstrip())    #"hello "
# print(s.rstrip())    #" hello"
# print("***hi***".strip("*"))   #hi
# print("cabheabc".strip("abc"))   #"he" not exact substring, matching characters
# print("cabheabc".lstrip("abc"))   #"heabc"

# search
# find = first position or -1
# rfind = last position or -1
# index = furst position or error
# rindex = last position or error
# count = number of occurrences

s = "banana"
# print(s.find("a"))     # 1
# print(s.rfind("a"))    # 5
# print(s.find(""))     # 0
# print(s.find("c"))     #-1
# print(s.rfind(""))     # 6 = it gives length

# print(s.index("a"))     # 1
# print(s.rindex("a"))    # 5
# print(s.index(""))     # 0
# # print(s.index("c"))     #value error 
# print(s.rindex(""))     # 6 = it gives length

# print(s.count("a"))     # 3
# print(s.count("c"))    # 0

# replace(old, new, count)
# s = "Hello world"
# print(s.replace("l", "b"))     # Hebbo worbd
# print(s.replace("l", "b", 2))     # Hebbo world = count = how many
# print(s.replace("l", ""))     # Heo word

# print(s.replace("Hello", "a"))     # a world
# print(s)     # Hello world

# split = divides string into list
s = "hello  allr"

# print(s.split(""))     # value error = empty separator
# print(s.split(" "))     # ['hello', '', 'allr']
# print(s.split(","))     # if not separator then given the original str = ['hello allr']

# join
words = ["I", "love", "Python"]
print("".join(words))     # IlovePython
print(" ".join(words))     # I love Python












"""js
indexing = no index = undefined
            -ve index use .at()
            
slice(4, 2) = "", same for -ve also
"""