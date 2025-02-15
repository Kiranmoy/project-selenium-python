class Calculator:
    num = 100

    def __init__(self, value1, value2):
        print("Constructor executed during object creation")
        self.value1 = value1
        self.value2 = value2

    def getMethod(self):
        print("Method executed")

    def add(self):
        return self.value2 + self.value2


obj = Calculator(10,20)
print(obj.num)
obj.getMethod()
print(obj.add())
