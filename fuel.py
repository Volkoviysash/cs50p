def main():    
    while True:
        fraction = str(input("Fraction: ")).split('/')        
        x = int(fraction[0])
        y = int(fraction[1])

        try:
            result = (x / y) * 100            
            if result <= 100:
                break
        except(ValueError, ZeroDivisionError):
            pass  
    
    if 99 <= result <= 100:
        print("F")
    elif 0 <= result <= 1:
        print("E")
    else:
        print(str(int(result)) + "%")

if __name__ == "__main__":
    main()