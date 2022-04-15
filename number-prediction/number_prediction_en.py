import random

correct_number = random.randint(1, 10)
live = 5
meter = 0
point = 120

while live > 0:
    live -= 1
    meter += 1
    point -= 20
    guess = int(input("your guess is: "))

    if correct_number == guess:
        print(f"Congratulations. You won on your {meter} try. Your point is {point}.")
        break
    elif correct_number > guess:
        print('Please choose a higher  number.')
    else:
        print('Please choose a smaller number.')
    
    if live == 0:
        print(f"You do not have live anymore. Correct number is {correct_number}")
