def max_number2(new1,new2):
    c=new1+new2
    d=max_number(c)
    return(d)
    
def max_number(list):
    i=0
    max=0
    while i<len(list):
        if list[i] > max:
            max=list[i]
        i=i+1
    return(max)

def even_odd(list):
    i=0
    new1=[]
    new2=[]
    while i<len(list):
        if list[i]%2==0:
            new1.append(list[i])
        else:
            new2.append(list[i])
        i=i+1
    #print(new1)
    #print(new2)
    c=max_number2(new1,new2)
    print(c)
even_odd([1,2,3,4,5,16,7,8,10,11,12,14,435,13,18,45,98,21,67,32])





