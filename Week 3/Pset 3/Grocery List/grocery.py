def main():
    my_list = {}

    item = input("What's in your grocery list? ")

    if item in my_list:
        my_list[item] += 1
    
    else:
        my_list[item] = 1

    

main()