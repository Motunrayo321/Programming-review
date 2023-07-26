import sys
import json

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    file_name = sys.argv[1]

    if not file_name.endswith('.py'):
        sys.exit("Not a Python file")

    file = line_check(file_name)
    
    print (len(file))

def line_check(file_name):
    actual_file = []

    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            
            if line and not line.startswith('#'):
                actual_file.append(line)
    
    print (json.dumps(actual_file, indent=2))
    return(actual_file)

main()