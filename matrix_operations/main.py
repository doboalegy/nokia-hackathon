import re

def print_matrix(matrix : list):
	for row in matrix:
		print(' '.join(map(str, row)))

def add_matrices(matrix1 : list, matrix2 : list) -> list:
	result = [
		[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))
		]

	return result

def multiply_matrices(matrix1 : list, matrix2 : list):
    result = []

    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError('Matrices cannot be multiplied: Invalid dimensions')
    
    # Iterate through rows of matrix1
    for i in range(len(matrix1)):
        row = []
        # Iterate through columns of matrix2
        for j in range(len(matrix2[0])):
            sum = 0
            # Iterate through rows of matrix2 to perform dot product
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    
    return result


with open('./input.txt') as f:
	matrices = {}
	operations = []

	key = ''
	matrix = []

	''' READING MATRICES '''
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

	# Multiplications 
	multiplications = re.findall(r'\w+\s\*\s\w+', operation)
	while multiplications:

		matrix_name = 'M' + str(i)
		factors = multiplications[0].split(' * ')
		matrices[matrix_name] = multiply_matrices(matrices[factors[0]], matrices[factors[1]])
		
		# Replacing operation with new matrix
		operation = operation.replace(multiplications[0], matrix_name)

		i += 1
		multiplications = re.findall(r'\w+\s\*\s\w+', operation)

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