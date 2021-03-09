def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print ("Kya main print ho payungi? :-(")

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
fri_menu = menu("friday")
print (fri_menu) 


####################################################################################################
def greet(*names):
    for name in names:
        print("Welcome", name)


greet("Rinki", "Vishal", "Kartik", "Bijender") 



#########################################################################################3

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))






