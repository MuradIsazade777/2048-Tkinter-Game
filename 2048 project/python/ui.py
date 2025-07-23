import tkinter as tk
from config import bg_colors

def create_ui(root):
    frame = tk.Frame(root, bg="#bbada0")
    frame.grid(padx=10, pady=10)

    cells = []
    for i in range(4):
        row = []
        for j in range(4):
            label = tk.Label(frame, text="", width=4, height=2, font=("Helvetica", 32, "bold"), bg=bg_colors[0])
            label.grid(row=i, column=j, padx=5, pady=5)
            row.append(label)
        cells.append(row)

    score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 24, "bold"))
    score_label.grid()
    return cells, score_label

def update_ui(grid, cells, score_label, score):
    for i in range(4):
        for j in range(4):
            val = grid[i][j]
            cells[i][j].configure(text=str(val) if val != 0 else "", bg=bg_colors.get(val, "#3c3a32"))
    score_label.config(text=f"Score: {score[0]}")

def show_message(text, color):
    popup = tk.Toplevel()
    popup.title(text)
    popup.geometry("300x100")
    label = tk.Label(popup, text=text, font=("Helvetica", 24, "bold"), fg="white", bg=color)
    label.pack(expand=True, fill="both")
    btn = tk.Button(popup, text="OK", command=popup.destroy)
    btn.pack()