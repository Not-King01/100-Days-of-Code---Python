rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human = int(input("Select an option 1.Rock 2.Paper 3.Scissors: "))
print("You chose:\n")
if human == 1:
    print(rock)
elif human == 2:
    print(paper)
elif human == 3:
    print(scissors)
else:
    print("Wrong option")

computer = 0
import random
choice = random.randint(1,3)
print("Computer chose:\n")
if choice == 1:
    computer = 'rock'
    print(rock)
elif choice == 2:
    computer = 'paper'
    print(paper)
else:
    computer = 'scissors'
    print(scissors)

if human == choice:
    print("Draw")
elif (human == 1 and computer == 'paper') or (human == 2 and computer == 'rock') or (human == 3 and computer == 'scissors'):
    print("Computer wins!")
else:
    print("You win!")
