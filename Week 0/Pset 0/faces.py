# If you keep doing that, your face will stay that way forever!

def main():
    emoticon = input("Okay boomer, state your cause! ")

    print (revolution(emoticon))

def revolution(emoticon):
    emoji1 = emoticon.replace(":)", "🙂")
    emoji2 = emoji1.replace(":(", "🙁")

    return emoji2

main()