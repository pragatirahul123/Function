def outer(a,b):
    def inner(n1,n2):
        res=n1+n2
        return res
    return inner(2,3)
print(outer(2,1))

*********************************************************************************************************



def outer(a,b):
    def inner(n1,n2):
        res=a+b
        return res
    return inner(2,3)
print(outer(2,1))



***********************************************************************************************
