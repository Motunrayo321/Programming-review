import sys
from os import path


def main():
    argv_check(['Python', 'py'], 1)

    file_name = sys.argv[1]
    file = line_check(file_name)
    
    print (len(file))


def argv_check(file_type:list, file_no:int, all_file=False, location=1):
    """ file_type should be a list with the file name being the first and the extensions as the other items
    file_no should be the number of expected files
    all_file should be true if all the files should have one of the extensions listed in the list
    location should be given if only all_file is false to know which file(s) to check its extension
    """

    arguments = sys.argv

    # Checking command line file numbers
    
    if len(arguments) < (file_no + 1):
        sys.exit("Too few arguments")

    elif len(arguments) > (file_no + 1):
        sys.exit("Too many arguments")

    # Checking file extension

    ext = file_type[0]

    if len(arguments) == 2:
        file_name, file_path = path.splitext(arguments[1])

        print (file_name, file_path)
        print(f".{file_type[1]}")
        if not file_path in f".{file_type[1]}":
            sys.exit(f"1. Not a {ext.title()} file")

    # If files should be of the same type...

    if all_file:
        for i in arguments[1:]:
            file_name, file_path = path.splitext(i)
            mark, file_path = file_path.split('.')

            if not file_path in file_type[1:]:
                sys.exit(f"2. Not a {ext.title()} file")

    #if files can be different types

    else:
        file_name, file_path = path.splitext(arguments[location])
        mark, file_path = file_path.split('.')
        if not file_path in file_type[1:]:
                sys.exit(f"3. Not a {ext.title()} file")


def line_check(file_name):
    actual_file = []

    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            
            if line and not line.startswith('#'):
                actual_file.append(line)
    
    #print (json.dumps(actual_file, indent=2))
    return(actual_file)


if __name__ == "__main__":
    main()