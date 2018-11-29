def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    for i in range(4):
        for j in range(4):
            print('%5d' % (grid[i][j]), end='')
        print()

def check_lost (grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[0][0] == grid[0][1] or grid[0][0] == grid[1][0]:
                return False
            elif grid[0][3] == grid[0][2] or grid[0][3] == grid[1][3]:
                return False
            elif grid[3][0] == grid[3][1] or grid[3][0] == grid[2][0]:
                return False
            elif grid[3][3] == grid[3][2] or grid[3][3] == grid[2][3]:
                return False
            if j == 0:
                if grid[i][j] == grid[i][j + 1]:
                    return False
            elif j == 3:
                if grid[i][j] == grid[i][j - 1]:
                    return False
            if i == 0:
                if grid[i][j] == grid[i + 1][j]:
                    return False
            elif i == 3:
                if grid[i][j] == grid[i - 1][j]:
                    return False
            elif (i == 1 or i == 2) and (j == 1 or j == 2):
                if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i - 1][j] or grid[i][j] == grid[i][j + 1] or grid[i][j] == grid[i][j - 1]:
                    return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the given grid"""
    another_grid = []
    for i in grid:
        another_grid.append(i)
    return another_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True