def print_grid(grid):
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=" ")
        print()


def find_empty_cell(grid: list[list], empty_cell: list):


    for row in range(9):
        for col in range(9):
            if(grid[row][col] == 0):
                empty_cell[0] = row
                empty_cell[1] = col
                return True
   
    return False


def is_checK_row_safe(grid, row, number):
    for col in range(9):
        if(grid[row][col] == number):
            return False
    return True


def is_checK_col_safe(grid, col, number):
    for row in range(9):
        if(grid[row][col] == number):
            return False
    return True


def is_checK_box_safe(grid, row, col, number):
    for i in range(3):
        for j in range(3):
            if(grid[row + i][col +j] == number):
                return False
    return True


def check_safe_of_number(grid, row, col, number):


    return is_checK_row_safe(grid, row, number) and is_checK_col_safe(grid, col, number) and is_checK_box_safe(grid, row - row%3, col - col %3, number)




def suduko_solver(grid):


    empty_cell = [0, 0]


    if(not find_empty_cell(grid, empty_cell)):
        return True
   
    row = empty_cell[0]
    col = empty_cell[1]


    for number in range(1,10):


        if(check_safe_of_number(grid, row, col, number)):


            grid[row][col] = number


            if(suduko_solver(grid)):
                return True
           
            grid[row][col] = 0
   
    return False


grid = [[0] * 9] * 9


grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
print_grid(grid)


print("Solution:")
if(suduko_solver(grid)):
    print_grid(grid)
else:
    print("No Solution")
