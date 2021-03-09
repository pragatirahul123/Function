def Different_Value(list):
    index=0
    new=[]
    new2=[]
    while index<len(list):
        if type(list[index])==int:
            new.append(list[index])
        elif type(list[index])==str:
            new2.append(list[index])
        index=index+1
    print(new+new2)

Different_Value([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1])


