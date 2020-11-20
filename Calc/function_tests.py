import calc

class FuncTests:
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

        return([flag,string])

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

        return([flag,string])