def Num_List(list):
    index=0
    while index<len(list):
        if list[index]%5==0:
            print(list[index])
        if list[index]==list[8]:
            break
        index=index+1
Num_List([12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200])



