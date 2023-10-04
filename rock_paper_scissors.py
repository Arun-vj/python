import random

rock = """

---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """

---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock,paper,scissor]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(game[user])
computer = random.randint(0,2)
print("computer choice")
print(game[computer])
if user == computer:
    print("Match Draw")
elif user == 0 and computer == 2:
    print("user win")
elif computer == 0 and user == 2:
    print("computer win")
elif computer > user:
    print("computer win")
elif user > computer:
    print("user win")
elif user>=4 or user <0:
    print("invalid input")