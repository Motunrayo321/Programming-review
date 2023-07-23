def main():
    my_list = {}

    try:
        while True:

            item = input("What's in your grocery list? ")

            if item in my_list:
                my_list[item] += 1
            
            else:
                my_list[item] = 1
        
    except (EOFError, KeyboardInterrupt):
        print ("List complete!")

    finally:
        #print (my_list)

        for thing in sorted(my_list.keys()):
            print (f"{my_list[thing]} {thing.upper()}")


    
main()