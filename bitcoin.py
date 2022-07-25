import sys
import requests

def main():
    #check if argv[1] exist
    if len(sys.argv) < 2:
        print("Missing command-line argument")    
        sys.exit(1)

    #check if argv is number 
    try:
        number = float(sys.argv[1])
        print(f"Number = {number}")
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        #making responce of current exchange rate
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()                

        #dollar amount calculation
        amount = o["bpi"]['USD']['rate_float'] * number
        
        #printing result
        print(f"${amount:,.4f}")       
    except requests.RequestException:
        print("Responce error!")
        sys.exit(1)

if __name__ == "__main__":
    main()