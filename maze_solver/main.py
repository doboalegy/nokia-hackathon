from collections import deque
        
class Maze:
    def __init__(self, matrix):
        self.cells = {}
        self.start = None
        self.goal = None

        # Cellák hozzáadása
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                type = matrix[i][j]
                self.cells[i, j] = type
                if type == 'S':
                    self.start = (i, j)
                if type == 'G':
                    self.goal = (i, j)
        
    def find_shortest_path(self):
        # Szomszédos cellák meghatározása
        def get_neighbors(cell):
            neighbours = set()
            for dx, dy, direction in [(-1, 0, ' U'), (1, 0, ' D'), (0, -1, ' L'), (0, 1, ' R')]:
                x, y = cell[0] + dx, cell[1] + dy
                if ( (x, y) in self.cells.keys() ) and ( self.cells[(x, y)] != '#' ):
                    neighbours.add( ((x, y), direction) )
            return neighbours

        # Start és Cél ellenörzése
        if not self.start or not self.goal:
            raise Exception('Maze is missing start or goal')
    
        # Legjobb út megkeresése BFS algoritmussal
        queue = deque([(self.start, "")])
        visited = set()
        visited.add((self.start))
        
        while queue:
            current_cell, path = queue.popleft()
            
            # Ha elértük a célt, visszadjuk az utat
            if current_cell == self.goal:
                return 'S' + path + ' G'
            
            # Szomszédos cellák bejárása
            for neighbour, direction in get_neighbors(current_cell):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, path + direction))
        
        raise Exception('Maze has no solution')

''' INPUT '''
# Az útvesztöket ebben a szótárban tároljuk
mazes = {}

with open('./maze_solver/input.txt', 'r') as f:
    key = ''
    matrix = []

    for line in f:
        row = line.strip().split()

        #Üres sort kihagyjuk
        if not row:
            continue

        if len(row) == 1: # Új útvesztö
            if key:
                mazes[key] = Maze(matrix)
            key = row[0]
            matrix = []
        else: # Jelenlegi útvesztö bövítése
            matrix.append(row)
    
    # Utolsó útvesztö hozzáadása
    mazes[key] = Maze(matrix)

''' MAIN '''
for key, maze in mazes.items():
    print(key)
    print(maze.find_shortest_path())
    print()