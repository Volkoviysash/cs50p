#sort digits in some number
def main ():
    num = 42145
    arr = [int(x) for x in str(num)]

    stringoutp = ''.join(str(e) for e in sorted(arr, reverse = True))
    print(int(stringoutp))

if __name__ == "__main__":
    main()