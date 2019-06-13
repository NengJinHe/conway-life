import numpy
import pylab
import random
import time
class ConwayGame():
    def __init__(self, N = 100,T = 200):
        self.N = N
        self.T = T
        self.old_grid = numpy.zeros(N * N, dtype = 'int').reshape(N, N)
        self.new_grid = numpy.zeros(N * N, dtype = 'int').reshape(N, N)

        for i in range(0, self.N):
            for j in range(0, self.N):
                if (random.randint(0,100) < 5):
                    self.old_grid[i][j] = 1
                else:
                    self.old_grid[i][j] = 0

    def live_neighbors(self, i, j):
        s = 0
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if (x == i and y == j):
                    continue
                elif(x != -1 and x != self.N and y != -1 and y != self.N):
                    s += self.old_grid[x][y]
        return s

    def state_change(self):
        pylab.pcolormesh(self.old_grid)
        pylab.colorbar()
        pylab.show()
        t = 1
        while t < self.T:
            for i in range(self.N):
                for j in range(self.N):
                    live = self.live_neighbors(i, j)
                    if (self.old_grid[i][j] == 1 and live < 2):
                        self.new_grid[i][j] = 0
                    elif (self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                        self.new_grid[i][j] = 1
                    elif (self.old_grid[i][j] == 1 and (live > 3)):
                        self.new_grid[i][j] = 0
                    elif (self.old_grid[i][j] == 0 and live == 3 ):
                        self.new_grid[i][j] = 1
            time.sleep(0.1)
            pylab.pcolormesh(self.new_grid)
            pylab.show()
            pylab.close('all')
            self.old_grid = self.new_grid.copy()
            t += 1

if __name__ == '__main__':
    con = ConwayGame(N = 100,T =5)
    con.state_change()