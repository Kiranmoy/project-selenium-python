# function - group of related statements that perform a specific task

# function declarations
def greetme():
    print("Hello Kiranmoy")


def greetuser(name):
    print("Hello {}".format(name))


def add(num1, num2):
    return num1 + num2


# function calls - executing functions
greetme()
greetuser("Kiranmoy Paul")
print(add(10,20))