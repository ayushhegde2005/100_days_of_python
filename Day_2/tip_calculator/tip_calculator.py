#This program calculates the amount to tip to be given to the restaurant based on the total bill and divides the bill among the peole of the group who went out to have food at restaurant

print("*************************************************************************")
print("Welcome to Tip Calculator!")
print("*************************************************************************")

bill_amount = int(input("What was the total bill?\nRs."))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
num_of_people = int(input("How many people to split the bill?\n"))

total = bill_amount*(1+tip/100)

bill_per_person = total/num_of_people

print(f"The the total amount is Rs.{round(total, 2)}")
print(f"Each person should pay Rs.{round(bill_per_person, 2)}")
print("*************************************************************************")


