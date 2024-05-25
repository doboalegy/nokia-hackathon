# Reading input
with open('./input.txt', 'r') as f:
	input = f.read().split('operations')

# Storing matrixes
matrixes = {}

key = ''
matrix = []

for row in input[0].split('\n'):
	row_list = row.strip().split()

	if not row_list:
		continue

	if len(row_list) == 1:
		if key:
			matrixes[key] = matrix
		key = row_list[0]
		matrix = []
	else:
		matrix.append(row_list)

if key:
	matrixes[key] = matrix

# Storing operations
operations = []
for row in input[1].split('\n'):
	if not row:
		continue
	
	operations.append(row)

print(operations)