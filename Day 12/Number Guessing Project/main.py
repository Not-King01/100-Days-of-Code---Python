import art
import random
print(art.logo)
print("Welcome to Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

def check_answer(value):
    if value == answer:
        print("Correct!")
        return True
    elif value < answer:
        print("Too low!")
        print("Guess again!")
        return False
    elif value > answer:
        print("Too high!")
        print("Guess again!")
        return False
    else:
        print("There is an input error! Please try again.")
        return False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
chances = 0
if difficulty == "easy":
    chances = 10
    a = False
    print(f"You have 10 guesses left.")
    for i in range(chances):
        user_input = int(input("Guess a number between 1 and 100: "))
        a = check_answer(user_input)
        if a == True:
            break
        else:
            print(f"You have {chances + i - 1} guesses left.")
    if a == False:
        print("You have run out of guesses, you lose.")
elif difficulty == "hard":
    chances = 5
    a = False
    print(f"You have 5 guesses left.")
    for i in range(chances):
        user_input = int(input("Guess a number between 1 and 100: "))
        a = check_answer(user_input)
        if a == True:
            break
        else:
            print(f"You have {chances - i - 1} guesses left.")
    if a == False:
        print("You have run out of guesses, you lose.")
else:
    print("That's not a valid input!")


