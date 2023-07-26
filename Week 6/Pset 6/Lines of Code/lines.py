import sys

def main():
    file_name = sys.argv[1]
    file = line_check(file_name)
    
    print (len(file))

def line_check(file_name):
    actual_file = []

    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            
            if line and not line.startswith('#'):
                actual_file.append(line)
        
    return(actual_file)


main()