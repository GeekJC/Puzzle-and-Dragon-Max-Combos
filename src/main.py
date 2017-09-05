import numpy as np

grid = np.random.randint(6, size=(5, 6))

print(grid)


def create_empty_grid():
    return np.full((5, 6), -1)


def find_score(grid):
    matches = []
    for x in range(0, 5):
        for y in range(0, 6):
            e1 = grid[x][y]
            # vertical (orientation = 0)
            if x < 3:
                e2 = grid[x + 1][y]
                e3 = grid[x + 2][y]
                if e1 == e2 and e1 == e3:
                    matches.append((e1, x, y, 0))
            # horizontal (orientation = 1)
            if y < 4:
                e2 = grid[x][y + 1]
                e3 = grid[x][y + 2]
                if e1 == e2 and e1 == e3:
                    matches.append((e1, x, y, 1))

    match_grid = create_empty_grid()
    score = 0
    for (e_type, x, y, orientation) in matches:
        for i in range(0, 3):
            is_in_match = False
            if orientation == 0:
                e1 = match_grid[x][y]
                e2 = match_grid[x + 1][y]
                e3 = match_grid[x + 2][y]
                if e1 == -1:
                    match_grid[x][y] = e_type
                else:
                    is_in_match = True
                if e2 == -1:
                    match_grid[x + 1][y] = e_type
                else:
                    is_in_match = True
                if e3 == -1:
                    match_grid[x + 2][y] = e_type
                else:
                    is_in_match = True

                if not is_in_match:
                    print (x, y)
                    score = score + 1
            else:
                e1 = match_grid[x][y]
                e2 = match_grid[x][y + 1]
                e3 = match_grid[x][y + 2]
                if e1 == -1:
                    match_grid[x][y] = e_type
                else:
                    is_in_match = True
                if e2 == -1:
                    match_grid[x][y + 1] = e_type
                else:
                    is_in_match = True
                if e3 == -1:
                    match_grid[x][y + 2] = e_type
                else:
                    is_in_match = True

                if not is_in_match:
                    print (x, y)
                    score = score + 1

    print(matches)
    print(score)


grid2 = [[0, 0, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]
         ]
print (grid2)
find_score(grid2)

find_score(grid)
