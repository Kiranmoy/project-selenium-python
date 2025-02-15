
# Iterate collection of object
mylist = [2, 3, 5, 7, 9]

for item in mylist:
    print(item)

# Sum of first 5 natural numbers
total = 0
for num in range(1,6):
    total += num
print("Sum of first 5 natural numbers: {}".format(total))

# Sum of first 5 odd numbers
total = 0
for num in range(1,11,2):
    total += num
print("Sum of first 5 odd numbers: {}".format(total))
