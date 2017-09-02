import numpy as np

grid = np.random.randint(6, size=(5, 6))

print(grid)

def find_score(grid):
    matches = []
    for x in range(0, 5):
        for y in range(0, 6):
            e1 = grid[x][y]
            if x < 3:
                e2 = grid[x + 1][y]
                e3 = grid[x + 2][y]
                if e1 == e2 and e1 == e3:
                    matches.append((x, y, x + 2, y))

            if y < 4:
                e2 = grid[x][y + 1]
                e3 = grid[x][y + 2]
                if e1 == e2 and e1 == e3:
                    matches.append((x, y, x, y + 2))

    
    print(matches)


find_score(grid)
