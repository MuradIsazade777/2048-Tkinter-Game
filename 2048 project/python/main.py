import tkinter as tk
from game_logic import *
from ui import create_ui, update_ui, show_message
from animations import highlight_cell
from sounds import play_move, play_game_over, play_win

root = tk.Tk()
root.title("2048 Game")
grid = init_grid()
score = [0]
game_over_flag = [False]
cells, score_label = create_ui(root)
def start_game():
    add_new_block(grid)
    add_new_block(grid)
    update_ui(grid, cells, score_label, score)

def move_left(event=None):
    if game_over_flag[0]: return
    old = [row[:] for row in grid]
    stack(grid)
    combine(grid, score, cells) 
    stack(grid)
    if old != grid:
        play_move()
        add_new_block(grid, cells)  
        update_ui(grid, cells, score_label, score)
        check_game_state()



def move_right(event=None):
    if game_over_flag[0]: return
    old = [row[:] for row in grid]
    reverse(grid)
    stack(grid)
    combine(grid, score, cells)   
    stack(grid)
    reverse(grid)
    if old != grid:
        play_move()
        add_new_block(grid, cells)  
        update_ui(grid, cells, score_label, score)
        check_game_state()

def move_up(event=None):
    if game_over_flag[0]: return
    old = [row[:] for row in grid]
    grid[:] = transpose(grid)
    stack(grid)
    combine(grid, score, cells)   
    stack(grid)
    grid[:] = transpose(grid)
    if old != grid:
        play_move()
        add_new_block(grid, cells)  
        update_ui(grid, cells, score_label, score)
        check_game_state()

def move_down(event=None):
    if game_over_flag[0]: return
    old = [row[:] for row in grid]
    grid[:] = transpose(grid)
    reverse(grid)
    stack(grid)
    combine(grid, score, cells)   
    stack(grid)
    reverse(grid)
    grid[:] = transpose(grid)
    if old != grid:
        play_move()
        add_new_block(grid, cells) 
        update_ui(grid, cells, score_label, score)
        check_game_state()

def check_game_state():
    if any(2048 in row for row in grid):
        game_over_flag[0] = True
        play_win()
        show_message("You Win!", "#ffcc00")
    elif not any(0 in row for row in grid) and not moves_exist(grid):
        game_over_flag[0] = True
        play_game_over()
        show_message("Game Over!", "#ff0000")

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

start_game()
root.mainloop()