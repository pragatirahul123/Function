def max_number(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    return(max)
print(max_number([6,3,1,8,99,22,100,7]))

def max_number2(list11,list12):
    a=max_number(list11)
    b=max_number(list12)
    return(a,b)
    

list1=[2,3,5,6,8,50,4]
list2=[7,4,2,8,10,89,5]
result = max_number2(list1, list2)
print(result)


*************************************************************************************************************************************

def max_number(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    return(max)
print(max_number([6,3,1,8,99,222,100,7]))

def max_number2(list11,list12):


    c=(list1+list2)
    d=max_number(c)
    return(d)
    

list1=[2,3,5,6,8,500,4]
list2=[7,4,2,8,100,89,5,1200]
result = max_number2(list1,list2)
print(result)


*******************************************************************************************************************
