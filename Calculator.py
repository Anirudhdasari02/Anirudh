def intelligent_calculator(expression):
    expression = expression.replace(" ", "")  
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '%': lambda x, y: x % y}

    for operator in operators.keys():
        if operator in expression:
            operands = expression.split(operator) 
            try:
                operand1 = float(operands[0])
                operand2 = float(operands[1])
                result = operators[operator](operand1, operand2)
                return str(result)
            except ValueError:
                return "Invalid input: operands must be numbers."
            except ZeroDivisionError:
                return "Invalid input: division by zero."
    
    return "Invalid input: no operator found."
input_expression = input("Enter an expression: ")
result = intelligent_calculator(input_expression)
print("Result: " + result)
