import re

# with open('./input.txt', 'r') as f:
with open('./input.txt', 'r', encoding='utf-8') as f:
    input = f.read()

# Storing expressions in a list
expressions = input.split('\n')

for expression in expressions:
    #Removing non numerical characters
    expression =  re.sub(r'\W+', '', expression)

    #Uppercasing expression
    expression = expression.upper()

    if expression == expression[::-1]:
        print(f'YES, {len(set(expression))}')
    else:
        print('NO, -1')