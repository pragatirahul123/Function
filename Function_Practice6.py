string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isupper()):
            count1=count1+1
      elif(i.islower()):
            count2=count2+1
print("upper:",count1)
print("lower:",count2)

