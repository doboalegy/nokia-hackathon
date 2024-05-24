import re

with open('./input.txt', 'r') as f:
    input = f.read()

# Storing expressions in a list
expressions = input.split('\n')

for expression in expressions:
    # Removing non alphanumerical characters
    expression =  re.sub(r'\W+', '', expression)

    # Getting the number of alphanumerical characters
    num = len(set(expression))

    # Uppercasing expression
    expression = expression.upper()

    if expression and expression == expression[::-1]:
        print(f'YES, {num}')
    else:
        print('NO, -1')