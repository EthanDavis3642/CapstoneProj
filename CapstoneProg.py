import random

def create_grid():
    rows = 4
    cols = 4
    arr = [[False for i in range(cols)] for j in range(rows)]
    for row in arr: 
        print(row)
    print()
    return arr

def create_piece(grid):
    i = random.randint(0,4)
    if i == 0:
        create_Z(grid)
    elif i == 1:
        create_long(grid)
    elif i == 2:
       create_L(grid)
    elif i == 3:
        create_square(grid)
    else:
        create_T(grid)
    for row in grid: 
       print(row) 
def create_T(grid):
    i = random.randint(0,3)
    if i == 0:
        draw_T_one(grid)
    elif i == 1:
        draw_T_two(grid)
    elif i == 2:
        draw_T_three(grid)
    else:
        draw_T_four(grid)
        
def draw_T_one(grid):
    #  x
    #x c
    #  x
    i = random.randint(1, 2)
    j = random.randint(1, 3)
    a = (i - 1)
    b = (i + 1)
    c = (j - 1)
    grid[i][j] = True
    grid[i][c]= True
    grid[a][j]= True
    grid[b][j]= True

def draw_T_two(grid):
    #x
    #c x
    #x
    i = random.randint(1, 2)
    j = random.randint(0, 2)
    a = (i - 1)
    b = (i + 1)
    c = (j + 1)
    grid[i][j] = True
    grid[i][c]= True
    grid[a][j]= True
    grid[b][j]= True
def draw_T_three(grid):
    #x c x
    #  x
    i = random.randint(0, 2)
    j = random.randint(1, 2)
    a = (i + 1)
    b = (j + 1)
    c = (j - 1)
    grid[i][j] = True
    grid[i][b]= True
    grid[i][c]= True
    grid[a][j]= True

def draw_T_four(grid):
    #  x
    #x c x
    i = random.randint(1, 3)
    j = random.randint(1, 2)
    a = (i - 1)
    b = (j + 1)
    c = (j - 1)
    grid[i][j] = True
    grid[i][b]= True
    grid[i][c]= True
    grid[a][j]= True
     
def create_Z(grid):
    i = random.randint(0,1)
    if i == 0:
        draw_Z_up(grid)
    else:
        draw_Z_side(grid)      
def draw_Z_up(grid):
    #c
    #x x
    #  x
    i = random.randint(0, 1)
    j = random.randint(0, 2)
    a = (i + 1)
    b = (j + 1)
    c = (i + 2)
    grid[i][j] = True
    grid[a][j]= True
    grid[a][b]= True
    grid[c][b]= True

def draw_Z_side(grid):
    #  x x
    #c x
    i = random.randint(1, 3)
    j = random.randint(0, 1)
    a = (i - 1)
    b = (j + 1)
    c = (j + 2)
    grid[i][j] = True
    grid[i][b]= True
    grid[a][b]= True
    grid[a][c]= True


def create_L(grid):
    i = random.randint(0,3)
    if i == 0:
        draw_L_one(grid)
    elif i == 1:
        draw_L_two(grid)
    elif i == 2:
        draw_L_three(grid)
    else:
        draw_L_four(grid)
        
def draw_L_one(grid):
    # c x x
    #     x
    i = random.randint(0, 2)
    j = random.randint(0, 1)
    a = (i + 1)
    b = (j + 1)
    c = (j + 2)
    grid[i][j] = True
    grid[a][c]= True
    grid[i][b]= True
    grid[i][c]= True

def draw_L_two(grid):
    # x
    # c x x
    i = random.randint(1, 3)
    j = random.randint(0, 1)
    a = (i - 1)
    b = (j + 1)
    c = (j + 2)
    grid[i][j] = True
    grid[a][j]= True
    grid[i][b]= True
    grid[i][c]= True
    
def draw_L_three(grid):
    # c x
    # x
    # x
    i = random.randint(0, 1)
    j = random.randint(0, 2)
    a = (j + 1)
    b = (i + 1)
    c = (i + 2)
    grid[i][j] = True
    grid[i][a]= True
    grid[b][j]= True
    grid[c][j]= True

def draw_L_four(grid):
    #   x
    #   x
    # c x
    i = random.randint(2, 3)
    j = random.randint(0, 2)
    a = (j + 1)
    b = (i - 1)
    c = (i - 2)
    grid[i][j] = True
    grid[i][a]= True
    grid[b][a]= True
    grid[c][a]= True
    
def create_long(grid):
    i = random.randint(0,1)
    if i == 0:
        draw_long_up(grid)
    else:
        draw_long_side(grid)
 
def draw_long_up(grid):
        i = random.randint(0, 3)
        grid[0][i] = True
        grid[1][i] = True
        grid[2][i] = True
        grid[3][i] = True

def draw_long_side(grid):
        i = random.randint(0, 3)
        grid[i][0] = True
        grid[i][1] = True
        grid[i][2] = True
        grid[i][3] = True


def create_square(grid):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        #a = (i + 1);
        #b = (j + 1); 
        draw_square(i,j,grid)
        
def draw_square(x, y, grid):
    a = (x + 1)
    b = (y + 1)
    grid[x][y] = True
    grid[a][y]= True
    grid[x][b]= True
    grid[a][b]= True


arr = create_grid()
create_piece(arr)
