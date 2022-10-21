#making pizza order application with python

size = str(input("What size of pizza do you want?: "))
add_pepperoni = str(input("Do you want to add pepperoni? Y/N:"))
extra_cheese = str(input("Do you want to add extra cheese?? Y/N:"))
print("--------------------------------------------------------")

def small():
    if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
        print("Your final bill is: 18$")
    elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
        print("Your final bill is: 17$")