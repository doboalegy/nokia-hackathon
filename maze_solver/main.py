class Maze:
    def __init__(self, matrix):
        self.blocks = {}
        self.start = None
        self.goal = None
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.blocks[(i, j)] = matrix[i][j]
                if matrix[i][j] == 'S':
                    self.start = (i, j)
                elif matrix[i][j] == 'G':
                    self.goal = (i, j)

    def explore(self, parent, block, actions, visited):
        if block in visited:
            return None
        if block not in self.blocks or self.blocks[block] == '#':
            return None
        if self.blocks[block] == 'G':
            return actions

        visited.add(block)

        neighbours = [
            ((block[0] + 1, block[1]), 'D'),
            ((block[0] - 1, block[1]), 'U'),
            ((block[0], block[1] + 1), 'R'),
            ((block[0], block[1] - 1), 'L')
        ]

        best_actions = None
        for neighbour, action in neighbours:
            if neighbour == parent:
                continue
            neighbour_actions = self.explore(block, neighbour, actions + action, visited.copy())
            if neighbour_actions and (best_actions is None or len(neighbour_actions) < len(best_actions)):
                best_actions = neighbour_actions

        return best_actions

# Reading mazes from file
mazes = {}
with open('./maze_solver/input.txt', 'r') as f:
    key = ''
    matrix = []

    for row in f:
        row_list = row.strip().split()

        if not row_list:
            continue

        if len(row_list) == 1:
            if key:
                mazes[key] = Maze(matrix)
            key = row_list[0]
            matrix = []
        else:
            matrix.append(row_list)
    
    if key:
        mazes[key] = Maze(matrix)

for key, maze in mazes.items():
    print(key)
    path = maze.explore(None, maze.start, 'S', set())
    if path:
        print(path + 'G')
    else:
        raise Exception('No path found')
    print()