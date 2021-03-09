def duplicate_element_not_count():
    #a="apple"
    #i=0
    #new=[]
    #count=0
    #while i<len(a):
        #if a[i] not in new:
            #new.append(a[i])
            #count=count+1
        #i=i+1
    #print(new,count)
        
#duplicate_element_not_count()
##########################################################################################



def duplicate_element_not_count():
    a1="apple"
    index=0
    new=[]
    count=0
    while index<len(a1):
        if a1[index] not in new:
            new.append(a1[index])
            count=count+1
        index=index+1
    return (count)
        
print(duplicate_element_not_count())
