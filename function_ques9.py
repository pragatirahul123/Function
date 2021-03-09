def multiply(list):
    index=0
    new=[]
    while index<len(list):
        a1=list[index]*list[index]
        new.append(a1)
        index=index+1
    print(new)
multiply([1, 2, 3, 4, 5, 6, 7])
        
