def sum(list1,list2):
    index=0
    while index<len(list1):
        sum=0
        sum=sum+list1[index]+list2[index]
        index=index+1
        print(sum)
sum([1,2,3,4],[2,3,4,1])


