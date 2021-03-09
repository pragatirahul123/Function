def add_number(number1,number2):
    num1=56
    num2=12
    sum=num1+ num2
    print(sum)
add_number(56,12)



########################################################################################




def add_numbers_list (list1,list2):
    index=0
    sum=0
    while index<len(list1):
        sum= list1[index]+list2[index]
        index=index+1
        print(sum)

add_numbers_list([50, 60, 10], [10, 20, 13])

#################################################################################






def add_numbers_list (list1,list2):
    index=0
    sum=0
    while index<len(list1):
        multi= list1[index]*list2[index]
        index=index+1
        print(multi)

add_numbers_list([5, 10, 50, 20], [2, 20, 3, 5])
