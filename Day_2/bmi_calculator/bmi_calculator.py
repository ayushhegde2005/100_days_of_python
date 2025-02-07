#This program takes input such as height in Metres and weight in KG's and then outputs the bmi number of the person

print("*************************************************************************")
print("Welcome to BMI Calculator!")
print("*************************************************************************")
height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in KG's:\n"))

bmi_num = weight/ height ** 2

print(f"Your BMI number is {round(bmi_num, 2)}.")
print("*************************************************************************")

