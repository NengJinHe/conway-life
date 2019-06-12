import numpy
import matplotlib
class conwayGame():
    def __init__(self, N = 100):
        self.N = N
        old_grid = numpy.zeros(N * N, dtype = 'int').reshape(N, N)
        old_new = numpy.zeros(N * N, dtyype = 'int').reshape(N, N)

def live_neighbors(self, i, j):
    s = 0
    for x in [i - 1, i, i + 1]:
        for y in [j - 1, j, j + 1]:
            self.old_grid[-1][y] = 0
            self.old_grid[self.N][y] = 0
            self.old_grid[x][-1] = 0
            self.old_grid[x][self.N] = 0
            if (x == i and y == j):
                continue
            else:
                s += self.old_grid[x][y]
    return s


