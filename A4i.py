from random import randint
from time import sleep


class A4i:

    def __init__(self, activated, hard):
        self.activated = activated
        self.grid = [[-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1]]
        self.hard = hard
        self.retour = randint(0, 7)

    def play(self, grid, taille):
        self.grid = grid
        self.taille = taille

        sleep(0.3)

        # check centre
        if grid[6][3] == -1:
            self.retour = 3
            return self.retour
        elif grid[6][4] == -1:
            self.retour = 4
            return self.retour

        # check ligne
        for i in range(7):

            if (i <= 0) or (i >= 6):
                iplusun = i
            else:
                iplusun = i + 1

            for ii in range(5):
                if (grid[i][ii] == -1) and (grid[i][ii + 1] == grid[i][ii + 2] == grid[i][ii + 3] != -1):
                    self.retour = ii
                    if (self.grid[iplusun][ii] != -1) or (iplusun == 6):
                        return self.retour
                if (grid[i][ii + 1] == -1) and (grid[i][ii] == grid[i][ii + 2] == grid[i][ii + 3] != -1):
                    self.retour = (ii + 1)
                    if (self.grid[iplusun][ii + 1] != -1) or (iplusun == 6):
                        return self.retour
                if (grid[i][ii + 2] == -1) and (grid[i][ii] == grid[i][ii + 1] == grid[i][ii + 3] != -1):
                    self.retour = (ii + 2)
                    if (self.grid[iplusun][ii + 2] != -1) or (iplusun == 6):
                        return self.retour
                if (grid[i][ii + 3] == -1) and (grid[i][ii] == grid[i][ii + 1] == grid[i][ii + 2] != -1):
                    self.retour = (ii + 3)
                    if (self.grid[iplusun][ii + 3] != -1) or (iplusun == 6):
                        return self.retour

        # check colone
        for i in range(4):
            for ii in range(8):
                if (grid[i][ii] == -1) and (grid[i + 1][ii] == grid[i + 2][ii] == grid[i + 3][ii] != -1):
                    self.retour = ii
                    return self.retour

        # check diagonal \
        for i in range(4):
            for ii in range(5):
                if (grid[i][ii] == -1) and (grid[i + 1][ii + 1] == grid[i + 2][ii + 2] == grid[i + 3][ii + 3] != -1):
                    if grid[i + 1][ii] != -1:
                        self.retour = ii
                        return self.retour
                if (grid[i + 1][ii + 1] == -1) and (grid[i][ii] == grid[i + 2][ii + 2] == grid[i + 3][ii + 3] != -1):
                    if grid[i + 2][ii + 1] != -1:
                        self.retour = ii + 1
                        return self.retour
                if (grid[i + 2][ii + 2] == -1) and (grid[i + 1][ii + 1] == grid[i][ii] == grid[i + 3][ii + 3] != -1):
                    if grid[i + 3][ii + 2] != -1:
                        self.retour = ii + 2
                        return self.retour
                if (grid[i + 3][ii + 3] == -1) and (grid[i + 1][ii + 1] == grid[i + 2][ii + 2] == grid[i][ii] != -1):
                    if i == 6:
                        self.retour = ii + 3
                        return self.retour
                    elif grid[i + 3][ii + 3] != -1:
                        self.retour == ii + 3
                        return self.retour

        # check diagonal /
        for i in range(4):
            for ii in range(5):
                if (grid[i][ii + 3] == -1) and (grid[i + 2][ii + 1] == grid[i + 1][ii + 2] == grid[i + 3][ii] != -1):
                    if grid[i + 1][ii + 3] != -1:
                        self.retour = ii + 3
                        return self.retour
                if (grid[i + 1][ii + 2] == -1) and (grid[i + 3][ii] == grid[i + 2][ii + 1] == grid[i][ii + 3] != -1):
                    if grid[i + 2][ii + 2] != -1:
                        self.retour = ii + 2
                        return self.retour
                if (grid[i + 2][ii + 1] == -1) and (grid[i + 1][ii + 2] == grid[i + 3][ii] == grid[i][ii + 3] != -1):
                    if grid[i + 3][ii + 1] != -1:
                        self.retour = ii + 1
                        return self.retour
                if (grid[i + 3][ii] == -1) and (grid[i + 2][ii + 1] == grid[i + 1][ii + 2] == grid[i][ii + 3] != -1):
                    if i == 6:
                        self.retour = ii
                        return self.retour
                    elif grid[i + 4][ii] != -1:
                        self.retour == ii
                        return self.retour

        # else random
        x = randint(0, 7)
        if self.taille[x] < 7:
            self.retour = x
            return self.retour


