

# read all contents at once
file = open("test.txt")
print("# read all contents at once")
print(file.read())
file.close()
print()

# read first n characters
file = open("test.txt")
print("# read first n characters")
print(file.read(5))
file.close()
print()

# read file line wise
file = open("test.txt")
print("# read file line wise")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
file.close()
print()