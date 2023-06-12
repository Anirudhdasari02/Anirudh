class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def mod(self):
        return self.num1 % self.num2
    

input_string = input("Enter the input:")
var = input_string.split()
op = var[1]
obj = Calculator(float(var[0]),float(var[2]))
try:
    if op == '+':
        a=obj.add()
    elif op == "-":
        a=obj.sub()
    elif op == "*":
        a=obj.mul()
    elif op == "/":
        try:
            a=obj.div()
        except:
            print("Invalid")
    elif op == "%":
        a=obj.mod()
    print(a)
    
except Exception as e:
    print(e)

        