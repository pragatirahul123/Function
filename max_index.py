def Number_index(list):
    i1=0
    max=0
    index=0
    while i1<len(list):
        if list[i1]>max:
            max=list[i1]
            index=i1
        i1=i1+1
    print("max", max,"index",index)
Number_index([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54])

