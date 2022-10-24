#making pizza

size = str(input("What size of pizza do you want?: "))
add_pepperoni = str(input("Do you want to add pepperoni? Y/N:"))
extra_cheese = str(input("Do you want to add extra cheese?? Y/N:"))
print("--------------------------------------------------------")

def small():
        if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
            print("Your final bill is: 18$")
        elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your final bill is: 17$")
        elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
            print("Your final bill is: 16$")
        else:
            print("Your final bill is: 15$")
        
    
def medium():
    while True:
        if size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
            print("Your bill is: 24$")
            break
        elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your bill is: 23$")
            break
        elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your bill is: 21$")
            break
        else:
            print("Your bill is: 20$")
            break
    
def large():
    while True:
        if size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
            print("Your bill is: 29$")
            break
        elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your bill is: 28$")
            break
        elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
            print("Your bill is: 26$")
            break
        else:
            print("Your bill is: 25$")
            break

first = small()
second = medium()
third = large()

print(medium, large)
















