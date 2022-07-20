inpt = input("Say hello: ")

if inpt.lower().find("hello") >= 0:
    print("$0")
elif inpt.lower().find('h') == 0:
    print("$20")
else:
    print("$100")