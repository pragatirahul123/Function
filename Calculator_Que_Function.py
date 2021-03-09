def calculator(x,y,operator):
    if operator == "add":
        print(x+y)
    elif operator =="sub":
        print(x-y)
    elif operator =="multi":
        print(x*y)
    elif operator == "divi":
        print(x/y)
    elif operator == "modu":
        print(x%y)
calculator(34,24,"add")
calculator(50,20,"sub")
calculator(2,7,"multi")
calculator(4,8,"divi")
calculator(5,3,"modu")
        


###################################################################################################

def calculator(x,y,operator):
    if operator =="add":
        result = (x+y)
        print(result)
    
    if operator =="sub":
        result = (x-y)
        print(result)
        
    if operator == "multi":
        result = (x*y)
        print(result)
    
    if operator =="modules":
        result= (x%y)
        print(result)
        
    if operator == "divide":
        result= (x/y)
        print(result)
        

calculator(2,3,"add")
calculator(6,2,"sub")
calculator(12,2,"multi")
calculator(7,3,"modules")
calculator(8,2 ,"divide")


