import re

def print_matrix(matrix : list):
	for row in matrix:
		print(' '.join(map(str, row)))

def add_matrices(matrix1 : list, matrix2 : list) -> list:
	matrix = []
	for i in range(len(matrix1)):
		matrix.append([])
		for j in range(len(matrix1[0])):
			matrix[i].append([])
			matrix[i][j] = matrix1[i][j] + matrix2[i][j]
	return matrix


with open('./input.txt') as f:
	matrices = {}
	operations = []

	key = ''
	matrix = []

	''' READING MATRIXES '''
	line = f.readline()
	while line:
		# Stripping line
		line = line.strip()
		
		if len(line) == 0: # empty line
			pass
		elif len(line) == 1: # new matrix
			if matrix:
				matrices[key] = matrix
				matrix = []
			key = line
		elif line == 'operations': # starting operations
			matrices[key] = matrix
			break
		elif all(c.isdigit() or c.isspace() for c in line): # If line contains digits and spaces
			matrix.append(list(map(int, line.split())))

		# Reading next line
		line = f.readline()
	
	''' READING OPERATIONS '''
	line = f.readline()
	while line:
		# Stripping line
		line = line.strip()

		# Adding line to operations
		if len(line) > 0:
			operations.append(line)

		# Reading next line
		line = f.readline()

''' MAIN '''
i = 0 # used to name new matrices

for operation in operations:
	# Printing operation
	print(operation)

	# Additions
	additions = re.findall(r'\w+\s\+\s\w+', operation)
	while additions:

		matrix_name = 'M' + str(i)
		addends = additions[0].split(' + ')
		matrices[matrix_name] = add_matrices(matrices[addends[0]], matrices[addends[1]])
		
		# Replacing operation with new matrix
		operation = operation.replace(additions[0], matrix_name)

		i += 1
		additions = re.findall(r'\w+\s\+\s\w+', operation)
	
	print_matrix(matrices['M' + str(i-1)])

	# Empty line
	print()