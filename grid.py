import random
import unittest

class Grid():
    Z = 0
    LONG = 1
    L = 2
    SQUARE = 3
    T = 4


    def __init__(self, seed=None):
        rows = 4
        cols = 4
        self.grid = [[False for i in range(cols)] for j in range(rows)]
        self.clear()
        self.reset()
        random.seed(seed)


    def __str__(self):
        ret = ""
        for row in self.grid:
            for cell in row:
                ret += " "
                if cell:
                    ret += "O"
                else:
                    ret += "-"
            ret += "\n"
        return ret


    def clear(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = False


    def reset(self):
        self.available_pieces = [
            (self.Z, self.__create_Z),
            (self.LONG, self.__create_long),
            (self.L, self.__create_L),
            (self.SQUARE, self.__create_square),
            (self.T, self.__create_T)
        ]


    def next_piece(self):
        self.clear()
        if len(self.available_pieces) == 0:
            self.reset()
        i = random.randrange(len(self.available_pieces))
        piece, func = self.available_pieces[i]
        func()
        self.available_pieces.pop(i)
        return piece, self.grid


    def __create_T(self):
        i = random.randint(0,3)
        if i == 0:
            self.__draw_T_one()
        elif i == 1:
            self.__draw_T_two()
        elif i == 2:
            self.__draw_T_three()
        else:
            self.__draw_T_four()


    def __draw_T_one(self):
        #  x
        #x c
        #  x
        i = random.randint(1, 2)
        j = random.randint(1, 3)
        a = (i - 1)
        b = (i + 1)
        c = (j - 1)
        self.grid[i][j] = True
        self.grid[i][c] = True
        self.grid[a][j] = True
        self.grid[b][j] = True

    def __draw_T_two(self):
        #x
        #c x
        #x
        i = random.randint(1, 2)
        j = random.randint(0, 2)
        a = (i - 1)
        b = (i + 1)
        c = (j + 1)
        self.grid[i][j] = True
        self.grid[i][c] = True
        self.grid[a][j] = True
        self.grid[b][j] = True


    def __draw_T_three(self):
        #x c x
        #  x
        i = random.randint(0, 2)
        j = random.randint(1, 2)
        a = (i + 1)
        b = (j + 1)
        c = (j - 1)
        self.grid[i][j] = True
        self.grid[i][b]= True
        self.grid[i][c]= True
        self.grid[a][j]= True


    def __draw_T_four(self):
        #  x
        #x c x
        i = random.randint(1, 3)
        j = random.randint(1, 2)
        a = (i - 1)
        b = (j + 1)
        c = (j - 1)
        self.grid[i][j] = True
        self.grid[i][b]= True
        self.grid[i][c]= True
        self.grid[a][j]= True


    def __create_Z(self):
        i = random.randint(0,1)
        if i == 0:
            self.__draw_Z_up()
        else:
            self.__draw_Z_side()


    def __draw_Z_up(self):
        #c
        #x x
        #  x
        i = random.randint(0, 1)
        j = random.randint(0, 2)
        a = (i + 1)
        b = (j + 1)
        c = (i + 2)
        self.grid[i][j] = True
        self.grid[a][j]= True
        self.grid[a][b]= True
        self.grid[c][b]= True


    def __draw_Z_side(self):
        #  x x
        #c x
        i = random.randint(1, 3)
        j = random.randint(0, 1)
        a = (i - 1)
        b = (j + 1)
        c = (j + 2)
        self.grid[i][j] = True
        self.grid[i][b]= True
        self.grid[a][b]= True
        self.grid[a][c]= True


    def __create_L(self):
        i = random.randint(0,3)
        if i == 0:
            self.__draw_L_one()
        elif i == 1:
            self.__draw_L_two()
        elif i == 2:
            self.__draw_L_three()
        else:
            self.__draw_L_four()


    def __draw_L_one(self):
        # c x x
        #     x
        i = random.randint(0, 2)
        j = random.randint(0, 1)
        a = (i + 1)
        b = (j + 1)
        c = (j + 2)
        self.grid[i][j] = True
        self.grid[a][c]= True
        self.grid[i][b]= True
        self.grid[i][c]= True


    def __draw_L_two(self):
        # x
        # c x x
        i = random.randint(1, 3)
        j = random.randint(0, 1)
        a = (i - 1)
        b = (j + 1)
        c = (j + 2)
        self.grid[i][j] = True
        self.grid[a][j]= True
        self.grid[i][b]= True
        self.grid[i][c]= True


    def __draw_L_three(self):
        # c x
        # x
        # x
        i = random.randint(0, 1)
        j = random.randint(0, 2)
        a = (j + 1)
        b = (i + 1)
        c = (i + 2)
        self.grid[i][j] = True
        self.grid[i][a]= True
        self.grid[b][j]= True
        self.grid[c][j]= True


    def __draw_L_four(self):
        #   x
        #   x
        # c x
        i = random.randint(2, 3)
        j = random.randint(0, 2)
        a = (j + 1)
        b = (i - 1)
        c = (i - 2)
        self.grid[i][j] = True
        self.grid[i][a]= True
        self.grid[b][a]= True
        self.grid[c][a]= True


    def __create_long(self):
        i = random.randint(0,1)
        if i == 0:
            self.__draw_long_up()
        else:
            self.__draw_long_side()


    def __draw_long_up(self):
            i = random.randint(0, 3)
            self.grid[0][i] = True
            self.grid[1][i] = True
            self.grid[2][i] = True
            self.grid[3][i] = True


    def __draw_long_side(self):
            i = random.randint(0, 3)
            self.grid[i][0] = True
            self.grid[i][1] = True
            self.grid[i][2] = True
            self.grid[i][3] = True


    def __create_square(self):
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            self.__draw_square(i, j)


    def __draw_square(self, x, y):
        a = (x + 1)
        b = (y + 1)
        self.grid[x][y] = True
        self.grid[a][y]= True
        self.grid[x][b]= True
        self.grid[a][b]= True


if __name__ == "__main__":
    grid = Grid()
    while True:
        print(grid)
        input()
        grid.next_piece()
     
