#This program outputs the order report with total price of the order based on the size of the pizza and the toppings ordered

import string
total_amount = 0

print("**********************************")
print("Welcome to python pizza.")
print("**********************************")
print("\n")
choice = input("Would you like to order pizza?\nType 'Y' for Yes and 'N' for No:\n")
print("\n")
if "y" == choice:
    size = input("What is the size of the pizza would you like:\nType 'S' for small, 'M' for medium and 'L' for large:\n").lower()
    if 's' == size  or 'm' == size or 'l' == size:
        if 's' == size:
            total_amount +=199
        elif 'm' == size:
            total_amount += 299
        else:
            total_amount += 399
        print("\n")
        
        quantity =  int(input("how many pizza would you like:\n"))
        print("\n")

        toppings = input("Would you like to add toppings?Type 'Y' for yes or 'N' for No:\n").lower()
        print("\n")
        if 'y' == toppings:
            cheese = input("Would you like extro cheese?\nType 'Y' for Yes or 'N' for No:\n").lower()
            if 'y' == cheese:
                total_amount += 39
            print("\n")

            peperonni = input("Would you like peperonni?\nType 'Y' for yes or 'N' for No:\n").lower()
            if 'y' == peperonni:
                total_amount += 49
             
        print("\n")
        print("____________________________")
        print("BILLING REPORT.")
        print(f"pizza = size(m)*{quantity}\ncheese = {cheese}\npeperonni = {peperonni}")
        print(f"The total amount is Rs.{total_amount * quantity}")
        print("____________________________")



    else:
        print("You have entered invalid character.")
    

else:
    print("Thank You! If you ever feel like having pizza, make sure you drop by for the most delicious pizza in the neighbourhood")

print("**********************************")

