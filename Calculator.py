# calculator  with python 

# entering the first number 
num1 = float(input("please enter the first number:"))

# opération 
operation = input("please enter: + ;or; -;or; × or/ ")

# entering the second number 
num2 = float(input("please enter the second number: "))

# do as what he choice 
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "error"
else:
    result = "operation fault"

# نعرض النتيجة
print("result is:", result)
