age     = 25         # int ====> whole numbers => 3.9 gives 3 not 4
name    = "ABC"      # str ====> immutable means cannot change.
price   = 55.5       # float = 10 / 2 => 5.0, / reproduce fload when division is exact.
is_adult= True       # bool => 

name1  = "Hello"
print(name1[0])      # H
print(len(name1))    # 5

name1 = "Python"     # reassign allowed
print(name1)

# name1[0] = "r"       # typeerror, we cannot change individual characters
name1 = name1.replace("t", "T") # we can change individual using this
print(name1)        

print(5 > 6)        # False = Capitalization matters

result  = None        # is a singleton object
print(result is None) # True