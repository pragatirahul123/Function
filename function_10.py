def change_num(list):
    x=[]
    y=[]
    z=[]
    for index in list:
        if type(index)==int:
            x.append(index)
        elif type(index)==float:
            y.append(index)
        elif type(index) == str:
            z.append(index)
    print(x)
    print(y)
    print(z)
change_num([1,2,3,"a","f","g",2.3,4.6,2.1])
    

