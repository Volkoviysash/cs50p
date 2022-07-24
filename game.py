import random

def main():
    n = int(input("Level = "))
    myint = random.randint(0, n)
    
    while True:
        guess = int(input("Guess: "))
        if guess > myint:
            print("Too large!")
        if guess < myint:
            print("Too small!")
        if guess == myint:
            print("Just right!")
            break
        
if __name__ == "__main__":
    main()