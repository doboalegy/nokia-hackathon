from collections import deque

class Maze:
    def __init__(self, cells):
        self.cells = cells
        self.start = None
        self.goal = None

        # Start és cél megkeresése
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] == 'S':
                    self.start = (i, j)
                elif self.cells[i][j] == 'G':
                    self.goal = (i, j)

    def find_best_path(self):
        # Cella szomszédjainak megadása
        def get_neighbors(x, y):
            for dx, dy, direction in [(-1, 0, ' U'), (1, 0, ' D'), (0, -1, ' L'), (0, 1, ' R')]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.cells) and 0 <= ny < len(self.cells[0]) and self.cells[nx][ny] != '#':
                    yield nx, ny, direction

        # Start és cél ellenörzése
        if self.start is None or self.goal is None:
            raise Exception('Start or goal is not set')

        # Legjobb út megkeresése BFS algoritmussal
        queue = deque([(self.start[0], self.start[1], "")])
        explored = set()
        explored.add((self.start[0], self.start[1]))

        while queue:
            x, y, path = queue.popleft()

            # Ha megtaláltuk a célt
            if (x, y) == self.goal:
                return 'S' + path + ' G'
            
            # Szomszédos cellák felfedezése
            for nx, ny, direction in get_neighbors(x, y):
                if (nx, ny) not in explored:
                    explored.add((nx, ny))
                    queue.append((nx, ny, path + direction))

        raise Exception("Maze has no solution")

mazes = {}

with open('./input.txt', 'r') as f:
    key = ''
    matrix = []

    for line in f:
        row = line.strip().split()

        # Üres sorok kihagyás
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
    if key:
        mazes[key] = Maze(matrix)

''' MAIN '''
for key, maze in mazes.items():
    print(key)
    print(maze.find_best_path())
    print()