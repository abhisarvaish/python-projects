# 1. Generate a random number between 1 to 100 2. Ask user for his guess 3. If user's guess is less than 1 or greater
# than 100, then print "Out of Bounds" 4. For user's first guess, if a guess is withon the range of 10 than that of
# actual number, then print "warm", else "cold" 5. From second guess onwards, if user moves closer to actual number
# than his previous guess, then print "warmer", else print "colder" 6. Once user guesses the actual number,
# print number of guesses in which user has guessed the number

import random

number = random.randint(1, 100)
print("Random Number : ", number)
guess_counter = 0
prev_input = 0
user_input = 0

while True:
    try:
        user_input = int(input("Enter your Guess : "))
        guess_counter = guess_counter + 1
        if number == user_input:
            print("Correct Guess, Your Guess Count is : ", guess_counter)
            break

        if user_input < 1 or user_input > 100:
            print("Out Of Bounds")

        if 10 > user_input - number > -10 and guess_counter == 1:
            print("Warm")

        elif guess_counter == 1:
            print("Cold")

        if guess_counter >= 2:
            if prev_input - number > user_input - number:
                print("Warmer")
            else:
                print("Colder")
        prev_input = user_input
    except:
        print("Enter Numbers only")



