from random import randrange

def main():
    guess = ''
    num = randrange(10)

    while guess != num:
        guess = int(input("What is your guess? "))

        if guess < num:
            print ("Too small!")
        elif guess > num:
            print ("Too large!")
        elif guess == num:
            print ("Just right!")


main()