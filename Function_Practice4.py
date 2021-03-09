#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def number(list):
    index=0
    new=[]
    while index<len(list):
        if list[index] not in new:
            new.append(list[index])
        index=index+1
    print (new)
        
number([1,2,3,3,3,3,4,5])




#####################################################################################################################




