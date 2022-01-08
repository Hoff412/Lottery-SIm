import random
from datetime import datetime

#picking lottery numbers

ticket_numbers = []

while len(ticket_numbers) < 6:
    try:
        guess = int(input("Select a number between 1 and 53: "))
    except ValueError:
        print("Must be a number")
    

    if guess not in ticket_numbers and 0 < guess < 54 and type(guess) == int:
        ticket_numbers.append(guess)
       # print(ticket_numbers)
    else:
        print("Number must be between 1 and 53, and no duplicates.")
        continue


ticket_numbers.sort()
print("Your numbers: ", ticket_numbers)

#drawing
start_time = datetime.now()
drawings = 0
while True:
    winning_numbers = []
    while len(winning_numbers) < 6:
        ball = random.randint(1, 53)
        if ball not in winning_numbers:
                winning_numbers.append(ball)
    winning_numbers.sort()
    drawings += 1
    print(drawings, winning_numbers)

    if winning_numbers == ticket_numbers:
        print(f"Winner!!!!! After {drawings} Drawings!")
        how_long = drawings / 104
        print(f"At 2 drawings per week, this would take {how_long} years")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        break
            
# 6 21 27 39 42 43
