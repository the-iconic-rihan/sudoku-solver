# representation of input puzzle as a list of list.
puzzle1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
""" the Outer list contains 9 rows as list of list.
every row contains 9 elements one in each column.
blank spaces in the sudoku is represented by ".".
"""

"""The only solution for the sudoku is represented below"""

solution1 = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
             ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
             ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
             ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
             ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
             ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
             ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
             ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
             ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

if str(len(solution1) == 9 and len(puzzle1) == 9):
    print(True)
row3 = solution1[3]
if row3 == ["8", "5", "9", "7", "6", "1", "4", "2", "3"]:
    print(True)
value_4_5 = solution1[4][5]
if value_4_5 == "3":
    print(True)
last_row_value = solution1[-1][0]
if last_row_value == "3":
    print(True)

# print(len(puzzle1[0]))
