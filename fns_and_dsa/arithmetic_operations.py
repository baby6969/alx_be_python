num1 = int(input('plese inpute number:'))
num2 = int(input('plese inpute number:'))
operation = input('please write your opratopn add , subtract , multiply ,divide:')
def perform_operation(num1, num2, operation):

  if operation == 'add':
    result = num1 + num2
    return result
  if operation == 'subtract':
    result = num1 - num2
    return result
  if operation == 'multiply':
    result = num1 * num2
    return result 
   elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
print( perform_operation(num1,num2,operation))
