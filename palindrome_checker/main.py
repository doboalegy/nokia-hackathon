import re

# with open('./input.txt', 'r') as f:
with open('./input.txt', 'r') as f:
    input = f.read()

# Storing expressions in a list
expressions = input.split('\n')

for expression in expressions:
    # Removing non alphanumerical characters
    expression =  re.sub(r'\W+', '', expression)

    # Uppercasing expression
    expression = expression.upper()

    if (len(expression) != 0) and (expression == expression[::-1]):
        print(f'YES, {len(set(expression))}')
    else:
        print('NO, -1')