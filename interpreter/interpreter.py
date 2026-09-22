import re

class maths:
    def __init__(self,first,op,last):
        self.first = float(first)
        self.op = op
        self.last = float(last)

    def formula(self, op):
        if self.op == "+":
            return self.first+self.last
        elif self.op == "-":
            return self.first-self.last
        elif self.op == "*":
            return self.first*self.last
        elif self.op == "/":
            if self.last == 0:
                raise "ZeroDivisionError: division by zero"
            return self.first/self.last
        else:
            return "invalid operator"

def main():
    expression =input("Expression: ").strip()
    x,y,z = re.split(r"\s*([+\-*/])\s*", expression)
    x, z= float(x),float(z)
    value = maths(x,y,z)
    calc = value.formula(y)
    print(calc)

main()
