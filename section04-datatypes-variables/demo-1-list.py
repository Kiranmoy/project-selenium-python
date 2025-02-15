
integer = 1
string = "Kiran"
boolean = True

# list data type - MUTABLE
mylist = [1, 2, "KIRAN", 4, 5]
print(mylist[0])    # 1
print(mylist[2])    # KIRAN
print(mylist[-1])   # 5

# slicing
print(mylist[1:3])  # [2, 'KIRAN']

# insert
mylist.insert(3, "PAUL")
print(mylist)

# append
mylist.append("END")
print(mylist)

# update
mylist[2] = "KIRANMOY"
print(mylist)

# delete
del mylist[0]
print(mylist)