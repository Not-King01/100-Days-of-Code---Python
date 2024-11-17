print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    if height > 180:
        print("You are too big to ride the rollercoaster!!")
    else:
        print("You can ride the rollercoaster!")
else:
    print("Sorry you have to grow taller before you can ride.")
