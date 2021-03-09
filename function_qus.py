def Even_Number(list):
    index=0
    new=[]
    while index<len(list):
        if list[index]%2==0:
            new.append(list[index])
        index=index+1
    print(new)
       
Even_Number([1, 2, 3, 4, 5, 6, 7, 8, 9])
