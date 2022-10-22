#making pizza order application with python

size = str(input("What size of pizza do you want?: "))
add_pepperoni = str(input("Do you want to add pepperoni? Y/N:"))
extra_cheese = str(input("Do you want to add extra cheese?? Y/N:"))
print("--------------------------------------------------------")

class main():


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
        if size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
            print("Your bill is: 24$")
        elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your bill is: 23$")
        elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your bill is: 21$")
        else:
            print("Your bill is: 20$")
    
    def large():
        if size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
            print("Your bill is: 29$")
        elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
            print("Your bill is: 28$")
        elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
            print("Your bill is: 26$")
        else:
            print("Your bill is: 25$")

result = main()

if __name__ == '__main__':
    print(result)