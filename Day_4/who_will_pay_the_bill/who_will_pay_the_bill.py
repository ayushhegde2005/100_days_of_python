import random

friends = ["John", "Alex", "Liza", "Sam", "Paul"]

choice = random.randint(0, (len(friends)-1))
choosen_friend = friends[choice]

print(f"The person who will be paying the bill is {choosen_friend}")

