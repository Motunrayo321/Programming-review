def main():
    tweet = input("Text: ")
    twt = shorten(tweet)

    print (f"Tweet: {twt}")


def shorten(word):
    vowel = ['a', 'e', 'i', 'o', 'u']

    twt = ''

    for i in word:
        if i.lower() not in vowel:
            twt += i.lower()

    return twt
    


if __name__ == "__main__":
    main()