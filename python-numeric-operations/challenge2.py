print('Simple calculator!')

print('First number?')
first_number = input()

print('Operation?')
operation = input()

print('Second number?')
second_number = input()

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

operation_string = ''
value = 0

if operation == '+':
    operation_string = 'sum'
    value = first_number + second_number
elif operation == '-':
    operation_string = 'difference'
    value = first_number - second_number
elif operation == '*':
    operation_string = 'product'
    value = first_number * second_number
elif operation == '**':
    operation_string = 'product'
    value = first_number ** second_number
elif operation == '%':
    operation_string = 'modulas'
    value = first_number % second_number
else:
    print('Operation not recognized.')
    exit()

print(operation_string + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(value))