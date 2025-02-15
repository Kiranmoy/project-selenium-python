
# read file line wise iteratively using while loop & readline()
with open("test.txt") as file:
    print("# read file line wise iteratively using while loop & readline()")
    line = file.readline()
    while line != "":
        print(line, end="")
        line = file.readline()

print("\n")

# read file line wise iteratively using for loop & readlines()
with open("test.txt") as file:
    print("# read file line wise iteratively using for loop & readlines()")
    for line in file.readlines():
        print(line, end="")

print("\n")
