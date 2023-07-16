def main():
    vowel = ['a', 'e', 'i', 'o', 'u']

    tweet = input("Text: ")

    twt = ''

    for i in tweet:
        if i.lower() not in vowel:
            twt += i.lower()

    print (f"Tweet: {twt}")


while True:
    main()