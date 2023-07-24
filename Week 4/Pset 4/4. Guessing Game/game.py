from random import randrange

def main():
    guess = int(input("What is your guess? "))

def game(guess):
    num = randrange(10)

    if guess < num:
        print ("Too low.")
    elif guess > num:
        print ("Too high.")
    elif guess == num:
        print ("You got it!")