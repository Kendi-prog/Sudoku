def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that is not filled yet--> rep with -1
    #return row, col tuple(or (None, None) if there is none
    
    #we are using 0-8 of our indices
    for r in range(9):
        for c in range(9):  #from 0, 1, 2, ..., 8
            if puzzle[r][c] == -1:
                return  r, c
    return None, None   #if no spaces in the puzzle are empty(-1)

def is_valid(puzzle, guess, row, col):
    #figures whether the guess at the row/col in the puzzle is a valid guess
    #returns True if valid, False otherwise

    #starting with the rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #columns
    col_vals = [puzzle[i][col] for i in range(9) ]
    if guess in col_vals:
        return False

    #the square; we want to get where the 3*3 square starts
    #and iterate through the three values in the row/col
    row_start = (row // 3) * 3   # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
            
    #if we get here, these checks pass
    return True




def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    #returns whether a solution exists
    #mutates the puzzle(if the solution exists)

    #step 1: chooose somewhere in the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1: If there's nowhere left then we are done because we only allowed valid inputs
    if row is None:
        return True
    
    #step 2: if there is a place to put a number then guess between 1 and 9
    for guess in range(1, 10):
        #step 3:check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1:if this is valid, place that guess in the puzzle
            puzzle[row][col] = guess
            #step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        #step 5: if not valid or our guess does not solve the puzzle , we need to backtrack and try a new number
            puzzle[row][col] = -1  #reset the guess

    #if none of the numbers we choose works then this puzzle is unsolvalble!!
    return False

if __name__ == '__main__':
    board = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]
    print(solve_sudoku(board))
    print(board)