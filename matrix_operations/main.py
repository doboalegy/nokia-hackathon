import re

''' Mátrix kiírása'''
def print_matrix(matrix : list):
	for row in matrix:
		print(' '.join(map(str, row)))

''' Két mátrix összeadása'''
def add_matrices(matrix1 : list, matrix2 : list) -> list:
	result = [
		[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))
		]

	return result

''' Két mátrix összeszorzása'''
def multiply_matrices(matrix1 : list, matrix2 : list) -> list:
    result = []

    # Mátrix szorzás szabályának ellenörzése
    if len(matrix1[0]) != len(matrix2):
        raise ValueError('Matrices cannot be multiplied')
    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    
    return result

'''INPUT'''
with open('./input.txt') as f:
	
	# Ezekben a változókban tároljuk a mátrixokat és a müveleteket
	matrices = {}
	operations = []

	''' Mátrixok beolvasása '''
	key = ''
	matrix = []

	line = f.readline()
	while line:
		# Sor strippelése
		line = line.strip()
		
		if len(line) == 0: # Üres sor
			pass
		elif len(line) == 1: # Új mátrix
			if matrix:
				matrices[key] = matrix
				matrix = []
			key = line
		elif all(c.isdigit() or c.isspace() for c in line): # Ha a sor számokat és szóközeket tartalmaz
			matrix.append(list(map(int, line.split())))
		elif line == 'operations': # Müveletek kezdete
			matrices[key] = matrix
			break

		# Következö sor
		line = f.readline()
	
	''' Müveletek beolvasása '''
	line = f.readline()
	while line:
		# Sor strippelése
		line = line.strip()

		# Hozzáadás a müveletekhez
		if len(line) > 0:
			operations.append(line)

		# Következö sor
		line = f.readline()

''' MAIN '''
i = 0 # új mátrixok nevéhez használjuk

for operation in operations:
	# Müvelet kiírása
	print(operation)

	# Szorzások 
	multiplications = re.findall(r'\w+\s\*\s\w+', operation)
	while multiplications:

		matrix_name = 'M' + str(i)
		factors = multiplications[0].split(' * ')
		matrices[matrix_name] = multiply_matrices(matrices[factors[0]], matrices[factors[1]])
		
		# Szorzás cseréje az új mátrixra
		operation = operation.replace(multiplications[0], matrix_name)

		i += 1
		multiplications = re.findall(r'\w+\s\*\s\w+', operation)

	# Összeadások
	additions = re.findall(r'\w+\s\+\s\w+', operation)
	while additions:

		matrix_name = 'M' + str(i)
		addends = additions[0].split(' + ')
		matrices[matrix_name] = add_matrices(matrices[addends[0]], matrices[addends[1]])
		
		# Összeadás cseréje az új mátrixra
		operation = operation.replace(additions[0], matrix_name)

		i += 1
		additions = re.findall(r'\w+\s\+\s\w+', operation)
	
	# Végleges mátrix kiírása
	print_matrix(matrices['M' + str(i-1)])

	# Üres sor
	print()