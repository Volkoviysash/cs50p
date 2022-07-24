import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()    

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":                     
        if sys.argv[2] in figlet.getFonts():
            font = sys.argv[2]    
        else:
            print("Invalid usage!")
            sys.exit(1)            
    elif len(sys.argv) == 1:
        font = figlet.getFonts()[random.randint(0,419)]        
    else:
        print("Invalid usage!")
        sys.exit(1)            

    text = input("Text: ")

    figlet.setFont(font=font) 
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()