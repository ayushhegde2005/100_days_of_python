import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
 
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Welcome to Rock Paper Scissors game!")
user_choice = int(input("Enter your choice:\n0 for Rock, 1 for paper and 2 for scissors\n"))
comp_choice = random.randint(0, 2)

if 0 == user_choice:
    print(f"Your choice is {rock}")
elif 1 == user_choice:
    print(f"Your choice is {paper}")
else:
    print(f"Your choice is {scissors}")

if 0 == comp_choice:
    print(f"Computer's choice is {rock}")
elif 1 == comp_choice:
    print(f"Computer's choice is {paper}")
else:
    print(f"Computer's choice is {scissors}")

if user_choice == comp_choice:
    print("Its a Draw!")
elif 0 == user_choice and 2 == comp_choice:
    print("You Win!")
elif 2 == user_choice and 1 == comp_choice:
    print("You Win!")
elif 1 == user_choice and 0 == comp_choice:
    print("You Win!")
else:
    print("You have Lost!")


