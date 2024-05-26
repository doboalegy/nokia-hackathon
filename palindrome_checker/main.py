import re

with open('./input.txt', 'r') as f:
    input = f.read()

# Kifejezések tárolása listában
expressions = input.split('\n')

for expression in expressions:

    # Üres kifejezéseket kihagyjuk
    if not expression:
        continue

    # Nem alfanumerikus karakterek elhagyása, kisbetüssé alakítás
    expression =  re.sub(r'[^a-zA-Z0-9]', '', expression).lower()

    if expression == expression[::-1]:
        print(f'YES, {len(set(expression))}')
    else:
        print('NO, -1')