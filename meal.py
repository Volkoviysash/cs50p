def main():
    time = input("What's time is it? ")        
    convertedtime = convert(time)
    
    if 7 <= convertedtime <= 8:
        print("breakfast time")
    elif 12 <= convertedtime <= 13:
        print("lunch time")
    elif 18 <= convertedtime <= 19:
        print("dinner time")


def convert(time):
    time = time.split(':')
    hours = float(time[0]) + float(time[1])/60
    return hours

if __name__ == "__main__":
    main()