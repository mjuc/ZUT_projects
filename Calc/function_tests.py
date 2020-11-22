import calc
from termcolor import colored



class FuncTests:
    # method printing results of tests
    def print_result(self,test,res_string,result):
        if(result == True):
            print(test,colored(res_string,'green'))
        else:
            print(test,colored(res_string,'red'))


    def AddingTest(self,temp_calc):
    
        flag = True
        
        temp = temp_calc.Add(2+3)    
        if(temp != 5):
            flag = False
            string = "Integer test failed"

        temp = temp_calc.Add(2.5+2.2)
        if(temp != 4.7):
            flag = False
            string = "Float test failed"
        
        if(flag == True):
            string = "Passed"

        self.print_result("Adding test",string,flag)

    def SubtractingTest(self,temp_calc):
        
        flag = True

        temp = temp_calc.Subtract(3,2)
        if(temp != 1):
            flag = False
            string = "Integer test failed"
        
        temp = temp_calc.Subtract(3.3,2)
        if(temp != 1.3):
            flag = False
            string = "Float test failed"
        
        if(flag == True):
            string = "Passed"

        self.print_result("Subtracting test",string,flag)

    def MultiplyingTest(self,temp_calc):

        flag = True

        temp = temp_calc.Multiply(3,2)
        if(temp != 6):
            flag = False
            string = "Integer test failed"
        
        temp = temp_calc.Multiply(4.5,2)
        if(temp != 9):
            flag = False
            string = "Float test failed"

        if(flag == True):
            string = "Passed"

        self.print_result("Multiplying test",string,flag)

    def DividingTest(self,temp_calc):

        flag = True

        temp = temp_calc.Divide(6,2)
        if(temp != 3):
            flag = False
            string = "Integer test failed"
        
        temp = temp_calc.Divide(4.5,2)
        if(temp != 2.25):
            flag = False
            string = "Float test failed"

        if(flag == True):
            string = "Passed"

        self.print_result("Dividing test",string,flag)

    def SquareRootTest(self,temp_calc):

        flag = True

        temp = temp_calc.SquareRoot(4)
        if(temp != 2):
            flag = False
            string = "Integer test failed"
        
        temp = temp_calc.SquareRoot(10.89)
        if(temp != 3.3):
            flag = False
            string = "Float test failed"

        if(flag == True):
            string = "Passed"

        self.print_result("Square root test",string,flag)

    # method executing all unit tests
    def Execute(self,temp_calc):
        flist = [
            self.AddingTest,
            self.SubtractingTest,
            self.MultiplyingTest,
            self.DividingTest,
            self.SquareRootTest]

        for test in flist:
            test(temp_calc)