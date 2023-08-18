from tkinter import *
from solver import solver

root = Tk()
root.title("Sudoku Solver")
root.geometry("330x550")

label = Label(root, text="Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

error_Label = Label(root, text="", fg="red")
error_Label.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

def Validate_Number(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out


reg = root.register(Validate_Number)


def draw3x3Grid(row, column, bg_color):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bg_color, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + 1 + j, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row + 1 + i, column + j + 1)] = e


first_color = "#ddedcc"

def draw9x9Grid():
    color = first_color
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == first_color:
                color = "#afde81"
            else:
                color = first_color


def Clear_Values():
    error_Label.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


def Get_Values():
    board = []
    error_Label.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    updateValues(board)


button = Button(root, command=Get_Values, text="Solve", width=10)
button.grid(row=20, column=1, columnspan=5, pady=20)

button = Button(root, command=Clear_Values, text="CLear", width=10)
button.grid(row=20, column=5, columnspan=5, pady=20)


def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows - 2][col - 1])
        solvedLabel.configure(text="Sudoku solved!")
    else:
        error_Label.configure(text="No solution exists for this sudoku")


draw9x9Grid()

root.mainloop()
