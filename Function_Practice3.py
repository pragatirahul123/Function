def Factorial_Num(var):
    index=1
    fact=1
    while index<=var:
        fact=fact*index
        index=index+1
    print(fact)

user=int(input("enter a number"))    
Factorial_Num(user)
