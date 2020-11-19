import calc

# print result
def print_result(result,test):
    if(result == True):
        print("{test} passed\n")
    else:
        print("{test} failed\n")

# tests definitions

def Tests(temp_calc):
    temp = temp_calc.Add(2+3)
    if(temp != 5):
        print_result(False,"Integer adding test")
    else:
        print_result(True,"Integer adding test")
    temp = temp_calc.Add(2.5+2.2)
    if(temp != 4.7):
        print_result(False,"Float adding test")
    else:
        print_result(True,"Float adding test")
    temp = temp_calc.Subtract(3,2)
    if(temp != 1):
        print_result(False,"Integer subtracting test")
    else:
        print_result(True,"Integer subtracting test")
    temp = temp_calc.Subtract(3.3,2)
    if(temp != 1.3):
        print_result(False,"Float subtracting test")
    else:
        print_result(True,"Float subtracting test")
    temp = temp_calc.Multiply(3,2)
    if(temp != 6):
        print_result(False,"Integer multiplying test")
    else:
        print_result(True,"Integer multiplying test")
    temp = temp_calc.Multiply(3.3,2)
    if(temp != 6.6):
        print_result(False,"Float multiplying test")
    else:
        print_result(True,"Float multiplying test")

# Calculator test instance
clc = calc.Calc()

# Run tests here

Tests(clc)
