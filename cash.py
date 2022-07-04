from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break
    print("Enter nonnegtiv number!")

cents = dollars*100
counter = 0

while cents >= 25:
    cents -= 25
    counter +=1

while cents >= 10:
    cents -= 10
    counter +=1

while cents >= 5:
    cents -= 5
    counter +=1

while cents >= 1:
    cents -= 1
    counter +=1

print(counter)