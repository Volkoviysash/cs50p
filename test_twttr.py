from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    if shorten("twitter") != "twttr":
        print("Twitter error!")
    if shorten("What's your name?") != "Wht's yr nm?":
        print("'What's your name?' error!")
    if shorten("CS50") != "CS50":
        print("CS50 error!")
    else:
        print("All is good!")

if __name__ == "__main__":
    main()