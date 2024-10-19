import numpy as np
import argparse

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return self.num1 / self.num2


    def random_operation(self):
        return self.num1 * self.num2 * np.random.rand(3,3)

def some_function(num):
    return np.random.randn(2,2) * num

def myargs():
    parser = argparse.ArgumentParser(description="This program performs basic arithmetic operations.",
                                    epilog='** Version 1.0 **',
                                    prog= 'Arithmetic operator')
    parser.add_argument("-n",
                        "--num1", 
                        type=float, 
                        help="First number", 
                        default = 2.20)
    parser.add_argument("-m",
                        "--num2", 
                        type=float, 
                        help="Second number", 
                        default = 2.20)

    parser.add_argument("-o",       
                        "--operation", 
                        choices=["add", "subtract", "multiply", "divide"],
                        help="Operation to perform", default = "add")

    return parser.parse_args()