from random import randrange

def main():
    guess = ''
    num = randrange(10)

    while guess != num:
        guess = int(input("What is your guess? "))

        if guess < num:
            print ("Too low.")
        elif guess > num:
            print ("Too high.")
        elif guess == num:
            print ("You got it!")

    print ("Congratulations!")

main()