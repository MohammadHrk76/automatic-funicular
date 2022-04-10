import random

number = random.randint(1, 100)

guess_tries = 0

while(guess_tries < 6): #Limited Try

    x = int(input("Please Enter a Number Between 1 to 100: "))

    guess_tries += 1

    print ("Your tries are %d right now" %guess_tries)

    if x > number:

        print("Your guess number is greater than answer number!! Continue!!")

    elif x < number:

        print("Your guess number is less than answer number!! Continue!!")

    elif x == number:

        print("YOU DID IT!!!!!! HOOORAYY!!!")

        break

if x != number:

    print("Bad Luck !! This was Correct Answer: " + str(number))

input("Press any key to exit......")

