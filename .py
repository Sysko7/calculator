print("basic calculator")

num1 = float(input('ENTER YOUR FIRST NUMBER:'))
operator= input("ENTER OPERATOR :+,-,*,**,//,/: ")
num2 = float(input("ENTER YOUR SECOND NUMBER:"))

if operator == "+":
    print("the answer is:", num1+num2)
elif operator == "-":
    print("the answer is :", num1-num2)
elif operator == "*":
    print("the answer is:", num1 * num2)
elif operator == "**":
    print("the answer is:" ,num1 ** num2)
elif operator == "//":
    print("the answer is:" ,num1 // num2)
elif operator == "/":
    print("the answer is:" ,num1 / num2)
else:
    print("Invalid operator")




