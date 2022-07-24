def main():
    names = []
    
    while True:
        name = input("Name: ")
        if name == "":
            break
        names.append(name)
    
    text = "Adieu, adieu, to "

    for x in range(len(names)):
        if x == 0:
            text += names[x]
        elif x == len(names) - 1 and len(names) > 2:
            text += ", and " + names[x]
        elif x == len(names) - 1 and len(names) == 2:
            text += " and " + names[x]
        else:
            text += ", " + names[x]
    print(text)

if __name__ == "__main__":
    main()