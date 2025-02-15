class Calculator:
    num = 100

    def __init__(self, value1, value2):
        print("Parent constructor executed during object creation")
        self.value1 = value1
        self.value2 = value2

    def getMethod(self):
        print("Parent method executed")

    def add(self):
        return self.value2 + self.value2


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self, value1, value2):
        print("Child constructor executed during object creation")
        Calculator.__init__(self, value1, value2)

    def getCompleteData(self):
        return self.num2 + self.num + self.add()


obj = ChildImpl(10, 20)
print(obj.getCompleteData())
