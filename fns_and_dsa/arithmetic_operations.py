num1 = int(input('plese inpute number:'))
num2 = int(input('plese inpute number:'))
operation = input('please write your opratopn add , sud , mult ,div:')
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
  if operation == 'divide':
    result = num1 / num2  
    return result
  if num2 == 0:
    return 'can not be done'
print( perform_operation(num1,num2,operation))
