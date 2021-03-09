def Duplicate_Que(list):
    index=0
    new=[]
    while index<len(list):
        j=i+1
        while j<len(list):
            if list[index]==list[j]:
                new.append(list[index])
                list.remove(list[index])
            j=j+1
        index=index+1
    print(list)
Duplicate_Que(['Python', 'Exercises', 'Practice', 'Solution', 'Exercises'])
    
