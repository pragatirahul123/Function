def element_count(list,var):
    count=0
    index=0
    while index<len(list):
        if var in list[index]:
            count=count+1
        index=index+1
    return count
    
list1 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
print("A :",element_count(list1,"A"))
print("E:", element_count(list1,"E"))
    
