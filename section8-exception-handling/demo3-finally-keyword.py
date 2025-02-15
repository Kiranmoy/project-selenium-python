try:
    print("Executing try block")
    with open("file.log") as file:
        print(file.read())
except FileNotFoundError as file_not_found:
    print("Caught exception - printing it in except block")
    print(file_not_found)
finally:
    print("Finally block will always execute irrespective of exception raised or not")