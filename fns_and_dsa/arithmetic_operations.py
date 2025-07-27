num1 = int(input('plese inpute number:'))
num2 = int(input('plese inpute number:'))
operation = input('please write your opratopn add , sud , mult ,div:')
def perform_operation(num1,num2,operation):

  if operation == 'add':
    result = num1 + num2
    return result
  if operation == 'sud':
    result = num1 - num2
    return result
  if operation == 'mult':
    result = num1 * num2
    return result 
  if operation == 'div':
    result = num1 / num2  
    return result
print( perform_operation(num1,num2,operation))
