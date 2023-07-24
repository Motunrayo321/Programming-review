from random import randrange

def main():
    n = -1 

    while type(n) != int and n < 0:
        limit = int(input("What is the level of this game? "))

    guess = ''
    num = randrange(limit)

    while guess != num:
        guess = int(input("What is your guess? "))

        if guess < num:
            print ("Too small!")
        elif guess > num:
            print ("Too large!")
        elif guess == num:
            print ("Just right!")



main()