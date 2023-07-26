import sys
import json


def main():
    argv_check('py', 1)

    file_name = sys.argv[1]
    file = line_check(file_name)
    
    print (len(file))


def argv_check(ext, file_no, all_file=False, location=1):

    arguments = sys.argv

    if len(arguments) < (file_no + 1):
        sys.exit("Too few arguments")

    elif len(arguments) > (file_no + 1):
        sys.exit("Too many arguments")

    if all_file:
        for i in arguments[1:]:
            if not arguments[i].endswith(f".{ext}"):
                sys.exit(f"Not a {ext} file")
    
    elif len(arguments) == 2:
        if not arguments[1].endswith(f".{ext}"):
                sys.exit(f"Not a {ext} file")

    else:
        if not arguments[location].endswith(f".{ext}"):
                sys.exit(f"Not a {ext} file")


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