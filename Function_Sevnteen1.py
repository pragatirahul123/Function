def different_ques(colour1,colour2):
    new=[]
    new2=[]
    index=len(colour1)-1
    while index>=0:
        j=0
        while j<len(colour2):
            if colour1[index]==colour2[j]:
                new.append(colour1[index])
                colour1.remove(colour1[index])
                new2.append(colour2[j])
                colour2.remove(colour2[j])
            j=j+1
        index=index-1
    print(colour1)
    print(colour2)

different_ques(["red", "orange", "green", "blue", "white"],["black", "yellow", "green", "blue"])
        
