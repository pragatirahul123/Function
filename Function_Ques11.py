def check_numbers_list(num1,num2):
    index=0
    while index<len(num1):
        if num1[index]%2==0 and num2[index]%2==0:
            print(num1[index] ,"and", num2[index],"dono even number h ")
            
        else:
            print(num1[index], "and" ,num2[index],"even nhi hai")
        index=index+1
        
check_numbers_list([2, 6, 18, 10, 3, 75], [6, 19, 24, 12, 3, 87])


