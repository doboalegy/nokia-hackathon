from collections import deque

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

    def bfs(self):
        queue = deque([(self.start, '')])
        visited = set()
        visited.add(self.start)
        
        while queue:
            current, actions = queue.popleft()
            
            if current == self.goal:
                return actions
            
            for direction, (dx, dy) in zip('DURL', [(1, 0), (-1, 0), (0, 1), (0, -1)]):
                neighbour = (current[0] + dx, current[1] + dy)
                
                if neighbour not in self.blocks or neighbour in visited or self.blocks[neighbour] == '#':
                    continue
                
                visited.add(neighbour)
                queue.append((neighbour, actions + direction))
        
        return None

# Reading mazes from file
mazes = {}
with open('./input.txt', 'r') as f:
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
    path = maze.bfs()
    if path:
        print(path)
    else:
        print(path)
        
    print()