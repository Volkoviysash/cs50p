input_ = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
answers = ["42", "fourty two", "fourty_two", "fourty-two"]

if input_ in answers:
    print("Yes")
else:
    print("No")
