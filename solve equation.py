
def  tot(equation):
                      
    try:                    
      equal=str(eval(equation))
      print(equal)
    except SyntaxError:          
             print("SyntaxError")  
    except  ZeroDivisionError:
             print("ZeroDivisionError")                                    