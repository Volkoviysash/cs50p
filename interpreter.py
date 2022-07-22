expression = input("");

expression = expression.split( )

try:
    firstnumber = float(expression[0])
    sign = expression[1]
    secondnumber = float(expression[2])

    if sign == "+":
        print(firstnumber + secondnumber)
    elif sign == "-":
        print(firstnumber - secondnumber)
    elif sign == "*":
        print(firstnumber * secondnumber)
    elif sign == "/":
        print(firstnumber + secondnumber)
except:
    print("Syntax error!")