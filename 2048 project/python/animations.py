def highlight_cell(cells, i, j):
    cell = cells[i][j]
    original_color = cell.cget("bg")
    cell.configure(bg="#ffff99")  
    cell.after(150, lambda: cell.configure(bg=original_color))