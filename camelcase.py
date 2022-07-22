def main():
    camelcase = input("camelCase: ")
    snakecase = snake_case(camelcase)    
    print(f"snake_case: {snakecase}")    

def snake_case(text):    
    snakeoutput = ""
    for c in text:
        if c.isupper():
            snakeoutput += "_" + c.lower()
        else:
            snakeoutput += c
    return snakeoutput

if __name__ == "__main__":
    main()