'''
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
'''

from collections import deque

def find_shortest_path(maze):
    # Segédfüggvény a szomszédos cellák meghatározására
    def get_neighbors(x, y):
        for dx, dy, direction in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
                yield nx, ny, direction
    
    # Keresd meg a start és cél koordinátáit
    start = goal = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    
    if not start or not goal:
        return "Start or goal not found in the maze."
    
    # BFS kezdeményezése
    queue = deque([(start[0], start[1], "")])
    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, path = queue.popleft()
        
        # Ha elérte a célt, visszatérítjük az utat
        if (x, y) == goal:
            return 'S' + path + 'G'
        
        # Szomszédos cellák bejárása
        for nx, ny, direction in get_neighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + direction))
    
    return "No path found from start to goal."

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
                mazes[key] = matrix
            key = row_list[0]
            matrix = []
        else:
            matrix.append(row_list)
    
    if key:
        mazes[key] = matrix

for key, maze in mazes.items():
    print(key)
    print(find_shortest_path(maze))