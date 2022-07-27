import sys
import csv
from tabulate import tabulate

def main():
    #check if argv[1] exists and is the only one
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    #check if argv[1] is CSV file
    if not sys.argv[1].endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)
    table = []
    try:    
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)                         
    #if file doesn't exist print Error
    except IOError:
        print("File doesn't exist")
        sys.exit(1)    

    print(tabulate(table[1:], headers=table[0] , tablefmt="grid"))

if __name__ == "__main__":
    main()
