import re

with open('./input.txt', 'r') as f:
    input = f.read()

# Storing expressions in a list
expressions = input.split('\n')

for expression in expressions:
    # Removing non alphanumerical characters and making text lowercase
    expression =  re.sub(r'[^a-zA-Z0-9]', '', expression).lower()

    if expression and expression == expression[::-1]:
        print(f'YES, {len(set(expression))}')
    else:
        print('NO, -1')