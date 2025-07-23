import random
from sounds import play_move, play_merge, play_win, play_game_over
from animations import highlight_cell

def init_grid():
    return [[0]*4 for _ in range(4)]

def add_new_block(grid, cells=None):
    empty = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        grid[i][j] = random.choice([2]*9 + [4])
        if cells:
            highlight_cell(cells, i, j)

def stack(grid):
    for i in range(4):
        new_row = [num for num in grid[i] if num != 0]
        new_row += [0] * (4 - len(new_row))
        grid[i] = new_row

def combine(grid, score, cells):
    for i in range(4):
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
                score[0] += grid[i][j]
                play_merge()
                highlight_cell(cells, i, j)
    return score

def reverse(grid):
    for i in range(4):
        grid[i].reverse()

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def moves_exist(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return True
    for j in range(4):
        for i in range(3):
            if grid[i][j] == grid[i+1][j]:
                return True
    return False