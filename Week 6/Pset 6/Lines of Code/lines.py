import sys

def main():
    file_name = sys.argv[1]
    file = line_check(file_name)
    
    print (len(file))

def line_check(file_name):
    actual_file = []

    with open(file_name, 'r') as file:
        for line in file.readlines():
            #print (line)
            line = line.strip()
            
            if line and not line.startswith('#'):
                actual_file.append(line)
                #print (line)
        
    return(actual_file)


main()