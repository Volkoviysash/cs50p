import sys

def main():
    #check if argv[1] exists and is the only one
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    #check if argv[1] is Python file
    if not sys.argv[1].endswith('.py'):
        print("Not a Python file")
        sys.exit(1)
        
    #try to open file to read
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()        
    #if file doesn't exist print Error
    except IOError:
        print("File doesn't exist")
        sys.exit(1)
        
    #print counter
    print(counter(lines))    
    
    #close file
    file.close()

def counter(lines):
    #create counter
    counter = 0

    #count lines
    for line in lines:
        #only if they are not comments or whitespaces
        if line[0] != '#' and not line[0].isspace():
            counter += 1
    return counter

if __name__ == "__main__":
    main()