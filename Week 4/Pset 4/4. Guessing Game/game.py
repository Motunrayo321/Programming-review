from random import randrange

def main():
    limit = -1 

    while limit < 1:
        try:
            limit = int(input("What is the level of this game? "))
        except ValueError:
            print ("Please input a positive integer!")

    guess = ''
    num = randrange(limit)

    while guess != limit:
        try:
            guess = int(input("What is your guess? "))
            print (game(guess, limit))
        except ValueError:
            print ("Please input a positive integer!")
    

def game(guess, num):

    if guess < num:
        return ("Too small!")
    elif guess > num:
        return ("Too large!")
    elif guess == num:
        return ("Just right!")

main()