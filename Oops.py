class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("i will execute automatically when object is created")

    def getData(self):
        print("i am now executing as a method in this class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())
