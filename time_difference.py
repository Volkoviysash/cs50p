import datetime
import re
import sys
import inflect


def main():
    inputdate = input("Enter your date of birth: ")    
    if re.search("[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}", inputdate):        
        print(minutes_counter(inputdate), "minutes")
    else:
        sys.exit("UsageError! use: YYYY-MM-DD format")


def minutes_counter(inputdate):
    birth_day = datetime.datetime.strptime(inputdate, '%Y-%m-%d').date()    
    today = datetime.date.today()       
    delta = today - birth_day    
    return int_to_words(int(delta.total_seconds() / 60))    


def int_to_words(number_of_minutes):
    p = inflect.engine()
    number_in_words = p.number_to_words(number_of_minutes)
    return number_in_words.capitalize()


if __name__ == "__main__":
    main()