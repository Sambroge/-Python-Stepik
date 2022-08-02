import random

class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.pole = [[Cell() for i in range(N)] for j in range(N)]
        self.set_mines = False
        self.M = M
        self.N = N

    def init(self):
        if not self.set_mines:
            while self.M:
                line = random.randint(0, self.N - 1)
                column = random.randint(0, self.N - 1)
                if self.pole[line][column].mine:
                    continue
                else:
                    self.pole[line][column].mine = True
                    self.pole[line][column].around_mines = 0
                    for i in range(line - 1, line + 2):
                        for j in range(column - 1, column + 2):
                            try:
                                assert (not (i < 0 or j < 0)) and (not self.pole[i][j].mine)
                                self.pole[i][j].around_mines += 1
                            except (IndexError, AssertionError):
                                continue
                    self.M -= 1
            self.set_mines = True


    def show(self):
        for line in self.pole:
            print(*[i.around_mines if i.fl_open else '#' for i in line])
            
            
pole_game = GamePole(10, 12)
