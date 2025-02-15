
# tuple data type - IMMUTABLE
mytuple = 1, 2, "KIRAN", 4, 5       # Equivalent to: mytuple = (1, 2, "KIRAN", 4, 5)

print(mytuple[0])    # 1
print(mytuple[2])    # KIRAN
print(mytuple[-1])   # 5

# slicing
print(mytuple[1:3])  # (2, 'KIRAN')

# exception - for any modification attempt
#mytuple.insert(3, "PAUL")       # AttributeError: 'tuple' object has no attribute 'insert'
#mytuple.append("END")           # AttributeError: 'tuple' object has no attribute 'append'
#mytuple[2] = "KIRANMOY"         # TypeError: 'tuple' object does not support item assignment

# delete
del mytuple[0]
print(mytuple)
