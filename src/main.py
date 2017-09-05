import numpy as np
import itertools

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
                    score = score + 1

    print(matches)
    print(score)
    return score


def get_element_numbers(grid):
    numbers = [0,0,0,0,0,0]
    for x in range(0, 5):
        for y in range(0, 6):
            element = grid[x][y]
            numbers[element] = numbers[element] + 1

    return numbers

def find_score_in_simple_way(grid):
    numbers = [n / 3 for n in get_element_numbers(grid)]
    return sum(numbers)


def all_grid_combinations(grid):
    return set(itertools.permutations(grid.ravel(), 30))

#testing use

grid2 = np.array([[0, 0, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]
         ])

print (grid2)
find_score(grid2)
print get_element_numbers(grid2)
print (find_score_in_simple_way(grid2))


grid = np.random.randint(6, size=(5, 6))

print(grid)
find_score(grid)
print get_element_numbers(grid)
print (find_score_in_simple_way(grid))

print (all_grid_combinations(grid2))

