import emoji

def main():
    text = input("Write your text to be emojized: ")
    output = emoji.emojize(text, language='alias')
    
    print (output)

main()