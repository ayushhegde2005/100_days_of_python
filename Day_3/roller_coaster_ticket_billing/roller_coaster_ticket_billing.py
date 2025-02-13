#This program checks the eligibility whether the person is eligible to ride the roller or not based on the persons height and outputs the cost of their ticket for the roller coaster ride based on their age and free ride for those who are in their mid life crisis

import string

print("***********************************************************************************************************")
print("Welcome to the Roller Coaster ride:")
print("***********************************************************************************************************")

height = int(input("Please enter your height:\n"))
total = 0
if 135 > height:
    print("You are not eligible to ride the roller coaster, you have to get tall to ride the roller coaster")

else:
    print("You are eligible to ride the roller coaster")
    print("You are not eligible to ride the roller coaster, you have to get tall to ride the roller coaster")
    age = int(input("Enter you age:\n"))
    if 12 >= age:
        total += 30
    elif 12 < age < 18:
        total += 40
    elif 45 <= age <= 55:
        total +=0
    else:
        total += 50

    photo = input("Do you want your photos to be taken:\nYes or no.\n").lower()
    if 'yes' == photo:
        total += 20

    else:
        total += 0

    print(f"The total ticket price is Rs.{total}")
print("***********************************************************************************************************")


