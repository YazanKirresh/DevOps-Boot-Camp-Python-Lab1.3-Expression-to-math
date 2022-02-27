from posixpath import split

def calcualte_expression(expression):
    position = 0
    value = 0    
    expression_list = expression.split(" ")
    print(expression_list)

    if expression_list[0] == " ":
        position = position + 1   

    first_number = int(expression_list[position])
    position  = position + 1
    operatrion = expression_list[position]
    position  = position + 1
    second_number = int(expression_list[position])
    position  = position + 1

    if operatrion == "+":
        value = first_number + second_number
    elif operatrion == "-":
        value = first_number - second_number
    elif operatrion == "X" or operatrion == "x" or operatrion == "*":
        value = first_number * second_number
    elif operatrion == "/":
        value = first_number / second_number
    else:
        print("Error, The format should be 'a + b' ")

    return value

expression = input("Enter an Expression: ")
result = calcualte_expression(expression)
print("The result of the equation = " + str(result))