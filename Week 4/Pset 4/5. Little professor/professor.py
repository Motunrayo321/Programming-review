from random import randrange


def main():
    count = 0
    level = get_level()
    print (f"Level: {level}")
    

    while count < 10:
        num1 = generate_integer(level)
        num2 = generate_integer(level)

        question = num1 + num2
        #print (question)
        answer = int(input(f"{num1} + {num2} = "))

        counter = 1
        while answer != question and counter < 3:
            print ("EEE")
            #print (f"Counter: {counter}")
            counter += 1
            answer = int(input(f"{num1} + {num2} = "))
        
        if counter == 3 and answer != question:
            print (f"Answer: {question}\n")

        count += 1


def get_level():
    while True:
        level = input("Which level do you want to play? ").strip()

        if level == '1' or level == '2' or level == '3':
            return int(level)
            break


def generate_integer(level):
    if level == 1:
        num = randrange(9)
    elif level == 2:
        num = randrange(99)
    elif level == 3:
        num = randrange(999)

    return num

if __name__ == "__main__":
    main()