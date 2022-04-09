from copy import deepcopy

"""
1. IT has 9 rows
2. 9 columns
3. It has 9 elements in every 3x3 block and has 9 block of 3x3.
4. "." represents the blank 
5. the number 1-9 must only appear once in every row, column and even 3x3 block 
"""

N = 9
# sudoku puzzle
field = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

"""converting the '.' into 0 and string numbers into integer type value"""


def convert_field(field):
    return [[0 if y == "." else int(y) for y in x] for x in field]


"""this function will check for null pointer exception and reconvert it to string"""


def return_field(field):
    if not field:
        return []

    return [[str(y) for y in x] for x in field]


"""
this function will copy the puzzle in state variable and will iterate over it 
if any cell == 0 it will assign the number from 1-10 at that cell
and return the state
"""


def read(field):

    state = deepcopy(field)
    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if cell == 0:
                state[i][j] = set(range(1, 10))

    return state


"""
I have use "set" to tell if we have got a unique row and column
"""


def done(state):
    for row in state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def propagate_step(state):
    new_units = False
    """propagating through the copy puzzle by each row"""
    for i in range(N):
        row = state[i]
        values = set([x for x in row if not isinstance(x, set)])
        for j in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    val = state[i][j].pop()
                    state[i][j] = val
                    values.add(val)
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for j in range(N):
        column = [state[x][j] for x in range(N)]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    val = state[i][j].pop()
                    state[i][j] = val
                    values.add(val)
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None
        """propagating through the copy puzzle by each 3x3 block and remove duplicates using list comprehension"""

    for x in range(3):
        for y in range(3):
            """converting the block to string"""
            values = set()
            """checking duplicated over row"""
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            """checking duplicated over column"""
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    if isinstance(state[i][j], set):
                        state[i][j] -= values
                        if len(state[i][j]) == 1:
                            val = state[i][j].pop()
                            state[i][j] = val
                            values.add(val)
                            new_units = True
                        elif len(state[i][j]) == 0:
                            return False, None

    return True, new_units


"""
The below check the puzzle is solvable or not.
Steps through subsequent states returned by propagate_step until it reaches final states of either solvable or recurring 
    unit"
"""


def propagate(state):
    while True:
        solvable, new_unit = propagate_step(state)
        if not solvable:
            return False
        if not new_unit:
            return True


"""
the below function will solve the puzzle by giving a call to propogate function.
"""


def solve(state):
    solvable = propagate(state)

    if not solvable:
        return None
    """
    the puzzle is solve it return state with new values without mutating the original sudoku
    """
    if done(state):
        return state
    """ Solving the puzzle by making the recursive calls for checking at every blank cell. """
    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_state = deepcopy(state)
                    new_state[i][j] = value
                    solved = solve(new_state)
                    if solved is not None:
                        return solved
                return None


"""
This function makes a call to 
1.Convert_field(field) -->converting string to integer
2.Read(convert_field(field)) --> reading the str puzzle and copying it to new list of list
3.Solve(read(convert_field(field)))--> this will solve the puzzle with help of recursive functions of propogating_step
    ()function
4.Return_field(solve(read(convert_field(field))))--> this will return the solved puzzled as a string
 """
print(return_field(solve(read(convert_field(field)))))
