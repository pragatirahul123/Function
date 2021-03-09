def sum(*list):
    index=0
    sum=0
    while index<len(list):
        sum=sum+list[index]
        index=index+1
    print(sum)
sum (8, 2, 3, 0, 7)




##################################################################################



def sum(list):
    index=0
    multi=1
    while index<len(list):
        multi=multi*list[index]
        index=index+1
    print(multi)
var= [8, 2, 3, -1, 7]
sum(var)
