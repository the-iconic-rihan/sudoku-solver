# representation of input puzzle as a list of list.
# puzzle = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#           [".", "9", "8", ".", ".", ".", ".", "6", "."],
#           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#           [".", "6", ".", ".", ".", ".", "2", "8", "."],
#           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def is_valid_move(puzzle, row, col, num):
    for x in range(9):
        if puzzle[row][x] == num:
            return False
    for x in range(9):
        if puzzle[x][col] == num:
            return False

    corner_row = row - (row % 3)
    corner_col = col - (col % 3)
    for x in range(3):
        for y in range(3):
            if puzzle[corner_row + x][corner_col + y] == num:
                return False
    return True


def solve(puzzle, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if puzzle[row][col] > 0:
        return solve(puzzle, row, col + 1)
    for num in range(1, 10):
        if is_valid_move(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve(puzzle, row, col + 1):
                return True
        puzzle[row][col] = 0
    return False


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

""" the Outer list contains 9 rows as list of list.
every row contains 9 elements one in each column.
blank spaces in the sudoku is represented by ".".
"""
if solve(puzzle, 0, 0):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=" ")
        print()
else:
    print("No Solution for this Sudoku")
