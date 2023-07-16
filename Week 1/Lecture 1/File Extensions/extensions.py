def main():
    file_name = input ("File name: ").lower().strip()
    print (file_type(file_name))

def file_type(file_name):
    if file_name.endswith('.gif'):
        return ("image/gif")
    elif file_name.endswith('.jpg'):
        return ("image/jpeg")
    elif file_name.endswith('.jpeg'):
        return ("image/jpeg")
    


while True: 
    main()